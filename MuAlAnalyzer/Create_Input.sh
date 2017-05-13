#!/bin/bash
eosComm="/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select"

#Folder="/store/group/alca_muonalign/$USER/MuAlRefit_Legacy_01/SingleMuon/crab_MuAlRefit_Legacy_01/170510_163116"
#fileTXT="MuAlRefit_Legacy/MuAlRefit_Legacy_list.py"

#Folder="/store/group/alca_muonalign/$USER/MuAlRefit_Prompt_02/SingleMuon/crab_MuAlRefit_Prompt_02/170510_164733"
#fileTXT="MuAlRefit_Prompt/MuAlRefit_Prompt_list.py"

#Folder="/store/group/alca_muonalign/lpernie/MuAlRefit_Legacy_APEminuitx2_02/SingleMuon/crab_MuAlRefit_Legacy_APEminuitx2_02/170511_213507"
#fileTXT="MuAlRefit_Legacy_APEminuitx2/MuAlRefit_Legacy_APEminuitx2_list.py"

Folder="/store/group/alca_muonalign/$USER/MuAlRefit_Legacy_APEold_01/SingleMuon/crab_MuAlRefit_Legacy_APEold_01/170512_144204"
fileTXT="MuAlRefit_Legacy_APEold/MuAlRefit_Legacy_APEold_list.py"

#Folder="/store/group/alca_muonalign/$USER/MuAlRefit_Legacy_GeoOld_APEold_02/SingleMuon/crab_MuAlRefit_Legacy_GeoOld_APEold_02/170512_215508"
#fileTXT="MuAlRefit_Legacy_GeoOld_APEold/MuAlRefit_Legacy_GeoOld_APEold_list.py"

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
