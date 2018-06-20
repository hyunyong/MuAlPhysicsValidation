from ROOT import TFile, TTree, TH1F, TLorentzVector, TMath, TRandom
import ROOT
from random import randint
import math, sys, os
from math import fabs
from histogrammar import *
import time

# Usage examples:
# python make_2d_plots.py ../MuAlAnalyzer/MuAlRefit_Legacy/MuAlRefit_Legacy.root MuAlRefit_Legacy std -b # std,pos,neg,equal
# python Step1_make_2d_plots.py root://eoscms.cern.ch//eos/cms/store/group/alca_muonalign/lpernie/MuAlAnalyzer/MuAlRefit_Legacy.root MuAlRefit_Legacy_out std -b
# python Step1_make_2d_plots.py MuAlRefit_Legacy.root MuAlRefit_Legacy_Out std -b
# python Step1_make_2d_plots.py MuAlRefit_Prompt.root MuAlRefit_Prompt_Out std -b
# python Step1_make_2d_plots_histogrammar.py MuAlRefit_Prompt.root MuAlRefit_Prompt_Out_test std -b
# python Step1_make_2d_plots_histogrammar.py MuAlRefit_Legacy.root MuAlRefit_Legacy_out_test std -b

# python Step1_make_2d_plots_histogrammar.py MuAlRefit_Legacy.root MuAlRefit_Legacy_out_test std -b

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
Event_ro_RUN = 1000099
#Events.Print(); genMuons.Print(); recoMuons.Print(); recoDimuons.Print()

startTime = time.time()
## First step, define your histograms in histograms.py
execfile("functions.py")
execfile("histograms_histogrammar.py")
execfile("recoMuonLoopHistogrammar.py")
## Second step, fill recoMuon and recoDimuon histograms  
#execfile("recoMuonLoop.py")
#execfile("recoDimuonLoop.py")
execfile("drawPng.py")
endTime = time.time()

print "This took", endTime - startTime, "seconds (including compilation)."

outFile.Write()
outFile.Close()
