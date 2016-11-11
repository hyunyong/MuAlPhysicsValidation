print >> sys.stderr, "Start draw histograms"

iGroup = -1
for sampleGroup in combineHistos:
  iGroup = iGroup + 1
  
  print "Group #", iGroup, ":", sampleGroup, "( number of samples in the group = ", len(sampleGroup),")"
  
  iFirstInGroup = sampleGroup[0]
  
#  # Normalize histograms in group to first-in-group
#  if len(sampleGroup) > 1:
#    iHisto = -1
#    for histo in histos:
#      iHisto = iHisto + 1
#      baseIntegral = histo[0][ iFirstInGroup ].Integral()
#      for iSample in sampleGroup[1:]:
#        integral = histo[0][ iSample ].Integral()
#        if integral != 0:
#          scale = baseIntegral / integral
#          histo[0][ iSample ].Scale( scale )
#          if len( histo ) > 8:
#            fitFunc = histo[0][ iSample ].GetFunction( "fit"+histo[0][ iSample ].GetName() )
#            fitFunc.SetParameter( "Norm", scale * fitFunc.GetParameter("Norm") )
#          
#          print "  Scale for histo #",iHisto,"sample #", iSample, ":", scale

  # Normalize histograms to 1
  histoNorm = 1.0
  iHisto = -1
  for histo in histos:
    iHisto = iHisto + 1
    iSample = -1
    for sample in samples:
      iSample = iSample + 1
      integral = histo[0][ iSample ].Integral()
      if integral != 0:
        scale = histoNorm / integral
        histo[0][ iSample ].Scale( scale )
        if len( histo ) > 8:
          fitFunc = histo[0][ iSample ].GetFunction( "fit"+histo[0][ iSample ].GetName() )
          if fitFunc != None: fitFunc.SetParameter( 0, scale * fitFunc.GetParameter(0) )
        
        print "  Scale for histo #",iHisto,"sample #", iSample, ":", scale

  # Set maximum
  iHisto = -1
  for histo in histos:
    iHisto = iHisto + 1
    histMax = 0
    for iSample in sampleGroup:
#      histMax_current = histo[0][ iSample ].GetMaximum()
      histMax_current = histo[0][ iSample ].GetBinContent( histo[0][ iSample ].GetMaximumBin() )
      print "  Maximum for histo #",iHisto,"sample #", iSample, ":", histMax_current, histo[0][ iSample ].GetMaximumBin(), histo[0][ iSample ].GetBinContent( histo[0][ iSample ].GetMaximumBin() )
      if histMax_current > histMax: histMax = histMax_current
    print " Max for histo #", iHisto, "in the group: ", histMax
    for iSample in sampleGroup:
      histo[0][ iSample ].SetMaximum( 1.5 * histMax )
  
  canvasHeader = samples[ iFirstInGroup ][0]
  execfile("plot_initCanvas.py")
  
  iHisto = -1
  for histo in histos:
    iHisto = iHisto + 1
    
    # Draw histograms
    histo[0][ iFirstInGroup ].Draw()
    for iSample in sampleGroup[1:]:
      histo[0][ iSample ].Draw("same")
    
    # Draw labels
    legend = ROOT.TLegend(0.18,0.96 - 0.05 - 0.05*len(sampleGroup),0.92,0.96)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.03)
    legend.SetMargin(0.13)
    legend.SetHeader( histo[0][0].GetTitle() )
    for iSample in sampleGroup:
      legend.AddEntry( histo[0][ iSample ], samples[ iSample ][1], "L")
    legend.Draw()
    
    # Save canvas
    histo_label  = histo[1]
    plotName = "h_"+histo_label
    for iSample in sampleGroup:
      sample_label = samples[ iSample ][ 2 ]
      plotName = plotName+"_"+sample_label
    c1.SaveAs( pngFolder+"/"+plotName+".png" )
    c1.SaveAs( pdfFolder+"/"+plotName+".pdf" )
    c1.SaveAs( cFolder+"/"+plotName+".C" )
    
  iProfile = -1
  for profile in profiles:
    iProfile = iProfile + 1
    
    # Draw profiles
    h_dummy = ROOT.TH2F(profile[1], profile[2], profile[8], profile[9], profile[10], profile[5], profile[6], profile[7])
    h_dummy.SetXTitle(profile[3])
    h_dummy.SetYTitle(profile[4])
    h_dummy.SetNdivisions(505, "X")
    h_dummy.Draw()
    for iSample in sampleGroup:
      profile[0][ iSample ].Draw("Psame")

    # Draw labels
    legend = ROOT.TLegend(0.18,0.96 - 0.05 - 0.05*len(sampleGroup),0.92,0.96)
    legend.SetFillColor(ROOT.kWhite)
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.03)
    legend.SetMargin(0.13)
    legend.SetHeader( profile[2] )
    for iSample in sampleGroup:
      legend.AddEntry( profile[0][ iSample ], samples[ iSample ][1], "LEP")
    legend.Draw()

    # Save canvas
    profile_label  = profile[1]
    plotName = "p_"+profile_label
    for iSample in sampleGroup:
      sample_label = samples[ iSample ][ 2 ]
      plotName = plotName+"_"+sample_label
    c1.SaveAs( pngFolder+"/"+plotName+".png" )
    c1.SaveAs( pdfFolder+"/"+plotName+".pdf" )
    c1.SaveAs( cFolder+"/"+plotName+".C" )

