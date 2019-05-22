import ROOT
from ROOT import TFile, TTree, TH1F, TCanvas, TProfile, TH2F,  TCollection, TLegend, gStyle, TPaveStats, TLatex, TRatioPlot
import  math, sys, os

gStyle.SetOptStat(0);
gStyle.SetLegendBorderSize(0);
gStyle.SetLegendFillColor(0);

execfile("functions.py")
execfile("constants.py")

#tot_fileList     = ["MuAlRefit_2017B_2016Geom.root","MuAlRefit_2017B_DT6DOFnoT0it1CSC3DOF_Official.root","MuAlRefit_2017B_DT3DOFnoT0it1CSC3DOF_1refit.root","MuAlRefit_2017B_DT6DOFnoT0it1CSC3DOF_OfficialAPEDTminuit_CSCasym.root","MuAlRefit_2017B_fromGT.root"]
#tot_fileListName = ["2017B data (2016 geom.)","2017B After 6DOF","2017B After 3DOF 1refit","2017B data (2017 geom.)","2017B Before"]
#tot_colors       = [ROOT.kRed,ROOT.kBlue,ROOT.kBlack,ROOT.kGreen+3,ROOT.kOrange]
#Combinations      = [[0,3]]#,[1,3],[3,4],[0,1,3]]
#tot_outputFolderName  = ["Out2017B_Legacy_After6DOFAPE","Out2017B_After6DOF_After6DOFAPE","Out2017B_After6DOFAPE_Before","Out2017B_Legacy_After6DOF_After6DOFAPE"]

tot_fileList     = ["MuAlRefit_Run2017F_UL_Vanilla_IOV3_step1.root", "MuAlRefit_Run2017F_UL_ReReco_IOV3_Step1.root", "MuAlRefit_Run2017B_UL_ReReco_IOV3_oldAPE_Step1.root"]
tot_fileList     = ["MuAlRefit_Run2017B_UL_old_IOV2_step1.root", "MuAlRefit_Run2017B_UL_ReReco_IOV2_step1.root", "MuAlRefit_Run2017B_UL_ReReco_IOV2_oldAPE_step1.root"]
tot_fileList     = ["MuAlRefit_Run2017B_UL_old_step1.root", "MuAlRefit_Run2017B_UL_ReReco_step1.root", "MuAlRefit_Run2017B_UL_ReReco_oldAPE_step1.root"]
tot_fileList     = ["vanilla.root", "oldAPE.root"]
tot_fileList     = ["MuAlRefit_Run2017F_UL_Vanilla_IOV3_step1.root", "MuAlRefit_Run2017B_UL_ReReco_IOV3_oldAPE_oldTracker_step1.root", "MuAlRefit_Run2017B_UL_ReReco_IOV3_oldAPE_Step1.root"]
#tot_fileList     = ["MuAlRefit_Run2017B_UL_old_IOV2_step1.root", "MuAlRefit_Run2017B_UL_ReReco_IOV2_step1.root"]
#tot_fileList     = ["MuAlRefit_Run2017B_UL_old_step1.root", "MuAlRefit_Run2017B_UL_ReReco_step1.root"]
tot_fileListName = ["EOY2017 + New Tracker", "EOY2017", "UL ReReco"]
tot_colors       = [ROOT.kRed,  ROOT.kBlue, ROOT.kBlack]
Combinations      = [[0,1,2]]#,[1,3],[3,4],[0,1,3]]
tot_outputFolderName  = ["2017_UL_IOV3_oldMA_oldTrk"]


drawTRatio = True

