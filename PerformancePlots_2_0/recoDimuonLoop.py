

for counter, event in enumerate(recoDimuons):
  if counter % 100000 == 0: print counter, (counter +0.0)/event.GetEntries()
  if(Event_ro_RUN>0):
    if counter > Event_ro_RUN: break
  
  # Di-MU MASS
  if ( event.pos_glb_trk_pt > thresholdPt and event.neg_glb_trk_pt > thresholdPt and fabs(event.pos_glb_trk_eta)<2.4 and fabs(event.neg_glb_trk_eta)<2.4):

    #delta Eta plots

    pos_STA = TLorentzVector()
    pos_STA.SetPtEtaPhiM(event.pos_sta_pt,event.pos_sta_eta,event.pos_sta_phi,0.105658)
    neg_STA = TLorentzVector()
    neg_STA.SetPtEtaPhiM(event.neg_sta_pt,event.neg_sta_eta,event.neg_sta_phi,0.105658)

    pos_GLB = TLorentzVector()
    pos_GLB.SetPtEtaPhiM(event.pos_glb_pt,event.pos_glb_eta,event.pos_glb_phi,0.105658)
    neg_GLB = TLorentzVector()
    neg_GLB.SetPtEtaPhiM(event.neg_glb_pt,event.neg_glb_eta,event.neg_glb_phi,0.105658)

    if( abs((pos_GLB + neg_GLB).M()-91.)<5. ):
      deltaEta = event.pos_glb_eta - event.neg_glb_eta
      TH2F_deltaEta_glb_Mass.Fill(deltaEta,(pos_GLB + neg_GLB).M())
      TH2F_deltaEta_glb_Mass_wide.Fill(deltaEta,(pos_GLB + neg_GLB).M())
    if( abs((pos_STA + neg_STA).M()-91.)<5. ):
      deltaEta = event.pos_sta_eta - event.neg_sta_eta
      TH2F_deltaEta_sta_Mass.Fill(deltaEta,(pos_STA + neg_STA).M())
      TH2F_deltaEta_sta_Mass_wide.Fill(deltaEta,(pos_STA + neg_STA).M())

    # HybridZ
    RandmonNumber=randint(0,1) # generate or 0 or 1
    hybridMu1 = TLorentzVector()
    hybridMu2 = TLorentzVector()
    
    if(RandmonNumber>0.5):
	hybridMu1.SetPtEtaPhiM(event.pos_sta_pt,event.pos_sta_eta,event.pos_sta_phi,0)
	hybridMu2.SetPtEtaPhiM(event.neg_glb_pt,event.neg_glb_eta,event.neg_glb_phi,0)
	etaSta=event.pos_sta_eta
	phiSta=event.pos_sta_phi
	pTSta = event.pos_glb_pt
    else:
	hybridMu1.SetPtEtaPhiM(event.pos_glb_pt,event.pos_glb_eta,event.pos_glb_phi,0)
	hybridMu2.SetPtEtaPhiM(event.neg_sta_pt,event.neg_sta_eta,event.neg_sta_phi,0)
	etaSta=event.neg_sta_eta
	phiSta=event.neg_sta_phi
	pTSta = event.neg_glb_pt
    
    hybridZ = TLorentzVector(); hybridZ=hybridMu1+hybridMu2
    
    if( abs(event.glb_m-91.)<5. ):  
	#TH2F_sta_glb_pt_HybridSTA_Mass.Fill(pTSta, hybridZ.M())
	#TH2F_sta_glb_eta_HybridSTA_Mass.Fill(etaSta, hybridZ.M())
	#TH2F_sta_glb_phi_HybridSTA_Mass.Fill(phiSta, hybridZ.M())
	TH2F_sta_glb_pt_HybridSTA_Mass.Fill(event.hyb_sta_pt, event.hyb_m)
	TH2F_sta_glb_eta_HybridSTA_Mass.Fill(event.hyb_sta_eta, event.hyb_m)
	TH2F_sta_glb_phi_HybridSTA_Mass.Fill(event.hyb_sta_phi, event.hyb_m)

	TH2F_sta_glb_glb_mu_pt_HybridSTA_Mass.Fill(event.hyb_glb_pt, event.hyb_m)
	TH2F_sta_glb_glb_mu_eta_HybridSTA_Mass.Fill(event.hyb_glb_eta, event.hyb_m)
	TH2F_sta_glb_glb_mu_phi_HybridSTA_Mass.Fill(event.hyb_glb_phi, event.hyb_m)
