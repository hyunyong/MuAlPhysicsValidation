print >> sys.stderr, "Set up histograms"

histos = []
profiles = []

# ------------------------------------------------------------------------------
# Transverse momentum pt
# ------------------------------------------------------------------------------
try:                pt_bin, pt_min, pt_max
except NameError: pt_bin, pt_min, pt_max = 100, 0., 1500

h_glb_pt, h_glb_pt_label, h_glb_pt_title, h_glb_pt_x, h_glb_pt_y = [], "glb_pt", "Transverse momentum for GLB muons", "p_{T GLB} [GeV]", "a.u."
histos.append( [h_glb_pt, h_glb_pt_label, h_glb_pt_title, h_glb_pt_x, h_glb_pt_y, pt_bin, pt_min, pt_max] )

h_sta_pt, h_sta_pt_label, h_sta_pt_title, h_sta_pt_x, h_sta_pt_y = [], "sta_pt", "Transverse momentum for STA muons", "p_{T STA} [GeV]", "a.u."
histos.append( [h_sta_pt, h_sta_pt_label, h_sta_pt_title, h_sta_pt_x, h_sta_pt_y, pt_bin, pt_min, pt_max] )

h_glb_trk_pt, h_glb_trk_pt_label, h_glb_trk_pt_title, h_glb_trk_pt_x, h_glb_trk_pt_y = [], "glb_trk_pt", "Transverse momentum for TRK muons", "p_{T TRK} [GeV]", "a.u."
histos.append( [h_glb_trk_pt, h_glb_trk_pt_label, h_glb_trk_pt_title, h_glb_trk_pt_x, h_glb_trk_pt_y, pt_bin, pt_min, pt_max] )

h_glb_pic_pt, h_glb_pic_pt_label, h_glb_pic_pt_title, h_glb_pic_pt_x, h_glb_pic_pt_y = [], "glb_pic_pt", "Transverse momentum for \"Picky\" muons", "p_{T Picky} [GeV]", "a.u."
histos.append( [h_glb_pic_pt, h_glb_pic_pt_label, h_glb_pic_pt_title, h_glb_pic_pt_x, h_glb_pic_pt_y, pt_bin, pt_min, pt_max] )

# ------------------------------------------------------------------------------
# Transverse momentum resolution
# ------------------------------------------------------------------------------
try:                ptRes_bin, ptRes_min, ptRes_max
except NameError: ptRes_bin, ptRes_min, ptRes_max = 60, -0.003, 0.003
ptRes_fit = "gauss"

try:                ptResFitSigma_bin, ptResFitSigma_min, ptResFitSigma_max
except NameError: ptResFitSigma_bin, ptResFitSigma_min, ptResFitSigma_max = 150, 0., 0.002

try:                ptResFitMean_bin, ptResFitMean_min, ptResFitMean_max
except NameError: ptResFitMean_bin, ptResFitMean_min, ptResFitMean_max = 300, -0.0005, 0.001

# ------------------------------------------------------------------------------
# Transverse momentum resolution in 16 bins of phi (-3.2 < phi < 3.2)
# ------------------------------------------------------------------------------

try:                profilePhi_bin, profilePhi_min, profilePhi_max
except NameError: profilePhi_bin, profilePhi_min, profilePhi_max = 16, -3.2, 3.2

# ------------------------------------------------------------------------------
# Transverse momentum resolution in 16 bins of eta (-2.4 < eta < 2.4)
# ------------------------------------------------------------------------------

try:                profileEta_bin, profileEta_min, profileEta_max
except NameError: profileEta_bin, profileEta_min, profileEta_max = 18, -2.7, 2.7

#execfile("plot_setHistos_ptRes_gen_trk.py")
execfile("plot_setHistos_ptRes_sta_glb.py")
#execfile("plot_setHistos_ptRes_sta_gen.py")
execfile("plot_setHistos_ptRes_pic_trk.py")
#execfile("plot_setHistos_ptRes_pic_gen.py")

# ------------------------------------------------------------------------------
# Normalized chi2/n
# ------------------------------------------------------------------------------
try:                nchi2_bin, nchi2_min, nchi2_max
except NameError: nchi2_bin, nchi2_min, nchi2_max = 60, 0., 3.

h_glb_nchi2, h_glb_nchi2_label, h_glb_nchi2_title, h_glb_nchi2_x, h_glb_nchi2_y = [], "glb_nchi2", "Normalized #chi^{2} for GLB muons", "#chi^{2}/n_{GLB}", "a.u."
histos.append( [h_glb_nchi2, h_glb_nchi2_label, h_glb_nchi2_title, h_glb_nchi2_x, h_glb_nchi2_y, nchi2_bin, nchi2_min, nchi2_max] )

h_sta_nchi2, h_sta_nchi2_label, h_sta_nchi2_title, h_sta_nchi2_x, h_sta_nchi2_y = [], "sta_nchi2", "Normalized #chi^{2} for STA muons", "#chi^{2}/n_{STA}", "a.u."
histos.append( [h_sta_nchi2, h_sta_nchi2_label, h_sta_nchi2_title, h_sta_nchi2_x, h_sta_nchi2_y, nchi2_bin, nchi2_min, nchi2_max] )

#h_glb_trk_nchi2, h_glb_trk_nchi2_label, h_glb_trk_nchi2_title, h_glb_trk_nchi2_x, h_glb_trk_nchi2_y = [], "glb_trk_nchi2", "Normalized #chi^{2} for TRK muons", "#chi^{2}/n_{TRK}", "a.u."
#histos.append( [h_glb_trk_nchi2, h_glb_trk_nchi2_label, h_glb_trk_nchi2_title, h_glb_trk_nchi2_x, h_glb_trk_nchi2_y, nchi2_bin, nchi2_min, nchi2_max] )

