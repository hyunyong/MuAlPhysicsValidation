
#ROOT.gInterpreter.Declare("""
#	double ptResGLBSTA(int q, double sta_pt, double glb_pt){
#		return (double) q * ( 1.0/sta_pt- 1.0/glb_pt);
#	}
#""")
#
#TH2F_glb_sta_eta_ptRes_histogrammar = Select("glb && sta ", Bin(etaBins, etaMin, etaMax, "glb_eta",  Bin(ptResBins, ptResMin, ptResMax, "ptResGLBSTA(q, sta_pt, glb_pt)") ) )
#
#
#
#TH2F_glb_sta_eta_ptRes_histogrammar.fill.root(recoMuons)
#
#TH2F_glb_sta_eta_ptRes = TH2F_glb_sta_eta_ptRes_histogrammar.plot.root("TH2F_glb_sta_eta_ptRes", "example")
#
#TH2F_glb_sta_eta_ptRes.Draw("colz");
#c1.SaveAs("example.png")


from root_numpy import  tree2array, array2tree
from root_numpy import fill_hist

#sta_TRK_delta_phi = Bin(phiResBins, phiResMin, phiResMax, lambda array : (array['glb_trk_phi']- array['sta_phi'])/ array['glb_phi_error'], Count() )

array = tree2array(recoMuons,
    branches=[	'glb', 'sta', 
    			'TMath::Abs(glb_eta)', 'glb_trk_eta',
    			'glb_phi',  'glb_trk_phi', 'sta_phi', 'glb_phi_error',
    			'glb_pt','glb_trk_pt',
    			'glb_nchi2', 'sta_nchi2',
    			'glb_nhits',
    			'q * (1.0/sta_pt-1.0/glb_pt)',
    			'(q/glb_pt-q/sta_pt)/glb_qoverpterror' ],
    selection='glb && sta',
    start=0, stop=Event_ro_RUN, step=1)

array.dtype.names = [	'glb', 'sta', 
						'glb_eta', 'glb_trk_eta',
						'glb_phi', 'glb_trk_phi', 'sta_phi', 'glb_phi_error',
						'glb_pt', 'glb_trk_pt',
						'glb_nchi2','sta_nchi2',
						'glb_nhits',
						'ptResSTAGLB',
						'ptPullSTAGLB' ]

#if isMC:
#	arrayMC = tree2array(recoMuons,
#    branches=[	'glb', 'sta', 
#    			'glb_gen_eta',
#    			'glb_gen_phi', 
#    			'glb__genpt'
#    			'q * (1.0/sta_pt-1.0/glb_gen_pt)',
#    			'q*(1.0/sta_pt - 1.0/glb_gen_pt)/glb_qoverpterror',
#    			'q * (1.0/glb_pt-1.0/glb_gen_pt)',
#    			'q*(1.0/glb_pt - 1.0/glb_gen_pt)/glb_qoverpterror' ],
#    selection='glb && sta',
#    start=0, stop=Event_ro_RUN, step=1)
#
#	arrayMC.dtype.names = [	'glb', 'sta', 
#							'glb_gen_eta',
#							'glb_gen_phi',
#							'glb_gen_pt', 
#							'ptResSTAGEN',
#							'ptPullSTAGEN',
#							'ptResGLBGEN',
#							'ptPullGLBGEN']
#
#	gen_histograms.fill.numpy(arrayMC)



diMuonArray = tree2array(recoDimuons,
    branches=['pos_glb_trk_pt', 'neg_glb_trk_pt',  'pos_glb_trk_eta',  'neg_glb_trk_eta',	'pos_sta_pt', 'neg_sta_pt', 'pos_sta_eta', 'neg_sta_eta', 'pos_sta_phi', 'neg_sta_phi' ],
    selection='glb && sta',
    start=0, stop=Event_ro_RUN, step=1)

recoDimuons = array2tree(diMuonArray)


standard_histograms.fill.numpy(array)

mass_histograms.fill.root(recoDimuons)



