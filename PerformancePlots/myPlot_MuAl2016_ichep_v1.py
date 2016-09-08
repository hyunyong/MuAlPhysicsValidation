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
[ch_Data2016B, "2016 (prompt)","2016Prompt",[ ROOT.kBlack, 20 ], maxEntries, "../MuAlAnalyzer/ana_PromptGT_TrackerMay2016_v1/FINALNTUPLES_2.root"],
[ch_Data2016B, "2016",         "2016",      [ ROOT.kRed,   24 ], maxEntries, "../MuAlAnalyzer/ana_PromptGT_TrackerMay2016_MuAlMay2016_v1/FINALNTUPLES_2.root"],
[ch_Data2016B, "2015",         "2015",      [ ROOT.kBlue,  21 ], maxEntries, "/afs/cern.ch/cms/CAF/CMSALCA/ALCA_MUONALIGN/www/muonGeometries/2015-11_data_Fall15AlignmentWithRun2015D/PhysValidation/ROOT/MuAlAnalyzer_refit_newGT_MuAlNov2015_v1.root"],
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
#  [0], [1], [2],
#  [0,1], [0,2],
  [0,1],
  [0,1,2]
]

execfile("plot_drawHistos.py")