#h_glb_pic_nchi2, h_glb_pic_nchi2_label, h_glb_pic_nchi2_title, h_glb_pic_nchi2_x, h_glb_pic_nchi2_y = [], "glb_pic_nchi2", "Normalized #chi^{2} for \"Picky\" muons", "#chi^{2}/n_{Picky}", "a.u."
#histos.append( [h_glb_pic_nchi2, h_glb_pic_nchi2_label, h_glb_pic_nchi2_title, h_glb_pic_nchi2_x, h_glb_pic_nchi2_y, nchi2_bin, nchi2_min, nchi2_max] )

# ------------------------------------------------------------------------------
# Pseudorpidity eta
# ------------------------------------------------------------------------------
try:                eta_bin, eta_min, eta_max
except NameError: eta_bin, eta_min, eta_max = 72, -2.7, 2.7

h_glb_eta, h_glb_eta_label, h_glb_eta_title, h_glb_eta_x, h_glb_eta_y = [], "glb_eta", "Pseudorapidity for GLB muons", "#eta_{GLB}", "a.u."
histos.append( [h_glb_eta, h_glb_eta_label, h_glb_eta_title, h_glb_eta_x, h_glb_eta_y, eta_bin, eta_min, eta_max] )

h_sta_eta, h_sta_eta_label, h_sta_eta_title, h_sta_eta_x, h_sta_eta_y = [], "sta_eta", "Pseudorapidity for STA muons", "#eta_{STA}", "a.u."
histos.append( [h_sta_eta, h_sta_eta_label, h_sta_eta_title, h_sta_eta_x, h_sta_eta_y, eta_bin, eta_min, eta_max] )

h_glb_trk_eta, h_glb_trk_eta_label, h_glb_trk_eta_title, h_glb_trk_eta_x, h_glb_trk_eta_y = [], "glb_trk_eta", "Pseudorapidity for TRK muons", "#eta_{TRK}", "a.u."
histos.append( [h_glb_trk_eta, h_glb_trk_eta_label, h_glb_trk_eta_title, h_glb_trk_eta_x, h_glb_trk_eta_y, eta_bin, eta_min, eta_max] )

h_glb_pic_eta, h_glb_pic_eta_label, h_glb_pic_eta_title, h_glb_pic_eta_x, h_glb_pic_eta_y = [], "glb_pic_eta", "Pseudorapidity for \"Picky\" muons", "#eta_{Picky}", "a.u."
histos.append( [h_glb_pic_eta, h_glb_pic_eta_label, h_glb_pic_eta_title, h_glb_pic_eta_x, h_glb_pic_eta_y, eta_bin, eta_min, eta_max] )

# ------------------------------------------------------------------------------
# Azimuthal angle phi
# ------------------------------------------------------------------------------
try:                phi_bin, phi_min, phi_max
except NameError: phi_bin, phi_min, phi_max = 64, -3.2, 3.2

h_glb_phi, h_glb_phi_label, h_glb_phi_title, h_glb_phi_x, h_glb_phi_y = [], "glb_phi", "Azimuthal angle for GLB muons", "#phi_{GLB} [rad]", "a.u."
histos.append( [h_glb_phi, h_glb_phi_label, h_glb_phi_title, h_glb_phi_x, h_glb_phi_y, phi_bin, phi_min, phi_max] )

h_sta_phi, h_sta_phi_label, h_sta_phi_title, h_sta_phi_x, h_sta_phi_y = [], "sta_phi", "Azimuthal angle for STA muons", "#phi_{STA} [rad]", "a.u."
histos.append( [h_sta_phi, h_sta_phi_label, h_sta_phi_title, h_sta_phi_x, h_sta_phi_y, phi_bin, phi_min, phi_max] )

h_glb_trk_phi, h_glb_trk_phi_label, h_glb_trk_phi_title, h_glb_trk_phi_x, h_glb_trk_phi_y = [], "glb_trk_phi", "Azimuthal angle for TRK muons", "#phi_{TRK} [rad]", "a.u."
histos.append( [h_glb_trk_phi, h_glb_trk_phi_label, h_glb_trk_phi_title, h_glb_trk_phi_x, h_glb_trk_phi_y, phi_bin, phi_min, phi_max] )

h_glb_pic_phi, h_glb_pic_phi_label, h_glb_pic_phi_title, h_glb_pic_phi_x, h_glb_pic_phi_y = [], "glb_pic_phi", "Azimuthal angle for \"Picky\" muons", "#phi_{Picky} [rad]", "a.u."
histos.append( [h_glb_pic_phi, h_glb_pic_phi_label, h_glb_pic_phi_title, h_glb_pic_phi_x, h_glb_pic_phi_y, phi_bin, phi_min, phi_max] )

# ------------------------------------------------------------------------------
# Dimuon mass
# ------------------------------------------------------------------------------
try:                m_bin, m_min, m_max
except NameError: m_bin, m_min, m_max = 40, 60, 120
m_fit = "gauss"

try:                mFitSigma_bin, mFitSigma_min, mFitSigma_max
except NameError: mFitSigma_bin, mFitSigma_min, mFitSigma_max = 40, 0., 20

try:                mFitMean_bin, mFitMean_min, mFitMean_max
except NameError: mFitMean_bin, mFitMean_min, mFitMean_max = 40, 80, 100

execfile("plot_setHistos_m_sta.py")
