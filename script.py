import subprocess
import compare_trees
import os

# Generate all of our NJ and Fast Tree 2 trees
#subprocess.call(['./generate_trees.sh'])

# Perform analysis on generated trees
NJ_trees = []
Fast_trees = []

# get the file paths for all trees
for i in range(20):
    current_dir = os.getcwd()
    NJ_trees.append(current_dir + "1000L1NJTrees/R" + str(i) + "_tree.tre")
    Fast_trees.append(current_dir + "1000L1FastTrees/R" + str(i) + "_true.tt")

proc = subprocess.Popen(['python', 'compare_trees.py',  '-t1', '1000L1NJTrees/R1_tree.tre', '-t2', '1000L1data/R1/rose.tt'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(proc.communicate()[0])
