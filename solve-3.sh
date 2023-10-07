#!/bin/bash
#SBATCH --account=def-vganesh
#SBATCH --time=0-01:00
#SBATCH --mem-per-cpu=1G
#SBATCH --array=1-59
#SBATCH --mail-type=ALL
#SBATCH --mail-user=piyush.jha@uwaterloo.ca
#SBATCH --output=e4-18-pysat/slurm-%A-%a.out 

module load python/3.8
source ~/physicscheck/bin/activate

./solve-single-cube.sh 18 constraints_18_c_100000_2_2_0_final.simp e4_18_pysat_var.cubes $SLURM_ARRAY_TASK_ID

# grep -h "CPU time* *[0-9]*\.*[0-9]*" e4-18-pysat/*.out | awk '{total += $(NF-1)} END {print "Total time: " total " seconds"}'
# grep -h "CPU time* *[0-9]*\.*[0-9]*" e4-18-pysat/*.out | awk '{print $(NF-1)}' > e4-18-pysat/out_times.txt

# python seq_solve_summary.py e4_18_pysat_var.cubes e4-18-pysat