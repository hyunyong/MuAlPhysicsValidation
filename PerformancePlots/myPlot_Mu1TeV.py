execfile("plot_Start.py")
mainScriptName, ext = os.path.splitext(__file__)
execfile("plot_setArea.py")

folder = "/home/pakhotin/Work/CMS_My_Service_Work/Muon_Alignment/2015/2015-11-10_MuAl_PerformancePlots/PerformancePlots/ROOT/"

maxEntries = -1

#Color codes:  2 - red, 4 - blue, 6 - magenta, 7 - cyan, 8 - dark green
# 0 - header of canvas (first histo drawn on canvas sets the header)
# 1 - legend for the sample
# 2 - short name of the sample (used in names of plots)
# 3 - 2D array (1) color for the sample and (2) line style
# 4 - number of entries from the sample to process
# 5 - name of input file for the sample

samples = [
[ch_CmsSim, "Muon 1 TeV MC + new 2011 scenario",    "MCMu1TeVNew2011", [ ROOT.kBlue, 24 ],
  maxEntries, folder+"muAlAnalyzer_singleMuonGun_pT-1TeV_Ideal_GEN-SIM-RECO_v1__MC_Scenario2011__v2.root"], # 0
[ch_CmsSim, "Muon 1 TeV MC + EXO Pes. scenario",          "MCMu1TeVExoPes",  [ ROOT.kMagenta, 22 ],
  maxEntries, folder+"muAlAnalyzer_singleMuonGun_pT-1TeV_Ideal_GEN-SIM-RECO_v1__MC_ExoPessim__v2.root"],    # 1
[ch_CmsSim, "Muon 1 TeV MC + former 2011 scenario", "MCMu1TeVOld2011", [ ROOT.kGreen+2, 23 ],
  maxEntries, folder+"muAlAnalyzer_singleMuonGun_pT-1TeV_Ideal_GEN-SIM-RECO_v1__START53_V14__v2.root"],     # 2
[ch_CmsSim, "Muon 1 TeV MC + Ideal scenario",       "MCMu1TeVIdeal",   [ ROOT.kCyan, 21 ],
  maxEntries, folder+"muAlAnalyzer_singleMuonGun_pT-1TeV_Ideal_GEN-SIM-RECO_v1.root"],                      # 3
]

execfile("plot_checkSamples.py")

pt_bin, pt_min, pt_max = 150, 0, 1500
 
execfile("plot_setHistos.py")

# additional histograms should be added here

execfile("plot_initHistos.py")

execfile("plot_analyzeSamples.py")

execfile("plot_fitHistos.py")
execfile("plot_fillProfiles.py")

# Don't combine more than 4 histos on one plot
combineHistos = [
  [ 0 ],
  [ 1 ],
  [ 2 ],
  [ 3 ],
  [ 0, 2 ],
  [ 0, 1, 2 ],
  [ 0, 1, 2, 3 ],
]

execfile("plot_drawHistos.py")
