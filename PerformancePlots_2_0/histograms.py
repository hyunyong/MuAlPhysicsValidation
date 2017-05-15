from ROOT import TH1F, TCanvas, TProfile, TProfile2D, TProfile3D, TH2F
from array import array

c1 = TCanvas("c1", "c1", 600, 400)

print "opening file: ", fileIn
print "creating file: ", fileOut

outFile = TFile("{}.root".format(fileOut), "recreate")


#leadingMuonPt = TH1F("leadingMuonPt", "leading #mu p_{T}; p_{T}; counts", 100, 0, 1000)

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

#glb gen 

TH2F_glb_gen_pt_ptRes = TH2F("glb_gen_pt_v_ptRes"," glb vs gen p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResMin, ptResMax )
TH2F_glb_gen_eta_ptRes = TH2F("glb_gen_eta_v_ptRes"," glb vs gen p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResMin, ptResMax )

#sta gen
TH2F_sta_gen_pt_ptRes = TH2F("sta_gen_pt_v_ptRes"," sta vs gen p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResSTA[0], ptResSTA[1] )
TH2F_sta_gen_eta_ptRes = TH2F("sta_gen_eta_v_ptRes"," sta vs gen p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResSTA[0], ptResSTA[1])

##
## phi
##

TH1F_sta_glb_delta_phi_barrel = TH1F("TH1F_sta_glb_delta_phi_barrel", "(#phi_{GLB}-#phi_{STA})/#phi_{GLB Error}  |#eta| < 0.9; #delta #phi",phiResBins, phiResMin, phiResMax )
TH1F_sta_glb_delta_phi_endcap = TH1F("TH1F_sta_glb_delta_phi_endcap", "(#phi_{GLB}-#phi_{STA})/#phi_{GLB Error}  |#eta| > 0.9; #delta #phi",phiResBins, phiResMin, phiResMax )
TH1F_sta_glb_delta_phi = TH1F("TH1F_sta_glb_delta_phi", "(#phi_{GLB}-#phi_{STA})/#phi_{GLB Error}; #delta #phi",phiResBins, phiResMin, phiResMax )

TH1F_sta_TRK_delta_phi_barrel = TH1F("TH1F_sta_TRK_delta_phi_barrel", "(#phi_{TRK}-#phi_{STA})/#phi_{GLB Error}  |#eta| < 0.9; #delta #phi",phiResBins, phiResMin, phiResMax )
TH1F_sta_TRK_delta_phi_endcap = TH1F("TH1F_sta_TRK_delta_phi_endcap", "(#phi_{TRK}-#phi_{STA})/#phi_{GLB Error}  |#eta| > 0.9; #delta #phi",phiResBins, phiResMin, phiResMax )
TH1F_sta_TRK_delta_phi = TH1F("TH1F_sta_TRK_delta_phi", "(#phi_{TRK}-#phi_{STA})/#phi_{GLB Error}; #delta #phi",phiResBins, phiResMin, phiResMax )



##
## nchi2
##

TH1F_sta_nChi2_barrel = TH1F("TH1F_sta_nChi2_barrel", "sta n#chi^{2} |#eta| < 0.9; n#chi^2",nChi2Bins, nChi2Min, nChi2Max )
TH1F_sta_nChi2_endcap = TH1F("TH1F_sta_nChi2_endcap", "sta n#chi^{2} |#eta| > 0.9; n#chi^2",nChi2Bins, nChi2Min, nChi2Max )
TH1F_glb_nChi2_endcap = TH1F("TH1F_glb_nChi2_endcap", "glb n#chi^{2} |#eta| > 0.9; n#chi^2",nChi2Bins, nChi2Min, nChi2Max )
TH1F_glb_nChi2_barrel = TH1F("TH1F_glb_nChi2_barrel", "glb n#chi^{2} |#eta| < 0.9; n#chi^2",nChi2Bins, nChi2Min, nChi2Max )

TH2F_glb_eta_nChi2 = TH2F("TH2F_glb_eta_nChi2", "glb n#chi^{2};#eta; normalized #chi^{2}", etaBins, etaMin, etaMax,nBins, nChi2Range[0], nChi2Range[1] )
TH2F_glb_pt_nChi2 = TH2F("TH2F_glb_nChi2_pt", "glb n#chi^{2}; p_{T}; normalized #chi^{2}", ptBins, ptMin, ptMax,nBins, nChi2Range[0], nChi2Range[1] )

##
## nhits
##

TH2F_glb_eta_nHits = TH2F("TH2F_glb_eta_nHits", "glb nHits; #eta; nHits", etaBins, etaMin, etaMax,nBins, nHitsRange[0], nHitsRange[1] )
TH2F_glb_pt_nHits = TH2F("TH2F_glb_pt_nHits", "glb nHits; p_{t}; nHits", ptBins, ptMin, ptMax,nBins, nHitsRange[0], nHitsRange[1]  )

##
## pt pull
##

TH2F_glb_sta_eta_ptPull = TH2F("TH2F_glb_sta_eta_ptPull", "glb sta p_{T} Pull;#eta;  p_{T} Pull", etaBins, etaMin, etaMax ,nBins, -100, 100  )
TH2F_glb_sta_pt_ptPull = TH2F("TH2F_glb_sta_pt_ptPull", "glb sta p_{T} Pull;p_{T},  p_{T} Pull", ptBins, ptMin, ptMax ,nBins, -100, 100  )

TH2F_gen_glb_eta_ptPull = TH2F("TH2F_gen_glb_eta_ptPull", "gen glb p_{T} Pull;#eta;  p_{T} Pull", etaBins, etaMin, etaMax ,nBins, ptPullRange[0], ptPullRange[1]  )
TH2F_gen_glb_pt_ptPull = TH2F("TH2F_gen_glb_pt_ptPull", "gen glb p_{T} Pull;p_{T};  p_{T} Pull", ptBins, ptMin, ptMax ,nBins, ptPullRange[0], ptPullRange[1]  )



##
## ptRes
##

TH2F_glb_sta_eta_ptRes = TH2F("glb_sta_eta_v_ptRes"," glb vs sta p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResMin, ptResMax )
TH2F_glb_sta_phi_ptRes = TH2F("glb_sta_phi_v_ptRes"," glb vs sta p_{T}Res ;#phi;pTRes",phiBins, phiMin, phiMax ,ptResBins, ptResMin, ptResMax )
TH2F_glb_sta_phi_ptRes_endcap = TH2F("glb_sta_phi_v_ptRes_endcap"," glb vs sta p_{T}Res |#eta| > 0.9;#phi;pTRes",phiBins, phiMin, phiMax ,ptResBins, ptResMin, ptResMax )
TH2F_glb_sta_phi_ptRes_barrel = TH2F("glb_sta_phi_v_ptRes_barrel"," glb vs sta p_{T}Res |#eta| < 0.9;#phi;pTRes",phiBins, phiMin, phiMax ,ptResBins, ptResMin, ptResMax )

TH2F_gen_glb_eta_ptRes = TH2F("gen_glb_eta_v_ptRes"," gen vs glb p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResGLB[0], ptResGLB[1] )
TH2F_gen_glb_phi_ptRes = TH2F("gen_glb_phi_v_ptRes"," gen vs glb p_{T}Res ;#phi;pTRes",phiBins, phiMin, phiMax ,ptResBins, ptResGLB[0], ptResGLB[1] )
TH2F_gen_glb_pt_ptRes = TH2F("gen_glb_pt_v_ptRes"," gen vs glb p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResGLB[0], ptResGLB[1] )

#TH2F_glb_sta_eta_ptRes_type_2 = TH2F("glb_sta_eta_v_ptRes_type_2"," glb vs sta p_{T}Res (type 2) ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins,ptResSTAType2[0], ptResSTAType2[1] )
#TH2F_glb_sta_phi_ptRes_type_2 = TH2F("glb_sta_phi_v_ptRes_type_2"," glb vs sta p_{T}Res (type 2) ;#phi;pTRes",phiBins, phiMin, phiMax ,ptResBins, ptResSTAType2[0], ptResSTAType2[1])
#TH2F_glb_sta_pt_ptRes_type_2 = TH2F("glb_sta_pt_v_ptRes_type_2"," glb vs sta p_{T}Res (type 2) ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResSTAType2[0], ptResSTAType2[1])


#TH2F_gen_sta_eta_ptRes_type_2 = TH2F("gen_sta_eta_v_ptRes_type_2"," gen vs glb p_{T}Res (type 2) ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResSTAType2[0], ptResSTAType2[1])
#TH2F_gen_sta_phi_ptRes_type_2 = TH2F("gen_sta_phi_v_ptRes_type_2"," gen vs glb p_{T}Res (type 2) ;#phi;pTRes",phiBins, phiMin, phiMax ,ptResBins, ptResSTAType2[0], ptResSTAType2[1] )
#TH2F_gen_sta_pt_ptRes_type_2 = TH2F("gen_sta_pt_v_ptRes_type_2"," gen vs glb p_{T}Res (type 2) ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResSTAType2[0], ptResSTAType2[1])

# recoDimuon plots
#glb gen 

TH2F_sta_glb_pt_HybridSTA_Mass = TH2F("sta_glb_pt_HybridSTA_Mass"," sta glb Hydrid Z Mass ;p_{T} mu STA;GeV",ptBins, ptMin, ptMax ,massBins, massMin, massMax )
TH2F_sta_glb_eta_HybridSTA_Mass = TH2F("sta_glb_eta_HybridSTA_Mass"," sta glb Hydrid Z Mass ;#eta mu STA;GeV",etaBins, etaMin, etaMax ,massBins, massMin, massMax )
TH2F_sta_glb_phi_HybridSTA_Mass = TH2F("sta_glb_phi_HybridSTA_Mass"," sta glb Hydrid Z Mass ;#phi mu STA;GeV",phiBins, phiMin, phiMax ,massBins, massMin, massMax )

#TH2F_sta_glb_pt_HybridSTA_Mass = TH2F("sta_glb_pt_HybridSTA_Mass"," sta Hydrid Z Mass ;p_{T};GeV",ptBins, ptMin, ptMax ,massBins, massMin, massMax )

#muonTypes = ["sta","glb_trk","glb","glb_pic","glb_gen"]
#if not isMC: del muonTypes[-1] 




#generic comparision plots
#TProfile_ptRes = []
#TH2F_pt_ptRes = []
#TH2F_eta_ptRes = []
#TH2F_phi_ptRes = []



#for counter, types in enumerate(muonTypes):
#	for counter2, types2 in enumerate(muonTypes):
#		if counter2 > counter:
#			prefix = '{}-{}-'.format(types,types2)
#			title = '{} vs {} '.format(types,types2)
			#print prefix
			#TProfile_ptRes.append( TProfile3D(prefix + "pt-ptRes",  title + "p_{T} ;p_{T};counts",  ptBins, ptMin, ptMax, phiBins, phiMin, phiMax, etaBins, etaMin, etaMax))
			#TProfile_ptRes.append( TProfile2D(prefix + "pt-ptRes",  title + "p_{T}Res ;#phi;#eta", phiBins, phiMin, phiMax, etaBins, etaMin, etaMax))

			#TH2F_pt_ptRes.append( TH2F( prefix + "pt-pt_v_ptRes",title + "p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResMin, ptResMax ))
			#TH2F_phi_ptRes.append( TH2F( prefix + "phi-phi_v_ptRes",title + "p_{T}Res ;#phi;pTRes",phiBins, phiMin, phiMax ,ptResBins, ptResMin, ptResMax  ))
			#TH2F_eta_ptRes.append( TH2F( prefix + "eta-eta_v_ptRes",title + "p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResMin, ptResMax  ))
