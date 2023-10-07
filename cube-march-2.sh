#!/bin/bash
#SBATCH --cpus-per-task=4
#SBATCH --mem=4G       
#SBATCH --account=def-vganesh
#SBATCH --mail-type=ALL
#SBATCH --mail-user=piyush.jha@uwaterloo.ca
#SBATCH --time=0-01:00      # time (DD-HH:MM)
#SBATCH --output=cubing_outputs/e4_19_march_var-%N-%j.out  # %N for node name, %j for jobID

module load python/3.8
source ~/physicscheck/bin/activate

./gen_cubes/march_cu/march_cu constraints_19_c_100000_2_2_0_final.simp -o e4_19_march_var.cubes -m 171 -n 20