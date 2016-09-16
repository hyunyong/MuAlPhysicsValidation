# Muon Alignment Physics Validation

Checkout the physics validation code

    cmsrel CMSSW_8_0_8_patch1
    cd CMSSW_8_0_8_patch1/src/
    cmsenv
    git clone https://github.com/cms-mual/MuAlPhysicsValidation.git -b CMSSW_8_0_X

---
## Refitting

1a. Change directory to MuAlRefit:

    cd MuAlPhysicsValidation/MuAlRefit

1b. You should create a working directory as CRAB_2016E_6vs3FOD. We will analyze all the things you have to customize each time.

    cp -r CRAB_2016E_6vs3FOD CRAB_MYSTUDY
    cd CRAB_MYSTUDY

1c. Change the crab configuration file: crab_data.py:

    Change the requestName and outLFNDirBase 
    Change the Input dataset: inputDataset and the json file (if data)
    The python command you will execute: psetName
    inputFiles: inputFiles (CRAB cannot see external files if you do not specify them. If you want to use special APE, Geometries or GPR, you have to give here the path. He will importthem and copy them in the same place he runs cmsRun. So in the python code you will run, do not put the path simple the name.)

1d. One your crab file if fine, change the python code you will run. You can rename it with a better name:

    mv refit_PromptGT_TrackerMay2016_MuAl_DT2016D6DOF_CSC2016D3DOF_cfg.py refit_PromptGT_MYNAME_cfg.py
 
1e. In refit_PromptGT_MYNAME_cfg.py you want to customize:

    The GT.
    The json file.
    The APE, GPR, muon geometry and tracker geometry (all external files have to be declared in the CRAB file as inputFiles).

1f. Submit CRAB jobs:

    crab submit -c crab_data.py
    crab status (and all the CRAB commands to check status, resubmit etc...)

1g. Once the jobs are finisced, the output will be opn EOS, as spdecified by outLFNDirBase in the crab cfg file.

---
## Analysis

2a. Change directory to MuAlAnalyzer:

        cd ../MuAlAnalyzer

2b. Create a filelist for the sample to be analyzed.

2c. Put the JSON file used in CRAB_MYSTUDY in L16 of **muAlAnalyzer_Data_cfg.py**.

2d. Create and submit analyzer jobs, provide working directory name, filelist name, and total number of jobs:

    python createJobs.py $WORKDIR$ $FILELIST$ $N_JOBS$
    source submit.sh
    
2e. hadd outout ROOT files into a single ROOT file.

---
## Plotting

3a. Change directory to PerformancePlots:

    cd ../PerformancePlots

3b. Use **comp_v2.py** to create a new python script

3c. Set location of ROOT files in L5.

3d. Edit list of samples in L17-22.

3e. Edit list of comparisons in L40-45 (each list defines what samples will be compared).
