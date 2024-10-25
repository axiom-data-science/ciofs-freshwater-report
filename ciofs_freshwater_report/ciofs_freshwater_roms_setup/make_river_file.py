"""
Script to run remap_river().
"""
import matplotlib
import sys
import glob
import os

import pyroms

from remap_river import remap_river

matplotlib.use("Agg")

lst_year = sys.argv[1:]

data_dir = os.getenv("HILL_DATA_DIR")  # "./coastal_runoff/"
dst_dir = os.getenv("TMP_OUTPUT_DIR")  # "/tmp/"

lst_file = []

for year in lst_year:
    year = str(year)
    for filename in glob.glob(data_dir + "*.nc"):
        if "0831" + year in filename:
            lst_file.append(filename)
        if "goa_dischargex_0901" + year in filename:
            lst_file.append(filename)
        
lst_file.sort()
print("Build CLM file from the following file list:")
print(lst_file)
print(" ")

# hist_file = "/Users/chang/Downloads/ciofs_his_example.nc"
# grid_file = "./assets/nos.ciofs.romsgrid.nc"
hist_file = None
grid_file = None
# os.environ["PYROMS_GRIDID_FILE"] = "./assets/gridid.txt"
dst_grd = pyroms.grid.get_ROMS_grid(gridid="CIOFS",
                                    hist_file=hist_file,
                                    grid_file=grid_file)

# remap
remap_river(lst_file, year, "q", dst_grd, dst_dir=dst_dir)
