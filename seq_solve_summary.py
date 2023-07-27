import statistics  

# command line arguments for this python file for cube file and sub directory
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("cube_file", help="cube file to be used", type=str)
parser.add_argument("sub_dir", help="sub directory with logs", type=str)
args = parser.parse_args()
print(args)

with open(f"{args.cube_file}") as f:
    all_cubes = f.readlines()

print("Number of cubes: ", len(all_cubes))

with open(f"{args.sub_dir}/out_times.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [float(x) for x in content]

print("Solving time count: ", len(content))
print("Solving time sum: ", sum(content))
print("Solving time max: ", max(content))
print("Solving time mean: ", statistics.mean(content))
print("Solving time variance: ", statistics.variance(content))