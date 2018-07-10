from ROOT import TFile, TTree, TH1F, TLorentzVector, TMath, TRandom, TCanvas
from histogrammar import *
import math, sys, os


def histogrammarToRoot(standard_histograms, mass_histograms, gen_histograms, fileOut, drawPNG):

    outFile = TFile("{}.root".format(fileOut), "recreate")
    
    c1 = TCanvas("c1", "c1", 600, 400)
    
    
    
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
    TH2F_glb_sta_pt_ptRes = standard_histograms.get("D2_glb_sta_pt_ptRes").plot.root("glb_sta_pt_v_ptRes"," glb vs sta p_{T}Res ;p_{T};pTRes")
    
    TH2F_glb_sta_phi_ptRes_endcap = standard_histograms.get("D2_glb_sta_phi_ptRes_endcap").plot.root("glb_sta_phi_v_ptRes_endcap"," glb vs sta p_{T}Res |#eta| > 0.9;#phi;pTRes")
    TH2F_glb_sta_phi_ptRes_barrel = standard_histograms.get("D2_glb_sta_phi_ptRes_barrel").plot.root("glb_sta_phi_v_ptRes_barrel"," glb vs sta p_{T}Res |#eta| < 0.9;#phi;pTRes")
    
    
    ##
    ## hybrid Z Mass
    ##
    
    
    TH2F_sta_glb_pt_HybridSTA_Mass = mass_histograms.get("D2_sta_glb_pt_HybridSTA_Mass").plot.root("sta_glb_pt_HybridSTA_Mass"," CMS preliminary ;p_{T}_{#mu}^{STA};")
    TH2F_sta_glb_eta_HybridSTA_Mass = mass_histograms.get("D2_sta_glb_eta_HybridSTA_Mass").plot.root("sta_glb_eta_HybridSTA_Mass"," CMS preliminary ;#eta_{#mu}^{STA};")
    TH2F_sta_glb_phi_HybridSTA_Mass = mass_histograms.get("D2_sta_glb_phi_HybridSTA_Mass").plot.root("sta_glb_phi_HybridSTA_Mass"," CMS preliminary ;#phi_{#mu}^{STA};")

    if gen_histograms:
        TH2F_gen_glb_eta_ptRes = gen_histograms.get("D2_gen_glb_eta_ptRes").plot.root("gen_glb_eta_v_ptRes"," gen vs glb p_{T}Res ;#eta;pTRes")
        TH2F_gen_glb_phi_ptRes = gen_histograms.get("D2_gen_glb_phi_ptRes").plot.root("gen_glb_phi_v_ptRes"," gen vs glb p_{T}Res ;#phi;pTRes")
        TH2F_gen_glb_pt_ptRes = gen_histograms.get("D2_gen_glb_pt_ptRes").plot.root("gen_glb_pt_v_ptRes"," gen vs glb p_{T}Res ;p_{T};pTRes")
        
        #glb gen 

        TH2F_gen_glb_eta_ptPull = gen_histograms.get("D2_gen_glb_eta_ptPull").plot.root("TH2F_gen_glb_eta_ptPull", "gen glb p_{T} Pull;#eta;  p_{T} Pull")
        TH2F_gen_glb_pt_ptPull = gen_histograms.get("D2_gen_glb_pt_ptPull").plot.root("TH2F_gen_glb_pt_ptPull", "gen glb p_{T} Pull;p_{T};  p_{T} Pull")

        #TH2F_sta_glb_pt_HybridSTA_Mass = TH2F("sta_glb_pt_HybridSTA_Mass"," sta glb Hydrid Z Mass ;p_{T} mu STA;GeV",ptBins, ptMin, ptMax ,massBins, massMin, massMax )
        #TH2F_sta_glb_eta_HybridSTA_Mass = TH2F("sta_glb_eta_HybridSTA_Mass"," sta glb Hydrid Z Mass ;#eta mu STA;GeV",etaBins, etaMin, etaMax ,massBins, massMin, massMax )
        #TH2F_sta_glb_phi_HybridSTA_Mass = TH2F("sta_glb_phi_HybridSTA_Mass"," sta glb Hydrid Z Mass ;#phi mu STA;GeV",phiBins, phiMin, phiMax ,massBins, massMin, massMax )
#
        ##glb gen 
#
        #TH2F_glb_gen_pt_ptRes = TH2F("glb_gen_pt_v_ptRes"," glb vs gen p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResMin, ptResMax )
        #TH2F_glb_gen_eta_ptRes = TH2F("glb_gen_eta_v_ptRes"," glb vs gen p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResMin, ptResMax )
