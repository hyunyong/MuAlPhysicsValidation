from ROOT import TFile, TTree, TH1F, TLorentzVector, TCanvas, TPaveStats, TLatex, gROOT
from random import randint
import math, sys, os
from math import fabs
gROOT.SetBatch(1)
execfile("constants.py")

# Usage examples:
# python Step1_make_2d_plots.py inputFile outputFolder Treating_Mu_AntiMU (std, use only positive, only negative, equal number)
# python Step1_make_2d_plots.py /afs/cern.ch/work/l/lpernie/MuonAlign/WD/CMSSW_9_4_0_pre3/src/MuAlPhysicsValidation/MuAlAnalyzer/MuAlRefit_Run2017part1_RAWreco_rerecov2 MuAlRefit_Run2017part1_RAWreco_rerecov2 std -b # std,pos,neg,equal
# python Step1_make_2d_plots.py /eos/cms/store/group/alca_muonalign/lpernie/MuAlAnalyzer/MuAlRefit_Run2017B_RAWreco_2016Geom_01.root MuAlRefit_2017B_2016Geom std -b # std,pos,neg,equal
# python Step1_make_2d_plots.py /eos/cms/store/group/alca_muonalign/lpernie/MuAlAnalyzer/MuAlRefit_Legacy.root MuAlRefit_2016Perform std -b # std,pos,neg,equal
# python Step1_make_2d_plots.py /eos/cms/store/group/alca_muonalign/lpernie/MuAlAnalyzer/MuAlRefit_Run2017B_RAWreco_DT6DOFCSC3DOF.root MuAlRefit_2017B_DT6DOFCSC3DOF std -b
# python Step1_make_2d_plots.py /eos/cms/store/group/alca_muonalign/lpernie/MuAlAnalyzer/MuAlRefit_Run2017B_RAWRECO_DT3DOFnoT0it1CSC3DOF.root MuAlRefit_2017B_DT3DOFnoT0it1CSC3DOF std -b
# python Step1_make_2d_plots.py /eos/cms/store/group/alca_muonalign/lpernie/MuAlAnalyzer/MuAlRefit_Run2017B_RAWRECO_DT3DOFnoT0it1CSC3DOF_1refit.root MuAlRefit_2017B_DT3DOFnoT0it1CSC3DOF_1refit std -b
# python Step1_make_2d_plots.py /eos/cms/store/group/alca_muonalign/lpernie/MuAlAnalyzer/MuAlRefit_Run2017B_RAWRECO_DT6DOFnoT0it1CSC3DOF_Official.root MuAlRefit_2017B_DT6DOFnoT0it1CSC3DOF_Official std -b
# python Step1_make_2d_plots.py /eos/cms/store/group/alca_muonalign/lpernie/MuAlAnalyzer/MuAlRefit_Run2017B_RAWRECO_DT6DOFnoT0it1CSC3DOF_OfficialAPEDTminuit_CSCasym.root MuAlRefit_2017B_DT6DOFnoT0it1CSC3DOF_OfficialAPEDTminuit_CSCasym std -b
# python Step1_make_2d_plots.py /eos/cms/store/group/alca_muonalign/lpernie/MuAlAnalyzer/MuAlRefit_Run2017B_RAWreco_FromGT.root MuAlRefit_2017B_fromGT std -b

#python Step1_make_2d_plots.py MuAlRefit_Run2018A_+2018MuonGeom_narrowAPEs_2.root pyroot_test std -b

# input arguments, first is input root file, second is output root file 
fileIn = sys.argv[1]
fileOut = sys.argv[2]
method = sys.argv[3]
if(method!="std" and method!="pos" and method!="neg" and method!="equal"):
  print "WARNIGN! method is unknown, options are std,pos,neg,equal";

# read the input root file
f            = TFile.Open(fileIn, "read")
td           = f.Get("muAlAnalyzer")
Events       = td.Get("Events")
genMuons     = td.Get("genMuons")
recoMuons    = td.Get("recoMuons")
recoDimuons  = td.Get("recoDimuons")
savePng      = True
Event_ro_RUN = 10000000

## First step, define your histograms in histograms.py
execfile("functions.py")
execfile("histograms.py")
## Second step, fill recoMuon and recoDimuon histograms  
execfile("recoMuonLoop.py")
execfile("recoDimuonLoop.py")
execfile("drawPng.py")

outFile.Write()
outFile.Close()
