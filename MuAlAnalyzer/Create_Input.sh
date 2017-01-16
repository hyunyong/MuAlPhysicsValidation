#!/bin/bash

eosComm="/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select"
Folder="/store/group/alca_muonalign/lpernie/MuAlRefit_Run2016G_RAWreco_DT3DOF_CSC3DOF_Z15mmsmean_oldGPR_01/SingleMuon/crab_MuAlRefit_Run2016G_RAWreco_DT3DOF_CSC3DOF_Z15mmsmean_oldGPR_01/170112_014955"
fileTXT="MuAlRefit_Run2016G_RAWreco_DT3DOF_CSC3DOF_Z155mmOldGPR/MuAlRefit_Run2016G_RAWreco_DT3DOF_CSC3DOF_Z155mmOldGPR_list.py"
#Folder="/store/group/alca_muonalign/lpernie/MuAlRefit_Run2016G_RAWreco_DT6DOF_CSC3DOF_APE_Z15mmsmean_oldGPR_01/SingleMuon/crab_MuAlRefit_Run2016G_RAWreco_DT6DOF_CSC3DOF_APE_Z15mmsmean_oldGPR_01/170112_155326"
#fileTXT="MuAlRefit_Run2016G_RAWreco_DT6DOF_CSC3DOF_Z155mmOldGPR/MuAlRefit_Run2016G_RAWreco_DT6DOF_CSC3DOF_Z155mmOldGPR_list.py"


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
