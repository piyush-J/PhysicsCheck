#!/bin/bash

start=1
end=25

for i in $(seq $start $end); do
    echo $i
    ./solve-single-cube.sh 15 constraints_15 tmp.cubes $i > seq_runs/log_15_$i.log 2>&1 &
done

# grep -h "CPU time* *[0-9]*\.*[0-9]*" seq_runs/log_15_*.log | awk '{total += $(NF-1)} END {print "Total time: " total " seconds"}'
# grep -h "CPU time* *[0-9]*\.*[0-9]*" seq_runs/log_15_*.log | awk '{print $(NF-1)}' > out_times.txt

