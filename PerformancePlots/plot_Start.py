import ROOT, sys, array, os, re, math, random
from math import *
from array import array

ROOT.gROOT.SetBatch(1)
execfile("tdrStyle.py")

# Define different canvas headers:
ch_CmsSim = "CMS Simulation"
ch_Data2016G = "CMS Prelim. 2016G   #sqrt{s} = 13 TeV   L_{int} = 7.5 fb^{-1}"
ch_Data2016H = "CMS Prelim. 2016H   #sqrt{s} = 13 TeV   L_{int} = 9.2 fb^{-1}"
ch_Data2017B = "CMS Prelim. 2017B   #sqrt{s} = 13 TeV   L_{int} = 3.6 fb^{-1}"
ch_MC = "Zmumu MC #sqrt{s} = 13 TeV"
