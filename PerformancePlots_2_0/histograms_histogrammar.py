from ROOT import TH1F, TCanvas, TProfile, TProfile2D, TProfile3D, TH2F
from array import array
import numpy
from histogrammar import *



Bundle = UntypedLabel


#leadingMuonPt = Bin("leadingMuonPt", "leading #mu p_{T}; p_{T}; counts", 100, 0, 1000)

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

standard_histograms = Select( lambda array: numpy.logical_and(array['glb_trk_pt'] > thresholdPt ,abs(array['glb_trk_eta']) < 2.4),
                        Select( lambda array: numpy.logical_and(array['glb'] == True ,abs(array['sta']) == True ),
                        Select( lambda array: numpy.logical_and(array['sta_pt'] != 0 ,abs(array['glb_trk_eta']) != 0), Bundle(
##
## phi
##

D1_sta_trk_delta_phi = Bin( phiResBins, phiResMin, phiResMax, 
    lambda array : (array['glb_trk_phi']- array['sta_phi'])/array['glb_phi_error'], Count() ),

D1_sta_trk_delta_phi_barrel = Select(lambda array: abs(array['glb_eta']) < .9 , 
    Bin(phiResBins, phiResMin, phiResMax, lambda array : (array['glb_trk_phi']- array['sta_phi'])/array['glb_phi_error'], Count() )),

D1_sta_trk_delta_phi_endcap = Select(lambda array: abs(array['glb_eta']) > .9 , 
    Bin(phiResBins, phiResMin, phiResMax, lambda array : (array['glb_trk_phi']- array['sta_phi'])/array['glb_phi_error'], Count() )),



D1_sta_glb_delta_phi = Bin( phiResBins, phiResMin, phiResMax, 
    lambda array : (array['glb_phi']- array['sta_phi'])/array['glb_phi_error'], Count() ),

D1_sta_glb_delta_phi_barrel = Select(lambda array: abs(array['glb_eta']) < .9 , 
    Bin(phiResBins, phiResMin, phiResMax, lambda array : (array['glb_phi']- array['sta_phi'])/array['glb_phi_error'], Count() )),

D1_sta_glb_delta_phi_endcap = Select(lambda array: abs(array['glb_eta']) > .9 , 
    Bin(phiResBins, phiResMin, phiResMax, lambda array : (array['glb_phi']- array['sta_phi'])/array['glb_phi_error'], Count() )),

##
## nchi2
##


D1_glb_nChi2_barrel = Select(lambda array: abs(array['glb_eta']) < .9 , 
    Bin(nChi2Bins, nChi2Min, nChi2Max, lambda array : array['glb_nchi2'], Count() )),

D1_glb_nChi2_endcap = Select(lambda array: abs(array['glb_eta']) > .9 , 
    Bin(nChi2Bins, nChi2Min, nChi2Max, lambda array : array['glb_nchi2'], Count() )),

D1_sta_nChi2 = Bin(nChi2Bins, nChi2Min, nChi2Max, 
    lambda array : array['sta_nchi2'], Count() ),

D1_sta_nChi2_barrel = Select(lambda array: abs(array['glb_eta']) < .9 , 
    Bin(nChi2Bins, nChi2Min, nChi2Max, lambda array : array['sta_nchi2'], Count() )),

D1_sta_nChi2_endcap = Select(lambda array: abs(array['glb_eta']) > .9 , 
    Bin(nChi2Bins, nChi2Min, nChi2Max, lambda array : array['sta_nchi2'], Count() )),


D2_glb_eta_nChi2 = Bin( etaBins, etaMin, etaMax, lambda array: array['glb_eta'], 
    Bin( nBins, nChi2Range[0], nChi2Range[1], lambda array: array['glb_nchi2'], Count() )),

D2_glb_pt_nChi2 = Bin( ptBins, ptMin, ptMax, lambda array: array['glb_pt'], 
    Bin( nBins, nChi2Range[0], nChi2Range[1], lambda array: array['glb_nchi2'], Count() )),

D2_sta_pt_nChi2 = Bin( ptBins, ptMin, ptMax, lambda array: array['sta_pt'], 
    Bin( nBins, nChi2Range[0], nChi2Range[1], lambda array: array['glb_nchi2'], Count() )),

D2_sta_eta_nChi2 = Bin( ptBins, ptMin, ptMax, lambda array: array['sta_eta'], 
    Bin( nBins, nChi2Range[0], nChi2Range[1], lambda array: array['glb_nchi2'], Count() )),

##
## nHits
##



D2_glb_eta_nHits = Bin( 48, -2.4, 2.4, lambda array: array['glb_eta'], 
    Bin( 24, 0, 75, lambda array: array['glb_nhits'], Count() )),

D2_glb_pt_nHits = Bin( ptBins, ptMin, ptMax, lambda array: array['glb_pt'], 
    Bin( nBins, nHitsRange[0], nHitsRange[1], lambda array: array['glb_nhits'], Count() )),

##
## ptRes
##

D2_glb_sta_eta_ptRes = Bin( etaBins, etaMin, etaMax, lambda array: array['glb_eta'], 
    Bin( ptResBins, ptResMin, ptResMax, lambda array: array['ptResSTAGLB'], Count() )),

D2_glb_sta_pt_ptRes = Bin( ptBins, ptMin, ptMax, lambda array: array['glb_pt'], 
    Bin( ptResBins, ptResMin, ptResMax, lambda array: array['ptResSTAGLB'], Count() )),

D2_glb_sta_phi_ptRes = Bin( phiBins, phiMin, phiMax, lambda array: array['glb_phi'], 
    Bin( ptResBins, ptResMin, ptResMax, lambda array: array['ptResSTAGLB'], Count() )),

D2_glb_sta_phi_ptRes_barrel = Select(lambda array: abs(array['glb_eta']) < .9 , 
    Bin( phiBins, phiMin, phiMax, lambda array: array['glb_phi'], 
    Bin( ptResBins, ptResMin, ptResMax, lambda array: array['ptResSTAGLB'], Count() ))),


D2_glb_sta_phi_ptRes_endcap = Select(lambda array: abs(array['glb_eta']) > .9 , 
    Bin( phiBins, phiMin, phiMax, lambda array: array['glb_phi'], 
    Bin( ptResBins, ptResMin, ptResMax, lambda array: array['ptResSTAGLB'], Count() ))),


##
##  ptPull
##

D2_glb_sta_eta_ptPull = Bin( etaBins, etaMin, etaMax, lambda array: array['glb_eta'], 
    Bin( nBins, ptPullRange[0], ptPullRange[1], lambda array: array['ptPullSTAGLB'], Count() )),

D2_glb_sta_pt_ptPull = Bin( ptBins, ptMin, ptMax, lambda array: array['glb_pt'], 
    Bin( nBins, ptPullRange[0], ptPullRange[1], lambda array: array['ptPullSTAGLB'], Count() )),

D2_glb_sta_phi_ptPull = Bin( phiBins, phiMin, phiMax, lambda array: array['glb_phi'], 
    Bin( nBins, ptPullRange[0], ptPullRange[1], lambda array: array['ptPullSTAGLB'], Count() )),



))))


