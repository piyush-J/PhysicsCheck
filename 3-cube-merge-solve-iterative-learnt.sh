#!/bin/bash

while getopts "p" opt
do
	case $opt in
        p) p="-p" ;;
	esac
done
shift $((OPTIND-1))

n=$1 #order
f=$2 #instance file name
d=$3 #directory to store into
v=$4 #num of var to eliminate during first cubing stage
t=$5 #num of conflicts for simplification
a=$6 #amount of additional variables to remove for each cubing call

mkdir -p $d/$v/$n-solve
mkdir -p $d/$v/simp
mkdir -p $d/$v/log
mkdir -p $d/$v/$n-cubes


di="$d/$v"

if [ "$p" == "-p" ]
then
    echo "cubing in parallel..."
    ./gen_cubes/cube.sh -p -a $n $f $v $di
fi

if [ "$p" != "-p" ]
then
    echo "cubing sequentially..."
    ./gen_cubes/cube.sh -a $n $f $v $di
    echo "cubing complete"
fi

files=$(ls $d/$v/$n-cubes/*.cubes)
highest_num=$(echo "$files" | awk -F '[./]' '{print $(NF-1)}' | sort -nr | head -n 1)
echo "currently the cubing depth is $highest_num"
cube_file=$d/$v/$n-cubes/$highest_num.cubes
cp $(echo $cube_file) .
cube_file=$(echo $cube_file | sed 's:.*/::')
new_cube=$((highest_num + 1))

numline=$(< $cube_file wc -l)
new_index=$((numline))

for i in $(seq 1 $new_index) #1-based indexing for cubes
    do 
        command1="./gen_cubes/apply.sh $f $cube_file $i > $d/$v/simp/$cube_file$i.adj"
        command2="./simplification/simplify-by-conflicts.sh $d/$v/simp/$cube_file$i.adj $n $t >> $d/$v/$n-solve/$i-solve.log"
        command3="./maplesat-solve-verify.sh -l $n $d/$v/simp/$cube_file$i.adj.simp $d/$v/$n-solve/$i-solve.exhaust >> $d/$v/$n-solve/$i-solve.log"
        command="$command1 && $command2 && $command3"
        echo $command >> $d/$v/$n-solve/solve.commands
        eval $command1
        eval $command2
        eval $command3
    done

for i in $(seq 1 $new_index)
    do
        file="$d/$v/$n-solve/$i-solve.log"
        if grep -q "UNSATISFIABLE" $file 
        then
                #do something
                continue
        elif grep -q "SATISFIABLE" $file
        then
                #do something
                continue
        else
                echo $file is not solved
                child_instance="$d/$v/simp/${highest_num}.cubes${i}.adj.simp"
                echo "further cube instance $child_instance"
                #add learnt clauses
                #./gen_cubes/concat.sh $child_instance $child_instance.noncanonical > $child_instance.temp
                #./gen_cubes/concat.sh $child_instance.temp $child_instance.unit > $child_instance.temp2
                #./gen_cubes/concat.sh $child_instance.temp2 $child_instance.nonembed > $child_instance.learnt
                ./gen_cubes/concat.sh $child_instance $child_instance.noncanonical |
    		./gen_cubes/concat.sh - $child_instance.unit |
    		./gen_cubes/concat.sh - $child_instance.nonembed > $child_instance.learnt

                command="./3-cube-merge-solve-iterative-learnt.sh $n $child_instance.learnt "$d/$v-$i" $(($v + $a)) $t $a $(($highest_num+2)) $new_cube_file"
                #for parallization, simply submit the command below using sbatch
                echo $command >> ${n}-iterative.commands
                eval $command
        fi
done
