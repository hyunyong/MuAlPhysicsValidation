#!/bin/bash
Folder="/store/group/alca_muonalign/$USER/MuAlRefit_Run2017B_RAWRECO_fromGT/SingleMuon/crab_MuAlRefit_Run2017B_RAWRECO_fromGT/170720_193943/"
fileTXT="MuAlRefit_Run2017B_RAWreco_FromGT/MuAlRefit_Run2017B_RAWreco_FromGT_list.py"

listfile=`eos find $Folder | grep root | grep -v failed`
echo 'fileNames = [' > $fileTXT

for item in $listfile
do
lenght=${#item}
item_fix=${item:8:$lenght} 
Mystring="       '$item_fix',"
echo $Mystring >> $fileTXT
done

echo ']' >> $fileTXT
