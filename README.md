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

1c. Change the crab configuration file: **crab_data.py**:

    Change the requestName and outLFNDirBase 
    Change the Input dataset: inputDataset and the json file (if data)
    The python command you will execute: psetName
    inputFiles: inputFiles (CRAB cannot see external files if you do not specify them. If you want to use special APE, Geometries or GPR, you have to give here the path. He will importthem and copy them in the same place he runs cmsRun. So in the python code you will run, do not put the path simple the name.)

1d. One your crab file if fine, change the python code you will run. You can rename it with a better name:

    mv refit_PromptGT_TrackerMay2016_MuAl_DT2016D6DOF_CSC2016D3DOF_cfg.py refit_PromptGT_MYNAME_cfg.py
 
1e. In **refit_PromptGT_MYNAME_cfg.py** you want to customize:

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

2b. Create a Working directory for this comparison (it could be the filder name on EOS from prev. step)

        mkdir MuAlRefit_MYSTUDY

2c. Create a filelist for the sample to be analyzed (need to specify in **Create_Input.sh** the EOS folder that contains the Refit files and the output txt file)

        bash Create_Input.sh 
        cd MYSTUDY

2d. Now copy here the python file you will change to run your comparison **muAlAnalyzer_Data_cfg.py**.
      
        cp ../muAlAnalyzer_Data_cfg.py .
        cp ../createJobs.py .
        pyhton createJobs.py $FILELIST$ $N_JOBS$ (FILELIST is the one you created and N_JOBS is the job splitting you want to use)

2e. Now you can submit the jobs:

    source submit.sh
    
2f. hadd the output ROOT files into a single ROOT file and clean space.
 
    hadd FINALFILE.root out_*root
    rm -rf out_*root
    rm -rf LSF*

---
## Plotting

3a. Change directory to PerformancePlots:

    cd ../PerformancePlots

3b. Use **myPlot_MuAl2016_ichep_v1.py** as a model for a new pyhton command to make the plots

    cp myPlot_MuAl2016_ichep_v1.py myPlot_MINE.py

3c. You need to change:
    
    maxEntries -> for test set to low value, for final plots set to -1 (all events)
    samples -> change the path to the root files you created in the previous step
    combineHistos -> decide what sample are shown in teh same plot (E.g. [0,1] the first and the second only).

3d. Launch the command:

    python myPlot_MINE.py
