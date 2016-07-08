import os, sys, optparse, math

def writeCfg(fname, inputNames, pwd, i, wd, cfg):
    file(fname, "w").write("""#!/bin/sh

echo $SHELL

export CAFDIR=`pwd`
cd %s

export AFSDIR=`pwd`
export IJOB=%d
export INPUTFILES='%s'

export SCRAM_ARCH=slc6_amd64_gcc530
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 run -sh`
cp %s $CAFDIR/
cd $CAFDIR/

cmsRun %s

eos mkdir -p /store/group/alca_muonalign/lpernie/%s/
cmsStage *root /store/group/alca_muonalign/lpernie/%s/
rm *root

""" % (pwd, i, inputNames, cfg, cfg, wd, wd))

working_dir = "refit_PromptGT_TrackerMay2016_MuAlMay2016_v1"
file_list = "SingleMuon_Run2016B_ZMu_v2_files_large.py"
njobs = 900
cfg = "refit_PromptGT_TrackerMay2016_MuAlMay2016_cfg.py"

print "working_dir =", working_dir
print "file_list =", file_list
print "njobs =", njobs
print "cfg =", cfg

os.system("rm -rf %s; mkdir %s" % (working_dir, working_dir))

execfile(file_list)

bsubfile = ["#!/bin/sh", ""]
#bsubfile.append("cd %s" % working_dir)

for i in range(njobs):
    inputNames = " ".join(fileNames[len(fileNames)*i/njobs:len(fileNames)*(i+1)/njobs])
    refitter = "%s/refitter%03d.sh" % (working_dir, i)
    writeCfg(refitter, inputNames, str(os.getcwdu()), i, working_dir, cfg)
    os.system("chmod +x %s" % refitter)
    bsubfile.append("echo %s/refitter%03d.sh" % (working_dir, i))
    bsubfile.append("bsub -R \"type==SLC6_64\" -q cmscaf1nd -J \"refitter%03d\" -u a@b refitter%03d.sh" % (i,i))

bsubfile.append("cd ..")
bsubfile.append("")
file(working_dir+"/submit.sh", "w").write("\n".join(bsubfile))
os.system("chmod +x "+working_dir+"/submit.sh")

