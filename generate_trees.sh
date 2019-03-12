for i in {0..19}
do
  echo "ToNEXUS format=FASTA fromFile= 1000L1data/R${i}/rose.aln.true.fasta toFile=~/Desktop/Research/ASTR_stuff/1000L1_analysis/1000L1NJTrees/R${i}_exe;
  exe ~/Desktop/Research/ASTR_stuff/1000L1_analysis/1000L1NJTrees/R${i}_exe; NJ distance=logDet showtree=No;
  savetrees file=~/Desktop/Research/ASTR_stuff/1000L1_analysis/1000L1NJTrees/R${i}_tree.tre format=newick;" | ./paup4a164_osx -n
done

#echo "ToNEXUS format=FASTA fromFile= 1000L1data/R0/rose.aln.true.fasta toFile=~/Desktop/tmp;
#exe ~/Desktop/tmp; NJ distance=logDet showtree=No;
#savetrees file=~/Desktop/test.tre format=newick;" | ./paup4a164_osx -n

#echo "ToNEXUS format=FASTA fromFile= 1000L1data/R0/rose.aln.true.fasta toFile=~/Desktop/Research/ASTR_stuff/1000L1_analysis/1000L1NJTrees/R0_exe;
#exe ~/Desktop/Research/ASTR_stuff/1000L1_analysis/1000L1NJTrees/R0_exe; NJ distance=logDet showtree=No;
#savetrees file=~/Desktop/Research/ASTR_stuff/1000L1_analysis/1000L1NJTrees/R0_tree.tre format=newick;" | ./paup4a164_osx -n
