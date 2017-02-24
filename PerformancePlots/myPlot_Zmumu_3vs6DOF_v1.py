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
[ch_MC, "MC 6DOF covAPE2","MC_6DOF_covAPE2",[ ROOT.kViolet,  20 ],maxEntries, "../MuAlAnalyzer/MuAlRefit_Zmumu_DT6DOF_CSCideal_APEcovx2_01/MuAlRefit_Zmumu_DT6DOF_CSCideal_APEcovx2_01.root"],
[ch_MC, "MC 6DOF covAPE","MC_6DOF_covAPE",  [ ROOT.kRed,  20 ],   maxEntries, "../MuAlAnalyzer/MuAlRefit_Zmumu_DT6DOF_CSCideal_APEcov_01/MuAlRefit_Zmumu_DT6DOF_CSCideal_APEcov_01.root"],
[ch_MC, "MC 6DOF diaAPE","MC_6DOF_diaAPE",  [ ROOT.kOrange,20 ],  maxEntries, "../MuAlAnalyzer/MuAlRefit_Zmumu_DT6DOF_CSCideal_APEdia_01/MuAlRefit_Zmumu_DT6DOF_CSCideal_APEdia_01.root"],
[ch_MC, "MC 3DOF diaAPE","MC_3DOF_diaAPE",  [ ROOT.kBlue, 24 ],   maxEntries, "../MuAlAnalyzer/MuAlRefit_Zmumu_DT3DOF_CSCideal_APEdia_01/MuAlRefit_Zmumu_DT3DOF_CSCideal_APEdia_01.root"],
[ch_MC, "MC ideal",      "Zmumu_MC",        [80,  33 ],           maxEntries, "../MuAlAnalyzer/MuAlRefit_Ideal_MC_Zmumu/FINALFILE.root"],
]

execfile("plot_checkSamples.py")

threshold_pT_GeV = 30

pt_bin, pt_min, pt_max = 125, 0, 250
ptRes_bin, ptRes_min, ptRes_max = 100, -0.01, 0.01
ptResFitSigma_bin, ptResFitSigma_min, ptResFitSigma_max = 80, 0., 0.008
ptResFitMean_bin, ptResFitMean_min, ptResFitMean_max = 300, -0.001, 0.002
mFitSigma_bin, mFitSigma_min, mFitSigma_max = 60, 0., 30
mFitMean_bin, mFitMean_min, mFitMean_max = 40, 80, 100
 
execfile("plot_setHistos.py")

# additional histograms should be added here

execfile("plot_initHistos.py")

execfile("plot_analyzeSamples.py")

execfile("plot_fitHistos.py")
execfile("plot_fillProfiles.py")

# Don't combine more than 4 histos on one plot
combineHistos = [ 
  [0,1,2,3,4],
  [0,1,2,3]
]

execfile("plot_drawHistos.py")
