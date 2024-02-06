#!/bin/bash

# This script runs cartesian_ddg 2020 with two inputs: a relaxed pdb file, and a mutfile.
# USAGE: sh <path to cartddg2020.sh> <path to relaxed pdb file> <path to mutfile.mut>

# make output directory if it does not exist
mkdir -p /Users/arjanhada/rosetta/results

# Specify variables for directories
ROSETTABIN=/Users/arjanhada/rosetta/main/source/bin
ROSETTADB=/Users/arjanhada/rosetta/main/database

# initialize a variable with an intuitive name to store the name of the input files
input_pdb=$1
mutfile=$2

# Run cartesian_ddg 2020
$ROSETTABIN/cartesian_ddg.default.macosclangrelease \
    -database $ROSETTADB\
    -s ${input_pdb}\
    -ddg::iterations 5\
    -ddg::score_cutoff 1.0\
    -ddg::dump_pdbs false\
    -ddg::bbnbrs 1\
    -score:weights ref2015_cart\
    -ddg::mut_file ${mutfile}\
    -ddg:frag_nbrs 2\
    -ignore_zero_occupancy false\
    -missing_density_to_jump \
    -ddg:flex_bb false\
    -ddg::force_iterations false\
    -fa_max_dis 9.0\
    -ddg::json true\
    -ddg:legacy false