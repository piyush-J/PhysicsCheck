#!/bin/bash

start=1
end=$(wc -l < $2)

mkdir -p $3

echo "Positional Parameters"
echo '$0 = ' $0 # file
echo '$1 = ' $1 # order
echo '$2 = ' $2 # cube file name
echo '$3 = ' $3 # log path

echo "No. of cubes = ${end}"

for i in $(seq $start $end); do
    echo $i
    ./solve-single-cube.sh ${1} constraints_${1}_c_100000_2_2_0_final.simp $2 $i > ${3}/log_${1}_$i.log 2>&1;
done

grep -h "CPU time* *[0-9]*\.*[0-9]*" ${3}/log_${1}_*.log | awk '{total += $(NF-1)} END {print "Total time: " total " seconds"}'
grep -h "CPU time* *[0-9]*\.*[0-9]*" ${3}/log_${1}_*.log | awk '{print $(NF-1)}' > ${3}/out_times.txt

python seq_solve_summary.py ${2} ${3}