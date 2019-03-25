import subprocess
import compare_trees
import os
import matplotlib.pyplot as plt
import math


# Generate all of our NJ and Fast Tree 2 trees
#subprocess.call(['./generate_trees.sh'])

# Perform analysis on generated trees
FP_rates_NJ = []
FN_rates_NJ = []
FP_rates_Fast = []
FN_rates_Fast = []

for i in range(20):
    arg_1 = "1000L1NJTrees/R" + str(i) + "_tree.tre"
    arg_2 = "1000L1data/R" + str(i) + "/rose.tt"
    proc = subprocess.Popen(['python', 'compare_trees.py',  '-t1', arg_1, '-t2', arg_2], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = proc.communicate()[0].decode().split()
    FN_rates_NJ.append(output[4][:-1])
    FP_rates_NJ.append(output[9][:-1]) # store FP and FN rates in tuple
    arg_1 = "1000L1FastTrees/R" + str(i) + "_true.tt"
    proc = subprocess.Popen(['python', 'compare_trees.py',  '-t1', arg_1, '-t2', arg_2], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = proc.communicate()[0].decode().split()
    FN_rates_Fast.append(output[4][:-1])
    FP_rates_Fast.append(output[9][:-1])
    ######## FN Error rate will be 4th element (minus a , at the end)###########
    ######## FP Error rate will be 9th element #################################

for i in range(20):
    FP_rates_NJ[i] = int(FP_rates_NJ[i])/997
    FN_rates_NJ[i] = int(FN_rates_NJ[i])/997
    FP_rates_Fast[i] = int(FP_rates_Fast[i])/997
    FN_rates_Fast[i] = int(FN_rates_Fast[i])/997
    # can normalize by dividing by n - 3, where n is the number of taxa (1000)

FP_avg_NJ = sum(FP_rates_NJ)/20
FN_avg_NJ = sum(FN_rates_NJ)/20
FP_avg_Fast = sum(FP_rates_Fast)/20
FN_avg_Fast = sum(FN_rates_Fast)/20

print("Average FP rate for NJ is ", FP_avg_NJ)
print("Average FN rate for NJ is ", FN_avg_NJ)
print("Average FP rate for FastTree is ", FP_avg_Fast)
print("Average FN rate for FastTree is ", FN_avg_Fast)

print("Average FP count for NJ is ", int((sum(FP_rates_NJ)*997)/20))
print("Average FN count for NJ is ", int((sum(FN_rates_NJ)*997)/20))
print("Average FP count for FastTree is ",int((sum(FP_rates_Fast)*997)/20))
print("Average FN count for FastTree is ", int((sum(FN_rates_Fast)*997)/20))

plt.plot([i for i in range(20)], FP_rates_NJ, '-', label='PAUP*')
plt.plot([i for i in range(20)], FP_rates_Fast, '-', label='FastTreee')
plt.legend(loc='best')
plt.title("FP rates for PAUP* NJ and FastTree2")
plt.xlabel("Replicate Number")
plt.ylabel("FP rate")
plt.savefig("FP_rates.png")
plt.show()


plt.plot([i for i in range(20)], FN_rates_NJ, '-', label='PAUP*')
plt.plot([i for i in range(20)], FN_rates_Fast, '-', label='FastTreee')
plt.legend(loc='best')
plt.title("FN rates for PAUP* NJ and FastTree2")
plt.xlabel("Replicate Number")
plt.ylabel("FN rate")
plt.savefig("FN_rates.png")
plt.show()
