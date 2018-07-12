from root_numpy import  tree2array, array2tree
from root_numpy import fill_hist

def recoMuonTree2Array(recoMuons, Event_to_RUN):
    recoMuonArray = tree2array(recoMuons,
        branches=[  'glb', 'sta', 
                    'TMath::Abs(glb_eta)', 'glb_eta', 'glb_trk_eta', 'sta_eta',
                    'glb_phi',  'glb_trk_phi', 'sta_phi', 'glb_phi_error',
                    'glb_pt','glb_trk_pt', 'sta_pt',
                    'glb_nchi2', 'sta_nchi2',
                    'glb_nhits',
                    'q * (1.0/sta_pt-1.0/glb_trk_pt)',
                    'q * (1.0/sta_pt-1.0/glb_pt)',
                    '(q/glb_pt-q/sta_pt)/glb_qoverpterror' ],
        selection='glb && sta',
        start=0, stop=Event_to_RUN, step=1)
    
    recoMuonArray.dtype.names = [   'glb', 'sta', 
                            'glb_eta_abs', 'glb_eta', 'glb_trk_eta', 'sta_eta',
                            'glb_phi', 'glb_trk_phi', 'sta_phi', 'glb_phi_error',
                            'glb_pt', 'glb_trk_pt','sta_pt',
                            'glb_nchi2','sta_nchi2',
                            'glb_nhits',
                            'ptResSTAGLBTRK',
                            'ptResSTAGLB',
                            'ptPullSTAGLB' ]
    return recoMuonArray

def genMuonTree2Array(recoMuons, Event_to_RUN):
    recoMuonArrayMC = tree2array(recoMuons,
    branches=[  'glb', 'sta', 
                'glb_gen_eta',
                'glb_gen_phi', 
                'glb__genpt'
                'q * (1.0/sta_pt-1.0/glb_gen_pt)',
                'q*(1.0/sta_pt - 1.0/glb_gen_pt)/glb_qoverpterror',
                'q * (1.0/glb_pt-1.0/glb_gen_pt)',
                'q*(1.0/glb_pt - 1.0/glb_gen_pt)/glb_qoverpterror' ],
    selection='glb && sta',
    start=0, stop=Event_to_RUN, step=1)

    recoMuonArrayMC.dtype.names = [ 'glb', 'sta', 
                            'glb_gen_eta',
                            'glb_gen_phi',
                            'glb_gen_pt', 
                            'ptResSTAGEN',
                            'ptPullSTAGEN',
                            'ptResGLBGEN',
                            'ptPullGLBGEN']
    return recoMuonArrayMC

    

def diMuonTree2Array(recoDimuons, Event_to_RUN):
    diMuonArray = tree2array(recoDimuons,
        branches=['hyb_pt', 'hyb_eta',  
        'hyb_phi',  'hyb_sta_pt',   'hyb_sta_eta', 
        'hyb_sta_phi', 'hyb_m', 'hyb_q', 'pos_sta_phi', 
        'neg_sta_phi', 
        'glb_m',
        'recoMu_neg_IsoPF04', 'recoMu_pos_IsoPF04',
        'pos_glb_trk_pt', 'neg_glb_trk_pt',
        'pos_glb_trk_eta',  'neg_glb_trk_eta',],
        selection='glb && sta',
        start=0, stop=Event_to_RUN, step=1)
    return diMuonArray