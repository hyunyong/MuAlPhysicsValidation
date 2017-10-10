#!/bin/bash
cd /afs/cern.ch/work/l/lpernie/MuonAlign/WD/CMSSW_9_2_5_patch2/src/MuAlPhysicsValidation/PerformancePlots/
eval `scramv1 runtime -sh`
python myPlot_2017_BeforeAfter.py
