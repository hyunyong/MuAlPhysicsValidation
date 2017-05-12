#!/bin/bash
cd /afs/cern.ch/work/l/lpernie/MuonAlign/WD/CMSSW_8_0_28/src/MuAlPhysicsValidation/PerformancePlots
eval `scramv1 runtime -sh`
python myPlot_Legacy_Prompt.py
