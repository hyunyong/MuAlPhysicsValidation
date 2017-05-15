from ROOT import TFile, TTree, TH1F, TLorentzVector
from ROOT import TLorentzVector
from random import randint
import math, sys, os
from math import fabs
#RUN WITH:
#python make_2d_plots.py ../MuAlAnalyzer/MuAlRefit_Legacy/MuAlRefit_Legacy.root MuAlRefit_Legacy std -b # std,pos,neg,equal

# input arguments, first is input root file, second is output root file 
fileIn = sys.argv[1]
fileOut = sys.argv[2]
method = sys.argv[3]
oldTTrees = sys.argv[4]=="oldTTrees"
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
Event_ro_RUN = -1
#Events.Print(); genMuons.Print(); recoMuons.Print(); recoDimuons.Print()

## First step, define your histograms in histograms.py
execfile("functions.py")
execfile("histograms.py")
## Second step, fill recoMuon and recoDimuon histograms  
execfile("recoMuonLoop.py")
execfile("recoDimuonLoop.py")
execfile("drawPng.py")

outFile.Write()
outFile.Close()
