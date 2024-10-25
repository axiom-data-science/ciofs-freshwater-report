import netCDF4 as nc4
import numpy as np
import shutil
import xarray as xr
import sys
import uuid

# original_river_file = "/Users/chang/Downloads/axiom.ciofs.river.20020101.nc"
original_river_file = sys.argv[1]
river_file = sys.argv[2]
tmpfile = f'/tmp/Hill_{uuid.uuid4().hex}.nc'
# shutil.copy(river_file, tmpfile)

with xr.open_dataset(river_file) as ds:
    # Keep only rivers with non-zero transport at any time
    # to reduce the file size
    idx = np.where(ds['river_transport'].any(axis=0))[0]
    ds = ds.isel(river=idx)
    ds = ds.assign_coords({"river": (np.arange(ds.sizes['river']) + 1)})
    ds.to_netcdf(tmpfile)

# get daily temperature from the original river file
# In the original river file, the temperature is vertically uniform so we take
# the surface value (s_rho index -1). We also pick a river with highest
# transport (river #32) from the original file to represent the temperature of
# all rivers. This approach is similar to the one used by Kate for NWGOA.
ds_orf = xr.open_dataset(original_river_file)
df = (ds_orf.set_coords('river_time')['river_temp']
      .isel(s_rho=-1, river=32)
      .to_dataframe())
df['date'] = df['river_time'].dt.date
df = df.groupby('date').first()
river_temp = np.array(df['river_temp'])
# expand the dimensions
river_temp = np.expand_dims(river_temp, axis=-1)
river_temp = np.expand_dims(river_temp, axis=1)

with nc4.Dataset(tmpfile, "a") as nc:
    N_river_time = nc.dimensions['river_time'].size
    N_s_rho = nc.dimensions['s_rho'].size
    N_river = nc.dimensions['river'].size

    assert np.shape(river_temp)[0] == N_river_time
    # Create the temperature variable
    temp_var = nc.createVariable('river_temp', float,
                                 ('river_time', 's_rho', 'river'))
    temp_var[:] = river_temp.repeat(N_s_rho, axis=1).repeat(N_river, axis=2)
    atts = {
        'units': 'Celsius',
        'long_name': 'river runoff potential temperature',
        'coordinates': 'river_time'
    }
    temp_var.setncatts(atts)
    # Create the salinity variable
    salt_var = nc.createVariable('river_salt', float,
                                 ('river_time', 's_rho', 'river'))
    salt_var[:] = 0.005*np.ones((N_river_time, N_s_rho, N_river))
    atts = {
        'units': '1',
        'long_name': 'river runoff salinity',
        'coordinates': 'river_time'
    }
    salt_var.setncatts(atts)
    # fix some variable attributes
    nc['river'].long_name = 'river runoff identification number'
    nc['river'].units = '1'
    nc['river_direction'].long_name = "river runoff grid-cell face flag"
    nc['river_direction'].flag_values = "0, 1, 2"
    nc['river_direction'].flag_meanings = (
        "flow across u-face, flow across v-face, flow across w-face"
    )
    nc['river_Xposition'].long_name = "river XI-position"
    nc['river_Xposition'].LuvSrc_meaning = (
        "i-index grid-cell of u- or v-face source/sink"
    )
    nc['river_Eposition'].long_name = "river ETA-position"
    nc['river_Eposition'].LuvSrc_True_meaning = (
        "j-index grid-cell of u- or v-face source/sink"
    )

shutil.move(tmpfile, river_file)