iC = 0
for Comb in Combinations:
  outputFolderName = tot_outputFolderName[iC]
  fileList = []
  for iF in Comb: fileList.append(tot_fileList[iF])
  fileListName = []
  for iF in Comb: fileListName.append(tot_fileListName[iF])
  colors = []
  for iF in Comb: colors.append(tot_colors[iF])
  print "Running on:"
  print fileList, fileListName
  print "Output", outputFolderName
  iC += 1

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
    makeProfile("glb_gen_pt_v_ptRes", "res", nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange, drawTRatio)
    makeProfile("sta_gen_pt_v_ptRes" , "res", nBins,"gaus",drawBinPlots,ptResSTAMeanRange,ptResSTASigmaRange, drawTRatio)
    makeProfile("sta_gen_eta_v_ptRes", "res", nBins,"gaus",drawBinPlots,ptResSTAMeanRange,ptResSTASigmaRange, drawTRatio)
    makeProfile("TH2F_gen_glb_eta_ptPull","pull",nBins,"gaus",drawBinPlots,ptPullGLBMeanRange,ptPullGLBSigmaRange, drawTRatio)
    makeProfile("TH2F_gen_glb_pt_ptPull","pull",nBins,"gaus",drawBinPlots,ptPullGLBMeanRange,ptPullGLBSigmaRange, drawTRatio)
    makeProfile("gen_glb_eta_v_ptRes","res",nBins, "gaus", drawBinPlots, ptResGLBMeanRange, ptResGLBSigmaRange, drawTRatio)
    makeProfile("gen_glb_phi_v_ptRes","res",nBins, "gaus", drawBinPlots, ptResGLBMeanRange, ptResGLBSigmaRange, drawTRatio)
    makeProfile("gen_glb_pt_v_ptRes","res",nBins, "gaus", drawBinPlots, ptResGLBMeanRange, ptResGLBSigmaRange), drawTRatio 

  makeProfile("TH2F_glb_sta_eta_ptPull","pull",nBins,"gaus",drawBinPlots,ptPullSTAMeanRange,ptPullSTASigmaRange, drawTRatio)
  makeProfile("TH2F_glb_sta_pt_ptPull" ,"pull", nBins,"gaus",drawBinPlots,ptPullSTAMeanRange,ptPullSTASigmaRange, drawTRatio)

  make1D("TH1F_sta_nChi2_barrel")
  make1D("TH1F_sta_nChi2_endcap")
  make1D("TH1F_glb_nChi2_endcap")
  make1D("TH1F_glb_nChi2_barrel")
  make1D("TH1F_sta_trk_delta_phi")
  make1D("TH1F_sta_trk_delta_phi_barrel")
  make1D("TH1F_sta_trk_delta_phi_endcap")
  make1D("TH1F_sta_glb_delta_phi")
  make1D("TH1F_sta_glb_delta_phi_barrel")
  make1D("TH1F_sta_glb_delta_phi_endcap")

  makeProfile("TH2F_glb_eta_nChi2","general",nBins,"mean",drawBinPlots,nChi2MeanRange,nChi2RMSRange, drawTRatio)
  makeProfile("TH2F_sta_eta_nChi2","general",nBins,"mean",drawBinPlots,nChi2MeanRange,nChi2RMSRange, drawTRatio)
  makeProfile("TH2F_glb_nChi2_pt","general",nBins,"mean",drawBinPlots,nChi2MeanRange,nChi2RMSRange, drawTRatio)
  makeProfile("TH2F_glb_eta_nHits","general",nBins,"mean",drawBinPlots,nHitsMeanRange,nHitsRMSRange, drawTRatio)
  makeProfile("TH2F_glb_pt_nHits","general",nBins,"mean",drawBinPlots,nHitsMeanRange,nHitsRMSRange, drawTRatio)

  makeProfile("TH2F_glb_sta_eta_ptPull","pull",nBins,"gaus",drawBinPlots,ptPullSTAMeanRange,ptPullSTASigmaRange, drawTRatio)
  makeProfile("TH2F_glb_sta_pt_ptPull","pull",nBins,"gaus",drawBinPlots,ptPullSTAMeanRange,ptPullSTASigmaRange, drawTRatio)

  makeProfile("glb_sta_eta_v_ptRes","res",nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange, drawTRatio)
  makeProfile("glb_sta_phi_v_ptRes","res",nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange, drawTRatio)
  makeProfile("glb_sta_pt_v_ptRes","res",nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange, drawTRatio)
  makeProfile("glb_sta_phi_v_ptRes_endcap","res",nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange, drawTRatio)
  makeProfile("glb_sta_phi_v_ptRes_barrel","res",nBins, "gaus", drawBinPlots,ptResMeanRange,ptResSigmaRange, drawTRatio)

  makeProfile("sta_glb_pt_HybridSTA_Mass","mass",nBins, "gaus", drawBinPlots,massMeanRange,massSigmaRange, drawTRatio)
  makeProfile("sta_glb_phi_HybridSTA_Mass","mass",nBins, "gaus", drawBinPlots,massMeanRange,massSigmaRange, drawTRatio)
  makeProfile("sta_glb_eta_HybridSTA_Mass","mass",nBins, "gaus", drawBinPlots,massMeanRange,massSigmaRange, drawTRatio)
  makeProfile("sta_glb_eta_HybridSTA_Mass","mass",nBins, "mean", drawBinPlots,massMeanRange,massSigmaRange, drawTRatio)
