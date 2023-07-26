#!/bin/bash

start=1
end=364

for i in $(seq $start $end); do
    echo $i
    ./solve-single-cube.sh 17 constraints_17_c_100000_2_2_0_final.simp ext_exh_k2_17.cubes.cubes $i > seq_runs/debug/log_17_$i.log 2>&1;
done

# grep -h "CPU time* *[0-9]*\.*[0-9]*" seq_runs/e1/march/17_broken/log_17_*.log | awk '{total += $(NF-1)} END {print "Total time: " total " seconds"}'
# grep -h "CPU time* *[0-9]*\.*[0-9]*" seq_runs/e1/march/17_broken/log_17_*.log | awk '{print $(NF-1)}' > seq_runs/e1/march/17_broken/out_times.txt

# ./solve-single-cube.sh 15 constraints_15 tmp.cubes $i > seq_runs/log_15_$i.log 2>&1 &