# Counting Pos and Neg muons if you want to run on equal number of positive and negative muons
nNeg = 0
nPos = 0
nMinPosNeg = 0
if(method=="equal"):
  for counter0, event in enumerate(recoMuons):
    if(event.glb_trk_pt < thresholdPt or fabs(event.glb_trk_eta)>2.4 or not event.glb or not event.sta or event.sta_pt== 0.0 or event.glb_pt == 0.0  ): continue
    if not oldTTrees:
      if(event.recoMu_IsoPF04 > 0.15): continue;
    if(Event_ro_RUN>0):
      if nMuonPassed > Event_ro_RUN: break
    if event.q<0: nNeg+=1
    if event.q>0: nPos+=1
  if nNeg<nPos: nMinPosNeg = nNeg
  if nNeg>nPos: nMinPosNeg = nPos

# Loop over recoMuons
nMuonPassed, nMuonPos, nMuonNeg = 0, 0, 0
for counter, event in enumerate(recoMuons):
  if counter % 100000 == 0: print counter, (counter +0.0)/event.GetEntries()
  if(event.glb_trk_pt < thresholdPt or fabs(event.glb_trk_eta)>2.4 or not event.glb or not event.sta or event.sta_pt== 0.0 or event.glb_pt == 0.0  ): continue
  if not oldTTrees:
    if(event.recoMu_IsoPF04 > 0.15): continue;
  if(Event_ro_RUN>0):
    if nMuonPassed > Event_ro_RUN: break

  nMuonPassed += 1
  if(event.q<0): nMuonNeg += 1
  if(event.q>0): nMuonPos += 1
  if(method=="pos" and event.q<0): continue
  if(method=="neg" and event.q>0): continue
  if(method=="equal" and event.q<0 and nMuonNeg>nMinPosNeg): continue
  if(method=="equal" and event.q>0 and nMuonPos>nMinPosNeg): continue

  if not oldTTrees:
   deltaPhiGLB = (event.glb_phi-event.sta_phi)/event.glb_phi_error
   deltaPhiTRK = (event.glb_trk_phi-event.sta_phi)/event.glb_phi_error
  # CHI2
  TH2F_glb_eta_nChi2.Fill(event.glb_eta, event.glb_nchi2)
  TH2F_glb_pt_nChi2.Fill(event.glb_pt, event.glb_nchi2)
  # N HITs
  if not oldTTrees:
    TH2F_glb_eta_nHits.Fill(event.glb_eta, event.glb_nhits)
    TH2F_glb_pt_nHits.Fill(event.glb_pt, event.glb_nhits)
  # Phi Pull
  if not oldTTrees:
   TH1F_sta_glb_delta_phi.Fill(deltaPhiGLB)
   TH1F_sta_trk_delta_phi.Fill(deltaPhiTRK)
  # Barrel
  if abs(event.glb_eta) < 0.9 :
    TH1F_sta_nChi2_barrel.Fill(event.sta_nchi2)
    TH1F_glb_nChi2_barrel.Fill(event.glb_nchi2)
    if not oldTTrees:
      TH1F_sta_glb_delta_phi_barrel.Fill(deltaPhiGLB)
      TH1F_sta_trk_delta_phi_barrel.Fill(deltaPhiTRK)
  # Endcap
  if abs(event.glb_eta) > 0.9 :
    TH1F_sta_nChi2_endcap.Fill(event.sta_nchi2)
    TH1F_glb_nChi2_endcap.Fill(event.glb_nchi2)
    if not oldTTrees:
      TH1F_sta_glb_delta_phi_endcap.Fill(deltaPhiGLB)
      TH1F_sta_trk_delta_phi_endcap.Fill(deltaPhiTRK)
  # pT PULL
  if event.glb and event.sta and  event.sta_pt != 0.0 and event.glb_pt != 0.0:
    glb_qoverp = event.q/event.glb_pt
    sta_qoverp = event.q/event.sta_pt
    if not oldTTrees:
      pTPull = (glb_qoverp-sta_qoverp)/event.glb_qoverpterror
      TH2F_glb_sta_eta_ptPull.Fill(event.glb_eta,pTPull)
      TH2F_glb_sta_pt_ptPull.Fill(event.glb_pt,pTPull)
  
  # pT RES
  ptResGLBSTA = event.q*(1.0/event.sta_pt-1.0/event.glb_trk_pt)
  TH2F_glb_sta_eta_ptRes.Fill(event.glb_eta, ptResGLBSTA)
  TH2F_glb_sta_phi_ptRes.Fill(event.glb_phi, ptResGLBSTA)
  if abs(event.glb_eta) > 0.9 :
    TH2F_glb_sta_phi_ptRes_endcap.Fill(event.glb_phi, ptResGLBSTA)
  if abs(event.glb_eta) < 0.9 :
    TH2F_glb_sta_phi_ptRes_barrel.Fill(event.glb_phi, ptResGLBSTA)
  # GEN
  if isMC and event.glb_gen:
    ptResGLB = (event.glb_pt-event.glb_gen_pt)/event.glb_gen_pt
    ptResSTA = (event.sta_pt-event.glb_gen_pt)/event.glb_gen_pt
    TH2F_glb_gen_pt_ptRes.Fill(event.glb_gen_pt, ptResGLB)
    TH2F_glb_gen_eta_ptRes.Fill(event.glb_gen_eta, ptResGLB)
    TH2F_sta_gen_pt_ptRes.Fill(event.glb_gen_pt, ptResSTA)
    TH2F_sta_gen_eta_ptRes.Fill(event.glb_gen_eta, ptResSTA)
    
    if event.glb_gen:
	# pT PULL
	glb_qoverp = event.q/event.glb_pt
	gen_qoverp = event.q/event.glb_gen_pt
	pTPull = (gen_qoverp- glb_qoverp)/event.glb_qoverpterror
	TH2F_gen_glb_eta_ptPull.Fill(event.glb_gen_eta,pTPull)
	TH2F_gen_glb_pt_ptPull.Fill(event.glb_gen_pt,pTPull)
	# pT RES
	ptResGENGLB = (event.glb_pt-event.glb_gen_pt)/event.glb_gen_pt
	TH2F_gen_glb_eta_ptRes.Fill(event.glb_gen_eta, ptResGENGLB)
	TH2F_gen_glb_phi_ptRes.Fill(event.glb_gen_phi, ptResGENGLB)
	TH2F_gen_glb_pt_ptRes.Fill(event.glb_gen_pt, ptResGENGLB)
