#!/usr/bin/env python
import os

IOVs = ["2016UL_IOV1", "2016UL_IOV2", "2016UL_IOV3"]

DTs = [
        "data_DT-1100-111111_2016UL_IOV1_CMSSW106_JSON-271036-276314_dataRun2_MuAl_v1_01.db", 
        "data_DT-1100-111111_2016UL_IOV2_CMSSW106_JSON-276315-280927_dataRun2_MuAl_v1_01.db", 
        "data_DT-1100-111111_2016UL_IOV3_CMSSW106_JSON-280928-284044_dataRun2_MuAl_v1_01.db"
      ]

CSCs = [ 
         "data_CSC-1100-110001_2016UL_IOV1_CMSSW106_JSON-271036-276314_dataRun2_MuAl_v1_01.db",  
         "data_CSC-1100-110001_2016UL_IOV2_CMSSW106_JSON-276315-280927_dataRun2_MuAl_v1_01.db",
         "data_CSC-1100-110001_2016UL_IOV3_CMSSW106_JSON-280928-284044_dataRun2_MuAl_v1_01.db"
       ]

GPRs = [
         "GPR_Oct5_2019_SW1064_GT106X_dataRun2_UL2016TkAl_v24_IOV1_dL4_iter1.db", 
         "GPR_Oct6_2019_SW1064_GT106X_dataRun2_UL2016TkAl_v24_IOV2_dL4_iter1.db", 
         "GPR_Oct7_2019_SW1064_GT106X_dataRun2_UL2016TkAl_v24_IOV3_dL4_iter1.db"
       ]

dataSets = [
            ["/SingleMuon/Run2016B-ZMu-07Aug17_ver2-v1/RAW-RECO", "/SingleMuon/Run2016C-ZMu-07Aug17-v1/RAW-RECO"], 
            ["/SingleMuon/Run2016D-ZMu-07Aug17-v1/RAW-RECO", "/SingleMuon/Run2016E-ZMu-07Aug17-v1/RAW-RECO"], 
            ["/SingleMuon/Run2016H-ZMu-07Aug17-v1/RAW-RECO"]
           ]

JSONs = [
          "2016UL_IOV1_JSON.txt",
          "2016UL_IOV2_JSON.txt",
          "2016UL_IOV3_JSON.txt"
        ]
GT = "106X_dataRun2_UL2016TkAl_v24" 

USER = "hyunyong"


tmpCFG = "refit_ideal_MuAl_tmp_cfg.py"
tmpCRAB = "crab_tmp_config.py"

for i, IOV in enumerate(IOVs):
  inputs = {'tmpCFG':tmpCFG, 'GT':GT, 'DT':DTs[i], 'CSC':CSCs[i], 'GPR':GPRs[i], 'outCFG':"refit_ideal_MuAl_{}_cfg.py".format(IOV)}
  os.system("cat {tmpCFG} | sed -e 's/GTINPUT/{GT}/; s/DTDBINPUT/{DT}/; s/CSCDBINPUT/{CSC}/; s/GPRDBINPUT/{GPR}/' > {outCFG}".format(**inputs))

for i, dataSet in enumerate(dataSets):
  for d in dataSet:
    ext = ""
    if len(dataSet)>1: ext = d.split("/")[2].split("-")[0][-1]
    d=d.replace("/","\/")
    inputs = {'tmpCRAB':tmpCRAB, 'REQUESTNAME':"MuAlRefit_data_"+IOVs[i]+ext, 'CFGNAME':"refit_ideal_MuAl_{}_cfg.py".format(IOVs[i]), 'DT':DTs[i], 'CSC':CSCs[i], 'GPR':GPRs[i], 'JSONINPUT':JSONs[i], 'DATASET':d, 'USER':USER,'STORAGEDIR':IOVs[i] ,'outCRAB':"crab_{}_config.py".format(IOVs[i]+ext)}
    os.system("cat {tmpCRAB} | sed -e 's/REQUESTNAME/{REQUESTNAME}/; s/CFGNAME/{CFGNAME}/; s/DTDBINPUT/{DT}/; s/CSCDBINPUT/{CSC}/; s/GPRDBINPUT/{GPR}/; s/DATASET/{DATASET}/; s/JSONINPUT/{JSONINPUT}/; s/USER/{USER}/; s/STORAGEDIR/{STORAGEDIR}/' > {outCRAB}".format(**inputs))
