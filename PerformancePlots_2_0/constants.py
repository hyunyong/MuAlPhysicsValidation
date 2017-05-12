

c1 = TCanvas("c1", "c1", 600, 600)



########################################################################################
##
## Make Profile Constants
##
########################################################################################

nBins = 10
nGausFit = 1.5
drawBinPlots = True
nBins = 16

ptResMeanRange = -.001,.002
ptResSigmaRange = .00, .008

ptResGLBMeanRange = -.01,.01
ptResGLBSigmaRange = .00, .2


ptResSTAMeanRange = -.5,.5
ptResSTASigmaRange = 0, .6

ptResType2STAMeanRange = -.1,.1
ptResType2STASigmaRange = 0, .3

ptPullSTAMeanRange = -10,10
ptPullSTASigmaRange = 0, 30

ptPullGLBMeanRange = -.3,.3
ptPullGLBSigmaRange = 0, 3

massMeanRange = 80, 100
massSigmaRange = 0, 20

nChi2MeanRange = .5, 2
nChi2RMSRange = 0, 1

nHitsMeanRange = 30, 60
nHitsRMSRange = 8, 12

isMC = False

verbose = 5
