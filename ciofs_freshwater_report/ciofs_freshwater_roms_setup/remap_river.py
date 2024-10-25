import numpy as np
import os
import netCDF4 as netCDF
import datetime

import pyroms_toolbox
import xarray as xr
import pandas as pd


class nctime(object):
    pass


def remap_river(
    src_files, src_year, src_varname, dst_grd, cdepth=0, kk=0, dst_dir="./"
):
    """
    Reads Hill model output files and remaps the river discharge points to
    the coastal cells of the rho grid.

    Args:
        src_files (str): path to the Hill model output files.
        src_year (str): year to process.
        src_varname (str): variable name (typically "q") to process.
        dst_grd (str): ROMS grid file object loaded using
            pyroms.grid.get_ROMS_grid().
        cdepth (int, optional): _description_. Defaults to 0.
        kk (int, optional): _description_. Defaults to 0.
        dst_dir (str, optional): output file directory. Defaults to "./".
    """

    dx = dst_grd.hgrid.dx
    dy = dst_grd.hgrid.dy
    area_dst = dx * dy
    # mask_rho = dst_grd.hgrid.mask_rho

    # get time
    nctime.long_name = "time"
    nctime.units = "days since 1900-01-01 00:00:00"
    time0 = datetime.date(1900, 1, 1)

    # create IC file
    # dst_file = src_files.rsplit('/')[-1]
    dst_file = (
        dst_dir + "goa_dischargex" + "_" + str(src_year) + "_"
        + src_varname + "_Hill_" + dst_grd.name + ".nc"
    )
    print("\nCreating file", dst_file)
    if os.path.exists(dst_file) is True:
        os.remove(dst_file)
    pyroms_toolbox.nc_create_roms_file(dst_file, dst_grd, nctime)

    # open River file
    nc = netCDF.Dataset(dst_file, "a")

    # load var
    # Each file is from Sep through Aug. Combine two files and select
    # the whole year.
    ds = xr.open_mfdataset(src_files, combine="nested", concat_dim="time")
    dates = pd.to_datetime(
        {
            "year": ds["year"].values,
            "month": ds["month"].values,
            "day": ds["day"].values,
        }
    )
    ds = ds.assign_coords(time=dates)
    src_year = int(src_year)
    cf = ds.sel(time=slice(f"{src_year}-01-01", f"{src_year+1}-01-01"))

    # Subset points only inside CIOFS domain
    idx = (
        pd.read_csv("./assets/Hill_in_CIOFS.csv")
        ["timeSeries"]
        .values
        .astype(int)
    )
    cf = cf.isel(timeSeries=idx).compute()

    years = cf.year.values
    months = cf.month.values
    days = cf.day.values
    src_lon = cf.lon.values  # + 360.0
    src_lat = cf.lat.values

    src_var_all = cf.q.values

    # get missing value
    spval = 1.0e30

    dst_varname = "Runoff_raw"
    dimensions = ("ocean_time", "eta_rho", "xi_rho")
    long_name = "river discharge"
    # field = "raw runoff, scalar, series"

    # create variable in file
    print("Creating variable", dst_varname)
    nc.createVariable(dst_varname, "f8", dimensions, fill_value=spval)
    nc.variables[dst_varname].long_name = long_name
    nc.variables[dst_varname].units = "m^3/day"

    nc.createVariable("Runoff", "f8", ("ocean_time", "eta_rho", "xi_rho"))
    nc.variables["Runoff"].long_name = "Hill River Runoff"
    nc.variables["Runoff"].units = "kg/s/m^2"

    # get littoral (here just 1 cell wide, no diagonals)
    width = 1
    idx = []
    idy = []
    maskl = dst_grd.hgrid.mask_rho.copy()
    for w in range(width):
        lit = pyroms_toolbox.get_littoral2(maskl)
        idx.extend(lit[0])
        idy.extend(lit[1])
        maskl[lit] = 0

    littoral_idx = (np.array(idx), np.array(idy))

    ntimes = len(years)
    for it in range(ntimes):
        src_var = src_var_all[it, :]
        net_flow = np.sum(src_var)
        src_var = xr.DataArray(src_var)
        src_var = src_var.fillna(0)
        src_var = src_var.data
        print(src_var.shape)

        time = datetime.date(years[it], months[it], days[it])
        print("time =", time)

        # horizontal interpolation
        print("horizontal interpolation using brute force")

        # write data in destination file
        print("write data in destination file")
        nc.variables["ocean_time"][it] = (time - time0).days

        runoff = pyroms_toolbox.remap_river(
            src_var,
            src_lon,
            src_lat,
            np.array(littoral_idx).T + 1,
            dst_grd.hgrid.lon_rho,
            dst_grd.hgrid.lat_rho,
        )
        net_flow2 = np.sum(runoff)
        print("flow before", net_flow)
        print("regridded flow", net_flow2)

        nc.variables[dst_varname][it] = runoff
        # zero out contribution from outside the domain
        runoff[0, :] = 0
        runoff[:, -1] = 0
        net_flow3 = np.sum(runoff)
        print("final flow", net_flow3)
        runoff = (
            runoff * 1000.0 / area_dst / 86400.0
        )  # convert units from m3/day to kg/s/m2
        nc.variables["Runoff"][it] = runoff

    # close destination file
    nc.close()
