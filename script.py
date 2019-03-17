import subprocess
import compare_trees
import os

# Generate all of our NJ and Fast Tree 2 trees
#subprocess.call(['./generate_trees.sh'])

# Perform analysis on generated trees
NJ_trees = []
Fast_trees = []
FP_FN_rates_NJ = []
FP_FN_rates_Fast = []

# get the file paths for all trees
for i in range(20):
    current_dir = os.getcwd()
    NJ_trees.append(current_dir + "1000L1NJTrees/R" + str(i) + "_tree.tre")
    Fast_trees.append(current_dir + "1000L1FastTrees/R" + str(i) + "_true.tt")

for i in range(20):
    arg_1 = "1000L1NJTrees/R" + str(i) + "_tree.tre"
    arg_2 = "1000L1data/R" + str(i) + "/rose.tt"
    proc = subprocess.Popen(['python', 'compare_trees.py',  '-t1', arg_1, '-t2', arg_2], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print((proc.communicate()[0]).decode().split())
    ######## FN Error rate will be 4th element (minus a , at the end)###########
    ######## FP Error rate will be 9th element #################################
