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

1b. Use **createJobs_PromptGT_TrackerMay2016_MuAlMay2016.py** to create a new python script for running with latest conditions.

1c. Check the output location in L23-L24 and other options in L29-L32.

1d. The prev. file is linked to the cfg: **refit_PromptGT_TrackerMay2016_MuAlMay2016_cfg.py**.

1e. Check the globaltag in L21 and additional conditions in L71-L87.

1f. Create and submit refit jobs:

    python createJobs_PromptGT_TrackerMay2016_MuAlMay2016.py
    source submit.sh

1g. Once the jobs containing latest conditions are finished... do the same using **createJobs_PromptGT_TrackerMay2016.py**,
that is linked to **refit_PromptGT_TrackerMay2016_cfg.py** and uses GT conditions (old ones), and new Tracker geoemtry.

---
## Analysis

2a. Change directory to MuAlAnalyzer:

        cd ../MuAlAnalyzer

2b. Create a filelist for the sample to be analyzed.

2c. Download the latest JSON file and define path to him in L16 of **muAlAnalyzer_Data_cfg.py**.

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