#D1_sta_glb_delta_phi_barrel = standard_histograms.get("D1_sta_glb_delta_phi_barrel").plot.root("TH1F_sta_glb_delta_phi_barrel", "(#phi_{GLB}-#phi_{STA})/#phi_{GLB Error}  |#eta| < 0.9; #delta #phi")
#
#TH1F_sta_trk_delta_phi = standard_histograms.get("D1_sta_trk_delta_phi").plot.root("TH1F_sta_TRK_delta_phi", "(#phi_{GLB}-#phi_{STA})/#phi_{GLB Error}; #delta #phi")
#
#TH2F_glb_eta_nChi2 = standard_histograms.get("D2_glb_eta_nChi2").plot.root("TH2F_glb_eta_nChi2", "glb n#chi^{2};#eta; normalized #chi^{2}")
#
#TH2F_glb_pt_nChi2 = standard_histograms.get("D2_glb_pt_nChi2").plot.root("TH2F_glb_pt_nChi2", "glb n#chi^{2};#p_{T}; normalized #chi^{2}")





##
## phi
##

TH1F_sta_glb_delta_phi_barrel = standard_histograms.get("D1_sta_glb_delta_phi_barrel").plot.root("TH1F_sta_glb_delta_phi_barrel", "(#phi_{GLB}-#phi_{STA})/#phi_{GLB Error}  |#eta| < 0.9; #delta #phi")
TH1F_sta_glb_delta_phi_endcap = standard_histograms.get("D1_sta_glb_delta_phi_endcap").plot.root("TH1F_sta_glb_delta_phi_endcap", "(#phi_{GLB}-#phi_{STA})/#phi_{GLB Error}  |#eta| > 0.9; #delta #phi")
TH1F_sta_glb_delta_phi = standard_histograms.get("D1_sta_glb_delta_phi").plot.root("TH1F_sta_glb_delta_phi", "(#phi_{GLB}-#phi_{STA})/#phi_{GLB Error}; #delta #phi")

TH1F_sta_trk_delta_phi_barrel = standard_histograms.get("D1_sta_trk_delta_phi_barrel").plot.root("TH1F_sta_trk_delta_phi_barrel", "(#phi_{TRK}-#phi_{STA})/#phi_{GLB Error}  |#eta| < 0.9; #delta #phi")
TH1F_sta_trk_delta_phi_endcap = standard_histograms.get("D1_sta_trk_delta_phi_endcap").plot.root("TH1F_sta_trk_delta_phi_endcap", "(#phi_{TRK}-#phi_{STA})/#phi_{GLB Error}  |#eta| > 0.9; #delta #phi")
TH1F_sta_trk_delta_phi = standard_histograms.get("D1_sta_trk_delta_phi").plot.root("TH1F_sta_trk_delta_phi", "(#phi_{TRK}-#phi_{STA})/#phi_{GLB Error}; #delta #phi")



##
## nchi2
##

TH1F_sta_nChi2_barrel = standard_histograms.get("D1_sta_nChi2_barrel").plot.root("TH1F_sta_nChi2_barrel", "sta n#chi^{2} |#eta| < 0.9; n#chi^2")
TH1F_sta_nChi2_endcap = standard_histograms.get("D1_sta_nChi2_endcap").plot.root("TH1F_sta_nChi2_endcap", "sta n#chi^{2} |#eta| > 0.9; n#chi^2")
TH1F_glb_nChi2_endcap = standard_histograms.get("D1_glb_nChi2_endcap").plot.root("TH1F_glb_nChi2_endcap", "glb n#chi^{2} |#eta| > 0.9; n#chi^2")
TH1F_glb_nChi2_barrel = standard_histograms.get("D1_glb_nChi2_barrel").plot.root("TH1F_glb_nChi2_barrel", "glb n#chi^{2} |#eta| < 0.9; n#chi^2")

TH2F_glb_eta_nChi2 = standard_histograms.get("D2_glb_eta_nChi2").plot.root("TH2F_glb_eta_nChi2", "glb n#chi^{2};#eta; normalized #chi^{2}")
TH2F_glb_pt_nChi2 = standard_histograms.get("D2_glb_pt_nChi2").plot.root("TH2F_glb_nChi2_pt", "glb n#chi^{2}; p_{T}; normalized #chi^{2}")
TH2F_sta_pt_nChi2 = standard_histograms.get("D2_sta_pt_nChi2").plot.root("TH2F_sta_nChi2_pt", "sta n#chi^{2}; p_{T}; normalized #chi^{2}")
TH2F_sta_eta_nChi2 = standard_histograms.get("D2_sta_eta_nChi2").plot.root("TH2F_sta_eta_nChi2", "sta n#chi^{2};#eta; normalized #chi^{2}")

##
## nhits
##

