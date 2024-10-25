#!/bin/bash

# python maskedge.py assets/nos.ciofs.romsgrid.nc >maskedge.out
export HILL_DATA_DIR=/mnt/vault/ciofs/coastal_runoff/
export TMP_OUTPUT_DIR=/tmp/
export RIVER_OUTPUT_DIR=/mnt/vault/ciofs/input/river_freshwater/
export PYROMS_GRIDID_FILE=./assets/gridid.txt
export ORIGINAL_RIVER_FILE_DIR=/mnt/vault/ciofs/input/river/

# Define a function to run the Python commands
run_python_commands() {
    year=$1
    python make_river_file.py ${year}
    python add_rivers.py $RIVER_OUTPUT_DIR/Hill_rivers_${year}.nc
    python make_river_clim.py $TMP_OUTPUT_DIR/goa_dischargex_${year}_q_Hill_CIOFS.nc $RIVER_OUTPUT_DIR/Hill_rivers_${year}.nc
    python set_vshape.py $RIVER_OUTPUT_DIR/Hill_rivers_${year}.nc
    python add_ts.py $ORIGINAL_RIVER_FILE_DIR/axiom.ciofs.river.${year}0101.nc $RIVER_OUTPUT_DIR/Hill_rivers_${year}.nc
}

# Export the function so that it can be used by parallel
export -f run_python_commands

# Run the loop in parallel
# parallel run_python_commands ::: {2002..2006}
parallel run_python_commands ::: {2011..2014}
