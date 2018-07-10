from ROOT import TFile, TTree, TH1F, TLorentzVector, TMath, TRandom, TCanvas
import ROOT
from random import randint
import math, sys, os
from math import fabs
from histogrammar import *
import time

# Usage examples:

# python step1_refactor.py MuAlRefit_Run2018A_+2018MuonGeom_narrowAPEs_2.root histogrammar_test std -b



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
isMC		 = False
Event_to_RUN = 100000
#Events.Print(); genMuons.Print(); recoMuons.Print(); recoDimuons.Print()



print "opening file: ", fileIn
print "creating file: ", fileOut





startTime = time.time()
## First step, define your histograms in histograms.py
#execfile("histograms_histogrammar.py")
from histograms_histogrammar import standard_histograms, gen_histograms, mass_histograms

from recoMuonLoopHistogrammar import recoMuonTree2Array, diMuonTree2Array, genMuonTree2Array

recoMuonArray = recoMuonTree2Array(recoMuons, Event_to_RUN)

diMuonArray = diMuonTree2Array(recoDimuons, Event_to_RUN)

standard_histograms.fill.numpy(recoMuonArray)

mass_histograms.fill.numpy(diMuonArray)

gen_histograms = False

if isMC:
    recoMuonArrayMC = genMuonTree2Array(recoMuons, Event_to_RUN)

    gen_histograms.fill.numpy(recoMuonArrayMC)

from histogrammarToRoot import histogrammarToRoot

histogrammarToRoot(standard_histograms, mass_histograms, gen_histograms, fileOut, savePng)


endTime = time.time()

print "This took", endTime - startTime, "seconds (including compilation)."

