from ROOT import TH1F, TCanvas, TProfile, TProfile2D, TProfile3D, TH2F
from array import array

c1 = TCanvas("c1", "c1", 600, 400)
print "opening file: ", fileIn
print "creating file: ", fileOut
outFile = TFile("{}.root".format(fileOut), "recreate")

#glb gen 
TH2F_glb_gen_pt_ptRes = TH2F("glb_gen_pt_v_ptRes"," glb vs gen p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResMin, ptResMax )
TH2F_glb_gen_eta_ptRes = TH2F("glb_gen_eta_v_ptRes"," glb vs gen p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResMin, ptResMax )
#sta gen
TH2F_sta_gen_pt_ptRes = TH2F("sta_gen_pt_v_ptRes"," sta vs gen p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResSTA[0], ptResSTA[1] )
TH2F_sta_gen_eta_ptRes = TH2F("sta_gen_eta_v_ptRes"," sta vs gen p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResSTA[0], ptResSTA[1])

#phi GLB
TH1F_sta_glb_delta_phi_barrel = TH1F("TH1F_sta_glb_delta_phi_barrel", "(#phi_{GLB}-#phi_{STA})/#phi_{GLB Error}  |#eta| < 0.9; #delta #phi",phiResBins, phiResMin, phiResMax )
TH1F_sta_glb_delta_phi_endcap = TH1F("TH1F_sta_glb_delta_phi_endcap", "(#phi_{GLB}-#phi_{STA})/#phi_{GLB Error}  |#eta| > 0.9; #delta #phi",phiResBins, phiResMin, phiResMax )
TH1F_sta_glb_delta_phi = TH1F("TH1F_sta_glb_delta_phi", "(#phi_{GLB}-#phi_{STA})/#phi_{GLB Error}; #delta #phi",phiResBins, phiResMin, phiResMax )
#phi TRK
TH1F_sta_trk_delta_phi_barrel = TH1F("TH1F_sta_trk_delta_phi_barrel", "(#phi_{TRK}-#phi_{STA})/#phi_{GLB Error}  |#eta| < 0.9; #delta #phi",phiResBins, phiResMin, phiResMax )
TH1F_sta_trk_delta_phi_endcap = TH1F("TH1F_sta_trk_delta_phi_endcap", "(#phi_{TRK}-#phi_{STA})/#phi_{GLB Error}  |#eta| > 0.9; #delta #phi",phiResBins, phiResMin, phiResMax )
TH1F_sta_trk_delta_phi = TH1F("TH1F_sta_trk_delta_phi", "(#phi_{TRK}-#phi_{STA})/#phi_{GLB Error}; #delta #phi",phiResBins, phiResMin, phiResMax )

#Nchi2
TH1F_sta_nChi2_barrel = TH1F("TH1F_sta_nChi2_barrel", "sta n#chi^{2} |#eta| < 0.9; n#chi^2",nChi2Bins, nChi2Min, nChi2Max )
TH1F_sta_nChi2_endcap = TH1F("TH1F_sta_nChi2_endcap", "sta n#chi^{2} |#eta| > 0.9; n#chi^2",nChi2Bins, nChi2Min, nChi2Max )
TH1F_glb_nChi2_endcap = TH1F("TH1F_glb_nChi2_endcap", "glb n#chi^{2} |#eta| > 0.9; n#chi^2",nChi2Bins, nChi2Min, nChi2Max )
TH1F_glb_nChi2_barrel = TH1F("TH1F_glb_nChi2_barrel", "glb n#chi^{2} |#eta| < 0.9; n#chi^2",nChi2Bins, nChi2Min, nChi2Max )
TH2F_glb_eta_nChi2 = TH2F("TH2F_glb_eta_nChi2", "glb n#chi^{2};#eta; normalized #chi^{2}", etaBins, etaMin, etaMax,nBins, nChi2Range[0], nChi2Range[1] )
TH2F_glb_pt_nChi2 = TH2F("TH2F_glb_nChi2_pt", "glb n#chi^{2}; p_{T}; normalized #chi^{2}", ptBins, ptMin, ptMax,nBins, nChi2Range[0], nChi2Range[1] )
TH2F_sta_eta_nChi2 = TH2F("TH2F_sta_eta_nChi2", "sta n#chi^{2};#eta; normalized #chi^{2}", etaBins, etaMin, etaMax,nBins, nChi2Range[0], nChi2Range[1] )
TH2F_sta_pt_nChi2 = TH2F("TH2F_sta_nChi2_pt", "sta n#chi^{2}; p_{T}; normalized #chi^{2}", ptBins, ptMin, ptMax,nBins, nChi2Range[0], nChi2Range[1] )

#Nhits
TH2F_glb_eta_nHits = TH2F("TH2F_glb_eta_nHits", "glb nHits; #eta; nHits", 48, -2.4, 2.4,24, 0, 75 )
TH2F_glb_pt_nHits = TH2F("TH2F_glb_pt_nHits", "glb nHits; p_{t}; nHits", ptBins, ptMin, ptMax,nBins, nHitsRange[0], nHitsRange[1]  )

#Pt pull GLB-STA
TH2F_glb_sta_eta_ptPull = TH2F("TH2F_glb_sta_eta_ptPull", "glb sta p_{T} Pull;#eta;  p_{T} Pull", etaBins, etaMin, etaMax ,nBins, -100, 100  )
TH2F_glb_sta_pt_ptPull = TH2F("TH2F_glb_sta_pt_ptPull", "glb sta p_{T} Pull;p_{T},  p_{T} Pull", ptBins, ptMin, ptMax ,nBins, -100, 100  )
#Pt pull GLB-GEN
TH2F_gen_glb_eta_ptPull = TH2F("TH2F_gen_glb_eta_ptPull", "gen glb p_{T} Pull;#eta;  p_{T} Pull", etaBins, etaMin, etaMax ,nBins, ptPullRange[0], ptPullRange[1]  )
TH2F_gen_glb_pt_ptPull = TH2F("TH2F_gen_glb_pt_ptPull", "gen glb p_{T} Pull;p_{T};  p_{T} Pull", ptBins, ptMin, ptMax ,nBins, ptPullRange[0], ptPullRange[1]  )

# pT Resolution (GLB-STA muons) as a function of eta/phi/pT.
TH2F_glb_sta_eta_ptRes = TH2F("glb_sta_eta_v_ptRes"," glb vs sta p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResMin, ptResMax )
TH2F_glb_sta_phi_ptRes = TH2F("glb_sta_phi_v_ptRes"," glb vs sta p_{T}Res ;#phi;pTRes",phiBins, phiMin, phiMax ,ptResBins, ptResMin, ptResMax )
TH2F_glb_sta_pt_ptRes = TH2F("glb_sta_pt_v_ptRes"," glb vs sta p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResMin, ptResMax )
# pT Resolution (GLB-STA muons) by region.
TH2F_glb_sta_phi_ptRes_endcap = TH2F("glb_sta_phi_v_ptRes_endcap"," glb vs sta p_{T}Res |#eta| > 0.9;#phi;pTRes",phiBins, phiMin, phiMax ,ptResBins, ptResMin, ptResMax )
TH2F_glb_sta_phi_ptRes_barrel = TH2F("glb_sta_phi_v_ptRes_barrel"," glb vs sta p_{T}Res |#eta| < 0.9;#phi;pTRes",phiBins, phiMin, phiMax ,ptResBins, ptResMin, ptResMax )
# pT Resolution (GLB-GEN muons) as a function of eta/phi/pT.
TH2F_gen_glb_eta_ptRes = TH2F("gen_glb_eta_v_ptRes"," gen vs glb p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResGLB[0], ptResGLB[1] )
TH2F_gen_glb_phi_ptRes = TH2F("gen_glb_phi_v_ptRes"," gen vs glb p_{T}Res ;#phi;pTRes",phiBins, phiMin, phiMax ,ptResBins, ptResGLB[0], ptResGLB[1] )
TH2F_gen_glb_pt_ptRes = TH2F("gen_glb_pt_v_ptRes"," gen vs glb p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResGLB[0], ptResGLB[1] )

# Reco Di-muon plots
# Hybrid Z-boson
TH2F_sta_glb_pt_HybridSTA_Mass = TH2F("sta_glb_pt_HybridSTA_Mass"," sta glb Hydrid Z Mass ;pT_{#mu}^{STA};Di-#mu mass",ptBins, ptMin, ptMax ,massBins, massMin, massMax )
TH2F_sta_glb_eta_HybridSTA_Mass = TH2F("sta_glb_eta_HybridSTA_Mass"," sta glb Hydrid Z Mass ;#eta_{#mu}^{STA};Di-#mu mass",etaBins, etaMin, etaMax ,massBins, massMin, massMax )
TH2F_sta_glb_phi_HybridSTA_Mass = TH2F("sta_glb_phi_HybridSTA_Mass"," sta glb Hydrid Z Mass ;#phi_{#mu}^{STA};Di-#mu mass",phiBins, phiMin, phiMax ,massBins, massMin, massMax )