#
        ##sta gen
        #TH2F_sta_gen_pt_ptRes = TH2F("sta_gen_pt_v_ptRes"," sta vs gen p_{T}Res ;p_{T};pTRes",ptBins, ptMin, ptMax ,ptResBins, ptResSTA[0], ptResSTA[1] )
        #TH2F_sta_gen_eta_ptRes = TH2F("sta_gen_eta_v_ptRes"," sta vs gen p_{T}Res ;#eta;pTRes",etaBins, etaMin, etaMax ,ptResBins, ptResSTA[0], ptResSTA[1])







    if not os.path.exists(fileOut):
        os.makedirs(fileOut)

    if drawPNG:
        if gen_histograms:
            #TH2F_glb_gen_pt_ptRes.Draw("colz")
            #c1.SaveAs("{}/TH2F_glb_gen_pt_ptRes.png".format(fileOut))
            #TH2F_glb_gen_eta_ptRes.Draw("colz")
            #c1.SaveAs("{}/TH2F_glb_gen_eta_ptRes.png".format(fileOut))
            #STA GEN
            #TH2F_sta_gen_pt_ptRes.Draw("colz")
            #c1.SaveAs("{}/TH2F_sta_gen_pt_ptRes.png".format(fileOut))
            #TH2F_sta_gen_eta_ptRes.Draw("colz")
            #c1.SaveAs("{}/TH2F_sta_gen_eta_ptRes.png".format(fileOut))
            #PT Pull
            TH2F_gen_glb_eta_ptPull.Draw("colz")
            c1.SaveAs("{}/TH2F_gen_glb_eta_ptPull.png".format(fileOut))
            TH2F_gen_glb_pt_ptPull.Draw("colz")
            c1.SaveAs("{}/TH2F_gen_glb_pt_ptPull.png".format(fileOut))
            #PT Res
            TH2F_gen_glb_eta_ptRes.Draw("colz")
            c1.SaveAs("{}/TH2F_gen_glb_eta_ptRes.png".format(fileOut))
            TH2F_gen_glb_phi_ptRes.Draw("colz")
            c1.SaveAs("{}/TH2F_gen_glb_phi_ptRes.png".format(fileOut))
            TH2F_gen_glb_pt_ptRes.Draw("colz")
            c1.SaveAs("{}/TH2F_gen_glb_pt_ptRes.png".format(fileOut))

        #Phi
        TH1F_sta_glb_delta_phi_barrel.Draw()
        c1.SaveAs("{}/TH1F_sta_glb_delta_phi_barrel.png".format(fileOut))
        TH1F_sta_glb_delta_phi_endcap.Draw()
        c1.SaveAs("{}/TH1F_sta_glb_delta_phi_endcap.png".format(fileOut)) 
        TH1F_sta_trk_delta_phi_barrel.Draw()
        c1.SaveAs("{}/TH1F_sta_trk_delta_phi_barrel.png".format(fileOut))
        TH1F_sta_trk_delta_phi_endcap.Draw()
        c1.SaveAs("{}/TH1F_sta_trk_delta_phi_endcap.png".format(fileOut))
        TH1F_sta_glb_delta_phi.Draw()
        c1.SaveAs("{}/TH1F_sta_glb_delta_phi.png".format(fileOut))
        TH1F_sta_trk_delta_phi.Draw()
        c1.SaveAs("{}/TH1F_sta_trk_delta_phi.png".format(fileOut))
        #PT Pull
        TH2F_glb_sta_eta_ptPull.Draw("colz")
        c1.SaveAs("{}/TH2F_glb_sta_eta_ptPull.png".format(fileOut))
        TH2F_glb_sta_pt_ptPull.Draw("colz")
        c1.SaveAs("{}/TH2F_glb_sta_pt_ptPull.png".format(fileOut))
        #Hybrid mass
        TH2F_sta_glb_pt_HybridSTA_Mass.Draw("colz")
        c1.SaveAs("{}/TH2F_sta_glb_pt_HybridSTA_Mass.png".format(fileOut))
        TH2F_sta_glb_eta_HybridSTA_Mass.Draw("colz")
        c1.SaveAs("{}/TH2F_sta_glb_eta_HybridSTA_Mass.png".format(fileOut))
        TH2F_sta_glb_phi_HybridSTA_Mass.Draw("colz")
        c1.SaveAs("{}/TH2F_sta_glb_phi_HybridSTA_Mass.png".format(fileOut))
        #NChi2
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
        TH2F_sta_eta_nChi2.Draw("colz")
        c1.SaveAs("{}/TH2F_sta_eta_nChi2.png".format(fileOut))
        TH2F_sta_pt_nChi2.Draw("colz")
        c1.SaveAs("{}/TH2F_sta_pt_nChi2.png".format(fileOut)) 
        #PT Res
        TH2F_glb_sta_eta_ptRes.Draw("colz")
        c1.SaveAs("{}/TH2F_glb_sta_eta_ptRes.png".format(fileOut))
        TH2F_glb_sta_phi_ptRes.Draw("colz")
        c1.SaveAs("{}/TH2F_glb_sta_phi_ptRes.png".format(fileOut))
        TH2F_glb_sta_pt_ptRes.Draw("colz")
        c1.SaveAs("{}/TH2F_glb_sta_pt_ptRes.png".format(fileOut))
        TH2F_glb_sta_phi_ptRes_endcap.Draw("colz")
        c1.SaveAs("{}/TH2F_glb_sta_phi_ptRes_endcap.png".format(fileOut))
        TH2F_glb_sta_phi_ptRes_barrel.Draw("colz")
        c1.SaveAs("{}/TH2F_glb_sta_phi_ptRes_barrel.png".format(fileOut))
        #N hits
        TH2F_glb_eta_nHits.Draw("colz")
        c1.SaveAs("{}/TH2F_glb_eta_nHits.png".format(fileOut))
        TH2F_glb_pt_nHits.Draw("colz")
        c1.SaveAs("{}/TH2F_glb_pt_nHits.png".format(fileOut)) 

    outFile.Write()
    outFile.Close()
    
     
        