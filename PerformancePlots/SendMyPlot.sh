#!/bin/bash
cd /afs/cern.ch/work/l/lpernie/MuonAlign/WD/CMSSW_8_0_24/src/MuAlPhysicsValidation/PerformancePlots
eval `scramv1 runtime -sh`
python myPlot_Zmumu_dataMC.py