TH2F_glb_eta_nHits = standard_histograms.get("D2_glb_eta_nHits").plot.root("TH2F_glb_eta_nHits", "glb nHits; #eta; nHits")
TH2F_glb_pt_nHits = standard_histograms.get("D2_glb_pt_nHits").plot.root("TH2F_glb_pt_nHits", "glb nHits; p_{t}; nHits")

##
## pt pull
##

TH2F_glb_sta_eta_ptPull = standard_histograms.get("D2_glb_sta_eta_ptPull").plot.root("TH2F_glb_sta_eta_ptPull", "glb sta p_{T} Pull;#eta;  p_{T} Pull")
TH2F_glb_sta_pt_ptPull = standard_histograms.get("D2_glb_sta_pt_ptPull").plot.root("TH2F_glb_sta_pt_ptPull", "glb sta p_{T} Pull;p_{T},  p_{T} Pull")





##
## ptRes
##

TH2F_glb_sta_eta_ptRes = standard_histograms.get("D2_glb_sta_eta_ptRes").plot.root("glb_sta_eta_v_ptRes"," glb vs sta p_{T}Res ;#eta;pTRes")
TH2F_glb_sta_phi_ptRes = standard_histograms.get("D2_glb_sta_phi_ptRes").plot.root("glb_sta_phi_v_ptRes"," glb vs sta p_{T}Res ;#phi;pTRes")
TH2F_glb_sta_phi_ptRes_endcap = standard_histograms.get("D2_glb_sta_phi_ptRes_endcap").plot.root("glb_sta_phi_v_ptRes_endcap"," glb vs sta p_{T}Res |#eta| > 0.9;#phi;pTRes")
TH2F_glb_sta_phi_ptRes_barrel = standard_histograms.get("D2_glb_sta_phi_ptRes_barrel").plot.root("glb_sta_phi_v_ptRes_barrel"," glb vs sta p_{T}Res |#eta| < 0.9;#phi;pTRes")


##
## hybrid Z Mass
##


TH2F_sta_glb_pt_HybridSTA_Mass = mass_histograms.get("D2_sta_glb_pt_HybridSTA_Mass").plot.root("sta_glb_pt_HybridSTA_Mass"," CMS preliminary ;p_{T}_{#mu}^{STA};")
TH2F_sta_glb_eta_HybridSTA_Mass = mass_histograms.get("D2_sta_glb_eta_HybridSTA_Mass").plot.root("sta_glb_eta_HybridSTA_Mass"," CMS preliminary ;#eta_{#mu}^{STA};")
TH2F_sta_glb_phi_HybridSTA_Mass = mass_histograms.get("D2_sta_glb_phi_HybridSTA_Mass").plot.root("sta_glb_phi_HybridSTA_Mass"," CMS preliminary ;#phi_{#mu}^{STA};")
 



# recoDimuon plots

#if isMC:
#	TH2F_gen_glb_eta_ptRes = standard_histograms.get("D2_gen_glb_eta_ptRes").plot.root("gen_glb_eta_v_ptRes"," gen vs glb p_{T}Res ;#eta;pTRes")
#	TH2F_gen_glb_phi_ptRes = standard_histograms.get("D2_gen_glb_phi_ptRes").plot.root("gen_glb_phi_v_ptRes"," gen vs glb p_{T}Res ;#phi;pTRes")
#	TH2F_gen_glb_pt_ptRes = standard_histograms.get("D2_gen_glb_pt_ptRes").plot.root("gen_glb_pt_v_ptRes"," gen vs glb p_{T}Res ;p_{T};pTRes")
#	TH2F_gen_glb_phi_ptRes_barrel = standard_histograms.get("D2_gen_glb_phi_ptRes_barrel").plot.root("gen_glb_phi_v_ptRes"," gen vs glb p_{T}Res |#eta| < 0.9;#phi;pTRes")
#	TH2F_gen_glb_phi_ptRes_endcap = standard_histograms.get("D2_gen_glb_phi_ptRes_endcap").plot.root("gen_glb_phi_v_ptRes"," gen vs glb p_{T}Res |#eta| > 0.9;#phi;pTRes")
#
#	TH2F_gen_glb_eta_ptPull = standard_histograms.get("D2_gen_glb_eta_ptPull").plot.root("gen_glb_eta_v_ptPull"," gen vs glb p_{T}Pull ;#eta;p_{T}Pull")
#	TH2F_gen_glb_phi_ptPull = standard_histograms.get("D2_gen_glb_phi_ptPull").plot.root("gen_glb_phi_v_ptPull"," gen vs glb p_{T}Pull ;#phi;p_{T}Pull")
#	TH2F_gen_glb_pt_ptPull = standard_histograms.get("D2_gen_glb_pt_ptPull").plot.root("gen_glb_pt_v_ptPull"," gen vs glb p_{T}Pull ;p_{T};p_{T}Pull")


