# ------------------------------------------------------------------------------
# Transverse momentum resolution q/pt_PIC - q/pt_TRK
# ------------------------------------------------------------------------------

h_ptRes_pic_trk, h_ptRes_pic_trk_label, h_ptRes_pic_trk_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y = [], "ptRes_pic-trk", "p_{T} res for #mu_{Picky}", "q/p_{T Picky} - q/p_{T TRK} [1/GeV]", "a.u."
histos.append( [h_ptRes_pic_trk, h_ptRes_pic_trk_label, h_ptRes_pic_trk_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )

# ------------------------------------------------------------------------------
# Transverse momentum resolution in 16 bins of eta (-2.4 < eta < 2.4)
# ------------------------------------------------------------------------------

h_ptRes_pic_trk_eta_m24_m21, h_ptRes_pic_trk_eta_m24_m21_label, h_ptRes_pic_trk_eta_m24_m21_title = [], "ptRes_pic_trk_eta_m24_m21", "p_{T} resolution for Picky muons: -2.4 < #eta < -2.1"
h_ptRes_pic_trk_eta_m21_m18, h_ptRes_pic_trk_eta_m21_m18_label, h_ptRes_pic_trk_eta_m21_m18_title = [], "ptRes_pic_trk_eta_m21_m18", "p_{T} resolution for Picky muons:  -2.1 < #eta < -1.8"
h_ptRes_pic_trk_eta_m18_m15, h_ptRes_pic_trk_eta_m18_m15_label, h_ptRes_pic_trk_eta_m18_m15_title = [], "ptRes_pic_trk_eta_m18_m15", "p_{T} resolution for Picky muons:  -1.8 < #eta < -1.5"
h_ptRes_pic_trk_eta_m15_m12, h_ptRes_pic_trk_eta_m15_m12_label, h_ptRes_pic_trk_eta_m15_m12_title = [], "ptRes_pic_trk_eta_m15_m12", "p_{T} resolution for Picky muons:  -1.5 < #eta < -1.2"
h_ptRes_pic_trk_eta_m12_m09, h_ptRes_pic_trk_eta_m12_m09_label, h_ptRes_pic_trk_eta_m12_m09_title = [], "ptRes_pic_trk_eta_m12_m09", "p_{T} resolution for Picky muons:  -1.2 < #eta < -0.9"
h_ptRes_pic_trk_eta_m09_m06, h_ptRes_pic_trk_eta_m09_m06_label, h_ptRes_pic_trk_eta_m09_m06_title = [], "ptRes_pic_trk_eta_m09_m06", "p_{T} resolution for Picky muons:  -0.9 < #eta < -0.6"
h_ptRes_pic_trk_eta_m06_m03, h_ptRes_pic_trk_eta_m06_m03_label, h_ptRes_pic_trk_eta_m06_m03_title = [], "ptRes_pic_trk_eta_m06_m03", "p_{T} resolution for Picky muons:  -0.6 < #eta < -0.3"
h_ptRes_pic_trk_eta_m03_m00, h_ptRes_pic_trk_eta_m03_m00_label, h_ptRes_pic_trk_eta_m03_m00_title = [], "ptRes_pic_trk_eta_m03_m00", "p_{T} resolution for Picky muons:  -0.3 < #eta < 0"
h_ptRes_pic_trk_eta_p00_p03, h_ptRes_pic_trk_eta_p00_p03_label, h_ptRes_pic_trk_eta_p00_p03_title = [], "ptRes_pic_trk_eta_p00_p03", "p_{T} resolution for Picky muons:  0 < #eta < 0.3"
h_ptRes_pic_trk_eta_p03_p06, h_ptRes_pic_trk_eta_p03_p06_label, h_ptRes_pic_trk_eta_p03_p06_title = [], "ptRes_pic_trk_eta_p03_p06", "p_{T} resolution for Picky muons:  0.3 < #eta < 0.6"
h_ptRes_pic_trk_eta_p06_p09, h_ptRes_pic_trk_eta_p06_p09_label, h_ptRes_pic_trk_eta_p06_p09_title = [], "ptRes_pic_trk_eta_p06_p09", "p_{T} resolution for Picky muons:  0.6 < #eta < 0.9"
h_ptRes_pic_trk_eta_p09_p12, h_ptRes_pic_trk_eta_p09_p12_label, h_ptRes_pic_trk_eta_p09_p12_title = [], "ptRes_pic_trk_eta_p09_p12", "p_{T} resolution for Picky muons:  0.9 < #eta < 1.2"
h_ptRes_pic_trk_eta_p12_p15, h_ptRes_pic_trk_eta_p12_p15_label, h_ptRes_pic_trk_eta_p12_p15_title = [], "ptRes_pic_trk_eta_p12_p15", "p_{T} resolution for Picky muons:  1.2 < #eta < 1.5"
h_ptRes_pic_trk_eta_p15_p18, h_ptRes_pic_trk_eta_p15_p18_label, h_ptRes_pic_trk_eta_p15_p18_title = [], "ptRes_pic_trk_eta_p15_p18", "p_{T} resolution for Picky muons:  1.5 < #eta < 1.8"
h_ptRes_pic_trk_eta_p18_p21, h_ptRes_pic_trk_eta_p18_p21_label, h_ptRes_pic_trk_eta_p18_p21_title = [], "ptRes_pic_trk_eta_p18_p21", "p_{T} resolution for Picky muons:  1.8 < #eta < 2.1"
h_ptRes_pic_trk_eta_p21_p24, h_ptRes_pic_trk_eta_p21_p24_label, h_ptRes_pic_trk_eta_p21_p24_title = [], "ptRes_pic_trk_eta_p21_p24", "p_{T} resolution for Picky muons:  2.1 < #eta < 2.4"

histos.append( [h_ptRes_pic_trk_eta_m24_m21, h_ptRes_pic_trk_eta_m24_m21_label, h_ptRes_pic_trk_eta_m24_m21_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_m21_m18, h_ptRes_pic_trk_eta_m21_m18_label, h_ptRes_pic_trk_eta_m21_m18_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_m18_m15, h_ptRes_pic_trk_eta_m18_m15_label, h_ptRes_pic_trk_eta_m18_m15_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_m15_m12, h_ptRes_pic_trk_eta_m15_m12_label, h_ptRes_pic_trk_eta_m15_m12_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_m12_m09, h_ptRes_pic_trk_eta_m12_m09_label, h_ptRes_pic_trk_eta_m12_m09_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_m09_m06, h_ptRes_pic_trk_eta_m09_m06_label, h_ptRes_pic_trk_eta_m09_m06_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_m06_m03, h_ptRes_pic_trk_eta_m06_m03_label, h_ptRes_pic_trk_eta_m06_m03_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_m03_m00, h_ptRes_pic_trk_eta_m03_m00_label, h_ptRes_pic_trk_eta_m03_m00_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_p00_p03, h_ptRes_pic_trk_eta_p00_p03_label, h_ptRes_pic_trk_eta_p00_p03_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_p03_p06, h_ptRes_pic_trk_eta_p03_p06_label, h_ptRes_pic_trk_eta_p03_p06_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_p06_p09, h_ptRes_pic_trk_eta_p06_p09_label, h_ptRes_pic_trk_eta_p06_p09_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_p09_p12, h_ptRes_pic_trk_eta_p09_p12_label, h_ptRes_pic_trk_eta_p09_p12_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_p12_p15, h_ptRes_pic_trk_eta_p12_p15_label, h_ptRes_pic_trk_eta_p12_p15_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_p15_p18, h_ptRes_pic_trk_eta_p15_p18_label, h_ptRes_pic_trk_eta_p15_p18_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_p18_p21, h_ptRes_pic_trk_eta_p18_p21_label, h_ptRes_pic_trk_eta_p18_p21_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_eta_p21_p24, h_ptRes_pic_trk_eta_p21_p24_label, h_ptRes_pic_trk_eta_p21_p24_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )

p_ptResFitSigma_pic_trk_eta, p_ptResFitSigma_pic_trk_eta_label, p_ptResFitSigma_pic_trk_eta_title, p_ptResFitSigma_pic_trk_eta_x, p_ptResFitSigma_pic_trk_eta_y = [], "ptResFitSigma_pic_trk_eta", "p_{T} res. for #mu_{Picky} (p_{T}>" + str(threshold_pT_GeV) + " GeV)", "#eta", "#sigma(q/p_{T Picky} - q/p_{T TRK}) [1/GeV]"
profiles.append( [p_ptResFitSigma_pic_trk_eta, p_ptResFitSigma_pic_trk_eta_label, p_ptResFitSigma_pic_trk_eta_title, p_ptResFitSigma_pic_trk_eta_x, p_ptResFitSigma_pic_trk_eta_y, ptResFitSigma_bin, ptResFitSigma_min, ptResFitSigma_max, profileEta_bin, profileEta_min, profileEta_max] )

p_ptResFitMean_pic_trk_eta, p_ptResFitMean_pic_trk_eta_label, p_ptResFitMean_pic_trk_eta_title, p_ptResFitMean_pic_trk_eta_x, p_ptResFitMean_pic_trk_eta_y = [], "ptResFitMean_pic_trk_eta", "p_{T} res. mean for #mu_{Picky} (p_{T}>" + str(threshold_pT_GeV) + " GeV)", "#eta", "mean(q/p_{T Picky} - q/p_{T TRK}) [1/GeV]"
profiles.append( [p_ptResFitMean_pic_trk_eta, p_ptResFitMean_pic_trk_eta_label, p_ptResFitMean_pic_trk_eta_title, p_ptResFitMean_pic_trk_eta_x, p_ptResFitMean_pic_trk_eta_y, ptResFitMean_bin, ptResFitMean_min, ptResFitMean_max, profileEta_bin, profileEta_min, profileEta_max] )

# ------------------------------------------------------------------------------
# Transverse momentum resolution in 16 bins of phi (-3.2 < phi < 3.2) for all eta (|eta| < 2.4)
# ------------------------------------------------------------------------------

h_ptRes_pic_trk_phi_m32_m28, h_ptRes_pic_trk_phi_m32_m28_label, h_ptRes_pic_trk_phi_m32_m28_title = [], "ptRes_pic_trk_eta_m32_m28", "p_{T} resolution for Picky muons: -#pi < #phi < -2.8"
h_ptRes_pic_trk_phi_m28_m24, h_ptRes_pic_trk_phi_m28_m24_label, h_ptRes_pic_trk_phi_m28_m24_title = [], "ptRes_pic_trk_phi_m28_m24", "p_{T} resolution for Picky muons: -2.8 < #phi < -2.4"
h_ptRes_pic_trk_phi_m24_m20, h_ptRes_pic_trk_phi_m24_m20_label, h_ptRes_pic_trk_phi_m24_m20_title = [], "ptRes_pic_trk_eta_m24_m20", "p_{T} resolution for Picky muons: -2.4 < #phi < -2.0"
h_ptRes_pic_trk_phi_m20_m16, h_ptRes_pic_trk_phi_m20_m16_label, h_ptRes_pic_trk_phi_m20_m16_title = [], "ptRes_pic_trk_eta_m20_m16", "p_{T} resolution for Picky muons: -2.0 < #phi < -1.6"
h_ptRes_pic_trk_phi_m16_m12, h_ptRes_pic_trk_phi_m16_m12_label, h_ptRes_pic_trk_phi_m16_m12_title = [], "ptRes_pic_trk_eta_m16_m12", "p_{T} resolution for Picky muons: -1.6 < #phi < -1.2"
h_ptRes_pic_trk_phi_m12_m08, h_ptRes_pic_trk_phi_m12_m08_label, h_ptRes_pic_trk_phi_m12_m08_title = [], "ptRes_pic_trk_eta_m12_m08", "p_{T} resolution for Picky muons: -1.2 < #phi < -0.8"
h_ptRes_pic_trk_phi_m08_m04, h_ptRes_pic_trk_phi_m08_m04_label, h_ptRes_pic_trk_phi_m08_m04_title = [], "ptRes_pic_trk_eta_m08_m04", "p_{T} resolution for Picky muons: -0.8 < #phi < -0.4"
h_ptRes_pic_trk_phi_m04_m00, h_ptRes_pic_trk_phi_m04_m00_label, h_ptRes_pic_trk_phi_m04_m00_title = [], "ptRes_pic_trk_eta_m04_m00", "p_{T} resolution for Picky muons: -0.4 < #phi < -0.0"
h_ptRes_pic_trk_phi_p00_p04, h_ptRes_pic_trk_phi_p00_p04_label, h_ptRes_pic_trk_phi_p00_p04_title = [], "ptRes_pic_trk_eta_p00_p04", "p_{T} resolution for Picky muons: 0.0 < #phi < 0.4"
h_ptRes_pic_trk_phi_p04_p08, h_ptRes_pic_trk_phi_p04_p08_label, h_ptRes_pic_trk_phi_p04_p08_title = [], "ptRes_pic_trk_phi_p04_p08", "p_{T} resolution for Picky muons: 0.4 < #phi < 0.8"
h_ptRes_pic_trk_phi_p08_p12, h_ptRes_pic_trk_phi_p08_p12_label, h_ptRes_pic_trk_phi_p08_p12_title = [], "ptRes_pic_trk_phi_p08_p12", "p_{T} resolution for Picky muons: 0.8 < #phi < 1.2"
h_ptRes_pic_trk_phi_p12_p16, h_ptRes_pic_trk_phi_p12_p16_label, h_ptRes_pic_trk_phi_p12_p16_title = [], "ptRes_pic_trk_phi_p12_p16", "p_{T} resolution for Picky muons: 1.2 < #phi < 1.6"
h_ptRes_pic_trk_phi_p16_p20, h_ptRes_pic_trk_phi_p16_p20_label, h_ptRes_pic_trk_phi_p16_p20_title = [], "ptRes_pic_trk_phi_p16_p20", "p_{T} resolution for Picky muons: 1.6 < #phi < 2.0"
h_ptRes_pic_trk_phi_p20_p24, h_ptRes_pic_trk_phi_p20_p24_label, h_ptRes_pic_trk_phi_p20_p24_title = [], "ptRes_pic_trk_phi_p20_p24", "p_{T} resolution for Picky muons: 2.0 < #phi < 2.4"
h_ptRes_pic_trk_phi_p24_p28, h_ptRes_pic_trk_phi_p24_p28_label, h_ptRes_pic_trk_phi_p24_p28_title = [], "ptRes_pic_trk_phi_p24_p28", "p_{T} resolution for Picky muons: 2.4 < #phi < 2.8"
h_ptRes_pic_trk_phi_p28_p32, h_ptRes_pic_trk_phi_p28_p32_label, h_ptRes_pic_trk_phi_p28_p32_title = [], "ptRes_pic_trk_phi_p28_p32", "p_{T} resolution for Picky muons: 2.8 < #phi < 3.2"

histos.append( [h_ptRes_pic_trk_phi_m32_m28, h_ptRes_pic_trk_phi_m32_m28_label, h_ptRes_pic_trk_phi_m32_m28_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_m28_m24, h_ptRes_pic_trk_phi_m28_m24_label, h_ptRes_pic_trk_phi_m28_m24_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_m24_m20, h_ptRes_pic_trk_phi_m24_m20_label, h_ptRes_pic_trk_phi_m24_m20_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_m20_m16, h_ptRes_pic_trk_phi_m20_m16_label, h_ptRes_pic_trk_phi_m20_m16_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_m16_m12, h_ptRes_pic_trk_phi_m16_m12_label, h_ptRes_pic_trk_phi_m16_m12_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_m12_m08, h_ptRes_pic_trk_phi_m12_m08_label, h_ptRes_pic_trk_phi_m12_m08_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_m08_m04, h_ptRes_pic_trk_phi_m08_m04_label, h_ptRes_pic_trk_phi_m08_m04_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_m04_m00, h_ptRes_pic_trk_phi_m04_m00_label, h_ptRes_pic_trk_phi_m04_m00_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_p00_p04, h_ptRes_pic_trk_phi_p00_p04_label, h_ptRes_pic_trk_phi_p00_p04_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_p04_p08, h_ptRes_pic_trk_phi_p04_p08_label, h_ptRes_pic_trk_phi_p04_p08_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_p08_p12, h_ptRes_pic_trk_phi_p08_p12_label, h_ptRes_pic_trk_phi_p08_p12_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_p12_p16, h_ptRes_pic_trk_phi_p12_p16_label, h_ptRes_pic_trk_phi_p12_p16_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_p16_p20, h_ptRes_pic_trk_phi_p16_p20_label, h_ptRes_pic_trk_phi_p16_p20_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_p20_p24, h_ptRes_pic_trk_phi_p20_p24_label, h_ptRes_pic_trk_phi_p20_p24_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_p24_p28, h_ptRes_pic_trk_phi_p24_p28_label, h_ptRes_pic_trk_phi_p24_p28_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trk_phi_p28_p32, h_ptRes_pic_trk_phi_p28_p32_label, h_ptRes_pic_trk_phi_p28_p32_title, h_ptRes_pic_trk_x, h_ptRes_pic_trk_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )

p_ptResFitSigma_pic_trk_phi, p_ptResFitSigma_pic_trk_phi_label, p_ptResFitSigma_pic_trk_phi_title, p_ptResFitSigma_pic_trk_phi_x, p_ptResFitSigma_pic_trk_phi_y = [], "ptResFitSigma_pic_trk_phi", "p_{T} res. for #mu_{Picky} (p_{T}>" + str(threshold_pT_GeV) + " GeV, |#eta|<2.4)", "#phi", "#sigma(q/p_{T Picky} - q/p_{T TRK}) [1/GeV]"
profiles.append( [p_ptResFitSigma_pic_trk_phi, p_ptResFitSigma_pic_trk_phi_label, p_ptResFitSigma_pic_trk_phi_title, p_ptResFitSigma_pic_trk_phi_x, p_ptResFitSigma_pic_trk_phi_y, ptResFitSigma_bin, ptResFitSigma_min, ptResFitSigma_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

p_ptResFitMean_pic_trk_phi, p_ptResFitMean_pic_trk_phi_label, p_ptResFitMean_pic_trk_phi_title, p_ptResFitMean_pic_trk_phi_x, p_ptResFitMean_pic_trk_phi_y = [], "ptResFitMean_pic_trk_phi", "p_{T} res. mean for #mu_{Picky} (p_{T}>" + str(threshold_pT_GeV) + " GeV, |#eta|<2.4)", "#phi", "mean(q/p_{T Picky} - q/p_{T TRK}) [1/GeV]"
profiles.append( [p_ptResFitMean_pic_trk_phi, p_ptResFitMean_pic_trk_phi_label, p_ptResFitMean_pic_trk_phi_title, p_ptResFitMean_pic_trk_phi_x, p_ptResFitMean_pic_trk_phi_y, ptResFitMean_bin, ptResFitMean_min, ptResFitMean_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

# ------------------------------------------------------------------------------
# Transverse momentum resolution in 16 bins of phi (-3.2 < phi < 3.2) for Barrel (|eta| < 0.9)
# ------------------------------------------------------------------------------

h_ptRes_pic_trkB_phi_m32_m28, h_ptRes_pic_trkB_phi_m32_m28_label, h_ptRes_pic_trkB_phi_m32_m28_title = [], "ptRes_pic_trkB_eta_m32_m28", "p_{T} resolution for Picky muons: -#pi < #phi < -2.8"
h_ptRes_pic_trkB_phi_m28_m24, h_ptRes_pic_trkB_phi_m28_m24_label, h_ptRes_pic_trkB_phi_m28_m24_title = [], "ptRes_pic_trkB_phi_m28_m24", "p_{T} resolution for Picky muons: -2.8 < #phi < -2.4"
h_ptRes_pic_trkB_phi_m24_m20, h_ptRes_pic_trkB_phi_m24_m20_label, h_ptRes_pic_trkB_phi_m24_m20_title = [], "ptRes_pic_trkB_eta_m24_m20", "p_{T} resolution for Picky muons: -2.4 < #phi < -2.0"
h_ptRes_pic_trkB_phi_m20_m16, h_ptRes_pic_trkB_phi_m20_m16_label, h_ptRes_pic_trkB_phi_m20_m16_title = [], "ptRes_pic_trkB_eta_m20_m16", "p_{T} resolution for Picky muons: -2.0 < #phi < -1.6"
h_ptRes_pic_trkB_phi_m16_m12, h_ptRes_pic_trkB_phi_m16_m12_label, h_ptRes_pic_trkB_phi_m16_m12_title = [], "ptRes_pic_trkB_eta_m16_m12", "p_{T} resolution for Picky muons: -1.6 < #phi < -1.2"
h_ptRes_pic_trkB_phi_m12_m08, h_ptRes_pic_trkB_phi_m12_m08_label, h_ptRes_pic_trkB_phi_m12_m08_title = [], "ptRes_pic_trkB_eta_m12_m08", "p_{T} resolution for Picky muons: -1.2 < #phi < -0.8"
h_ptRes_pic_trkB_phi_m08_m04, h_ptRes_pic_trkB_phi_m08_m04_label, h_ptRes_pic_trkB_phi_m08_m04_title = [], "ptRes_pic_trkB_eta_m08_m04", "p_{T} resolution for Picky muons: -0.8 < #phi < -0.4"
h_ptRes_pic_trkB_phi_m04_m00, h_ptRes_pic_trkB_phi_m04_m00_label, h_ptRes_pic_trkB_phi_m04_m00_title = [], "ptRes_pic_trkB_eta_m04_m00", "p_{T} resolution for Picky muons: -0.4 < #phi < -0.0"
h_ptRes_pic_trkB_phi_p00_p04, h_ptRes_pic_trkB_phi_p00_p04_label, h_ptRes_pic_trkB_phi_p00_p04_title = [], "ptRes_pic_trkB_eta_p00_p04", "p_{T} resolution for Picky muons: 0.0 < #phi < 0.4"
h_ptRes_pic_trkB_phi_p04_p08, h_ptRes_pic_trkB_phi_p04_p08_label, h_ptRes_pic_trkB_phi_p04_p08_title = [], "ptRes_pic_trkB_phi_p04_p08", "p_{T} resolution for Picky muons: 0.4 < #phi < 0.8"
h_ptRes_pic_trkB_phi_p08_p12, h_ptRes_pic_trkB_phi_p08_p12_label, h_ptRes_pic_trkB_phi_p08_p12_title = [], "ptRes_pic_trkB_phi_p08_p12", "p_{T} resolution for Picky muons: 0.8 < #phi < 1.2"
h_ptRes_pic_trkB_phi_p12_p16, h_ptRes_pic_trkB_phi_p12_p16_label, h_ptRes_pic_trkB_phi_p12_p16_title = [], "ptRes_pic_trkB_phi_p12_p16", "p_{T} resolution for Picky muons: 1.2 < #phi < 1.6"
h_ptRes_pic_trkB_phi_p16_p20, h_ptRes_pic_trkB_phi_p16_p20_label, h_ptRes_pic_trkB_phi_p16_p20_title = [], "ptRes_pic_trkB_phi_p16_p20", "p_{T} resolution for Picky muons: 1.6 < #phi < 2.0"
h_ptRes_pic_trkB_phi_p20_p24, h_ptRes_pic_trkB_phi_p20_p24_label, h_ptRes_pic_trkB_phi_p20_p24_title = [], "ptRes_pic_trkB_phi_p20_p24", "p_{T} resolution for Picky muons: 2.0 < #phi < 2.4"
h_ptRes_pic_trkB_phi_p24_p28, h_ptRes_pic_trkB_phi_p24_p28_label, h_ptRes_pic_trkB_phi_p24_p28_title = [], "ptRes_pic_trkB_phi_p24_p28", "p_{T} resolution for Picky muons: 2.4 < #phi < 2.8"
h_ptRes_pic_trkB_phi_p28_p32, h_ptRes_pic_trkB_phi_p28_p32_label, h_ptRes_pic_trkB_phi_p28_p32_title = [], "ptRes_pic_trkB_phi_p28_p32", "p_{T} resolution for Picky muons: 2.8 < #phi < 3.2"

h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y = h_ptRes_pic_trk_x, h_ptRes_pic_trk_y
histos.append( [h_ptRes_pic_trkB_phi_m32_m28, h_ptRes_pic_trkB_phi_m32_m28_label, h_ptRes_pic_trkB_phi_m32_m28_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_m28_m24, h_ptRes_pic_trkB_phi_m28_m24_label, h_ptRes_pic_trkB_phi_m28_m24_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_m24_m20, h_ptRes_pic_trkB_phi_m24_m20_label, h_ptRes_pic_trkB_phi_m24_m20_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_m20_m16, h_ptRes_pic_trkB_phi_m20_m16_label, h_ptRes_pic_trkB_phi_m20_m16_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_m16_m12, h_ptRes_pic_trkB_phi_m16_m12_label, h_ptRes_pic_trkB_phi_m16_m12_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_m12_m08, h_ptRes_pic_trkB_phi_m12_m08_label, h_ptRes_pic_trkB_phi_m12_m08_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_m08_m04, h_ptRes_pic_trkB_phi_m08_m04_label, h_ptRes_pic_trkB_phi_m08_m04_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_m04_m00, h_ptRes_pic_trkB_phi_m04_m00_label, h_ptRes_pic_trkB_phi_m04_m00_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_p00_p04, h_ptRes_pic_trkB_phi_p00_p04_label, h_ptRes_pic_trkB_phi_p00_p04_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_p04_p08, h_ptRes_pic_trkB_phi_p04_p08_label, h_ptRes_pic_trkB_phi_p04_p08_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_p08_p12, h_ptRes_pic_trkB_phi_p08_p12_label, h_ptRes_pic_trkB_phi_p08_p12_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_p12_p16, h_ptRes_pic_trkB_phi_p12_p16_label, h_ptRes_pic_trkB_phi_p12_p16_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_p16_p20, h_ptRes_pic_trkB_phi_p16_p20_label, h_ptRes_pic_trkB_phi_p16_p20_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_p20_p24, h_ptRes_pic_trkB_phi_p20_p24_label, h_ptRes_pic_trkB_phi_p20_p24_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_p24_p28, h_ptRes_pic_trkB_phi_p24_p28_label, h_ptRes_pic_trkB_phi_p24_p28_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkB_phi_p28_p32, h_ptRes_pic_trkB_phi_p28_p32_label, h_ptRes_pic_trkB_phi_p28_p32_title, h_ptRes_pic_trkB_x, h_ptRes_pic_trkB_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )

p_ptResFitSigma_pic_trkB_phi, p_ptResFitSigma_pic_trkB_phi_label, p_ptResFitSigma_pic_trkB_phi_title, p_ptResFitSigma_pic_trkB_phi_x, p_ptResFitSigma_pic_trkB_phi_y = [], "ptResFitSigma_pic_trkB_phi", "p_{T} res. for #mu_{Picky} (p_{T}>" + str(threshold_pT_GeV) + " GeV, |#eta|<0.9)", "#phi", "#sigma(q/p_{T Picky} - q/p_{T TRK}) [1/GeV]"
profiles.append( [p_ptResFitSigma_pic_trkB_phi, p_ptResFitSigma_pic_trkB_phi_label, p_ptResFitSigma_pic_trkB_phi_title, p_ptResFitSigma_pic_trkB_phi_x, p_ptResFitSigma_pic_trkB_phi_y, ptResFitSigma_bin, ptResFitSigma_min, ptResFitSigma_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

p_ptResFitMean_pic_trkB_phi, p_ptResFitMean_pic_trkB_phi_label, p_ptResFitMean_pic_trkB_phi_title, p_ptResFitMean_pic_trkB_phi_x, p_ptResFitMean_pic_trkB_phi_y = [], "ptResFitMean_pic_trkB_phi", "p_{T} res. mean for #mu_{Picky} (p_{T}>" + str(threshold_pT_GeV) + " GeV, |#eta|<0.9)", "#phi", "mean(q/p_{T Picky} - q/p_{T TRK}) [1/GeV]"
profiles.append( [p_ptResFitMean_pic_trkB_phi, p_ptResFitMean_pic_trkB_phi_label, p_ptResFitMean_pic_trkB_phi_title, p_ptResFitMean_pic_trkB_phi_x, p_ptResFitMean_pic_trkB_phi_y, ptResFitMean_bin, ptResFitMean_min, ptResFitMean_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

# ------------------------------------------------------------------------------
# Transverse momentum resolution in 16 bins of phi (-3.2 < phi < 3.2) for Plus Endcap + Overlap ( 0.9 < eta < 2.4)
# ------------------------------------------------------------------------------

h_ptRes_pic_trkEOp_phi_m32_m28, h_ptRes_pic_trkEOp_phi_m32_m28_label, h_ptRes_pic_trkEOp_phi_m32_m28_title = [], "ptRes_pic_trkEOp_eta_m32_m28", "p_{T} resolution for Picky muons: -#pi < #phi < -2.8"
h_ptRes_pic_trkEOp_phi_m28_m24, h_ptRes_pic_trkEOp_phi_m28_m24_label, h_ptRes_pic_trkEOp_phi_m28_m24_title = [], "ptRes_pic_trkEOp_phi_m28_m24", "p_{T} resolution for Picky muons: -2.8 < #phi < -2.4"
h_ptRes_pic_trkEOp_phi_m24_m20, h_ptRes_pic_trkEOp_phi_m24_m20_label, h_ptRes_pic_trkEOp_phi_m24_m20_title = [], "ptRes_pic_trkEOp_eta_m24_m20", "p_{T} resolution for Picky muons: -2.4 < #phi < -2.0"
h_ptRes_pic_trkEOp_phi_m20_m16, h_ptRes_pic_trkEOp_phi_m20_m16_label, h_ptRes_pic_trkEOp_phi_m20_m16_title = [], "ptRes_pic_trkEOp_eta_m20_m16", "p_{T} resolution for Picky muons: -2.0 < #phi < -1.6"
h_ptRes_pic_trkEOp_phi_m16_m12, h_ptRes_pic_trkEOp_phi_m16_m12_label, h_ptRes_pic_trkEOp_phi_m16_m12_title = [], "ptRes_pic_trkEOp_eta_m16_m12", "p_{T} resolution for Picky muons: -1.6 < #phi < -1.2"
h_ptRes_pic_trkEOp_phi_m12_m08, h_ptRes_pic_trkEOp_phi_m12_m08_label, h_ptRes_pic_trkEOp_phi_m12_m08_title = [], "ptRes_pic_trkEOp_eta_m12_m08", "p_{T} resolution for Picky muons: -1.2 < #phi < -0.8"
h_ptRes_pic_trkEOp_phi_m08_m04, h_ptRes_pic_trkEOp_phi_m08_m04_label, h_ptRes_pic_trkEOp_phi_m08_m04_title = [], "ptRes_pic_trkEOp_eta_m08_m04", "p_{T} resolution for Picky muons: -0.8 < #phi < -0.4"
h_ptRes_pic_trkEOp_phi_m04_m00, h_ptRes_pic_trkEOp_phi_m04_m00_label, h_ptRes_pic_trkEOp_phi_m04_m00_title = [], "ptRes_pic_trkEOp_eta_m04_m00", "p_{T} resolution for Picky muons: -0.4 < #phi < -0.0"
h_ptRes_pic_trkEOp_phi_p00_p04, h_ptRes_pic_trkEOp_phi_p00_p04_label, h_ptRes_pic_trkEOp_phi_p00_p04_title = [], "ptRes_pic_trkEOp_eta_p00_p04", "p_{T} resolution for Picky muons: 0.0 < #phi < 0.4"
h_ptRes_pic_trkEOp_phi_p04_p08, h_ptRes_pic_trkEOp_phi_p04_p08_label, h_ptRes_pic_trkEOp_phi_p04_p08_title = [], "ptRes_pic_trkEOp_phi_p04_p08", "p_{T} resolution for Picky muons: 0.4 < #phi < 0.8"
h_ptRes_pic_trkEOp_phi_p08_p12, h_ptRes_pic_trkEOp_phi_p08_p12_label, h_ptRes_pic_trkEOp_phi_p08_p12_title = [], "ptRes_pic_trkEOp_phi_p08_p12", "p_{T} resolution for Picky muons: 0.8 < #phi < 1.2"
h_ptRes_pic_trkEOp_phi_p12_p16, h_ptRes_pic_trkEOp_phi_p12_p16_label, h_ptRes_pic_trkEOp_phi_p12_p16_title = [], "ptRes_pic_trkEOp_phi_p12_p16", "p_{T} resolution for Picky muons: 1.2 < #phi < 1.6"
h_ptRes_pic_trkEOp_phi_p16_p20, h_ptRes_pic_trkEOp_phi_p16_p20_label, h_ptRes_pic_trkEOp_phi_p16_p20_title = [], "ptRes_pic_trkEOp_phi_p16_p20", "p_{T} resolution for Picky muons: 1.6 < #phi < 2.0"
h_ptRes_pic_trkEOp_phi_p20_p24, h_ptRes_pic_trkEOp_phi_p20_p24_label, h_ptRes_pic_trkEOp_phi_p20_p24_title = [], "ptRes_pic_trkEOp_phi_p20_p24", "p_{T} resolution for Picky muons: 2.0 < #phi < 2.4"
h_ptRes_pic_trkEOp_phi_p24_p28, h_ptRes_pic_trkEOp_phi_p24_p28_label, h_ptRes_pic_trkEOp_phi_p24_p28_title = [], "ptRes_pic_trkEOp_phi_p24_p28", "p_{T} resolution for Picky muons: 2.4 < #phi < 2.8"
h_ptRes_pic_trkEOp_phi_p28_p32, h_ptRes_pic_trkEOp_phi_p28_p32_label, h_ptRes_pic_trkEOp_phi_p28_p32_title = [], "ptRes_pic_trkEOp_phi_p28_p32", "p_{T} resolution for Picky muons: 2.8 < #phi < 3.2"

h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y = h_ptRes_pic_trk_x, h_ptRes_pic_trk_y
histos.append( [h_ptRes_pic_trkEOp_phi_m32_m28, h_ptRes_pic_trkEOp_phi_m32_m28_label, h_ptRes_pic_trkEOp_phi_m32_m28_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_m28_m24, h_ptRes_pic_trkEOp_phi_m28_m24_label, h_ptRes_pic_trkEOp_phi_m28_m24_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_m24_m20, h_ptRes_pic_trkEOp_phi_m24_m20_label, h_ptRes_pic_trkEOp_phi_m24_m20_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_m20_m16, h_ptRes_pic_trkEOp_phi_m20_m16_label, h_ptRes_pic_trkEOp_phi_m20_m16_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_m16_m12, h_ptRes_pic_trkEOp_phi_m16_m12_label, h_ptRes_pic_trkEOp_phi_m16_m12_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_m12_m08, h_ptRes_pic_trkEOp_phi_m12_m08_label, h_ptRes_pic_trkEOp_phi_m12_m08_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_m08_m04, h_ptRes_pic_trkEOp_phi_m08_m04_label, h_ptRes_pic_trkEOp_phi_m08_m04_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_m04_m00, h_ptRes_pic_trkEOp_phi_m04_m00_label, h_ptRes_pic_trkEOp_phi_m04_m00_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_p00_p04, h_ptRes_pic_trkEOp_phi_p00_p04_label, h_ptRes_pic_trkEOp_phi_p00_p04_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_p04_p08, h_ptRes_pic_trkEOp_phi_p04_p08_label, h_ptRes_pic_trkEOp_phi_p04_p08_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_p08_p12, h_ptRes_pic_trkEOp_phi_p08_p12_label, h_ptRes_pic_trkEOp_phi_p08_p12_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_p12_p16, h_ptRes_pic_trkEOp_phi_p12_p16_label, h_ptRes_pic_trkEOp_phi_p12_p16_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_p16_p20, h_ptRes_pic_trkEOp_phi_p16_p20_label, h_ptRes_pic_trkEOp_phi_p16_p20_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_p20_p24, h_ptRes_pic_trkEOp_phi_p20_p24_label, h_ptRes_pic_trkEOp_phi_p20_p24_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_p24_p28, h_ptRes_pic_trkEOp_phi_p24_p28_label, h_ptRes_pic_trkEOp_phi_p24_p28_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOp_phi_p28_p32, h_ptRes_pic_trkEOp_phi_p28_p32_label, h_ptRes_pic_trkEOp_phi_p28_p32_title, h_ptRes_pic_trkEOp_x, h_ptRes_pic_trkEOp_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )

p_ptResFitSigma_pic_trkEOp_phi, p_ptResFitSigma_pic_trkEOp_phi_label, p_ptResFitSigma_pic_trkEOp_phi_title, p_ptResFitSigma_pic_trkEOp_phi_x, p_ptResFitSigma_pic_trkEOp_phi_y = [], "ptResFitSigma_pic_trkEOp_phi", "p_{T} res. for #mu_{Picky} (p_{T}>" + str(threshold_pT_GeV) + " GeV, 0.9<#eta<2.4)", "#phi", "#sigma(q/p_{T Picky} - q/p_{T TRK}) [1/GeV]"
profiles.append( [p_ptResFitSigma_pic_trkEOp_phi, p_ptResFitSigma_pic_trkEOp_phi_label, p_ptResFitSigma_pic_trkEOp_phi_title, p_ptResFitSigma_pic_trkEOp_phi_x, p_ptResFitSigma_pic_trkEOp_phi_y, ptResFitSigma_bin, ptResFitSigma_min, ptResFitSigma_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

p_ptResFitMean_pic_trkEOp_phi, p_ptResFitMean_pic_trkEOp_phi_label, p_ptResFitMean_pic_trkEOp_phi_title, p_ptResFitMean_pic_trkEOp_phi_x, p_ptResFitMean_pic_trkEOp_phi_y = [], "ptResFitMean_pic_trkEOp_phi", "p_{T} res. mean for #mu_{Picky} (p_{T}>" + str(threshold_pT_GeV) + " GeV, 0.9<#eta<2.4)", "#phi", "mean(q/p_{T Picky} - q/p_{T TRK}) [1/GeV]"
profiles.append( [p_ptResFitMean_pic_trkEOp_phi, p_ptResFitMean_pic_trkEOp_phi_label, p_ptResFitMean_pic_trkEOp_phi_title, p_ptResFitMean_pic_trkEOp_phi_x, p_ptResFitMean_pic_trkEOp_phi_y, ptResFitMean_bin, ptResFitMean_min, ptResFitMean_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

# ------------------------------------------------------------------------------
# Transverse momentum resolution in 16 bins of phi (-3.2 < phi < 3.2) for Minus Endcap + Overlap ( -2.4 < eta < -0.9)
# ------------------------------------------------------------------------------

h_ptRes_pic_trkEOm_phi_m32_m28, h_ptRes_pic_trkEOm_phi_m32_m28_label, h_ptRes_pic_trkEOm_phi_m32_m28_title = [], "ptRes_pic_trkEOm_eta_m32_m28", "p_{T} resolution for Picky muons: -#pi < #phi < -2.8"
h_ptRes_pic_trkEOm_phi_m28_m24, h_ptRes_pic_trkEOm_phi_m28_m24_label, h_ptRes_pic_trkEOm_phi_m28_m24_title = [], "ptRes_pic_trkEOm_phi_m28_m24", "p_{T} resolution for Picky muons: -2.8 < #phi < -2.4"
h_ptRes_pic_trkEOm_phi_m24_m20, h_ptRes_pic_trkEOm_phi_m24_m20_label, h_ptRes_pic_trkEOm_phi_m24_m20_title = [], "ptRes_pic_trkEOm_eta_m24_m20", "p_{T} resolution for Picky muons: -2.4 < #phi < -2.0"
h_ptRes_pic_trkEOm_phi_m20_m16, h_ptRes_pic_trkEOm_phi_m20_m16_label, h_ptRes_pic_trkEOm_phi_m20_m16_title = [], "ptRes_pic_trkEOm_eta_m20_m16", "p_{T} resolution for Picky muons: -2.0 < #phi < -1.6"
h_ptRes_pic_trkEOm_phi_m16_m12, h_ptRes_pic_trkEOm_phi_m16_m12_label, h_ptRes_pic_trkEOm_phi_m16_m12_title = [], "ptRes_pic_trkEOm_eta_m16_m12", "p_{T} resolution for Picky muons: -1.6 < #phi < -1.2"
h_ptRes_pic_trkEOm_phi_m12_m08, h_ptRes_pic_trkEOm_phi_m12_m08_label, h_ptRes_pic_trkEOm_phi_m12_m08_title = [], "ptRes_pic_trkEOm_eta_m12_m08", "p_{T} resolution for Picky muons: -1.2 < #phi < -0.8"
h_ptRes_pic_trkEOm_phi_m08_m04, h_ptRes_pic_trkEOm_phi_m08_m04_label, h_ptRes_pic_trkEOm_phi_m08_m04_title = [], "ptRes_pic_trkEOm_eta_m08_m04", "p_{T} resolution for Picky muons: -0.8 < #phi < -0.4"
h_ptRes_pic_trkEOm_phi_m04_m00, h_ptRes_pic_trkEOm_phi_m04_m00_label, h_ptRes_pic_trkEOm_phi_m04_m00_title = [], "ptRes_pic_trkEOm_eta_m04_m00", "p_{T} resolution for Picky muons: -0.4 < #phi < -0.0"
h_ptRes_pic_trkEOm_phi_p00_p04, h_ptRes_pic_trkEOm_phi_p00_p04_label, h_ptRes_pic_trkEOm_phi_p00_p04_title = [], "ptRes_pic_trkEOm_eta_p00_p04", "p_{T} resolution for Picky muons: 0.0 < #phi < 0.4"
h_ptRes_pic_trkEOm_phi_p04_p08, h_ptRes_pic_trkEOm_phi_p04_p08_label, h_ptRes_pic_trkEOm_phi_p04_p08_title = [], "ptRes_pic_trkEOm_phi_p04_p08", "p_{T} resolution for Picky muons: 0.4 < #phi < 0.8"
h_ptRes_pic_trkEOm_phi_p08_p12, h_ptRes_pic_trkEOm_phi_p08_p12_label, h_ptRes_pic_trkEOm_phi_p08_p12_title = [], "ptRes_pic_trkEOm_phi_p08_p12", "p_{T} resolution for Picky muons: 0.8 < #phi < 1.2"
h_ptRes_pic_trkEOm_phi_p12_p16, h_ptRes_pic_trkEOm_phi_p12_p16_label, h_ptRes_pic_trkEOm_phi_p12_p16_title = [], "ptRes_pic_trkEOm_phi_p12_p16", "p_{T} resolution for Picky muons: 1.2 < #phi < 1.6"
h_ptRes_pic_trkEOm_phi_p16_p20, h_ptRes_pic_trkEOm_phi_p16_p20_label, h_ptRes_pic_trkEOm_phi_p16_p20_title = [], "ptRes_pic_trkEOm_phi_p16_p20", "p_{T} resolution for Picky muons: 1.6 < #phi < 2.0"
h_ptRes_pic_trkEOm_phi_p20_p24, h_ptRes_pic_trkEOm_phi_p20_p24_label, h_ptRes_pic_trkEOm_phi_p20_p24_title = [], "ptRes_pic_trkEOm_phi_p20_p24", "p_{T} resolution for Picky muons: 2.0 < #phi < 2.4"
h_ptRes_pic_trkEOm_phi_p24_p28, h_ptRes_pic_trkEOm_phi_p24_p28_label, h_ptRes_pic_trkEOm_phi_p24_p28_title = [], "ptRes_pic_trkEOm_phi_p24_p28", "p_{T} resolution for Picky muons: 2.4 < #phi < 2.8"
h_ptRes_pic_trkEOm_phi_p28_p32, h_ptRes_pic_trkEOm_phi_p28_p32_label, h_ptRes_pic_trkEOm_phi_p28_p32_title = [], "ptRes_pic_trkEOm_phi_p28_p32", "p_{T} resolution for Picky muons: 2.8 < #phi < 3.2"

h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y = h_ptRes_pic_trk_x, h_ptRes_pic_trk_y
histos.append( [h_ptRes_pic_trkEOm_phi_m32_m28, h_ptRes_pic_trkEOm_phi_m32_m28_label, h_ptRes_pic_trkEOm_phi_m32_m28_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_m28_m24, h_ptRes_pic_trkEOm_phi_m28_m24_label, h_ptRes_pic_trkEOm_phi_m28_m24_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_m24_m20, h_ptRes_pic_trkEOm_phi_m24_m20_label, h_ptRes_pic_trkEOm_phi_m24_m20_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_m20_m16, h_ptRes_pic_trkEOm_phi_m20_m16_label, h_ptRes_pic_trkEOm_phi_m20_m16_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_m16_m12, h_ptRes_pic_trkEOm_phi_m16_m12_label, h_ptRes_pic_trkEOm_phi_m16_m12_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_m12_m08, h_ptRes_pic_trkEOm_phi_m12_m08_label, h_ptRes_pic_trkEOm_phi_m12_m08_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_m08_m04, h_ptRes_pic_trkEOm_phi_m08_m04_label, h_ptRes_pic_trkEOm_phi_m08_m04_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_m04_m00, h_ptRes_pic_trkEOm_phi_m04_m00_label, h_ptRes_pic_trkEOm_phi_m04_m00_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_p00_p04, h_ptRes_pic_trkEOm_phi_p00_p04_label, h_ptRes_pic_trkEOm_phi_p00_p04_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_p04_p08, h_ptRes_pic_trkEOm_phi_p04_p08_label, h_ptRes_pic_trkEOm_phi_p04_p08_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_p08_p12, h_ptRes_pic_trkEOm_phi_p08_p12_label, h_ptRes_pic_trkEOm_phi_p08_p12_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_p12_p16, h_ptRes_pic_trkEOm_phi_p12_p16_label, h_ptRes_pic_trkEOm_phi_p12_p16_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_p16_p20, h_ptRes_pic_trkEOm_phi_p16_p20_label, h_ptRes_pic_trkEOm_phi_p16_p20_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_p20_p24, h_ptRes_pic_trkEOm_phi_p20_p24_label, h_ptRes_pic_trkEOm_phi_p20_p24_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_p24_p28, h_ptRes_pic_trkEOm_phi_p24_p28_label, h_ptRes_pic_trkEOm_phi_p24_p28_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )
histos.append( [h_ptRes_pic_trkEOm_phi_p28_p32, h_ptRes_pic_trkEOm_phi_p28_p32_label, h_ptRes_pic_trkEOm_phi_p28_p32_title, h_ptRes_pic_trkEOm_x, h_ptRes_pic_trkEOm_y, ptRes_bin, ptRes_min, ptRes_max, ptRes_fit] )

p_ptResFitSigma_pic_trkEOm_phi, p_ptResFitSigma_pic_trkEOm_phi_label, p_ptResFitSigma_pic_trkEOm_phi_title, p_ptResFitSigma_pic_trkEOm_phi_x, p_ptResFitSigma_pic_trkEOm_phi_y = [], "ptResFitSigma_pic_trkEOm_phi", "p_{T} res. for #mu_{Picky} (p_{T}>" + str(threshold_pT_GeV) + " GeV, -2.4<#eta<-0.9)", "#phi", "#sigma(q/p_{T Picky} - q/p_{T TRK}) [1/GeV]"
profiles.append( [p_ptResFitSigma_pic_trkEOm_phi, p_ptResFitSigma_pic_trkEOm_phi_label, p_ptResFitSigma_pic_trkEOm_phi_title, p_ptResFitSigma_pic_trkEOm_phi_x, p_ptResFitSigma_pic_trkEOm_phi_y, ptResFitSigma_bin, ptResFitSigma_min, ptResFitSigma_max, profilePhi_bin, profilePhi_min, profilePhi_max] )

p_ptResFitMean_pic_trkEOm_phi, p_ptResFitMean_pic_trkEOm_phi_label, p_ptResFitMean_pic_trkEOm_phi_title, p_ptResFitMean_pic_trkEOm_phi_x, p_ptResFitMean_pic_trkEOm_phi_y = [], "ptResFitMean_pic_trkEOm_phi", "p_{T} res. mean for #mu_{Picky} (p_{T}>" + str(threshold_pT_GeV) + " GeV, -2.4<#eta<-0.9)", "#phi", "mean(q/p_{T Picky} - q/p_{T TRK}) [1/GeV]"
profiles.append( [p_ptResFitMean_pic_trkEOm_phi, p_ptResFitMean_pic_trkEOm_phi_label, p_ptResFitMean_pic_trkEOm_phi_title, p_ptResFitMean_pic_trkEOm_phi_x, p_ptResFitMean_pic_trkEOm_phi_y, ptResFitMean_bin, ptResFitMean_min, ptResFitMean_max, profilePhi_bin, profilePhi_min, profilePhi_max] )
