#!/bin/bash

eosComm="/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select"
Folder="/store/group/alca_muonalign/lpernie/MuAlRefit_Run2016E_RAWreco_DT6DOF_CSC3DOF_APE02"
fileTXT="MuAlRefit_Run2016E_RAWreco_DT6DOF_CSC3DOF_APE02/MuAlRefit_Run2016E_RAWreco_DT6DOF_CSC3DOF_APE02_list.py"

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