#TH2F_gen_glb_eta_ptRes = standard_histograms.get("D2_gen_glb_eta_ptRes").plot.root("gen_glb_eta_v_ptRes"," gen vs glb p_{T}Res ;#eta;pTRes")
#TH2F_gen_glb_phi_ptRes = standard_histograms.get("D2_gen_glb_phi_ptRes").plot.root("gen_glb_phi_v_ptRes"," gen vs glb p_{T}Res ;#phi;pTRes")
#TH2F_gen_glb_pt_ptRes = standard_histograms.get("D2_gen_glb_pt_ptRes").plot.root("gen_glb_pt_v_ptRes"," gen vs glb p_{T}Res ;p_{T};pTRes")
#
#glb gen 

#TH2F_gen_glb_eta_ptPull = standard_histograms.get("D2_gen_glb_eta_ptPull").plot.root("TH2F_gen_glb_eta_ptPull", "gen glb p_{T} Pull;#eta;  p_{T} Pull")
#TH2F_gen_glb_pt_ptPull = standard_histograms.get("D2_gen_glb_pt_ptPull").plot.root("TH2F_gen_glb_pt_ptPull", "gen glb p_{T} Pull;p_{T};  p_{T} Pull")

#TH2F_sta_glb_pt_HybridSTA_Mass = TH2F("sta_glb_pt_HybridSTA_Mass"," sta glb Hydrid Z Mass ;p_{T} mu STA;GeV",ptBins, ptMin, ptMax ,massBins, massMin, massMax )
#TH2F_sta_glb_eta_HybridSTA_Mass = TH2F("sta_glb_eta_HybridSTA_Mass"," sta glb Hydrid Z Mass ;#eta mu STA;GeV",etaBins, etaMin, etaMax ,massBins, massMin, massMax )
#TH2F_sta_glb_phi_HybridSTA_Mass = TH2F("sta_glb_phi_HybridSTA_Mass"," sta glb Hydrid Z Mass ;#phi mu STA;GeV",phiBins, phiMin, phiMax ,massBins, massMin, massMax )

#glb gen 

#TH2F_glb_gen_pt_ptRes = TH2F("glb_gen_pt_v_ptRes"," glb vs gen p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResMin, ptResMax )
#TH2F_glb_gen_eta_ptRes = TH2F("glb_gen_eta_v_ptRes"," glb vs gen p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResMin, ptResMax )

#sta gen
#TH2F_sta_gen_pt_ptRes = TH2F("sta_gen_pt_v_ptRes"," sta vs gen p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResSTA[0], ptResSTA[1] )
#TH2F_sta_gen_eta_ptRes = TH2F("sta_gen_eta_v_ptRes"," sta vs gen p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResSTA[0], ptResSTA[1])














#TH1F_sta_TRK_delta_phi = sta_TRK_delta_phi.plot.root("TH1F_sta_TRK_delta_phi", "(#phi_{TRK}-#phi_{STA})/#phi_{GLB error}; #delta #phi")
#TH1F_sta_glb_delta_phi.Draw()
#c1.SaveAs("TH1F_sta_glb_delta_phi.png")

#TH2F_glb_sta_eta_ptRes_histogrammar = Select(lambda array: array['glb_eta'] < 10 , Bin(etaBins, etaMin, etaMax, lambda array : array['glb_eta'],  Bin(ptResBins, ptResMin, ptResMax, lambda array : array['ptResSTAGLB'] ) ) )

#TH2F_glb_sta_eta_ptRes_histogrammar.fill.numpy(array)

#TH2F_glb_sta_eta_ptRes = TH2F_glb_sta_eta_ptRes_histogrammar.plot.root("TH2F_glb_sta_eta_ptRes", "example")

#TH2F_glb_sta_eta_ptRes.Draw("colz");

#fill_hist(TH2F_glb_sta_eta_ptRes, array['glb_eta'], array['ptResSTAGLB'] )