gen_histograms = Select( lambda array: array['glb_trk_pt'] > thresholdPt, Bundle(
##
## ptRes
##

D2_gen_glb_eta_ptRes = Bin( etaBins, etaMin, etaMax, lambda array: array['glb_gen_eta'], 
    Bin( ptResBins, ptResMin, ptResMax, lambda array: array['ptResGLBGEN'], Count() )),

D2_gen_glb_pt_ptRes = Bin( ptBins, ptMin, ptMax, lambda array: array['glb_gen_pt'], 
    Bin( ptResBins, ptResMin, ptResMax, lambda array: array['ptResGLBGEN'], Count() )),

D2_gen_glb_phi_ptRes = Bin( phiBins, phiMin, phiMax, lambda array: array['glb_gen_phi'], 
    Bin( ptResBins, ptResMin, ptResMax, lambda array: array['ptResGLBGEN'], Count() )),

D2_gen_glb_phi_ptRes_barrel = Select(lambda array: abs(array['glb_eta']) < .9 , 
    Bin( phiBins, phiMin, phiMax, lambda array: array['glb_gen_phi'], 
    Bin( ptResBins, ptResMin, ptResMax, lambda array: array['ptResGLBGEN'], Count() ))),


D2_gen_glb_phi_ptRes_endcap = Select(lambda array: abs(array['glb_eta']) > .9 , 
    Bin( phiBins, phiMin, phiMax, lambda array: array['glb_gen_phi'], 
    Bin( ptResBins, ptResMin, ptResMax, lambda array: array['ptResGLBGEN'], Count() ))),


##
##  ptPull
##

D2_gen_glb_eta_ptPull = Bin( etaBins, etaMin, etaMax, lambda array: array['glb_gen_eta'], 
    Bin( nBins, ptPullRange[0], ptPullRange[1], lambda array: array['ptPullGLBGEN'], Count() )),

D2_gen_glb_pt_ptPull = Bin( ptBins, ptMin, ptMax, lambda array: array['glb_gen_pt'], 
    Bin( nBins, ptPullRange[0], ptPullRange[1], lambda array: array['ptPullGLBGEN'], Count() )),

D2_gen_glb_phi_ptPull = Bin( phiBins, phiMin, phiMax, lambda array: array['glb_gen_phi'], 
    Bin( nBins, ptPullRange[0], ptPullRange[1], lambda array: array['ptPullGLBGEN'], Count() )),



))


mass_histograms = Select( lambda array: numpy.logical_and(array['pos_glb_trk_pt'] > thresholdPt ,abs(array['pos_glb_trk_eta']) < 2.4), 
                   Select( lambda array: numpy.logical_and(array['neg_glb_trk_pt'] > thresholdPt ,abs(array['neg_glb_trk_eta']) < 2.4), 
                   #Select( lambda array: numpy.logical_and(array['recoMu_neg_IsoPF04'] > 0.15 ,array['recoMu_pos_IsoPF04'] > 0.15), Bundle(
                   #Select( lambda array:   numpy.logical_and(array['glb_m'] < hybridMassValue+hydridMassCut ,array['glb_m'] > hybridMassValue-hydridMassCut),  Bundle(
                   Select( lambda array:   abs(array['glb_m']-hybridMassValue) <hydridMassCut,  Bundle(
 
    D2_sta_glb_pt_HybridSTA_Mass = 
    Bin( ptBins, ptMin, ptMax, lambda array: array['hyb_sta_pt'], 
    Bin( nBins, massMin, massMax, lambda array: array['hyb_m'], Count() )),
    D2_sta_glb_phi_HybridSTA_Mass = 
    Bin( phiBins, phiMin, phiMax, lambda array: array['hyb_sta_phi'], 
    Bin( nBins, massMin, massMax, lambda array: array['hyb_m'], Count() )),

    D2_sta_glb_eta_HybridSTA_Mass = 
    Bin(etaBins,etaMin,etaMax, lambda array: array['hyb_sta_eta'], 
    Bin( nBins, massMin, massMax, lambda array: array['hyb_m'], Count() )),


    ))))
    #)))))

