for counter, event in enumerate(recoMuons):
  if counter % 100000 == 0: print counter, (counter +0.0)/event.GetEntries()
  if(Event_ro_RUN>0):
    if counter > Event_ro_RUN: break
  
  if(event.glb_trk_pt < thresholdPt or fabs(event.glb_trk_eta)>2.4  ): continue;
  if verbosity > 10:
    print "event eta " , event.glb_eta
    print "event pt " , event.glb_pt
    print "mu glb, mu sta: ", event.glb, event.sta
  
  deltaPhiGLB = (event.glb_phi-event.sta_phi)/event.glb_phi_error
  deltaPhiTRK = (event.glb_trk_phi-event.sta_phi)/event.glb_phi_error
  # CHI2
  TH2F_glb_eta_nChi2.Fill(event.glb_eta, event.glb_nchi2)
  TH2F_glb_pt_nChi2.Fill(event.glb_pt, event.glb_nchi2)
  # N HITs
  TH2F_glb_eta_nHits.Fill(event.glb_eta, event.glb_nhits)
  TH2F_glb_pt_nHits.Fill(event.glb_pt, event.glb_nhits)
  # Phi Pull
  TH1F_sta_glb_delta_phi.Fill(deltaPhiGLB)
  TH1F_sta_TRK_delta_phi.Fill(deltaPhiTRK)
  # Barrel
  if abs(event.glb_eta) < 0.9 :
    TH1F_sta_nChi2_barrel.Fill(event.sta_nchi2)
    TH1F_glb_nChi2_barrel.Fill(event.glb_nchi2)
    TH1F_sta_glb_delta_phi_barrel.Fill(deltaPhiGLB)
    TH1F_sta_TRK_delta_phi_barrel.Fill(deltaPhiTRK)
  # Endcap
  if abs(event.glb_eta) > 0.9 :
    TH1F_sta_nChi2_endcap.Fill(event.sta_nchi2)
    TH1F_glb_nChi2_endcap.Fill(event.glb_nchi2)
    TH1F_sta_glb_delta_phi_endcap.Fill(deltaPhiGLB)
    TH1F_sta_TRK_delta_phi_endcap.Fill(deltaPhiTRK)
  # pT PULL
  if event.glb and event.sta and  event.sta_pt != 0.0 and event.glb_pt != 0.0:
    glb_qoverp = event.q/event.glb_pt
    sta_qoverp = event.q/event.sta_pt
    if isNewMuAlAnalyzer:
	pTPull = (glb_qoverp- sta_qoverp)/event.glb_qoverpterror
	TH2F_glb_sta_eta_ptPull.Fill(event.glb_eta,pTPull)
	TH2F_glb_sta_pt_ptPull.Fill(event.glb_pt,pTPull)
  
  # pT RES
  if  event.glb and event.sta and event.sta_pt != 0.0 and event.glb_pt != 0.0:
    ptResGLBSTA = event.q*(1.0/event.sta_pt-1.0/event.glb_pt)
    TH2F_glb_sta_eta_ptRes.Fill(event.glb_eta, ptResGLBSTA)
    TH2F_glb_sta_phi_ptRes.Fill(event.glb_phi, ptResGLBSTA)
    if abs(event.glb_eta) > 0.9 :
	TH2F_glb_sta_phi_ptRes_endcap.Fill(event.glb_phi, ptResGLBSTA)
    if abs(event.glb_eta) < 0.9 :
	TH2F_glb_sta_phi_ptRes_barrel.Fill(event.glb_phi, ptResGLBSTA)
    ptResGLBSTA = (event.sta_pt-event.glb_pt)/event.glb_pt
    TH2F_glb_sta_eta_ptRes_type_2.Fill(event.glb_eta, ptResGLBSTA)
    TH2F_glb_sta_phi_ptRes_type_2.Fill(event.glb_phi, ptResGLBSTA)
    TH2F_glb_sta_pt_ptRes_type_2.Fill(event.glb_pt, ptResGLBSTA)  
  # GEN
  if isMC and event.glb_gen:
    ptResGLB = (event.glb_pt-event.glb_gen_pt)/event.glb_gen_pt
    ptResSTA = (event.sta_pt-event.glb_gen_pt)/event.glb_gen_pt
    TH2F_glb_gen_pt_ptRes.Fill(event.glb_gen_pt, ptResGLB)
    TH2F_glb_gen_eta_ptRes.Fill(event.glb_gen_eta, ptResGLB)
    TH2F_sta_gen_pt_ptRes.Fill(event.glb_gen_pt, ptResSTA)
    TH2F_sta_gen_eta_ptRes.Fill(event.glb_gen_eta, ptResSTA)
    
    if  event.glb and event.glb_gen and  event.sta_pt != 0.0 and event.glb_pt != 0.0:
	# pT PULL
	glb_qoverp = event.q/event.glb_pt
	gen_qoverp = event.q/event.glb_gen_pt
	pTPull = (gen_qoverp- glb_qoverp)/event.glb_qoverpterror
	TH2F_gen_glb_eta_ptPull.Fill(event.glb_gen_eta,pTPull)
	TH2F_gen_glb_pt_ptPull.Fill(event.glb_gen_pt,pTPull)
	# pT RES
	ptResGENGLB = (event.glb_pt-event.glb_gen_pt)/event.glb_gen_pt
	TH2F_gen_sta_eta_ptRes_type_2.Fill(event.glb_gen_eta, ptResGLBSTA)
	TH2F_gen_sta_phi_ptRes_type_2.Fill(event.glb_gen_phi, ptResGLBSTA)
	TH2F_gen_sta_pt_ptRes_type_2.Fill(event.glb_gen_pt, ptResGLBSTA)

	TH2F_gen_glb_eta_ptRes.Fill(event.glb_gen_eta, ptResGENGLB)
	TH2F_gen_glb_phi_ptRes.Fill(event.glb_gen_phi, ptResGENGLB)
	TH2F_gen_glb_pt_ptRes.Fill(event.glb_gen_pt, ptResGENGLB)
