import ROOT
from ROOT import TFile, TTree, TH1F, TCanvas, TProfile, TH2F,  TCollection, TLegend, gStyle
import  math, sys, os

gStyle.SetOptStat(0);
gStyle.SetLegendBorderSize(0);
gStyle.SetLegendFillColor(0);

execfile("functions.py")
execfile("constants.py")
oldTTrees = False

for Samples in range(2):
  oldTTrees = True
  if Samples==0:
    outputFolderName = "MuAlRefit_Zmumu_3dof_6dof"
    fileList = ["MuAlRefit_Zmumu_DT3DOF_CSCideal_APEdia.root","MuAlRefit_Zmumu_DT6DOF_CSCideal_APEcovx2.root"]#    fileListName = [ "Legacy","Legacy pos","Legacy neg"]
    fileListName = [ "3dof","6dof"]
    colors = [ROOT.kRed,ROOT.kBlack]
  if Samples==1:
    outputFolderName = "MuAlRefit_Zmumu_6dof_6dofpos_6dofneg"
    fileList = ["MuAlRefit_Zmumu_DT6DOF_CSCideal_APEcovx2.root","MuAlRefit_Zmumu_DT6DOF_CSCideal_APEcovx2_pos.root","MuAlRefit_Zmumu_DT6DOF_CSCideal_APEcovx2_neg.root"]#    fileListName = [ "Legacy","Legacy pos","Legacy neg"]
    fileListName = [ "6dof","6dof pos","6dof neg"]
    colors = [ROOT.kRed,ROOT.kBlack,ROOT.kBlue]

#  if Samples==0:
#    outputFolderName = "MuAlRefit_3dof_pos_neg"
#    fileList = ["MuAlRefit_Legacy_GeoOld_APEold.root","MuAlRefit_Legacy_GeoOld_APEold_pos.root","MuAlRefit_Legacy_GeoOld_APEold_neg.root"]#    fileListName = [ "Legacy","Legacy pos","Legacy neg"]
#    fileListName = [ "3dof","3dof pos","3dof neg"]
#    colors = [ROOT.kRed,ROOT.kBlack,ROOT.kBlue]

#  if Samples==0:
#    outputFolderName = "MuAlRefit_Leg_Legpos_Legneg"
#    fileList = ["MuAlRefit_Legacy.root","MuAlRefit_Legacy_pos.root","MuAlRefit_Legacy_neg.root"]
#    fileListName = [ "Legacy","Legacy pos","Legacy neg"]
#    colors = [ROOT.kRed,ROOT.kBlack,ROOT.kBlue]
#  if Samples==1:
#    outputFolderName = "MuAlRefit_Leg_Eq"
#    fileList = ["MuAlRefit_Legacy.root","MuAlRefit_Legacy_equal.root"]
#    fileListName = [ "Legacy","Legacy pos=nef"]
#    colors = [ROOT.kRed,ROOT.kBlack]

#  if Samples==0:
#    outputFolderName = "MuAlRefit_Leg_Pro_3DOFapeOld_apeOld"
#    fileList = ["MuAlRefit_Legacy.root","MuAlRefit_Prompt.root","MuAlRefit_Legacy_GeoOld_APEold.root","MuAlRefit_Legacy_APEold.root"]
#    fileListName = [ "Legacy","Prompt","3DOF_oldAPE","oldAPE"]
#    colors = [ROOT.kBlack,ROOT.kRed,ROOT.kBlue,ROOT.kGreen]
# 
#  if Samples==1:
#    outputFolderName = "MuAlRefit_Leg_Pro_apeOld"
#    fileList = ["MuAlRefit_Legacy.root","MuAlRefit_Prompt.root","MuAlRefit_Legacy_APEold.root"]
#    fileListName = [ "Legacy","Prompt","oldAPE"]
#    colors = [ROOT.kBlack,ROOT.kRed,ROOT.kGreen]
#  if Samples==2:
#    outputFolderName = "MuAlRefit_Leg_Pro_APEx2"
#    fileList = ["MuAlRefit_Legacy.root","MuAlRefit_Prompt.root","MuAlRefit_Legacy_APEminuitx2.root"]
#    fileListName = [ "Legacy","Prompt","APE minuit"]
#    colors = [ROOT.kBlack,ROOT.kRed,ROOT.kGreen]
#  if Samples==3:
#    outputFolderName = "MuAlRefit_Leg_Pro_3DOF"
#    fileList = ["MuAlRefit_Legacy.root","MuAlRefit_Prompt.root","MuAlRefit_Legacy_GeoOld_APEold.root"]
#    fileListName = [ "Legacy","Prompt","3DOF_oldAPE"]
#    colors = [ROOT.kBlack,ROOT.kRed,ROOT.kGreen]
#  if Samples==4:
#    outputFolderName = "MuAlRefit_Leg_Pro"
#    fileList = ["MuAlRefit_Legacy.root","MuAlRefit_Prompt.root"]
#    fileListName = [ "Legacy","Prompt"]
#    colors = [ROOT.kBlack,ROOT.kRed]

  print "Running on: ",fileList
  print "Output: ",outputFolderName,"----------------------------------"
  
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
  if not oldTTrees:
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
  
  #makeProfile("glb_sta_eta_v_ptRes_type_2","res",nBins,"gaus",drawBinPlots,ptResType2STAMeanRange,ptResType2STASigmaRange)
  #makeProfile("glb_sta_phi_v_ptRes_type_2","res",nBins,"gaus",drawBinPlots,ptResType2STAMeanRange,ptResType2STASigmaRange)
  #makeProfile("glb_sta_pt_v_ptRes_type_2","res",nBins,"gaus",drawBinPlots,ptResType2STAMeanRange,ptResType2STASigmaRange)
  #makeProfile("gen_sta_eta_v_ptRes_type_2","res",nBins,"gaus",drawBinPlots,ptResType2STAMeanRange,ptResType2STASigmaRange)
  #makeProfile("gen_sta_phi_v_ptRes_type_2","res",nBins,"gaus",drawBinPlots,ptResType2STAMeanRange,ptResType2STASigmaRange)
  #makeProfile("gen_sta_pt_v_ptRes_type_2","res",nBins,"gaus",drawBinPlots,ptResType2STAMeanRange,ptResType2STASigmaRange)
  
  makeProfile("TH2F_glb_sta_eta_ptPull","pull",nBins,"gaus",drawBinPlots,ptPullSTAMeanRange,ptPullSTASigmaRange)
  makeProfile("TH2F_glb_sta_pt_ptPull","pull",nBins,"gaus",drawBinPlots,ptPullSTAMeanRange,ptPullSTASigmaRange)
  
  makeProfile("glb_sta_eta_v_ptRes","res",nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange)
  makeProfile("glb_sta_phi_v_ptRes","res",nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange)
  makeProfile("glb_sta_phi_v_ptRes_endcap","res",nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange)
  makeProfile("glb_sta_phi_v_ptRes_barrel","res",nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange)
  
  makeProfile("sta_glb_pt_HybridSTA_Mass","mass",nBins, "gaus", drawBinPlots,massMeanRange,massSigmaRange)
  makeProfile("sta_glb_phi_HybridSTA_Mass","mass",nBins, "gaus", drawBinPlots,massMeanRange,massSigmaRange)
  makeProfile("sta_glb_eta_HybridSTA_Mass","mass",nBins, "gaus", drawBinPlots,massMeanRange,massSigmaRange)
