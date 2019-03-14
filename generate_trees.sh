#!/bin/sh
for i in {0..19}
do
  echo "ToNEXUS format=FASTA fromFile= 1000L1data/R${i}/rose.aln.true.fasta toFile=~/Desktop/Research/ASTR_stuff/1000L1_analysis/1000L1NJTrees/R${i}_exe;
  exe ~/Desktop/Research/ASTR_stuff/1000L1_analysis/1000L1NJTrees/R${i}_exe; NJ distance=logDet showtree=No;
  savetrees file=~/Desktop/Research/ASTR_stuff/1000L1_analysis/1000L1NJTrees/R${i}_tree.tre format=newick;" | ./paup4a164_osx -n
done

for i in {0..19}
do
  touch 1000L1FastTrees/R${i}_true.tt
  ./FastTree -nt -gtr 1000L1data/R${i}/rose.aln.true.fasta > 1000L1FastTrees/R${i}_true.tt
done
