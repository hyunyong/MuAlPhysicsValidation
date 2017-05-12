from ROOT import TFile, TTree, TH1F, TCanvas, TProfile, TH2F,  TCollection, TLegend, gStyle
import  math, sys, os

gStyle.SetOptStat(0);
gStyle.SetLegendBorderSize(0);
gStyle.SetLegendFillColor(0);

execfile("functions.py")
execfile("constants.py")

#outputFolderName = "MuAlRefit_Legacy_Prompt"
##fileList = ["MuAlRefit_Legacy.root","MuAlRefit_Prompt.root"]
#fileListName = [ "Legacy","Prompt"]
outputFolderName = "MuAlRefit_Legacy_local"
fileList = ["MuAlRefit_Legacy.root","MuAlRefit_Legacy_dbLocal.root"]
fileListName = [ "Legacy","Legacy_loc"]
colors = [2,1]

files = []
TH2F_temp = []
if not os.path.exists(outputFolderName):
	os.makedirs(outputFolderName)
for count, file in enumerate(fileList):
	files.append( TFile.Open(file, "read"))

########################################################################################
## Draw Profiles
########################################################################################

if isMC:
	makeProfile("glb_gen_pt_v_ptRes", "res", nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange)
	makeProfile("sta_gen_pt_v_ptRes" , "res", nBins,"gaus",drawBinPlots,ptResSTAMeanRange,ptResSTASigmaRange)
	makeProfile("sta_gen_eta_v_ptRes", "res", nBins,"gaus",drawBinPlots,ptResSTAMeanRange,ptResSTASigmaRange)
	makeProfile("TH2F_gen_glb_eta_ptPull","pull",nBins,"gaus",drawBinPlots,ptPullGLBMeanRange,ptPullGLBSigmaRange)
	makeProfile("TH2F_gen_glb_pt_ptPull","pull",nBins,"gaus",drawBinPlots,ptPullGLBMeanRange,ptPullGLBSigmaRange) 
	makeProfile("gen_glb_eta_v_ptRes","res",nBins, "gaus", drawBinPlots, ptResGLBMeanRange, ptResGLBSigmaRange)
	makeProfile("gen_glb_phi_v_ptRes","res",nBins, "gaus", drawBinPlots, ptResGLBMeanRange, ptResGLBSigmaRange)
	makeProfile("gen_glb_pt_v_ptRes","res",nBins, "gaus", drawBinPlots, ptResGLBMeanRange, ptResGLBSigmaRange) 

makeProfile("TH2F_glb_sta_eta_ptPull","pull",nBins,"gaus",drawBinPlots,ptPullSTAMeanRange,ptPullSTASigmaRange)
makeProfile("TH2F_glb_sta_pt_ptPull" ,"pull", nBins,"gaus",drawBinPlots,ptPullSTAMeanRange,ptPullSTASigmaRange)


make1D("TH1F_sta_nChi2_barrel")
make1D("TH1F_sta_nChi2_endcap")
make1D("TH1F_glb_nChi2_endcap")
make1D("TH1F_glb_nChi2_barrel")


make1D("TH1F_sta_TRK_delta_phi")     
make1D("TH1F_sta_TRK_delta_phi_barrel")     
make1D("TH1F_sta_TRK_delta_phi_endcap")     
make1D("TH1F_sta_glb_delta_phi")     
make1D("TH1F_sta_glb_delta_phi_barrel")     
make1D("TH1F_sta_glb_delta_phi_endcap")  


makeProfile("TH2F_glb_eta_nChi2","general",nBins,"mean",drawBinPlots,nChi2MeanRange,nChi2RMSRange)
makeProfile("TH2F_glb_nChi2_pt","general",nBins,"mean",drawBinPlots,nChi2MeanRange,nChi2RMSRange)
makeProfile("TH2F_glb_eta_nHits","general",nBins,"mean",drawBinPlots,nHitsMeanRange,nHitsRMSRange)
makeProfile("TH2F_glb_pt_nHits","general",nBins,"mean",drawBinPlots,nHitsMeanRange,nHitsRMSRange)

makeProfile("glb_sta_eta_v_ptRes_type_2","res",nBins,"gaus",drawBinPlots,ptResType2STAMeanRange,ptResType2STASigmaRange)
makeProfile("glb_sta_phi_v_ptRes_type_2","res",nBins,"gaus",drawBinPlots,ptResType2STAMeanRange,ptResType2STASigmaRange)
makeProfile("glb_sta_pt_v_ptRes_type_2","res",nBins,"gaus",drawBinPlots,ptResType2STAMeanRange,ptResType2STASigmaRange)
makeProfile("gen_sta_eta_v_ptRes_type_2","res",nBins,"gaus",drawBinPlots,ptResType2STAMeanRange,ptResType2STASigmaRange)
makeProfile("gen_sta_phi_v_ptRes_type_2","res",nBins,"gaus",drawBinPlots,ptResType2STAMeanRange,ptResType2STASigmaRange)
makeProfile("gen_sta_pt_v_ptRes_type_2","res",nBins,"gaus",drawBinPlots,ptResType2STAMeanRange,ptResType2STASigmaRange)


makeProfile("TH2F_glb_sta_eta_ptPull","pull",nBins,"gaus",drawBinPlots,ptPullSTAMeanRange,ptPullSTASigmaRange)
makeProfile("TH2F_glb_sta_pt_ptPull","pull",nBins,"gaus",drawBinPlots,ptPullSTAMeanRange,ptPullSTASigmaRange)



makeProfile("glb_sta_eta_v_ptRes","res",nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange)
makeProfile("glb_sta_phi_v_ptRes","res",nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange)
makeProfile("glb_sta_phi_v_ptRes_endcap","res",nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange)
makeProfile("glb_sta_phi_v_ptRes_barrel","res",nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange)

makeProfile("sta_glb_pt_HybridSTA_Mass","mass",nBins, "gaus", drawBinPlots,massMeanRange,massSigmaRange)
makeProfile("sta_glb_phi_HybridSTA_Mass","mass",nBins, "gaus", drawBinPlots,massMeanRange,massSigmaRange)
makeProfile("sta_glb_eta_HybridSTA_Mass","mass",nBins, "gaus", drawBinPlots,massMeanRange,massSigmaRange)



