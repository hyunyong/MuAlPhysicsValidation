if not os.path.exists(fileOut):
	os.makedirs(fileOut)

if savePng:

	if isMC:	
		TH2F_glb_gen_pt_ptRes.Draw("colz")
		c1.SaveAs("{}/TH2F_glb_gen_pt_ptRes.png".format(fileOut))
		TH2F_glb_gen_eta_ptRes.Draw("colz")
		c1.SaveAs("{}/TH2F_glb_gen_eta_ptRes.png".format(fileOut))
	
		#sta gen
		TH2F_sta_gen_pt_ptRes.Draw("colz")
		c1.SaveAs("{}/TH2F_sta_gen_pt_ptRes.png".format(fileOut))
	
		TH2F_sta_gen_eta_ptRes.Draw("colz")
		c1.SaveAs("{}/TH2F_sta_gen_eta_ptRes.png".format(fileOut))
		##
		##	ptPull
		##

		TH2F_gen_glb_eta_ptPull.Draw("colz")
		c1.SaveAs("{}/TH2F_gen_glb_eta_ptPull.png".format(fileOut))
		TH2F_gen_glb_pt_ptPull.Draw("colz")
		c1.SaveAs("{}/TH2F_gen_glb_pt_ptPull.png".format(fileOut))
		##
		##	ptRes
		##

		TH2F_gen_sta_eta_ptRes_type_2.Draw("colz")
		c1.SaveAs("{}/TH2F_gen_sta_eta_ptRes_type_2.png".format(fileOut))
		TH2F_gen_sta_phi_ptRes_type_2.Draw("colz")
		c1.SaveAs("{}/TH2F_gen_sta_phi_ptRes_type_2.png".format(fileOut))
		TH2F_gen_sta_pt_ptRes_type_2.Draw("colz")
		c1.SaveAs("{}/TH2F_gen_sta_pt_ptRes_type_2.png".format(fileOut)) 

		TH2F_gen_glb_eta_ptRes.Draw("colz")
		c1.SaveAs("{}/TH2F_gen_glb_eta_ptRes.png".format(fileOut))
		TH2F_gen_glb_phi_ptRes.Draw("colz")
		c1.SaveAs("{}/TH2F_gen_glb_phi_ptRes.png".format(fileOut))




		TH2F_gen_glb_pt_ptRes.Draw("colz")
		c1.SaveAs("{}/TH2F_gen_glb_pt_ptRes.png".format(fileOut))
	##
	##	phi
	##

	TH1F_sta_glb_delta_phi_barrel.Draw()
	c1.SaveAs("{}/TH1F_sta_glb_delta_phi_barrel.png".format(fileOut))
	TH1F_sta_glb_delta_phi_endcap.Draw()
	c1.SaveAs("{}/TH1F_sta_glb_delta_phi_endcap.png".format(fileOut)) 
	TH1F_sta_TRK_delta_phi_barrel.Draw()
	c1.SaveAs("{}/TH1F_sta_TRK_delta_phi_barrel.png".format(fileOut))
	TH1F_sta_TRK_delta_phi_endcap.Draw()
	c1.SaveAs("{}/TH1F_sta_TRK_delta_phi_endcap.png".format(fileOut))
	TH1F_sta_glb_delta_phi.Draw()
	c1.SaveAs("{}/TH1F_sta_glb_delta_phi.png".format(fileOut))
	TH1F_sta_TRK_delta_phi.Draw()
	c1.SaveAs("{}/TH1F_sta_TRK_delta_phi.png".format(fileOut))

	##
	##	ptPull
	##

	TH2F_glb_sta_eta_ptPull.Draw("colz")
	c1.SaveAs("{}/TH2F_glb_sta_eta_ptPull.png".format(fileOut))
	TH2F_glb_sta_pt_ptPull.Draw("colz")
	c1.SaveAs("{}/TH2F_glb_sta_pt_ptPull.png".format(fileOut))

	##
	##hybrid mass
	##
	
	TH2F_sta_glb_pt_HybridSTA_Mass.Draw("colz")
	c1.SaveAs("{}/TH2F_sta_glb_pt_HybridSTA_Mass.png".format(fileOut))
	TH2F_sta_glb_eta_HybridSTA_Mass.Draw("colz")
	c1.SaveAs("{}/TH2F_sta_glb_eta_HybridSTA_Mass.png".format(fileOut))
	TH2F_sta_glb_phi_HybridSTA_Mass.Draw("colz")
	c1.SaveAs("{}/TH2F_sta_glb_phi_HybridSTA_Mass.png".format(fileOut))


	##
	##	nChi2
	##

	TH1F_sta_nChi2_barrel.Draw()
	c1.SaveAs("{}/TH1F_sta_nChi2_barrel.png".format(fileOut))
	TH1F_sta_nChi2_endcap.Draw()
	c1.SaveAs("{}/TH1F_sta_nChi2_endcap.png".format(fileOut))
	TH1F_glb_nChi2_endcap.Draw()
	c1.SaveAs("{}/TH1F_glb_nChi2_endcap.png".format(fileOut))
	TH1F_glb_nChi2_barrel.Draw()
	c1.SaveAs("{}/TH1F_glb_nChi2_barrel.png".format(fileOut))

	TH2F_glb_eta_nChi2.Draw("colz")
	c1.SaveAs("{}/TH2F_glb_eta_nChi2.png".format(fileOut))
	TH2F_glb_pt_nChi2.Draw("colz")
	c1.SaveAs("{}/TH2F_glb_pt_nChi2.png".format(fileOut)) 


	##
	##	ptRes
	##

	TH2F_glb_sta_eta_ptRes.Draw("colz")
	c1.SaveAs("{}/TH2F_glb_sta_eta_ptRes.png".format(fileOut))
	TH2F_glb_sta_phi_ptRes.Draw("colz")
	c1.SaveAs("{}/TH2F_glb_sta_phi_ptRes.png".format(fileOut))


	TH2F_glb_sta_eta_ptRes_type_2.Draw("colz")
	c1.SaveAs("{}/TH2F_glb_sta_eta_ptRes_type_2.png".format(fileOut))
	TH2F_glb_sta_phi_ptRes_type_2.Draw("colz")
	c1.SaveAs("{}/TH2F_glb_sta_phi_ptRes_type_2.png".format(fileOut))
	TH2F_glb_sta_phi_ptRes_endcap.Draw("colz")
	c1.SaveAs("{}/TH2F_glb_sta_phi_ptRes_endcap.png".format(fileOut))
	TH2F_glb_sta_phi_ptRes_barrel.Draw("colz")
	c1.SaveAs("{}/TH2F_glb_sta_phi_ptRes_barrel.png".format(fileOut))
	TH2F_glb_sta_pt_ptRes_type_2.Draw("colz")
	c1.SaveAs("{}/TH2F_glb_sta_pt_ptRes_type_2.png".format(fileOut)) 



	##
	## nhits
	##
	TH2F_glb_eta_nHits.Draw("colz")
	c1.SaveAs("{}/TH2F_glb_eta_nHits.png".format(fileOut))
	TH2F_glb_pt_nHits.Draw("colz")
	c1.SaveAs("{}/TH2F_glb_pt_nHits.png".format(fileOut)) 