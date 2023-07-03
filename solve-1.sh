#!/bin/bash
#SBATCH --account=def-vganesh
#SBATCH --time=1-00:00
#SBATCH --mem-per-cpu=8G
#SBATCH --array=1-5000

module load python/3.8

./solve-single-cube.sh 23 constraints_23_c_100000_2_2_0_final.simp 41.cubes $SLURM_ARRAY_TASK_ID