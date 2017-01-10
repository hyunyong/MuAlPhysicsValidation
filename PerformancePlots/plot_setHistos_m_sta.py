# ------------------------------------------------------------------------------
# Dimuon mass
# ------------------------------------------------------------------------------

h_m_sta, h_m_sta_label, h_m_sta_title, h_m_sta_x, h_m_sta_y = [], "sta_m", "Mass for STA dimuons", "m_{STA}", "a.u."
histos.append( [h_m_sta, h_m_sta_label, h_m_sta_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )

# ------------------------------------------------------------------------------
# Dimuon mass in 16 bins of etaMuP (-2.4 < etaMuP < 2.4)
# ------------------------------------------------------------------------------

h_m_HybSta_etaSta_m24_m21, h_m_HybSta_etaSta_m24_m21_label, h_m_HybSta_etaSta_m24_m21_title = [], "m_HybSta_etaSta_m24_m21", "Mass for GLB+STA dimuons:  -2.4 < #eta_{#mu^{+}} < -2.1"
h_m_HybSta_etaSta_m21_m18, h_m_HybSta_etaSta_m21_m18_label, h_m_HybSta_etaSta_m21_m18_title = [], "m_HybSta_etaSta_m21_m18", "Mass for GLB+STA dimuons:  -2.1 < #eta_{#mu^{+}} < -1.8"
h_m_HybSta_etaSta_m18_m15, h_m_HybSta_etaSta_m18_m15_label, h_m_HybSta_etaSta_m18_m15_title = [], "m_HybSta_etaSta_m18_m15", "Mass for GLB+STA dimuons:  -1.8 < #eta_{#mu^{+}} < -1.5"
h_m_HybSta_etaSta_m15_m12, h_m_HybSta_etaSta_m15_m12_label, h_m_HybSta_etaSta_m15_m12_title = [], "m_HybSta_etaSta_m15_m12", "Mass for GLB+STA dimuons:  -1.5 < #eta_{#mu^{+}} < -1.2"
h_m_HybSta_etaSta_m12_m09, h_m_HybSta_etaSta_m12_m09_label, h_m_HybSta_etaSta_m12_m09_title = [], "m_HybSta_etaSta_m12_m09", "Mass for GLB+STA dimuons:  -1.2 < #eta_{#mu^{+}} < -0.9"
h_m_HybSta_etaSta_m09_m06, h_m_HybSta_etaSta_m09_m06_label, h_m_HybSta_etaSta_m09_m06_title = [], "m_HybSta_etaSta_m09_m06", "Mass for GLB+STA dimuons:  -0.9 < #eta_{#mu^{+}} < -0.6"
h_m_HybSta_etaSta_m06_m03, h_m_HybSta_etaSta_m06_m03_label, h_m_HybSta_etaSta_m06_m03_title = [], "m_HybSta_etaSta_m06_m03", "Mass for GLB+STA dimuons:  -0.6 < #eta_{#mu^{+}} < -0.3"
h_m_HybSta_etaSta_m03_m00, h_m_HybSta_etaSta_m03_m00_label, h_m_HybSta_etaSta_m03_m00_title = [], "m_HybSta_etaSta_m03_m00", "Mass for GLB+STA dimuons:  -0.3 < #eta_{#mu^{+}} < 0"
h_m_HybSta_etaSta_p00_p03, h_m_HybSta_etaSta_p00_p03_label, h_m_HybSta_etaSta_p00_p03_title = [], "m_HybSta_etaSta_p00_p03", "Mass for GLB+STA dimuons:  0 < #eta_{#mu^{+}} < 0.3"
h_m_HybSta_etaSta_p03_p06, h_m_HybSta_etaSta_p03_p06_label, h_m_HybSta_etaSta_p03_p06_title = [], "m_HybSta_etaSta_p03_p06", "Mass for GLB+STA dimuons:  0.3 < #eta_{#mu^{+}} < 0.6"
h_m_HybSta_etaSta_p06_p09, h_m_HybSta_etaSta_p06_p09_label, h_m_HybSta_etaSta_p06_p09_title = [], "m_HybSta_etaSta_p06_p09", "Mass for GLB+STA dimuons:  0.6 < #eta_{#mu^{+}} < 0.9"
h_m_HybSta_etaSta_p09_p12, h_m_HybSta_etaSta_p09_p12_label, h_m_HybSta_etaSta_p09_p12_title = [], "m_HybSta_etaSta_p09_p12", "Mass for GLB+STA dimuons:  0.9 < #eta_{#mu^{+}} < 1.2"
h_m_HybSta_etaSta_p12_p15, h_m_HybSta_etaSta_p12_p15_label, h_m_HybSta_etaSta_p12_p15_title = [], "m_HybSta_etaSta_p12_p15", "Mass for GLB+STA dimuons:  1.2 < #eta_{#mu^{+}} < 1.5"
h_m_HybSta_etaSta_p15_p18, h_m_HybSta_etaSta_p15_p18_label, h_m_HybSta_etaSta_p15_p18_title = [], "m_HybSta_etaSta_p15_p18", "Mass for GLB+STA dimuons:  1.5 < #eta_{#mu^{+}} < 1.8"
h_m_HybSta_etaSta_p18_p21, h_m_HybSta_etaSta_p18_p21_label, h_m_HybSta_etaSta_p18_p21_title = [], "m_HybSta_etaSta_p18_p21", "Mass for GLB+STA dimuons:  1.8 < #eta_{#mu^{+}} < 2.1"
h_m_HybSta_etaSta_p21_p24, h_m_HybSta_etaSta_p21_p24_label, h_m_HybSta_etaSta_p21_p24_title = [], "m_HybSta_etaSta_p21_p24", "Mass for GLB+STA dimuons:  2.1 < #eta_{#mu^{+}} < 2.4"

histos.append( [h_m_HybSta_etaSta_m24_m21, h_m_HybSta_etaSta_m24_m21_label, h_m_HybSta_etaSta_m24_m21_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_m21_m18, h_m_HybSta_etaSta_m21_m18_label, h_m_HybSta_etaSta_m21_m18_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_m18_m15, h_m_HybSta_etaSta_m18_m15_label, h_m_HybSta_etaSta_m18_m15_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_m15_m12, h_m_HybSta_etaSta_m15_m12_label, h_m_HybSta_etaSta_m15_m12_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_m12_m09, h_m_HybSta_etaSta_m12_m09_label, h_m_HybSta_etaSta_m12_m09_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_m09_m06, h_m_HybSta_etaSta_m09_m06_label, h_m_HybSta_etaSta_m09_m06_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_m06_m03, h_m_HybSta_etaSta_m06_m03_label, h_m_HybSta_etaSta_m06_m03_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_m03_m00, h_m_HybSta_etaSta_m03_m00_label, h_m_HybSta_etaSta_m03_m00_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_p00_p03, h_m_HybSta_etaSta_p00_p03_label, h_m_HybSta_etaSta_p00_p03_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_p03_p06, h_m_HybSta_etaSta_p03_p06_label, h_m_HybSta_etaSta_p03_p06_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_p06_p09, h_m_HybSta_etaSta_p06_p09_label, h_m_HybSta_etaSta_p06_p09_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_p09_p12, h_m_HybSta_etaSta_p09_p12_label, h_m_HybSta_etaSta_p09_p12_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_p12_p15, h_m_HybSta_etaSta_p12_p15_label, h_m_HybSta_etaSta_p12_p15_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_p15_p18, h_m_HybSta_etaSta_p15_p18_label, h_m_HybSta_etaSta_p15_p18_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_p18_p21, h_m_HybSta_etaSta_p18_p21_label, h_m_HybSta_etaSta_p18_p21_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_etaSta_p21_p24, h_m_HybSta_etaSta_p21_p24_label, h_m_HybSta_etaSta_p21_p24_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )

h_m_sta_etaMuP_m24_m21, h_m_sta_etaMuP_m24_m21_label, h_m_sta_etaMuP_m24_m21_title = [], "m_sta_etaMuP_m24_m21", "Mass for STA dimuons:  -2.4 < #eta_{#mu^{+}} < -2.1"
h_m_sta_etaMuP_m21_m18, h_m_sta_etaMuP_m21_m18_label, h_m_sta_etaMuP_m21_m18_title = [], "m_sta_etaMuP_m21_m18", "Mass for STA dimuons:  -2.1 < #eta_{#mu^{+}} < -1.8"
h_m_sta_etaMuP_m18_m15, h_m_sta_etaMuP_m18_m15_label, h_m_sta_etaMuP_m18_m15_title = [], "m_sta_etaMuP_m18_m15", "Mass for STA dimuons:  -1.8 < #eta_{#mu^{+}} < -1.5"
h_m_sta_etaMuP_m15_m12, h_m_sta_etaMuP_m15_m12_label, h_m_sta_etaMuP_m15_m12_title = [], "m_sta_etaMuP_m15_m12", "Mass for STA dimuons:  -1.5 < #eta_{#mu^{+}} < -1.2"
h_m_sta_etaMuP_m12_m09, h_m_sta_etaMuP_m12_m09_label, h_m_sta_etaMuP_m12_m09_title = [], "m_sta_etaMuP_m12_m09", "Mass for STA dimuons:  -1.2 < #eta_{#mu^{+}} < -0.9"
h_m_sta_etaMuP_m09_m06, h_m_sta_etaMuP_m09_m06_label, h_m_sta_etaMuP_m09_m06_title = [], "m_sta_etaMuP_m09_m06", "Mass for STA dimuons:  -0.9 < #eta_{#mu^{+}} < -0.6"
h_m_sta_etaMuP_m06_m03, h_m_sta_etaMuP_m06_m03_label, h_m_sta_etaMuP_m06_m03_title = [], "m_sta_etaMuP_m06_m03", "Mass for STA dimuons:  -0.6 < #eta_{#mu^{+}} < -0.3"
h_m_sta_etaMuP_m03_m00, h_m_sta_etaMuP_m03_m00_label, h_m_sta_etaMuP_m03_m00_title = [], "m_sta_etaMuP_m03_m00", "Mass for STA dimuons:  -0.3 < #eta_{#mu^{+}} < 0"
h_m_sta_etaMuP_p00_p03, h_m_sta_etaMuP_p00_p03_label, h_m_sta_etaMuP_p00_p03_title = [], "m_sta_etaMuP_p00_p03", "Mass for STA dimuons:  0 < #eta_{#mu^{+}} < 0.3"
h_m_sta_etaMuP_p03_p06, h_m_sta_etaMuP_p03_p06_label, h_m_sta_etaMuP_p03_p06_title = [], "m_sta_etaMuP_p03_p06", "Mass for STA dimuons:  0.3 < #eta_{#mu^{+}} < 0.6"
h_m_sta_etaMuP_p06_p09, h_m_sta_etaMuP_p06_p09_label, h_m_sta_etaMuP_p06_p09_title = [], "m_sta_etaMuP_p06_p09", "Mass for STA dimuons:  0.6 < #eta_{#mu^{+}} < 0.9"
h_m_sta_etaMuP_p09_p12, h_m_sta_etaMuP_p09_p12_label, h_m_sta_etaMuP_p09_p12_title = [], "m_sta_etaMuP_p09_p12", "Mass for STA dimuons:  0.9 < #eta_{#mu^{+}} < 1.2"
h_m_sta_etaMuP_p12_p15, h_m_sta_etaMuP_p12_p15_label, h_m_sta_etaMuP_p12_p15_title = [], "m_sta_etaMuP_p12_p15", "Mass for STA dimuons:  1.2 < #eta_{#mu^{+}} < 1.5"
h_m_sta_etaMuP_p15_p18, h_m_sta_etaMuP_p15_p18_label, h_m_sta_etaMuP_p15_p18_title = [], "m_sta_etaMuP_p15_p18", "Mass for STA dimuons:  1.5 < #eta_{#mu^{+}} < 1.8"
h_m_sta_etaMuP_p18_p21, h_m_sta_etaMuP_p18_p21_label, h_m_sta_etaMuP_p18_p21_title = [], "m_sta_etaMuP_p18_p21", "Mass for STA dimuons:  1.8 < #eta_{#mu^{+}} < 2.1"
h_m_sta_etaMuP_p21_p24, h_m_sta_etaMuP_p21_p24_label, h_m_sta_etaMuP_p21_p24_title = [], "m_sta_etaMuP_p21_p24", "Mass for STA dimuons:  2.1 < #eta_{#mu^{+}} < 2.4"

histos.append( [h_m_sta_etaMuP_m24_m21, h_m_sta_etaMuP_m24_m21_label, h_m_sta_etaMuP_m24_m21_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_m21_m18, h_m_sta_etaMuP_m21_m18_label, h_m_sta_etaMuP_m21_m18_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_m18_m15, h_m_sta_etaMuP_m18_m15_label, h_m_sta_etaMuP_m18_m15_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_m15_m12, h_m_sta_etaMuP_m15_m12_label, h_m_sta_etaMuP_m15_m12_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_m12_m09, h_m_sta_etaMuP_m12_m09_label, h_m_sta_etaMuP_m12_m09_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_m09_m06, h_m_sta_etaMuP_m09_m06_label, h_m_sta_etaMuP_m09_m06_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_m06_m03, h_m_sta_etaMuP_m06_m03_label, h_m_sta_etaMuP_m06_m03_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_m03_m00, h_m_sta_etaMuP_m03_m00_label, h_m_sta_etaMuP_m03_m00_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_p00_p03, h_m_sta_etaMuP_p00_p03_label, h_m_sta_etaMuP_p00_p03_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_p03_p06, h_m_sta_etaMuP_p03_p06_label, h_m_sta_etaMuP_p03_p06_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_p06_p09, h_m_sta_etaMuP_p06_p09_label, h_m_sta_etaMuP_p06_p09_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_p09_p12, h_m_sta_etaMuP_p09_p12_label, h_m_sta_etaMuP_p09_p12_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_p12_p15, h_m_sta_etaMuP_p12_p15_label, h_m_sta_etaMuP_p12_p15_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_p15_p18, h_m_sta_etaMuP_p15_p18_label, h_m_sta_etaMuP_p15_p18_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_p18_p21, h_m_sta_etaMuP_p18_p21_label, h_m_sta_etaMuP_p18_p21_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_etaMuP_p21_p24, h_m_sta_etaMuP_p21_p24_label, h_m_sta_etaMuP_p21_p24_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )

p_mFitSigma_HybSta_etaSta, p_mFitSigma_HybSta_etaSta_label, p_mFitSigma_HybSta_etaSta_title, p_mFitSigma_HybSta_etaSta_x, p_mFitSigma_HybSta_etaSta_y = [], "mFitSigma_HybSta_etaSta", "Mass res. for GLB-STA dimuons (p_{T}>" + str(threshold_pT_GeV) + " GeV)", "#eta_{#mu_{STA}}", "#sigma m_{#mu#mu} [GeV]"
profiles.append( [p_mFitSigma_HybSta_etaSta, p_mFitSigma_HybSta_etaSta_label, p_mFitSigma_HybSta_etaSta_title, p_mFitSigma_HybSta_etaSta_x, p_mFitSigma_HybSta_etaSta_y, mFitSigma_bin, mFitSigma_min, mFitSigma_max, profileEta_bin, profileEta_min, profileEta_max] )

p_mFitMean_HybSta_etaSta, p_mFitMean_HybSta_etaSta_label, p_mFitMean_HybSta_etaSta_title, p_mFitMean_HybSta_etaSta_x, p_mFitMean_HybSta_etaSta_y = [], "mFitMean_HybSta_etaSta", "Mass for GLB-STA dimuons (p_{T}>" + str(threshold_pT_GeV) + " GeV)", "#eta_{#mu_{STA}}", "m_{#mu#mu} [GeV]"
profiles.append( [p_mFitMean_HybSta_etaSta, p_mFitMean_HybSta_etaSta_label, p_mFitMean_HybSta_etaSta_title, p_mFitMean_HybSta_etaSta_x, p_mFitMean_HybSta_etaSta_y, mFitMean_bin, mFitMean_min, mFitMean_max, profileEta_bin, profileEta_min, profileEta_max] )

p_mFitSigma_sta_etaMuP, p_mFitSigma_sta_etaMuP_label, p_mFitSigma_sta_etaMuP_title, p_mFitSigma_sta_etaMuP_x, p_mFitSigma_sta_etaMuP_y = [], "mFitSigma_sta_etaMuP", "Mass res. for STA dimuons (p_{T}>" + str(threshold_pT_GeV) + " GeV)", "#eta_{#mu^{+}}", "#sigma m_{#mu#mu} [GeV]"
profiles.append( [p_mFitSigma_sta_etaMuP, p_mFitSigma_sta_etaMuP_label, p_mFitSigma_sta_etaMuP_title, p_mFitSigma_sta_etaMuP_x, p_mFitSigma_sta_etaMuP_y, mFitSigma_bin, mFitSigma_min, mFitSigma_max, profileEta_bin, profileEta_min, profileEta_max] )

p_mFitMean_sta_etaMuP, p_mFitMean_sta_etaMuP_label, p_mFitMean_sta_etaMuP_title, p_mFitMean_sta_etaMuP_x, p_mFitMean_sta_etaMuP_y = [], "mFitMean_sta_etaMuP", "Mass for STA dimuons (p_{T}>" + str(threshold_pT_GeV) + " GeV)", "#eta_{#mu^{+}}", "m_{#mu#mu} [GeV]"
profiles.append( [p_mFitMean_sta_etaMuP, p_mFitMean_sta_etaMuP_label, p_mFitMean_sta_etaMuP_title, p_mFitMean_sta_etaMuP_x, p_mFitMean_sta_etaMuP_y, mFitMean_bin, mFitMean_min, mFitMean_max, profileEta_bin, profileEta_min, profileEta_max] )

# ------------------------------------------------------------------------------
# Dimuon mass in 16 bins of phi (-3.2 < phi < 3.2) 
# ------------------------------------------------------------------------------

h_m_HybSta_phiSta_m32_m28, h_m_HybSta_phiSta_m32_m28_label, h_m_HybSta_phiSta_m32_m28_title = [], "m_HybSta_phiSta_m32_m28", "Mass for GLB+STA dimuons:  -#pi < #phi_{#mu^{+}} < -2.8" 
h_m_HybSta_phiSta_m28_m24, h_m_HybSta_phiSta_m28_m24_label, h_m_HybSta_phiSta_m28_m24_title = [], "m_HybSta_phiSta_m28_m24", "Mass for GLB+STA dimuons:  -2.8 < #phi_{#mu^{+}} < -2.4" 
h_m_HybSta_phiSta_m24_m20, h_m_HybSta_phiSta_m24_m20_label, h_m_HybSta_phiSta_m24_m20_title = [], "m_HybSta_phiSta_m24_m20", "Mass for GLB+STA dimuons:  -2.4 < #phi_{#mu^{+}} < -2.0" 
h_m_HybSta_phiSta_m20_m16, h_m_HybSta_phiSta_m20_m16_label, h_m_HybSta_phiSta_m20_m16_title = [], "m_HybSta_phiSta_m20_m16", "Mass for GLB+STA dimuons:  -2.0 < #phi_{#mu^{+}} < -1.6" 
h_m_HybSta_phiSta_m16_m12, h_m_HybSta_phiSta_m16_m12_label, h_m_HybSta_phiSta_m16_m12_title = [], "m_HybSta_phiSta_m16_m12", "Mass for GLB+STA dimuons:  -1.6 < #phi_{#mu^{+}} < -1.2" 
h_m_HybSta_phiSta_m12_m08, h_m_HybSta_phiSta_m12_m08_label, h_m_HybSta_phiSta_m12_m08_title = [], "m_HybSta_phiSta_m12_m08", "Mass for GLB+STA dimuons:  -1.2 < #phi_{#mu^{+}} < -0.8" 
h_m_HybSta_phiSta_m08_m04, h_m_HybSta_phiSta_m08_m04_label, h_m_HybSta_phiSta_m08_m04_title = [], "m_HybSta_phiSta_m08_m04", "Mass for GLB+STA dimuons:  -0.8 < #phi_{#mu^{+}} < -0.4" 
h_m_HybSta_phiSta_m04_m00, h_m_HybSta_phiSta_m04_m00_label, h_m_HybSta_phiSta_m04_m00_title = [], "m_HybSta_phiSta_m04_m00", "Mass for GLB+STA dimuons:  -0.4 < #phi_{#mu^{+}} < -0.0" 
h_m_HybSta_phiSta_p00_p04, h_m_HybSta_phiSta_p00_p04_label, h_m_HybSta_phiSta_p00_p04_title = [], "m_HybSta_phiSta_p00_p04", "Mass for GLB+STA dimuons:  0.0 < #phi_{#mu^{+}} < 0.4"   
h_m_HybSta_phiSta_p04_p08, h_m_HybSta_phiSta_p04_p08_label, h_m_HybSta_phiSta_p04_p08_title = [], "m_HybSta_phiSta_p04_p08", "Mass for GLB+STA dimuons:  0.4 < #phi_{#mu^{+}} < 0.8"   
h_m_HybSta_phiSta_p08_p12, h_m_HybSta_phiSta_p08_p12_label, h_m_HybSta_phiSta_p08_p12_title = [], "m_HybSta_phiSta_p08_p12", "Mass for GLB+STA dimuons:  0.8 < #phi_{#mu^{+}} < 1.2"   
h_m_HybSta_phiSta_p12_p16, h_m_HybSta_phiSta_p12_p16_label, h_m_HybSta_phiSta_p12_p16_title = [], "m_HybSta_phiSta_p12_p16", "Mass for GLB+STA dimuons:  1.2 < #phi_{#mu^{+}} < 1.6"   
h_m_HybSta_phiSta_p16_p20, h_m_HybSta_phiSta_p16_p20_label, h_m_HybSta_phiSta_p16_p20_title = [], "m_HybSta_phiSta_p16_p20", "Mass for GLB+STA dimuons:  1.6 < #phi_{#mu^{+}} < 2.0"   
h_m_HybSta_phiSta_p20_p24, h_m_HybSta_phiSta_p20_p24_label, h_m_HybSta_phiSta_p20_p24_title = [], "m_HybSta_phiSta_p20_p24", "Mass for GLB+STA dimuons:  2.0 < #phi_{#mu^{+}} < 2.4"   
h_m_HybSta_phiSta_p24_p28, h_m_HybSta_phiSta_p24_p28_label, h_m_HybSta_phiSta_p24_p28_title = [], "m_HybSta_phiSta_p24_p28", "Mass for GLB+STA dimuons:  2.4 < #phi_{#mu^{+}} < 2.8"   
h_m_HybSta_phiSta_p28_p32, h_m_HybSta_phiSta_p28_p32_label, h_m_HybSta_phiSta_p28_p32_title = [], "m_HybSta_phiSta_p28_p32", "Mass for GLB+STA dimuons:  2.8 < #phi_{#mu^{+}} < #pi"   

histos.append( [h_m_HybSta_phiSta_m32_m28, h_m_HybSta_phiSta_m32_m28_label, h_m_HybSta_phiSta_m32_m28_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_m28_m24, h_m_HybSta_phiSta_m28_m24_label, h_m_HybSta_phiSta_m28_m24_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_m24_m20, h_m_HybSta_phiSta_m24_m20_label, h_m_HybSta_phiSta_m24_m20_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_m20_m16, h_m_HybSta_phiSta_m20_m16_label, h_m_HybSta_phiSta_m20_m16_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_m16_m12, h_m_HybSta_phiSta_m16_m12_label, h_m_HybSta_phiSta_m16_m12_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_m12_m08, h_m_HybSta_phiSta_m12_m08_label, h_m_HybSta_phiSta_m12_m08_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_m08_m04, h_m_HybSta_phiSta_m08_m04_label, h_m_HybSta_phiSta_m08_m04_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_m04_m00, h_m_HybSta_phiSta_m04_m00_label, h_m_HybSta_phiSta_m04_m00_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_p00_p04, h_m_HybSta_phiSta_p00_p04_label, h_m_HybSta_phiSta_p00_p04_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_p04_p08, h_m_HybSta_phiSta_p04_p08_label, h_m_HybSta_phiSta_p04_p08_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_p08_p12, h_m_HybSta_phiSta_p08_p12_label, h_m_HybSta_phiSta_p08_p12_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_p12_p16, h_m_HybSta_phiSta_p12_p16_label, h_m_HybSta_phiSta_p12_p16_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_p16_p20, h_m_HybSta_phiSta_p16_p20_label, h_m_HybSta_phiSta_p16_p20_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_p20_p24, h_m_HybSta_phiSta_p20_p24_label, h_m_HybSta_phiSta_p20_p24_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_p24_p28, h_m_HybSta_phiSta_p24_p28_label, h_m_HybSta_phiSta_p24_p28_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_HybSta_phiSta_p28_p32, h_m_HybSta_phiSta_p28_p32_label, h_m_HybSta_phiSta_p28_p32_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )                        


p_mFitSigma_HybSta_phiSta, p_mFitSigma_HybSta_phiSta_label, p_mFitSigma_HybSta_phiSta_title, p_mFitSigma_HybSta_phiSta_x, p_mFitSigma_HybSta_phiSta_y = [], "mFitSigma_HybSta_phiSta", "Mass res. for GLB-STA dimuons (p_{T}>" + str(threshold_pT_GeV) + " GeV)", "#phi_{#mu_{STA}}", "#sigma m_{#mu#mu} [GeV]"
profiles.append( [p_mFitSigma_HybSta_phiSta, p_mFitSigma_HybSta_phiSta_label, p_mFitSigma_HybSta_phiSta_title, p_mFitSigma_HybSta_phiSta_x, p_mFitSigma_HybSta_phiSta_y, mFitSigma_bin, mFitSigma_min, mFitSigma_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

p_mFitMean_HybSta_phiSta, p_mFitMean_HybSta_phiSta_label, p_mFitMean_HybSta_phiSta_title, p_mFitMean_HybSta_phiSta_x, p_mFitMean_HybSta_phiSta_y = [], "mFitMean_HybSta_phiSta", "Mass for GLB-STA dimuons (p_{T}>" + str(threshold_pT_GeV) + " GeV)", "#phi_{#mu_{STA}}", "m_{#mu#mu} [GeV]"
profiles.append( [p_mFitMean_HybSta_phiSta, p_mFitMean_HybSta_phiSta_label, p_mFitMean_HybSta_phiSta_title, p_mFitMean_HybSta_phiSta_x, p_mFitMean_HybSta_phiSta_y, mFitMean_bin, mFitMean_min, mFitMean_max, profilePhi_bin, profilePhi_min, profilePhi_max] )                         

# ------------------------------------------------------------------------------
# Dimuon mass in 16 bins of phi (-3.2 < phi < 3.2) for all etaMuP (|etaMuP| < 2.4)
# ------------------------------------------------------------------------------

h_m_sta_phiMuP_m32_m28, h_m_sta_phiMuP_m32_m28_label, h_m_sta_phiMuP_m32_m28_title = [], "m_sta_phiMuP_m32_m28", "Mass for STA dimuons: -#pi < #phi_{#mu^{+}} < -2.8"
h_m_sta_phiMuP_m28_m24, h_m_sta_phiMuP_m28_m24_label, h_m_sta_phiMuP_m28_m24_title = [], "m_sta_phiMuP_m28_m24", "Mass for STA dimuons: -2.8 < #phi_{#mu^{+}} < -2.4"
h_m_sta_phiMuP_m24_m20, h_m_sta_phiMuP_m24_m20_label, h_m_sta_phiMuP_m24_m20_title = [], "m_sta_phiMuP_m24_m20", "Mass for STA dimuons: -2.4 < #phi_{#mu^{+}} < -2.0"
h_m_sta_phiMuP_m20_m16, h_m_sta_phiMuP_m20_m16_label, h_m_sta_phiMuP_m20_m16_title = [], "m_sta_phiMuP_m20_m16", "Mass for STA dimuons: -2.0 < #phi_{#mu^{+}} < -1.6"
h_m_sta_phiMuP_m16_m12, h_m_sta_phiMuP_m16_m12_label, h_m_sta_phiMuP_m16_m12_title = [], "m_sta_phiMuP_m16_m12", "Mass for STA dimuons: -1.6 < #phi_{#mu^{+}} < -1.2"
h_m_sta_phiMuP_m12_m08, h_m_sta_phiMuP_m12_m08_label, h_m_sta_phiMuP_m12_m08_title = [], "m_sta_phiMuP_m12_m08", "Mass for STA dimuons: -1.2 < #phi_{#mu^{+}} < -0.8"
h_m_sta_phiMuP_m08_m04, h_m_sta_phiMuP_m08_m04_label, h_m_sta_phiMuP_m08_m04_title = [], "m_sta_phiMuP_m08_m04", "Mass for STA dimuons: -0.8 < #phi_{#mu^{+}} < -0.4"
h_m_sta_phiMuP_m04_m00, h_m_sta_phiMuP_m04_m00_label, h_m_sta_phiMuP_m04_m00_title = [], "m_sta_phiMuP_m04_m00", "Mass for STA dimuons: -0.4 < #phi_{#mu^{+}} < -0.0"
h_m_sta_phiMuP_p00_p04, h_m_sta_phiMuP_p00_p04_label, h_m_sta_phiMuP_p00_p04_title = [], "m_sta_phiMuP_p00_p04", "Mass for STA dimuons: 0.0 < #phi_{#mu^{+}} < 0.4"
h_m_sta_phiMuP_p04_p08, h_m_sta_phiMuP_p04_p08_label, h_m_sta_phiMuP_p04_p08_title = [], "m_sta_phiMuP_p04_p08", "Mass for STA dimuons: 0.4 < #phi_{#mu^{+}} < 0.8"
h_m_sta_phiMuP_p08_p12, h_m_sta_phiMuP_p08_p12_label, h_m_sta_phiMuP_p08_p12_title = [], "m_sta_phiMuP_p08_p12", "Mass for STA dimuons: 0.8 < #phi_{#mu^{+}} < 1.2"
h_m_sta_phiMuP_p12_p16, h_m_sta_phiMuP_p12_p16_label, h_m_sta_phiMuP_p12_p16_title = [], "m_sta_phiMuP_p12_p16", "Mass for STA dimuons: 1.2 < #phi_{#mu^{+}} < 1.6"
h_m_sta_phiMuP_p16_p20, h_m_sta_phiMuP_p16_p20_label, h_m_sta_phiMuP_p16_p20_title = [], "m_sta_phiMuP_p16_p20", "Mass for STA dimuons: 1.6 < #phi_{#mu^{+}} < 2.0"
h_m_sta_phiMuP_p20_p24, h_m_sta_phiMuP_p20_p24_label, h_m_sta_phiMuP_p20_p24_title = [], "m_sta_phiMuP_p20_p24", "Mass for STA dimuons: 2.0 < #phi_{#mu^{+}} < 2.4"
h_m_sta_phiMuP_p24_p28, h_m_sta_phiMuP_p24_p28_label, h_m_sta_phiMuP_p24_p28_title = [], "m_sta_phiMuP_p24_p28", "Mass for STA dimuons: 2.4 < #phi_{#mu^{+}} < 2.8"
h_m_sta_phiMuP_p28_p32, h_m_sta_phiMuP_p28_p32_label, h_m_sta_phiMuP_p28_p32_title = [], "m_sta_phiMuP_p28_p32", "Mass for STA dimuons: 2.8 < #phi_{#mu^{+}} < #pi"

histos.append( [h_m_sta_phiMuP_m32_m28, h_m_sta_phiMuP_m32_m28_label, h_m_sta_phiMuP_m32_m28_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_m28_m24, h_m_sta_phiMuP_m28_m24_label, h_m_sta_phiMuP_m28_m24_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_m24_m20, h_m_sta_phiMuP_m24_m20_label, h_m_sta_phiMuP_m24_m20_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_m20_m16, h_m_sta_phiMuP_m20_m16_label, h_m_sta_phiMuP_m20_m16_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_m16_m12, h_m_sta_phiMuP_m16_m12_label, h_m_sta_phiMuP_m16_m12_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_m12_m08, h_m_sta_phiMuP_m12_m08_label, h_m_sta_phiMuP_m12_m08_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_m08_m04, h_m_sta_phiMuP_m08_m04_label, h_m_sta_phiMuP_m08_m04_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_m04_m00, h_m_sta_phiMuP_m04_m00_label, h_m_sta_phiMuP_m04_m00_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_p00_p04, h_m_sta_phiMuP_p00_p04_label, h_m_sta_phiMuP_p00_p04_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_p04_p08, h_m_sta_phiMuP_p04_p08_label, h_m_sta_phiMuP_p04_p08_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_p08_p12, h_m_sta_phiMuP_p08_p12_label, h_m_sta_phiMuP_p08_p12_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_p12_p16, h_m_sta_phiMuP_p12_p16_label, h_m_sta_phiMuP_p12_p16_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_p16_p20, h_m_sta_phiMuP_p16_p20_label, h_m_sta_phiMuP_p16_p20_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_p20_p24, h_m_sta_phiMuP_p20_p24_label, h_m_sta_phiMuP_p20_p24_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_p24_p28, h_m_sta_phiMuP_p24_p28_label, h_m_sta_phiMuP_p24_p28_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_sta_phiMuP_p28_p32, h_m_sta_phiMuP_p28_p32_label, h_m_sta_phiMuP_p28_p32_title, h_m_sta_x, h_m_sta_y, m_bin, m_min, m_max, m_fit] )

p_mFitSigma_sta_phiMuP, p_mFitSigma_sta_phiMuP_label, p_mFitSigma_sta_phiMuP_title, p_mFitSigma_sta_phiMuP_x, p_mFitSigma_sta_phiMuP_y = [], "mFitSigma_sta_phi", "Mass res. for STA dimuons (p_{T}>" + str(threshold_pT_GeV) + " GeV, |#eta_{#mu^{+}}|<2.4)", "#phi_{#mu^{+}}", "#sigma m_{#mu#mu} [GeV]"
profiles.append( [p_mFitSigma_sta_phiMuP, p_mFitSigma_sta_phiMuP_label, p_mFitSigma_sta_phiMuP_title, p_mFitSigma_sta_phiMuP_x, p_mFitSigma_sta_phiMuP_y, mFitSigma_bin, mFitSigma_min, mFitSigma_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

p_mFitMean_sta_phiMuP, p_mFitMean_sta_phiMuP_label, p_mFitMean_sta_phiMuP_title, p_mFitMean_sta_phiMuP_x, p_mFitMean_sta_phiMuP_y = [], "mFitMean_sta_phi", "Mass for STA dimuons (p_{T}>" + str(threshold_pT_GeV) + " GeV, |#eta_{#mu^{+}}|<2.4)", "#phi_{#mu^{+}}", "m_{#mu#mu} [GeV]"
profiles.append( [p_mFitMean_sta_phiMuP, p_mFitMean_sta_phiMuP_label, p_mFitMean_sta_phiMuP_title, p_mFitMean_sta_phiMuP_x, p_mFitMean_sta_phiMuP_y, mFitMean_bin, mFitMean_min, mFitMean_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

# ------------------------------------------------------------------------------
# Dimuon mass in 16 bins of phi (-3.2 < phi < 3.2) for Barrel (|etaMuP| < 0.9)
# ------------------------------------------------------------------------------

h_m_staB_phiMuP_m32_m28, h_m_staB_phiMuP_m32_m28_label, h_m_staB_phiMuP_m32_m28_title = [], "m_staB_phiMuP_m32_m28", "Mass for STA dimuons: -#pi < #phi_{#mu^{+}} < -2.8"
h_m_staB_phiMuP_m28_m24, h_m_staB_phiMuP_m28_m24_label, h_m_staB_phiMuP_m28_m24_title = [], "m_staB_phiMuP_m28_m24", "Mass for STA dimuons: -2.8 < #phi_{#mu^{+}} < -2.4"
h_m_staB_phiMuP_m24_m20, h_m_staB_phiMuP_m24_m20_label, h_m_staB_phiMuP_m24_m20_title = [], "m_staB_phiMuP_m24_m20", "Mass for STA dimuons: -2.4 < #phi_{#mu^{+}} < -2.0"
h_m_staB_phiMuP_m20_m16, h_m_staB_phiMuP_m20_m16_label, h_m_staB_phiMuP_m20_m16_title = [], "m_staB_phiMuP_m20_m16", "Mass for STA dimuons: -2.0 < #phi_{#mu^{+}} < -1.6"
h_m_staB_phiMuP_m16_m12, h_m_staB_phiMuP_m16_m12_label, h_m_staB_phiMuP_m16_m12_title = [], "m_staB_phiMuP_m16_m12", "Mass for STA dimuons: -1.6 < #phi_{#mu^{+}} < -1.2"
h_m_staB_phiMuP_m12_m08, h_m_staB_phiMuP_m12_m08_label, h_m_staB_phiMuP_m12_m08_title = [], "m_staB_phiMuP_m12_m08", "Mass for STA dimuons: -1.2 < #phi_{#mu^{+}} < -0.8"
h_m_staB_phiMuP_m08_m04, h_m_staB_phiMuP_m08_m04_label, h_m_staB_phiMuP_m08_m04_title = [], "m_staB_phiMuP_m08_m04", "Mass for STA dimuons: -0.8 < #phi_{#mu^{+}} < -0.4"
h_m_staB_phiMuP_m04_m00, h_m_staB_phiMuP_m04_m00_label, h_m_staB_phiMuP_m04_m00_title = [], "m_staB_phiMuP_m04_m00", "Mass for STA dimuons: -0.4 < #phi_{#mu^{+}} < -0.0"
h_m_staB_phiMuP_p00_p04, h_m_staB_phiMuP_p00_p04_label, h_m_staB_phiMuP_p00_p04_title = [], "m_staB_phiMuP_p00_p04", "Mass for STA dimuons: 0.0 < #phi_{#mu^{+}} < 0.4"
h_m_staB_phiMuP_p04_p08, h_m_staB_phiMuP_p04_p08_label, h_m_staB_phiMuP_p04_p08_title = [], "m_staB_phiMuP_p04_p08", "Mass for STA dimuons: 0.4 < #phi_{#mu^{+}} < 0.8"
h_m_staB_phiMuP_p08_p12, h_m_staB_phiMuP_p08_p12_label, h_m_staB_phiMuP_p08_p12_title = [], "m_staB_phiMuP_p08_p12", "Mass for STA dimuons: 0.8 < #phi_{#mu^{+}} < 1.2"
h_m_staB_phiMuP_p12_p16, h_m_staB_phiMuP_p12_p16_label, h_m_staB_phiMuP_p12_p16_title = [], "m_staB_phiMuP_p12_p16", "Mass for STA dimuons: 1.2 < #phi_{#mu^{+}} < 1.6"
h_m_staB_phiMuP_p16_p20, h_m_staB_phiMuP_p16_p20_label, h_m_staB_phiMuP_p16_p20_title = [], "m_staB_phiMuP_p16_p20", "Mass for STA dimuons: 1.6 < #phi_{#mu^{+}} < 2.0"
h_m_staB_phiMuP_p20_p24, h_m_staB_phiMuP_p20_p24_label, h_m_staB_phiMuP_p20_p24_title = [], "m_staB_phiMuP_p20_p24", "Mass for STA dimuons: 2.0 < #phi_{#mu^{+}} < 2.4"
h_m_staB_phiMuP_p24_p28, h_m_staB_phiMuP_p24_p28_label, h_m_staB_phiMuP_p24_p28_title = [], "m_staB_phiMuP_p24_p28", "Mass for STA dimuons: 2.4 < #phi_{#mu^{+}} < 2.8"
h_m_staB_phiMuP_p28_p32, h_m_staB_phiMuP_p28_p32_label, h_m_staB_phiMuP_p28_p32_title = [], "m_staB_phiMuP_p28_p32", "Mass for STA dimuons: 2.8 < #phi_{#mu^{+}} < 3.2"

h_m_staB_x, h_m_staB_y = h_m_sta_x, h_m_sta_y
histos.append( [h_m_staB_phiMuP_m32_m28, h_m_staB_phiMuP_m32_m28_label, h_m_staB_phiMuP_m32_m28_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_m28_m24, h_m_staB_phiMuP_m28_m24_label, h_m_staB_phiMuP_m28_m24_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_m24_m20, h_m_staB_phiMuP_m24_m20_label, h_m_staB_phiMuP_m24_m20_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_m20_m16, h_m_staB_phiMuP_m20_m16_label, h_m_staB_phiMuP_m20_m16_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_m16_m12, h_m_staB_phiMuP_m16_m12_label, h_m_staB_phiMuP_m16_m12_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_m12_m08, h_m_staB_phiMuP_m12_m08_label, h_m_staB_phiMuP_m12_m08_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_m08_m04, h_m_staB_phiMuP_m08_m04_label, h_m_staB_phiMuP_m08_m04_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_m04_m00, h_m_staB_phiMuP_m04_m00_label, h_m_staB_phiMuP_m04_m00_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_p00_p04, h_m_staB_phiMuP_p00_p04_label, h_m_staB_phiMuP_p00_p04_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_p04_p08, h_m_staB_phiMuP_p04_p08_label, h_m_staB_phiMuP_p04_p08_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_p08_p12, h_m_staB_phiMuP_p08_p12_label, h_m_staB_phiMuP_p08_p12_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_p12_p16, h_m_staB_phiMuP_p12_p16_label, h_m_staB_phiMuP_p12_p16_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_p16_p20, h_m_staB_phiMuP_p16_p20_label, h_m_staB_phiMuP_p16_p20_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_p20_p24, h_m_staB_phiMuP_p20_p24_label, h_m_staB_phiMuP_p20_p24_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_p24_p28, h_m_staB_phiMuP_p24_p28_label, h_m_staB_phiMuP_p24_p28_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staB_phiMuP_p28_p32, h_m_staB_phiMuP_p28_p32_label, h_m_staB_phiMuP_p28_p32_title, h_m_staB_x, h_m_staB_y, m_bin, m_min, m_max, m_fit] )

p_mFitSigma_staB_phiMuP, p_mFitSigma_staB_phiMuP_label, p_mFitSigma_staB_phiMuP_title, p_mFitSigma_staB_phiMuP_x, p_mFitSigma_staB_phiMuP_y = [], "mFitSigma_staB_phi", "Mass res. for STA dimuons (p_{T}>" + str(threshold_pT_GeV) + " GeV, |#eta_{#mu^{+}}|<0.9)", "#phi_{#mu^{+}}", "#sigma m_{#mu#mu} [GeV]"
profiles.append( [p_mFitSigma_staB_phiMuP, p_mFitSigma_staB_phiMuP_label, p_mFitSigma_staB_phiMuP_title, p_mFitSigma_staB_phiMuP_x, p_mFitSigma_staB_phiMuP_y, mFitSigma_bin, mFitSigma_min, mFitSigma_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

p_mFitMean_staB_phiMuP, p_mFitMean_staB_phiMuP_label, p_mFitMean_staB_phiMuP_title, p_mFitMean_staB_phiMuP_x, p_mFitMean_staB_phiMuP_y = [], "mFitMean_staB_phi", "Mass for STA dimuons (p_{T}>" + str(threshold_pT_GeV) + " GeV, |#eta_{#mu^{+}}|<0.9)", "#phi_{#mu^{+}}", "m_{#mu#mu} [GeV]"
profiles.append( [p_mFitMean_staB_phiMuP, p_mFitMean_staB_phiMuP_label, p_mFitMean_staB_phiMuP_title, p_mFitMean_staB_phiMuP_x, p_mFitMean_staB_phiMuP_y, mFitMean_bin, mFitMean_min, mFitMean_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

# ------------------------------------------------------------------------------
# Dimuon mass in 16 bins of phi (-3.2 < phi < 3.2) for Plus Endcap + Overlap ( 0.9 < etaMuP < 2.4)
# ------------------------------------------------------------------------------

h_m_staEOp_phiMuP_m32_m28, h_m_staEOp_phiMuP_m32_m28_label, h_m_staEOp_phiMuP_m32_m28_title = [], "m_staEOp_phiMuP_m32_m28", "Mass for STA dimuons: -#pi < #phi_{#mu^{+}} < -2.8"
h_m_staEOp_phiMuP_m28_m24, h_m_staEOp_phiMuP_m28_m24_label, h_m_staEOp_phiMuP_m28_m24_title = [], "m_staEOp_phiMuP_m28_m24", "Mass for STA dimuons: -2.8 < #phi_{#mu^{+}} < -2.4"
h_m_staEOp_phiMuP_m24_m20, h_m_staEOp_phiMuP_m24_m20_label, h_m_staEOp_phiMuP_m24_m20_title = [], "m_staEOp_phiMuP_m24_m20", "Mass for STA dimuons: -2.4 < #phi_{#mu^{+}} < -2.0"
h_m_staEOp_phiMuP_m20_m16, h_m_staEOp_phiMuP_m20_m16_label, h_m_staEOp_phiMuP_m20_m16_title = [], "m_staEOp_phiMuP_m20_m16", "Mass for STA dimuons: -2.0 < #phi_{#mu^{+}} < -1.6"
h_m_staEOp_phiMuP_m16_m12, h_m_staEOp_phiMuP_m16_m12_label, h_m_staEOp_phiMuP_m16_m12_title = [], "m_staEOp_phiMuP_m16_m12", "Mass for STA dimuons: -1.6 < #phi_{#mu^{+}} < -1.2"
h_m_staEOp_phiMuP_m12_m08, h_m_staEOp_phiMuP_m12_m08_label, h_m_staEOp_phiMuP_m12_m08_title = [], "m_staEOp_phiMuP_m12_m08", "Mass for STA dimuons: -1.2 < #phi_{#mu^{+}} < -0.8"
h_m_staEOp_phiMuP_m08_m04, h_m_staEOp_phiMuP_m08_m04_label, h_m_staEOp_phiMuP_m08_m04_title = [], "m_staEOp_phiMuP_m08_m04", "Mass for STA dimuons: -0.8 < #phi_{#mu^{+}} < -0.4"
h_m_staEOp_phiMuP_m04_m00, h_m_staEOp_phiMuP_m04_m00_label, h_m_staEOp_phiMuP_m04_m00_title = [], "m_staEOp_phiMuP_m04_m00", "Mass for STA dimuons: -0.4 < #phi_{#mu^{+}} < -0.0"
h_m_staEOp_phiMuP_p00_p04, h_m_staEOp_phiMuP_p00_p04_label, h_m_staEOp_phiMuP_p00_p04_title = [], "m_staEOp_phiMuP_p00_p04", "Mass for STA dimuons: 0.0 < #phi_{#mu^{+}} < 0.4"
h_m_staEOp_phiMuP_p04_p08, h_m_staEOp_phiMuP_p04_p08_label, h_m_staEOp_phiMuP_p04_p08_title = [], "m_staEOp_phiMuP_p04_p08", "Mass for STA dimuons: 0.4 < #phi_{#mu^{+}} < 0.8"
h_m_staEOp_phiMuP_p08_p12, h_m_staEOp_phiMuP_p08_p12_label, h_m_staEOp_phiMuP_p08_p12_title = [], "m_staEOp_phiMuP_p08_p12", "Mass for STA dimuons: 0.8 < #phi_{#mu^{+}} < 1.2"
h_m_staEOp_phiMuP_p12_p16, h_m_staEOp_phiMuP_p12_p16_label, h_m_staEOp_phiMuP_p12_p16_title = [], "m_staEOp_phiMuP_p12_p16", "Mass for STA dimuons: 1.2 < #phi_{#mu^{+}} < 1.6"
h_m_staEOp_phiMuP_p16_p20, h_m_staEOp_phiMuP_p16_p20_label, h_m_staEOp_phiMuP_p16_p20_title = [], "m_staEOp_phiMuP_p16_p20", "Mass for STA dimuons: 1.6 < #phi_{#mu^{+}} < 2.0"
h_m_staEOp_phiMuP_p20_p24, h_m_staEOp_phiMuP_p20_p24_label, h_m_staEOp_phiMuP_p20_p24_title = [], "m_staEOp_phiMuP_p20_p24", "Mass for STA dimuons: 2.0 < #phi_{#mu^{+}} < 2.4"
h_m_staEOp_phiMuP_p24_p28, h_m_staEOp_phiMuP_p24_p28_label, h_m_staEOp_phiMuP_p24_p28_title = [], "m_staEOp_phiMuP_p24_p28", "Mass for STA dimuons: 2.4 < #phi_{#mu^{+}} < 2.8"
h_m_staEOp_phiMuP_p28_p32, h_m_staEOp_phiMuP_p28_p32_label, h_m_staEOp_phiMuP_p28_p32_title = [], "m_staEOp_phiMuP_p28_p32", "Mass for STA dimuons: 2.8 < #phi_{#mu^{+}} < 3.2"

h_m_staEOp_x, h_m_staEOp_y = h_m_sta_x, h_m_sta_y
histos.append( [h_m_staEOp_phiMuP_m32_m28, h_m_staEOp_phiMuP_m32_m28_label, h_m_staEOp_phiMuP_m32_m28_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_m28_m24, h_m_staEOp_phiMuP_m28_m24_label, h_m_staEOp_phiMuP_m28_m24_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_m24_m20, h_m_staEOp_phiMuP_m24_m20_label, h_m_staEOp_phiMuP_m24_m20_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_m20_m16, h_m_staEOp_phiMuP_m20_m16_label, h_m_staEOp_phiMuP_m20_m16_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_m16_m12, h_m_staEOp_phiMuP_m16_m12_label, h_m_staEOp_phiMuP_m16_m12_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_m12_m08, h_m_staEOp_phiMuP_m12_m08_label, h_m_staEOp_phiMuP_m12_m08_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_m08_m04, h_m_staEOp_phiMuP_m08_m04_label, h_m_staEOp_phiMuP_m08_m04_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_m04_m00, h_m_staEOp_phiMuP_m04_m00_label, h_m_staEOp_phiMuP_m04_m00_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_p00_p04, h_m_staEOp_phiMuP_p00_p04_label, h_m_staEOp_phiMuP_p00_p04_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_p04_p08, h_m_staEOp_phiMuP_p04_p08_label, h_m_staEOp_phiMuP_p04_p08_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_p08_p12, h_m_staEOp_phiMuP_p08_p12_label, h_m_staEOp_phiMuP_p08_p12_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_p12_p16, h_m_staEOp_phiMuP_p12_p16_label, h_m_staEOp_phiMuP_p12_p16_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_p16_p20, h_m_staEOp_phiMuP_p16_p20_label, h_m_staEOp_phiMuP_p16_p20_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_p20_p24, h_m_staEOp_phiMuP_p20_p24_label, h_m_staEOp_phiMuP_p20_p24_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_p24_p28, h_m_staEOp_phiMuP_p24_p28_label, h_m_staEOp_phiMuP_p24_p28_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOp_phiMuP_p28_p32, h_m_staEOp_phiMuP_p28_p32_label, h_m_staEOp_phiMuP_p28_p32_title, h_m_staEOp_x, h_m_staEOp_y, m_bin, m_min, m_max, m_fit] )

p_mFitSigma_staEOp_phiMuP, p_mFitSigma_staEOp_phiMuP_label, p_mFitSigma_staEOp_phiMuP_title, p_mFitSigma_staEOp_phiMuP_x, p_mFitSigma_staEOp_phiMuP_y = [], "mFitSigma_staEOp_phi", "Mass res. for STA dimuons (p_{T}>" + str(threshold_pT_GeV) + " GeV, 0.9<#eta_{#mu^{+}}<2.4)", "#phi_{#mu^{+}}", "#sigma m_{#mu#mu} [GeV]"
profiles.append( [p_mFitSigma_staEOp_phiMuP, p_mFitSigma_staEOp_phiMuP_label, p_mFitSigma_staEOp_phiMuP_title, p_mFitSigma_staEOp_phiMuP_x, p_mFitSigma_staEOp_phiMuP_y, mFitSigma_bin, mFitSigma_min, mFitSigma_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

p_mFitMean_staEOp_phiMuP, p_mFitMean_staEOp_phiMuP_label, p_mFitMean_staEOp_phiMuP_title, p_mFitMean_staEOp_phiMuP_x, p_mFitMean_staEOp_phiMuP_y = [], "mFitMean_staEOp_phi", "Mass for STA dimuons (p_{T}>" + str(threshold_pT_GeV) + " GeV, 0.9<#eta_{#mu^{+}}<2.4)", "#phi_{#mu^{+}}", "m_{#mu#mu} [GeV]"
profiles.append( [p_mFitMean_staEOp_phiMuP, p_mFitMean_staEOp_phiMuP_label, p_mFitMean_staEOp_phiMuP_title, p_mFitMean_staEOp_phiMuP_x, p_mFitMean_staEOp_phiMuP_y, mFitMean_bin, mFitMean_min, mFitMean_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

# ------------------------------------------------------------------------------
# Dimuon mass in 16 bins of phi (-3.2 < phi < 3.2) for Minus Endcap + Overlap ( -2.4 < etaMuP < -0.9)
# ------------------------------------------------------------------------------

h_m_staEOm_phiMuP_m32_m28, h_m_staEOm_phiMuP_m32_m28_label, h_m_staEOm_phiMuP_m32_m28_title = [], "m_staEOm_phiMuP_m32_m28", "Mass for STA dimuons: -#pi < #phi_{#mu^{+}} < -2.8"
h_m_staEOm_phiMuP_m28_m24, h_m_staEOm_phiMuP_m28_m24_label, h_m_staEOm_phiMuP_m28_m24_title = [], "m_staEOm_phiMuP_m28_m24", "Mass for STA dimuons: -2.8 < #phi_{#mu^{+}} < -2.4"
h_m_staEOm_phiMuP_m24_m20, h_m_staEOm_phiMuP_m24_m20_label, h_m_staEOm_phiMuP_m24_m20_title = [], "m_staEOm_phiMuP_m24_m20", "Mass for STA dimuons: -2.4 < #phi_{#mu^{+}} < -2.0"
h_m_staEOm_phiMuP_m20_m16, h_m_staEOm_phiMuP_m20_m16_label, h_m_staEOm_phiMuP_m20_m16_title = [], "m_staEOm_phiMuP_m20_m16", "Mass for STA dimuons: -2.0 < #phi_{#mu^{+}} < -1.6"
h_m_staEOm_phiMuP_m16_m12, h_m_staEOm_phiMuP_m16_m12_label, h_m_staEOm_phiMuP_m16_m12_title = [], "m_staEOm_phiMuP_m16_m12", "Mass for STA dimuons: -1.6 < #phi_{#mu^{+}} < -1.2"
h_m_staEOm_phiMuP_m12_m08, h_m_staEOm_phiMuP_m12_m08_label, h_m_staEOm_phiMuP_m12_m08_title = [], "m_staEOm_phiMuP_m12_m08", "Mass for STA dimuons: -1.2 < #phi_{#mu^{+}} < -0.8"
h_m_staEOm_phiMuP_m08_m04, h_m_staEOm_phiMuP_m08_m04_label, h_m_staEOm_phiMuP_m08_m04_title = [], "m_staEOm_phiMuP_m08_m04", "Mass for STA dimuons: -0.8 < #phi_{#mu^{+}} < -0.4"
h_m_staEOm_phiMuP_m04_m00, h_m_staEOm_phiMuP_m04_m00_label, h_m_staEOm_phiMuP_m04_m00_title = [], "m_staEOm_phiMuP_m04_m00", "Mass for STA dimuons: -0.4 < #phi_{#mu^{+}} < -0.0"
h_m_staEOm_phiMuP_p00_p04, h_m_staEOm_phiMuP_p00_p04_label, h_m_staEOm_phiMuP_p00_p04_title = [], "m_staEOm_phiMuP_p00_p04", "Mass for STA dimuons: 0.0 < #phi_{#mu^{+}} < 0.4"
h_m_staEOm_phiMuP_p04_p08, h_m_staEOm_phiMuP_p04_p08_label, h_m_staEOm_phiMuP_p04_p08_title = [], "m_staEOm_phiMuP_p04_p08", "Mass for STA dimuons: 0.4 < #phi_{#mu^{+}} < 0.8"
h_m_staEOm_phiMuP_p08_p12, h_m_staEOm_phiMuP_p08_p12_label, h_m_staEOm_phiMuP_p08_p12_title = [], "m_staEOm_phiMuP_p08_p12", "Mass for STA dimuons: 0.8 < #phi_{#mu^{+}} < 1.2"
h_m_staEOm_phiMuP_p12_p16, h_m_staEOm_phiMuP_p12_p16_label, h_m_staEOm_phiMuP_p12_p16_title = [], "m_staEOm_phiMuP_p12_p16", "Mass for STA dimuons: 1.2 < #phi_{#mu^{+}} < 1.6"
h_m_staEOm_phiMuP_p16_p20, h_m_staEOm_phiMuP_p16_p20_label, h_m_staEOm_phiMuP_p16_p20_title = [], "m_staEOm_phiMuP_p16_p20", "Mass for STA dimuons: 1.6 < #phi_{#mu^{+}} < 2.0"
h_m_staEOm_phiMuP_p20_p24, h_m_staEOm_phiMuP_p20_p24_label, h_m_staEOm_phiMuP_p20_p24_title = [], "m_staEOm_phiMuP_p20_p24", "Mass for STA dimuons: 2.0 < #phi_{#mu^{+}} < 2.4"
h_m_staEOm_phiMuP_p24_p28, h_m_staEOm_phiMuP_p24_p28_label, h_m_staEOm_phiMuP_p24_p28_title = [], "m_staEOm_phiMuP_p24_p28", "Mass for STA dimuons: 2.4 < #phi_{#mu^{+}} < 2.8"
h_m_staEOm_phiMuP_p28_p32, h_m_staEOm_phiMuP_p28_p32_label, h_m_staEOm_phiMuP_p28_p32_title = [], "m_staEOm_phiMuP_p28_p32", "Mass for STA dimuons: 2.8 < #phi_{#mu^{+}} < 3.2"

h_m_staEOm_x, h_m_staEOm_y = h_m_sta_x, h_m_sta_y
histos.append( [h_m_staEOm_phiMuP_m32_m28, h_m_staEOm_phiMuP_m32_m28_label, h_m_staEOm_phiMuP_m32_m28_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_m28_m24, h_m_staEOm_phiMuP_m28_m24_label, h_m_staEOm_phiMuP_m28_m24_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_m24_m20, h_m_staEOm_phiMuP_m24_m20_label, h_m_staEOm_phiMuP_m24_m20_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_m20_m16, h_m_staEOm_phiMuP_m20_m16_label, h_m_staEOm_phiMuP_m20_m16_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_m16_m12, h_m_staEOm_phiMuP_m16_m12_label, h_m_staEOm_phiMuP_m16_m12_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_m12_m08, h_m_staEOm_phiMuP_m12_m08_label, h_m_staEOm_phiMuP_m12_m08_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_m08_m04, h_m_staEOm_phiMuP_m08_m04_label, h_m_staEOm_phiMuP_m08_m04_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_m04_m00, h_m_staEOm_phiMuP_m04_m00_label, h_m_staEOm_phiMuP_m04_m00_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_p00_p04, h_m_staEOm_phiMuP_p00_p04_label, h_m_staEOm_phiMuP_p00_p04_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_p04_p08, h_m_staEOm_phiMuP_p04_p08_label, h_m_staEOm_phiMuP_p04_p08_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_p08_p12, h_m_staEOm_phiMuP_p08_p12_label, h_m_staEOm_phiMuP_p08_p12_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_p12_p16, h_m_staEOm_phiMuP_p12_p16_label, h_m_staEOm_phiMuP_p12_p16_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_p16_p20, h_m_staEOm_phiMuP_p16_p20_label, h_m_staEOm_phiMuP_p16_p20_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_p20_p24, h_m_staEOm_phiMuP_p20_p24_label, h_m_staEOm_phiMuP_p20_p24_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_p24_p28, h_m_staEOm_phiMuP_p24_p28_label, h_m_staEOm_phiMuP_p24_p28_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )
histos.append( [h_m_staEOm_phiMuP_p28_p32, h_m_staEOm_phiMuP_p28_p32_label, h_m_staEOm_phiMuP_p28_p32_title, h_m_staEOm_x, h_m_staEOm_y, m_bin, m_min, m_max, m_fit] )

p_mFitSigma_staEOm_phiMuP, p_mFitSigma_staEOm_phiMuP_label, p_mFitSigma_staEOm_phiMuP_title, p_mFitSigma_staEOm_phiMuP_x, p_mFitSigma_staEOm_phiMuP_y = [], "mFitSigma_staEOm_phi", "Mass res. for STA dimuons (p_{T}>" + str(threshold_pT_GeV) + " GeV, -2.4<#eta_{#mu^{+}}<-0.9)", "#phi_{#mu^{+}}", "#sigma m_{#mu#mu} [GeV]"
profiles.append( [p_mFitSigma_staEOm_phiMuP, p_mFitSigma_staEOm_phiMuP_label, p_mFitSigma_staEOm_phiMuP_title, p_mFitSigma_staEOm_phiMuP_x, p_mFitSigma_staEOm_phiMuP_y, mFitSigma_bin, mFitSigma_min, mFitSigma_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

p_mFitMean_staEOm_phiMuP, p_mFitMean_staEOm_phiMuP_label, p_mFitMean_staEOm_phiMuP_title, p_mFitMean_staEOm_phiMuP_x, p_mFitMean_staEOm_phiMuP_y = [], "mFitMean_staEOm_phi", "Mass for STA dimuons (p_{T}>" + str(threshold_pT_GeV) + " GeV, -2.4<#eta_{#mu^{+}}<-0.9)", "#phi_{#mu^{+}}", "m_{#mu#mu} [GeV]"
profiles.append( [p_mFitMean_staEOm_phiMuP, p_mFitMean_staEOm_phiMuP_label, p_mFitMean_staEOm_phiMuP_title, p_mFitMean_staEOm_phiMuP_x, p_mFitMean_staEOm_phiMuP_y, mFitMean_bin, mFitMean_min, mFitMean_max, profilePhi_bin, profilePhi_min, profilePhi_max] )
