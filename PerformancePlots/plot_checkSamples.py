print >> sys.stderr, "List of samples: "

iSample = -1

for sample in samples:
  iSample = iSample + 1
  
  header     = sample[0]
  legend     = sample[1]
  label      = sample[2]
  color      = sample[3][0]
  maxEntries = sample[4]
  filenames  = sample[5:]
  
  print >> sys.stderr, "   Sample #", iSample
  print >> sys.stderr, "      legend = ", legend
  print >> sys.stderr, "      label  = ", label
  print >> sys.stderr, "      color  = ", color
  print >> sys.stderr, "      entries to process = ", maxEntries
  
  for filename in filenames:
    try:
      with open(filename):
        print >> sys.stderr, "      file exist = ", filename
    except IOError:
      print >> sys.stderr, "      ERROR! No file = ", filename
      print >> sys.stderr, "Exit"
      exit(0)
  
