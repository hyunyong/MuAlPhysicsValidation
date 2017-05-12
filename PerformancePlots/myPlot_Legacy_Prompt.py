execfile("plot_Start.py")
mainScriptName, ext = os.path.splitext(__file__)
execfile("plot_setArea.py")

#maxEntries = -1 #2500000
maxEntries = 3000000

#Color codes:  2 - red, 4 - blue, 6 - magenta, 7 - cyan, 8 - dark green
# 0 - header of canvas (first histo drawn on canvas sets the header)
# 1 - legend for the sample
# 2 - short name of the sample (used in names of plots)
# 3 - 2D array (1) color for the sample and (2) marker style
# 4 - number of entries from the sample to process
# 5 - name of input file for the sample

samples = [
[ch_Data2016H, "2016H Legacy", "2016H Legacy",[ ROOT.kBlack, 24 ], maxEntries, "../MuAlAnalyzer/MuAlRefit_Legacy/MuAlRefit_Legacy.root"],
#[ch_Data2016H, "2016H Legacy loc", "2016H Legacy loc",[ ROOT.kBlue, 24 ], maxEntries, "../MuAlAnalyzer/MuAlRefit_Legacy_dbLocal/MuAlRefit_Legacy_dbLocal.root"],
#[ch_Data2016H, "2016H Legacy APE min", "2016H APE min",[ ROOT.kGreen, 24 ], maxEntries, "../MuAlAnalyzer/MuAlRefit_Legacy_APEminuitx2/MuAlRefit_Legacy_APEminuitx2.root"],
[ch_Data2016H, "2016H Prompt", "2016H Prompt",[ ROOT.kRed,   24 ], maxEntries, "../MuAlAnalyzer/MuAlRefit_Prompt/MuAlRefit_Prompt.root"],
]

execfile("plot_checkSamples.py")

threshold_pT_GeV = 30

pt_bin, pt_min, pt_max = 125, 0, 250
ptRes_bin, ptRes_min, ptRes_max = 100, -0.01, 0.01
ptResFitSigma_bin, ptResFitSigma_min, ptResFitSigma_max = 80, 0., 0.007
ptResFitMean_bin, ptResFitMean_min, ptResFitMean_max = 300, -0.003, 0.003
mFitSigma_bin, mFitSigma_min, mFitSigma_max = 50, 3, 13
mFitMean_bin, mFitMean_min, mFitMean_max = 40, 80, 100
 
execfile("plot_setHistos.py")

# additional histograms should be added here
execfile("plot_initHistos.py")
execfile("plot_analyzeSamples.py")
execfile("plot_fitHistos.py")
execfile("plot_fillProfiles.py")

# Don't combine more than 4 histos on one plot
combineHistos = [ 
  [0,1],
  [0,3],
  [0,2,3]
]

execfile("plot_drawHistos.py")
