#!/bin/bash
#SBATCH --cpus-per-task=4
#SBATCH --mem=16000M       
#SBATCH --account=def-vganesh
#SBATCH --mail-type=ALL
#SBATCH --mail-user=piyush.jha@uwaterloo.ca
#SBATCH --time=0-01:30      # time (DD-HH:MM)
#SBATCH --output=exptResultsSolve/run-%N-%j.out  # %N for node name, %j for jobID

set -x

module load python/3.8
source ~/physicscheck/bin/activate

./seq_solve_arg.sh 19 pysat_19_n20var.cubes seq_runs/pysat_19_n20var2

# sbatch seq_solve_all_cc.sh