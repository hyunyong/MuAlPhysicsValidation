def returnValues(name):
	nameSplit = name.split("-")
	varName = [nameSplit[0]+"_"+nameSplit[2],nameSplit[1]+"_"+nameSplit[2]]
	exec("etaValue = event." + nameSplit[1]+"_eta")
	exec("phiValue = event." +nameSplit[1]+"_phi")
	exec("firstValue = event." + varName[0])
	exec("secondValue = event." + varName[1])
	return etaValue, phiValue, firstValue, secondValue



def getFitParams(hist):
    fit = hist.GetFunction("pol1")
    
    p0 = fit.GetParameter(0) # offset from x axis
    p0e = fit.GetParError(0) # offset from x axis
    
    p1 = fit.GetParameter(1) # slope
    p1e = fit.GetParError(1) # slope


def getFitParamsGauss(hist):
    fit = hist.GetFunction("gaus")
    
    p0 = fit.GetParameter(0) # const
    p0e = fit.GetParError(0) # const
    
    p1 = fit.GetParameter(1) # mean
    p1e = fit.GetParError(1) # mean error

    p2 = fit.GetParameter(2) # sigma?
    p2e = fit.GetParError(2) # sigma error?

    #print p0, p0e, p1, p1e
    return p0, p0e, p1, p1e, p2, p2e

def fitCut(hist, sigmas, opts):
    lower, upper = hist.GetMean()-sigmas*hist.GetRMS(), hist.GetMean()+sigmas*hist.GetRMS()
    hist.Fit("gaus",opts, "", lower, upper)

def makeProfile(TH2F_name, dirName, lnBins, fitType, drawBinPlots, meanRange, sigmaRange):
	TH2F_temp_input = []
	TH1F_fit_mean_output = []
	TH1F_fit_sigma_output = []

	path = "{}/{}".format(outputFolderName,dirName)
	if not os.path.exists(path):
		os.makedirs(path)

	

	widthType = "RMS"
	meanType = "mean"
	if fitType == "gaus":  
		widthType = "fit #sigma"
		meanType = "fit center"

	for fileCount, file in enumerate(files):
		TH2F_temp_input.append(file.Get(TH2F_name))
	
	

	for histoCount, histo in enumerate(TH2F_temp_input):
		histoBounds = histo.GetXaxis().GetXmin(), histo.GetXaxis().GetXmax()
		TH1F_fit_mean_output.append(TH1F("{}_{}_mean".format(histo.GetName(),histoCount) , "{} {} ;{};{} fit mean".format(histo.GetTitle(),meanType,histo.GetXaxis().GetTitle(), histo.GetYaxis().GetTitle()), lnBins, histoBounds[0], histoBounds[1])) #,  histo.GetYaxis().GetXmin(),histo.GetYaxis().GetXmax()  )
		TH1F_fit_sigma_output.append(TH1F("{}_{}_sigma".format(histo.GetName(),histoCount) , "{} {} ;{};{} fit #sigma".format(histo.GetTitle(),widthType ,histo.GetXaxis().GetTitle(), histo.GetYaxis().GetTitle()), lnBins, histoBounds[0], histoBounds[1])) 
	
	for bins in range(lnBins):
		temp = []
		for fileCount, histo in enumerate(TH2F_temp_input):
				histoBounds = histo.GetXaxis().GetXmin(), histo.GetXaxis().GetXmax()
				length = histoBounds[1] -  histoBounds[0] + 0.0
				lengthBins = histo.GetNbinsX() #-  histo.GetlNbinsX() + 0.0
				width = length/lnBins
				widthBins = (lengthBins+.0)/(lnBins +.0)
				minValue = histo.GetXaxis().GetXmin()
				boundsBins = int(bins*widthBins), int((bins+1)*widthBins)
				bounds = minValue + bins*width, minValue + (bins+1)*width
	#
				boundsValue = histoBounds[0]+ length/(lnBins+.0)*bins, histoBounds[0]+ length/(lnBins+.0)*(bins+1)
				#print lengthBins, lnBins, widthBins,  boundsBins, bins, boundsValue
				temp.append(histo.ProjectionY("temp_{:b}".format(fileCount),boundsBins[0], boundsBins[1], ""))
				temp[fileCount].SetLineColor(fileCount)

				temp[fileCount].Sumw2()
				if temp[fileCount].Integral() > 0: temp[fileCount].Scale(1.0/temp[fileCount].Integral())
				if fitType == "gaus" and temp[fileCount].GetEntries() > 20:
					#temp.Fit("gaus","QC")
					fitCut(temp[fileCount], nGausFit, "QC")
					values = getFitParamsGauss(temp[fileCount])
					#print values[2], values[3], getFitParamsGauss
					TH1F_fit_mean_output[fileCount].SetBinContent(bins+1, values[2])
					TH1F_fit_mean_output[fileCount].SetBinError(bins+1, values[3])
					TH1F_fit_sigma_output[fileCount].SetBinContent(bins+1, values[4])
					TH1F_fit_sigma_output[fileCount].SetBinError(bins+1, values[5])
					#print boundsValue, bins, temp[fileCount].GetEntries()
					if verbose > 10:
						print meanType, " ", values[2]
						print widthType, " ", values[4]
				if fitType != "gaus":
					#fitCut(temp, nGausFit, "")
					#temp.Fit("gaus","QC")
					values = temp[fileCount].GetMean(), temp[fileCount].GetMeanError(), temp[fileCount].GetRMS(), temp[fileCount].GetRMSError()
					#print values[2], values[3], getFitParamsGauss
					TH1F_fit_mean_output[fileCount].SetBinContent(bins+1, values[0])
					TH1F_fit_mean_output[fileCount].SetBinError(bins+1, values[1])
					TH1F_fit_sigma_output[fileCount].SetBinContent(bins+1, values[2])
					TH1F_fit_sigma_output[fileCount].SetBinError(bins+1, values[3])
				

					

					#on last file draw plots
				if drawBinPlots and fileCount +1 == len(TH2F_temp_input): 

					path = "{}/{}/{}_{}".format(outputFolderName,dirName,TH2F_name,fitType )
					if not os.path.exists(path):
						os.makedirs(path)

					for count, binHisto in enumerate(temp):
						#binHisto.SetLineColor(colors[count])
						#binHisto.SetMarkerStyle(1)
						setHistoStyle(binHisto, colors[count] )
						#if binHisto.GetEntries() > 0: binHisto.Scale(1.0/binHisto.GetEntries())

						if count == 0: 
							print binHisto.GetMean()
							binHisto.Draw()
						if count > 0: 
							print binHisto.GetMean()
							binHisto.Draw("same")

					titleString = histo.GetXaxis().GetTitle().replace("{", "")
					titleString = titleString.replace("}", "")
					titleString = titleString.replace("_", "")
					titleString = titleString.replace("#", "")
					binlegend =  TLegend(0.12,0.68,0.5,0.88)
					makeLegend(binlegend, temp)
					#binlegend.SetHeader("{} {:0.3f} to {:0.3f}".format(histo.GetTitle(), boundsValue[0], boundsValue[1]))

					c1.SaveAs('{}/{}_{}_from_{:0.3f}_to_{:0.3f}_{}.png'.format(path,TH2F_name,fitType, boundsValue[0],boundsValue[1],titleString ))
				
					#print "%s_from_%0.3f_to_%0.3f_%s" % (TH2F_name,boundsValue[0],boundsValue[1],histo.GetXaxis().GetTitle())
	temp = []
	legend =  TLegend(0.12,0.68,0.5,0.88)
	drawProfile(TH1F_fit_mean_output, meanRange, legend)
	c1.SaveAs('{}/{}/{}_{}_mean.png'.format(outputFolderName,dirName,TH2F_name, fitType))

	legendRMS =  TLegend(0.12,0.68,0.5,0.88)
	drawProfile(TH1F_fit_sigma_output, sigmaRange, legendRMS)
	c1.SaveAs('{}/{}/{}_{}_sigma.png'.format(outputFolderName,dirName,TH2F_name, fitType))





