#!/bin/bash
eosComm="/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select"

Folder="/store/group/alca_muonalign/$USER/MuAlRefit_Run2017B_RAWRECO_2016Geom/SingleMuon/crab_MuAlRefit_Run2017B_RAWRECO_2016Geom/170713_202109/"
fileTXT="MuAlRefit_Run2017B_RAWreco_2016Geom_01/MuAlRefit_Run2017B_RAWreco_2016Geom_01_list.py"

listfile=`$eosComm find $Folder | grep root | grep -v failed`
echo 'fileNames = [' > $fileTXT

for item in $listfile
do
lenght=${#item}
item_fix=${item:8:$lenght} 
Mystring="       '$item_fix',"
echo $Mystring >> $fileTXT
done

echo ']' >> $fileTXT
