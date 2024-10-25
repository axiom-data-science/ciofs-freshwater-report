import numpy as np
import netCDF4 as netCDF
import os
import sys
import pyroms

"""
Reads the remapped, rho-grid discharge file and populates river_transport
in the ROMS rivers file.
"""

infile = sys.argv[1]
outfile = sys.argv[2]

# load 2-dimentional discharge data
print("Load discharge data")
nc_data = netCDF.Dataset(infile, "r")
nc_rivers = netCDF.Dataset(outfile, "a")
data = nc_data.variables["Runoff"][:]
time = nc_data.variables["ocean_time"][:]
# area = nc_data.variables['area'][:]
sign = nc_rivers.variables["river_sign"][:]
xi = nc_rivers.variables["river_Xposition"][:]
eta = nc_rivers.variables["river_Eposition"][:]
dir = nc_rivers.variables["river_direction"][:]

# load grid object
print("===Load grid")
hist_file = None
grid_file = None
os.environ["PYROMS_GRIDID_FILE"] = "./assets/gridid.txt"
grd = pyroms.grid.get_ROMS_grid(gridid="CIOFS",
                                hist_file=hist_file,
                                grid_file=grid_file)
print("===Done")


# define some variables
nt = data.shape[0]
Nr = sign.shape[0]
Mp, Lp = grd.hgrid.mask_rho.shape
area = grd.hgrid.dx * grd.hgrid.dy
runoff = np.zeros((Nr))
count = np.zeros(grd.hgrid.mask_rho.shape, dtype=np.int32)
irho = 1 / 1000.0  # m3/kg

# Point mapped to from (-1,-1) for this grid
# ileftover = 681
# jleftover = 1081
# data[:,jleftover,ileftover] = 0

# from a Python forum - create an array of lists
filler = np.frompyfunc(lambda x: list(), 1, 1)
rivers = np.empty((Mp, Lp), dtype=object)
filler(rivers, rivers)

# Count the river segments pouring into each coastal cell
# pdb.set_trace()
for k in range(Nr):
    eta2 = int(eta[k])
    xi2 = int(xi[k])
    if sign[k] == 1:
        count[eta2, xi2] += 1
        rivers[eta2, xi2].append(k)
    elif sign[k] == -1 and dir[k] == 0:
        count[eta2, xi2 - 1] += 1
        rivers[eta2, xi2 - 1].append(k)
    elif sign[k] == -1 and dir[k] == 1:
        count[eta2 - 1, xi2] += 1
        rivers[eta2 - 1, xi2].append(k)

nct = 0
for t in range(nt):
    print("Remapping runoff for time %f" % time[t])
    for j in range(Mp):
        for i in range(Lp):
            for n in range(count[j, i]):
                frac = 1.0 / count[j, i]
                k = rivers[j, i][n]
                # runoff[k] = (frac * data[t, j - 1, i - 1] *
                #              area[j - 1, i - 1] * irho)
                runoff[k] = (frac * data[t, j, i] *
                             area[j, i] * irho)

    if t == 110:
        suminput = irho * np.sum(data[t, :, :] * area[:, :])
        # badinput = irho*data[t,jleftover,ileftover]*area[jleftover,ileftover]
        sum180 = np.sum(runoff)
    runoff = runoff * sign

    # write data in destination file
    nc_rivers.variables["river_transport"][nct] = runoff
    nc_rivers.variables["river_time"][nct] = time[nct]
    nct = nct + 1


# close netcdf file
nc_rivers.close()

print("sum 3, 4", suminput, sum180)
print("x,y", xi[6800], eta[6800])
