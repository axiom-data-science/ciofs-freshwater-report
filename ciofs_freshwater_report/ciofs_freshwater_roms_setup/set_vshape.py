import numpy as np
import netCDF4
import sys
import shutil
import xarray as xr
import uuid

outfile = sys.argv[1]
tmpfile = f'/tmp/vshape_{uuid.uuid4().hex}.nc'

with xr.open_dataset(outfile) as ds:
    # For a few points with extremely large trasport, evenly distribute the
    # transport among several nearby river points to increase numerical
    # stability.
    idx_list = [[1, 10, 20, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66],  # Susitna River
                [2127, 2125, 2123, 2129, 2131, 2314, 2316, 2318, 2320, 1933, 1935, 1937, 1974, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544],  # Knik Arm
                [8220, 8221, 8222, 8223, 8224, 8225, 8226, 8227, 8228, 8229, 8230, 8231, 8232],  # McArthur/Chakachatna
                [4962, 4963, 4964, 4965, 4966, 4967, 4968],  # Kenai
                [3928, 3769, 3770, 3771],  # Turnagain Arm
                [5554, 5598, 5599, 951, 952, 953, 954, 5595, 5596, 5597, 5560, 5561, 5562],  # Fox River
                [8052, 8048, 8056, 8057],  # Drift River
                [5608, 5609, 5612, 5613]]
    for river_idx in idx_list:
        mean_values = np.fabs(ds['river_transport'].sel(river=river_idx)).mean(dim='river')
        mean_values_expanded = mean_values.expand_dims(river=len(river_idx)).T
        sign = ds['river_sign'].loc[dict(river=river_idx)]
        mean_values_expanded_signed = mean_values_expanded * sign
        ds['river_transport'].loc[dict(river=river_idx)] = mean_values_expanded_signed

    # swap rivers 3928 and 3772
    idx_a = 3928
    idx_b = 3772
    swap = np.fabs(ds['river_transport'].sel(river=idx_a))
    ds['river_transport'].loc[dict(river=idx_a)] = ds['river_sign'].loc[dict(river=idx_a)] * np.fabs(ds['river_transport'].sel(river=idx_b))
    ds['river_transport'].loc[dict(river=idx_b)] = ds['river_sign'].loc[dict(river=idx_b)] * swap

    # swap 3811 3812 3815 3817 3818 with 3780 959 960 961 962
    for idx_a, idx_b in zip([3811, 3812, 3815, 3817, 3818], [3780, 959, 960, 961, 962]):
        swap = np.fabs(ds['river_transport'].sel(river=idx_a))
        ds['river_transport'].loc[dict(river=idx_a)] = ds['river_sign'].loc[dict(river=idx_a)] * np.fabs(ds['river_transport'].sel(river=idx_b))
        ds['river_transport'].loc[dict(river=idx_b)] = ds['river_sign'].loc[dict(river=idx_b)] * swap

    for idx_a, idx_b in zip([6139, 6140], [6147, 6148]):
        swap = np.fabs(ds['river_transport'].sel(river=idx_a))
        ds['river_transport'].loc[dict(river=idx_a)] = ds['river_sign'].loc[dict(river=idx_a)] * np.fabs(ds['river_transport'].sel(river=idx_b))
        ds['river_transport'].loc[dict(river=idx_b)] = ds['river_sign'].loc[dict(river=idx_b)] * swap

    ds.to_netcdf(tmpfile)

# Set the vertical distribution of the river transport.

out = netCDF4.Dataset(tmpfile, "a")
N = len(out.dimensions["s_rho"])
Nr = len(out.dimensions["river"])

vshape = np.zeros([N, Nr])
for k in range(N):
    vshape[k, :] = k

area = sum(vshape[:, 0])
vshape = (1.0 / area) * vshape
print(vshape[:, 0])

vshape2 = np.ones(N)
area = sum(vshape2[:])
vshape2 = (1.0 / area) * vshape2


with xr.open_dataset(tmpfile) as ds:
    # For high volumn river points (with total annual discharge rate >10,000 m3/s),
    # set the vertical distribution to be uniform.
    high_volumn_rivers = np.where(np.fabs(ds["river_transport"].sum(dim="river_time")) > 6000)[0]
for k in high_volumn_rivers:
    vshape[:, k] = vshape2

print(vshape[:, high_volumn_rivers[2]])

out.variables["river_Vshape"][:] = vshape

out.close()
shutil.move(tmpfile, outfile)