def drawProfile(l_histogram, range,l_legend):
	for TH2FCount, histo in enumerate(l_histogram):

		setHistoStyle(histo, colors[TH2FCount])

		histo.GetYaxis().SetRangeUser(range[0], range[1])
		histo.GetYaxis().SetTitleOffset(1.4)
		if TH2FCount == 0: histo.Draw()
		if TH2FCount > 0: histo.Draw("same")

	
	makeLegend(l_legend, l_histogram)




def draw1D(l_histogram, range,l_legend):
    for TH2FCount, histo in enumerate(l_histogram):

		setHistoStyle(histo, colors[TH2FCount])

		histo.SetStats(0)
		histo.GetYaxis().SetTitleOffset(1.4)
		if TH2FCount == 0: histo.Draw()
		if TH2FCount > 0: histo.Draw("same")
    makeLegend1D(l_legend, l_histogram)
	

def setHistoStyle(histogram, color):
    histogram.SetLineColor(color)
    histogram.SetMarkerStyle(8)
    histogram.SetMarkerColor(color)
    histogram.SetMarkerSize(.5)


def makeLegend(legend, histogram):
	legend.SetTextSize(0.03)
	legend.SetFillStyle(0)
	legend.SetHeader(histogram[0].GetTitle())
	for TH2FCount, histo in enumerate(histogram):
		legend.AddEntry(histo,fileListName[TH2FCount],"lep")
	legend.Draw()

def makeLegend1D(legend, histogram):
	legend.SetTextSize(0.03)
	legend.SetFillStyle(0)
	for TH2FCount, histo in enumerate(histogram):
		legend.AddEntry(histo,fileListName[TH2FCount],"lep")
	legend.Draw()



def make1D(TH1F_name):
	TH1F_temp_input = []


	for fileCount, file in enumerate(files):
		TH1F_temp_input.append(file.Get(TH1F_name))

	histoBounds = TH1F_temp_input[0].GetXaxis().GetXmin(), TH1F_temp_input[0].GetXaxis().GetXmax()
	
	temp = []
	legend =  TLegend(0.65,0.68,0.7,0.88)
	draw1D(TH1F_temp_input, histoBounds, legend)
	c1.SaveAs('{}/{}.png'.format(outputFolderName,TH1F_name))





