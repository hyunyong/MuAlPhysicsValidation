print >> sys.stderr, "Create local area for output"

outputFolder = mainScriptName+"_output"

if not os.path.exists( outputFolder ):
  os.makedirs( outputFolder )

outFileName1 = outputFolder+"/"+mainScriptName+".output.txt"
outFile1 = open(outFileName1, 'w+')

pngFolder = outputFolder+"/PNG"

if not os.path.exists(pngFolder):
  os.makedirs(pngFolder)

pdfFolder = outputFolder+"/PDF"

if not os.path.exists(pdfFolder):
  os.makedirs(pdfFolder)

cFolder = outputFolder+"/C"

if not os.path.exists(cFolder):
  os.makedirs(cFolder)
