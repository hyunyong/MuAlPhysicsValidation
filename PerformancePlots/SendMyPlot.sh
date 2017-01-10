#!/bin/bash
cd /afs/cern.ch/work/l/lpernie/MuonAlign/WD/CMSSW_8_0_24/src/MuAlPhysicsValidation/PerformancePlots
eval `scramv1 runtime -sh`
python myPlot_MuAl2016_rereco2016G_v1.py
