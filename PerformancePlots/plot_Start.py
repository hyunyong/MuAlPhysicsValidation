import ROOT, sys, array, os, re, math, random
from math import *
from array import array

ROOT.gROOT.SetBatch(1)
execfile("tdrStyle.py")

# Define different canvas headers:
ch_CmsSim = "CMS Simulation"
ch_Data2015 = "CMS Prelim. 2015   #sqrt{s} = 13 TeV   L_{int} = 2.6 fb^{-1}"
ch_Data2016B = "CMS Prelim. 2016B   #sqrt{s} = 13 TeV   L_{int} = 0.87 fb^{-1}"
ch_Data2016E = "CMS Prelim. 2016E   #sqrt{s} = 13 TeV   L_{int} = 4.1 fb^{-1}"
ch_MC = "Zmumu MC #sqrt{s} = 13 TeV"
