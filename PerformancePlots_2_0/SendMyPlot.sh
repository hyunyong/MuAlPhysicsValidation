#!/bin/bash
cd /afs/cern.ch/work/l/lpernie/MuonAlign/WD/CMSSW_9_2_5_patch2/src/MuAlPhysicsValidation/PerformancePlots_2_0
eval `scramv1 runtime -sh`
python Step1_make_2d_plots.py /eos/cms/store/group/alca_muonalign/lpernie/MuAlAnalyzer/MuAlRefit_Run2017B_RAWRECO_DT6DOFnoT0it1CSC3DOF_OfficialAPEDTminuit_CSCasym.root MuAlRefit_2017B_DT6DOFnoT0it1CSC3DOF_OfficialAPEDTminuit_CSCasym std -b
