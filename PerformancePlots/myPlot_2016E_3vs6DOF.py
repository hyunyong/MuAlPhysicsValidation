execfile("plot_Start.py")
mainScriptName, ext = os.path.splitext(__file__)
execfile("plot_setArea.py")

maxEntries = -1

#Color codes:  2 - red, 4 - blue, 6 - magenta, 7 - cyan, 8 - dark green
# 0 - header of canvas (first histo drawn on canvas sets the header)
# 1 - legend for the sample
# 2 - short name of the sample (used in names of plots)
# 3 - 2D array (1) color for the sample and (2) marker style
# 4 - number of entries from the sample to process
# 5 - name of input file for the sample

folder = "./ROOT/"
samples = [
[ch_Data2016E, "2016E 3 DOF", "2016E 3 DOF",[ ROOT.kRed,   24 ], maxEntries, "../MuAlAnalyzer/MuAlRefit_Run2016E_RAWreco_DT3DOF_CSC3DOF_02/FINALFILE.root"],
#[ch_Data2016E, "2016E 6 DOF", "2016E 6 DOF",[ ROOT.kBlue,  21 ], maxEntries, "../MuAlAnalyzer/MuAlRefit_Run2016E_RAWreco_DT6DOF_CSC3DOF_01/FINALFILE.root"],
#[ch_Data2016E, "2016E 6 DOF APE", "2016E 6 DOF APE",[ ROOT.kBlack,  22 ], maxEntries, "../MuAlAnalyzer/MuAlRefit_Run2016E_RAWreco_DT6DOF_CSC3DOF_APE02/FINALFILE.root"],
[ch_MC, "Zmumu MC", "Zmumu MC",[80,  33 ], maxEntries, "../MuAlAnalyzer/MuAlRefit_Ideal_MC_Zmumu/FINALFILE.root"],
]

execfile("plot_checkSamples.py")

threshold_pT_GeV = 30

pt_bin, pt_min, pt_max = 125, 0, 250
ptRes_bin, ptRes_min, ptRes_max = 100, -0.01, 0.01
ptResFitSigma_bin, ptResFitSigma_min, ptResFitSigma_max = 80, 0., 0.008
ptResFitMean_bin, ptResFitMean_min, ptResFitMean_max = 300, -0.001, 0.002
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
#   [0]
  [0,1]
#  [0,3],
#  [1,2],
#  [0,2],
#  [0,1,2,3]
]

execfile("plot_drawHistos.py")
