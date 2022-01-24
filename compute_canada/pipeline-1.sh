i=$1 #input instance file
c=$2 #cubing file
o=$3 #order

set -x

echo "#!/bin/bash" > simp-solve-$i-$c.sh
numline=$(< "$c" wc -l)
index=$((numline-1))
echo "#SBATCH --array=0-${index}" >> simp-solve-$i-$c.sh
echo "#SBATCH --time=01:00:00" >> simp-solve-$i-$c.sh
echo "#SBATCH --account=def-janehowe" >> simp-solve-$i-$c.sh
echo "#SBATCH --mem=4G" >> simp-solve-$i-$c.sh
echo "./adjoin-cube-simplify.sh $i $c \$SLURM_ARRAY_TASK_ID 70" >> simp-solve-$i-$c.sh
echo "if [[ $(wc -l < tocube-leftover+19.cubes${SLURM_ARRAY_TASK_ID}.adj.simp) -ge 3 ]]" >> simp-solve-$i-$c.sh
echo "then" >> simp-solve-$i-$c.sh
echo "./maplesat-ks/simp/maplesat_static $c\${CLURM_ARRAY_TASK_ID}.adj.simp -no-pre -exhaustive=$o.exhaust -order=$o" >> simp-solve-$i-$c.sh
echo "else" >> simp-solve-$i-$c.sh
echo "echo "UNSATISFIABLE"" >> simp-solve-$i-$c.sh
echo "fi" >> simp-solve-$i-$c.sh
#sbatch simp-solve-$i-$c #compute canada execute adjoin and simplification
