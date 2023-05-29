#!/bin/bash
#SBATCH --account=def-vganesh
#SBATCH --time=0-01:00
#SBATCH --mem-per-cpu=8G
#SBATCH --array=1-4
#SBATCH --mail-type=ALL
#SBATCH --mail-user=piyush.jha@uwaterloo.ca
#SBATCH --output=19-files/slurm-%A-%a.out 

module load python/3.8
source ~/physicscheck/bin/activate

./solve-single-cube.sh 19 constraints_19_c_100000_2_2_0_final.simp 19_4.cubes $SLURM_ARRAY_TASK_ID

# Checklist: out dir, order, constraint file, cube file