# Parameters
IntLumi = "L_{int}=3.7 fb^{-1} (13 TeV)"
DataStr = "2017 pp Data"

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


phiResBins = 200
phiResMin = -0.1
phiResMax = 0.1



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
ptPullRange = [-2.8, 2.8]
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

massMeanRange = 85, 95
massSigmaRange = 0, 20

DEmassMeanRange = 90, 92
DEmassSigmaRange = 0, 10
DEnBins = 12
DEetaMin = -3.5
DEetaMax = 3.5


nChi2MeanRange = .5, 2
nChi2RMSRange = 0, 1

nHitsMeanRange = 30, 60
nHitsRMSRange = 8, 12

c1 = TCanvas("Canvas_1", "Canvas_1",600,600)
#c1 = TCanvas("Canvas_1", "Canvas_1",485,176,700,600)
#c1.Range(42.21429,-38.745,102.9286,284.13)
c1.SetFillColor(0)
c1.SetBorderMode(0)
c1.SetBorderSize(2)
c1.SetLeftMargin(0.12)
c1.SetRightMargin(0.04)
c1.SetTopMargin(0.08)
c1.SetBottomMargin(0.12)
c1.SetFrameFillStyle(0)
c1.SetFrameBorderMode(0)
c1.SetFrameFillStyle(0)
c1.SetFrameBorderMode(0)
ptstats = TPaveStats(0.5,0.73,0.7 ,0.88,"brNDC")
ptstats.SetBorderSize(0)
ptstats.SetFillColor(0)
ptstats.SetTextSize(0.04)

texLumi = TLatex(0.96,0.936, IntLumi)
texLumi.SetNDC()
texLumi.SetTextAlign(31)
texLumi.SetTextFont(52)
texLumi.SetTextSize(0.04)
texData = TLatex(0.15,0.905,DataStr)
texData.SetNDC()
texData.SetTextAlign(13)
texData.SetTextFont(52)
texData.SetTextSize(0.04)
texPrelim = TLatex(0.15,0.96,"CMS Preliminary")
texPrelim.SetNDC()
texPrelim.SetTextAlign(13)
texPrelim.SetTextFont(52)
texPrelim.SetTextSize(0.04)
