import os, sys, optparse, math

def writeCfg(fname, inputNames, pwd, i):
    file(fname, "w").write("""#!/bin/sh

echo $SHELL

export CAFDIR=`pwd`
cd %s

export AFSDIR=`pwd`
export IJOB=%d
export INPUTFILES='%s'

export SCRAM_ARCH=slc6_amd64_gcc530
eval `scramv1 run -sh`
cp muAlAnalyzer_Data_cfg.py $CAFDIR/
cd $CAFDIR/

cmsRun muAlAnalyzer_Data_cfg.py

cp out_*root $AFSDIR
rm *root

""" % (pwd, i, inputNames))

file_list = sys.argv[1]   # MuAlRefit_Run2016E_RAWreco_DT3DOF_CSC3DOF_02_list.py
njobs = int(sys.argv[2])  # 700

print "file_list =", file_list
print "njobs =", njobs

execfile(file_list)

bsubfile = ["#!/bin/sh", ""]

for i in range(njobs):
    inputNames = " ".join(fileNames[len(fileNames)*i/njobs:len(fileNames)*(i+1)/njobs])
    analyzer = "analyzer%03d.sh" % (i)
    writeCfg(analyzer, inputNames, str(os.getcwdu()), i)
    os.system("chmod +x %s" % analyzer)
    bsubfile.append("echo analyzer%03d.sh" % (i))
    bsubfile.append("bsub -R \"type==SLC6_64\" -q cmscaf1nd -J \"analyzer%03d\" -u a@b analyzer%03d.sh" % (i,i))

#bsubfile.append("cd ..")
bsubfile.append("")
file("submit.sh", "w").write("\n".join(bsubfile))
os.system("chmod +x submit.sh")
