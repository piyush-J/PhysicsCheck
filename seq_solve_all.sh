#!/bin/bash
set -x

./seq_solve_arg.sh 17 e3_17_n20_pysat.cubes seq_runs/e3_17_n20 > dump.out;
./seq_solve_arg.sh 18 e3_18_n20_pysat.cubes seq_runs/e3_18_n20 >> dump.out;
./seq_solve_arg.sh 19 e3_19_n20_pysat.cubes seq_runs/e3_19_n20 >> dump.out;
./seq_solve_arg.sh 20 e3_20_n20_pysat.cubes seq_runs/e3_20_n20 >> dump.out;

./seq_solve_arg.sh 17 e3_17_n40_pysat.cubes seq_runs/e3_17_n40 >> dump.out;
./seq_solve_arg.sh 19 e3_19_n40_pysat.cubes seq_runs/e3_19_n40 >> dump.out;
./seq_solve_arg.sh 20 e3_20_n40_pysat.cubes seq_runs/e3_20_n40 >> dump.out;

# nohup ./seq_solve_all.sh > seq_solve_all.out 2>&1 &