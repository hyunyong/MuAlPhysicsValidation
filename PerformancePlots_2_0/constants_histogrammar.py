verbosity = 0

isMC = False

ptBins = 48
ptMin = 0
ptMax = 200

thresholdPt = 30.0

phiBins = 48
phiMin = -3.2
phiMax = 3.2

phiResBins = 48
phiResMin = -100
phiResMax = 100

etaBins = 48
etaMin = -2.4
etaMax = 2.4

ptResBins = 48
ptResMin = -0.1
ptResMax = 0.1
#ptResMin = -0.7 for other definition as seen in code but commented out
#ptResMax = 0.7


massBins = 48
massMin = 60
massMax = 120

hydridMassCut = 5.
hybridMassValue = 91.


nChi2Bins = 48
nChi2Min = 0
nChi2Max = 3

nBins = 48

nHitsRange = [0,75]

nChi2Range = [0,4]

ptPullRange = [-2.8, 2.8]
ptResSTA = [-.75,.75]
ptResSTAType2 = [-1,1]

ptResGLB = [-.1,.1]

deltaPhiRange = .03
phiErrorRange = .001


##############

isMC = False
#Step 1
ptBins = 48
ptMin = 0
ptMax = 200
thresholdPt = 30.0

phiBins = 48
phiMin = -3.2
phiMax = 3.2
phiResBins = 48
phiResMin = -100
phiResMax = 100

etaBins = 48
etaMin = -2.4
etaMax = 2.4
ptResBins = 48
ptResMin = -0.1
ptResMax = 0.1

massBins = 48
massMin = 60
massMax = 120

hydridMassCut = 10.
hybridMassValue = 91.
nChi2Bins = 48
nChi2Min = 0
nChi2Max = 3

nBins = 48
nHitsRange = [0,75]
nChi2Range = [0,4]
ptPullRange = [-100, 100]
ptResSTA = [-.75,.75]
ptResSTAType2 = [-1,1]
ptResGLB = [-.1,.1]

# Step 2
nBins = 10
nGausFit = 1.1
drawBinPlots = True
nBins = 16

ptResMeanRange = -.003,.003
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


##############