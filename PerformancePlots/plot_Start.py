import ROOT, sys, array, os, re, math, random
from math import *
from array import array

ROOT.gROOT.SetBatch(1)
execfile("tdrStyle.py")

# Define different canvas headers:
ch_Data2011 = "CMS Prelim. 2011   #sqrt{s} = 7 TeV   L_{int} = 5.3 fb^{-1}"
ch_Data2015 = "CMS Prelim. 2015   #sqrt{s} = 13 TeV   L_{int} = 2.6 fb^{-1}"
ch_Data2016 = "CMS Prelim. 2016   #sqrt{s} = 13 TeV   L_{int} = 0.6 fb^{-1}"
#ch_Data2011 = "CMS 2011   #sqrt{s} = 7 TeV   L_{int} = 5.3 fb^{-1}"
#ch_Data2012AB = "CMS Prelim. 2012 A+B   #sqrt{s} = 8 TeV   L_{int} = 5.7 fb^{-1}"
#ch_Data2012AB = "CMS 2012 A+B   #sqrt{s} = 8 TeV   L_{int} = 5.7 fb^{-1}"
ch_CmsSim = "CMS Simulation"
