import os, sys

from collections import defaultdict
import numpy as np

from matplotlib import pyplot
#import matplotlib.colors as cl
from matplotlib.ticker import LogLocator, FormatStrFormatter, MaxNLocator
from matplotlib import gridspec



folder = '34Ar+a'
savefile = '../rate_'+folder+'_alpha'+'.pdf'

if os.path.isfile(savefile):
	os.remove(savefile)


t = [.1,.2,.3,.4,.5,.6,.7,.8,.9,1,1.5,2,3,4,5,6,7,8,9,10]
temps = np.asarray(t)


talysFile = '../'+folder+'/HFRates/talys1.6/astrorate.p'
nonSmokerFile = '../'+folder+'/HFRates/nonSmoker/nonSmokerWeb.dat'
calcRateFile = '../'+folder+'/rateFit.dat'
standardRateFile = '../'+folder+'/randStandardRate.dat'
rMatrixRateFile = '../'+folder+'/RmatrixRate/rate.dat'
#calcRateFile = '../'+folder+'/rateFit.dat'

#quotedFile = './'+folder+'/quotedRates/almaraz.dat'


########################################################################
#	Reading in TALYS rates 
########################################################################

#List for reading in temperatures and rates from NON-SMOKER 
#.......................................................................
talysTemp = []
talysRate = []

#Reading in TALYS Rates from file. 
#.......................................................................
with open(talysFile,'r') as talysInputFile:
	Comments = talysInputFile.readline()
	Comments = talysInputFile.readline()


	for line in talysInputFile:
		talysline = line.split()
		if float(talysline[0]) in temps:
			talysTemp.append(float(talysline[0]))
			talysRate.append(float(talysline[1]))


########################################################################
#	Reading in NON-SMOKER rates 
########################################################################

#List for reading in temperatures and rates from NON-SMOKER 
#.......................................................................
NsTemp = []
NsRate = []
NsRate_10up = []
NsRate_10down = []

#Reading in NON-SMOKER Rates from file. 
#.......................................................................
with open(nonSmokerFile,'r') as NsFile:

	for line in NsFile:
		Nsline = line.split()
		if float(Nsline[0]) in temps:
			NsTemp.append(float(Nsline[0]))
			NsRate.append(float(Nsline[1]))
			NsRate_10up.append(float(Nsline[1])*10)
			NsRate_10down.append(float(Nsline[1])/10)

########################################################################
#	Reading in quoted Rates
########################################################################

#	List for reading in temperatures and rates from rates quoted by Almaraz
#.......................................................................
if folder == '26Si+a':
	
	qTemp = []
	qRate = []
	with open(quotedFile,'r') as qFile:

		for line in qFile:
			qline = line.split()
			if float(qline[0]) in temps:
				qTemp.append(float(qline[0]))
				qRate.append(float(qline[1]))
			
########################################################################
#	Reading in calculated Rates
########################################################################

#	List for reading in temperatures and rates from rate calculation
#.......................................................................
calcTemp = []
medianRate = []
upperRate = []
lowerRate = []
upper95Rate = []
lower95Rate = []
upper68Rate = []
lower68Rate = []

#	Reading in NON-SMOKER Rates from file.
#....................................................................... 
with open(calcRateFile,'r') as rateFile:
	Comments = rateFile.readline()

	for line in rateFile:
		rateline = line.split()
		if float(rateline[0]) in temps:
			calcTemp.append(float(rateline[0]))
			lowerRate.append(float(rateline[1]))
			lower95Rate.append(float(rateline[2]))
			lower68Rate.append(float(rateline[3]))
			medianRate.append(float(rateline[4]))
			upper68Rate.append(float(rateline[5]))
			upper95Rate.append(float(rateline[6]))
			upperRate.append(float(rateline[7]))


#	Reading in RMatrix Rates from file.
#....................................................................... 
rmTemp = []
rmRate = []

with open(rMatrixRateFile,'r') as rmFile:

	for line in rmFile:
		rmline = line.split()
		if float(rmline[0]) in temps:
			rmTemp.append(float(rmline[0]))
			rmRate.append(float(rmline[1]))

#	Reading in random spin Rate from file.
#....................................................................... 
rdStanTemp = []
rdStanRate = []

with open(standardRateFile,'r') as rdStanFile:

	for line in rdStanFile:
		rdStanline = line.split()
		if float(rdStanline[0]) in temps:
			rdStanTemp.append(float(rdStanline[0]))
			rdStanRate.append(float(rdStanline[1]))


########################################################################
#	Normalizing all rates to the TALYS rate 
########################################################################

if folder == '26Si+a':
	qRatioRate = [float(rate) / float(NS) for rate,NS in zip(qRate, NsRate)]


talysRatioRate = [float(rate) / float(NS) for rate,NS in zip(talysRate, NsRate)]
rmRatioRate = [float(rate) / float(NS) for rate,NS in zip(rmRate, NsRate)]
rdStanRatioRate = [float(rate) / float(NS) for rate,NS in zip(rdStanRate, NsRate)]
NsRatioRate = [float(rate) / float(NS) for rate,NS in zip(NsRate, NsRate)]
NsRatioRate_10up = [float(rate) / float(NS) for rate,NS in zip(NsRate_10up, NsRate)]
NsRatioRate_10down = [float(rate) / float(NS) for rate,NS in zip(NsRate_10down, NsRate)]

upperRatioRate = [float(rate) / float(NS) for rate,NS in zip(upperRate, NsRate)]
upper68RatioRate = [float(rate) / float(NS) for rate,NS in zip(upper68Rate, NsRate)]
upper95RatioRate = [float(rate) / float(NS) for rate,NS in zip(upper95Rate, NsRate)]

medianRatioRate = [float(rate) / float(NS) for rate,NS in zip(medianRate, NsRate)]

lowerRatioRate = [float(rate) / float(NS) for rate,NS in zip(lowerRate, NsRate)]
lower68RatioRate = [float(rate) / float(NS) for rate,NS in zip(lower68Rate, NsRate)]
lower95RatioRate = [float(rate) / float(NS) for rate,NS in zip(lower95Rate, NsRate)]




########################################################################
#	Plotting all rate.
########################################################################


#	Setting up figure
#....................................................................... 
figure = pyplot.figure(figsize=(8, 10))
axis1 = pyplot.subplot2grid((3,2), (0,0), colspan=2,rowspan=2)
axis2 = pyplot.subplot2grid((3,2), (2,0), colspan=2, sharex=axis1)
pyplot.subplots_adjust(hspace=0.0)
axis1.set_yscale('log')
axis1.set_xscale('log')
if folder == '26Si+a':
	axis1.set_xlim([0.2,3.0])
	axis1.set_ylim([2E-26,7E5])
elif folder == '34Ar+a':
	axis1.set_xlim([0.2,3.0])
	axis1.set_ylim([2E-32,7E5])
else:
	axis1.set_xlim([0.2,3.0])
	axis1.set_ylim([2E-26,7E5])
axis1.set_ylabel (r'N$_{A}$ <$ \sigma \nu$> (cm$^{3}$ mol$^{-1}$ s$^{-1}$)', fontsize=16)
pyplot.setp(axis1.get_xticklabels(), visible=False)
axis2.set_yscale('log')
axis2.set_xscale('log')
axis2.set_xlim([0.2,3.0])
axis2.set_ylim([2E-4,2E1])
axis2.set_xlabel(r'Temperature (GK)',fontsize=16, labelpad=+1)
axis2.set_ylabel('Normalized to \nNON-SMOKER$^{WEB}$', fontsize=16,labelpad=+5)


#colors= [  talys  ,nonSmoker, Starlib , fitRate , MCRate  ]
#....................................................................... 
colors = ['#2c7bb6','#abcae9','#d7191c','#fdae61','#ffffbf','#4110B2']


#Plotting all rates.
#....................................................................... 

nonSmokerPlot, = axis1.plot(temps,NsRate, color=colors[1], linewidth=1.5,linestyle="-", label = 'NON-SMOKER Rate')
nonSmokerPlot_up = axis1.plot(temps,NsRate_10up, color=colors[1], alpha=0.01,linewidth=1.5, linestyle="-", label = 'NON-SMOKER Rate')
nonSmokerPlot_down = axis1.plot(temps,NsRate_10down, color=colors[1], alpha=0.01,linewidth=1.5, linestyle="-", label = 'NON-SMOKER Rate')
tayls16Plot, = axis1.plot(temps,talysRate, color=colors[0], linewidth=1.5, linestyle="-", label = 'talys1.6 Rate')
rmatrixPlot, = axis1.plot(temps,rmRate, color=colors[5], linewidth=1.5,linestyle="--", label = 'R-Matrix Rate')
rdStanPlot, = axis1.plot(temps,rdStanRate, color=colors[5], linewidth=1.5,linestyle="-", label = 'random spin set Rate')
#if folder == '26Si+a':
#	qPlot, = axis1.plot(temps,qRate, color=colors[0], linewidth=1.5, linestyle="-", label = 'Almaraz Rate')

medianRatePlot, = axis1.plot(temps,medianRate, color=colors[2], linewidth=1.5, linestyle="-", label = 'Median Rate')
upperRatePlot, = axis1.plot(temps,upperRate, color=colors[3], alpha=0.01, linewidth=1.5, linestyle="-", label = 'Upper Rate')
lowerRatePlot, = axis1.plot(temps,lowerRate, color=colors[3], alpha=0.01, linewidth=1.5, linestyle="-", label = 'lower Rate')
upper68RatePlot, = axis1.plot(temps,upper68Rate, color=colors[3], linewidth=1.5, linestyle="--", label = 'upper68 Rate')
lower68RatePlot, = axis1.plot(temps,lower68Rate, color=colors[3], linewidth=1.5, linestyle="--", label = 'lower68 Rate')
upper95RatePlot, = axis1.plot(temps,upper95Rate, color=colors[3], linewidth=1.5, linestyle="-.", label = 'upper95 Rate')
lower95RatePlot, = axis1.plot(temps,lower95Rate, color=colors[3], linewidth=1.5, linestyle="-.", label = 'lower95 Rate')

axis1.fill_between(temps, NsRate_10down,NsRate_10up, color=colors[1],alpha=0.4)
axis1.fill_between(temps, lowerRate ,upperRate, color=colors[3],alpha=0.5)

axis2.plot(temps,NsRatioRate, color=colors[1], linewidth=1.5,linestyle="-", label = 'NON-SMOKER Rate')
axis2.plot(temps,NsRatioRate_10down, color=colors[1], linewidth=1.5, alpha=0.01, linestyle="-", label = 'NON-SMOKER Rate down')
axis2.plot(temps,NsRatioRate_10up, color=colors[1], linewidth=1.5, alpha=0.01, linestyle="-", label = 'NON-SMOKER Rate up')
axis2.plot(temps,talysRatioRate, color=colors[0], linewidth=1.5, linestyle="-", label = 'talys1.6 Rate')
axis2.plot(temps,rmRatioRate, color=colors[5], linewidth=1.5, linestyle="--", label = 'R-Matrix Rate')
axis2.plot(temps,rdStanRatioRate , color=colors[5], linewidth=1.5, linestyle="-", label = 'R-Matrix Rate')
#if folder == '26Si+a':
#	axis2.plot(temps,qRatioRate, color=colors[0], linewidth=1.5, linestyle="-", label = 'Almaraz Rate')
axis2.plot(temps,medianRatioRate, color=colors[2], linewidth=1.5, linestyle="-", label = 'medianRatioRate')
axis2.plot(temps,upperRatioRate, color=colors[3], alpha=0.01, linewidth=1.5, linestyle="-", label = 'upperRatioRate')
axis2.plot(temps,lowerRatioRate, color=colors[3], alpha=0.01, linewidth=1.5, linestyle="-", label = 'lowerRatioRate')
axis2.plot(temps,upper68RatioRate, color=colors[3], linewidth=1.5, linestyle="--", label = 'upper68RatioRate')
axis2.plot(temps,lower68RatioRate, color=colors[3], linewidth=1.5, linestyle="--", label = 'lower68RatioRate')
axis2.plot(temps,upper95RatioRate, color=colors[3], linewidth=1.5, linestyle="-.", label = 'upper95RatioRate')
axis2.plot(temps,lower95RatioRate, color=colors[3], linewidth=1.5, linestyle="-.", label = 'lower95RatioRate')

axis2.fill_between(temps, NsRatioRate_10down ,NsRatioRate_10up, color=colors[1],alpha=0.4)
axis2.fill_between(temps, lowerRatioRate ,upperRatioRate, color=colors[3],alpha=0.5)

#	Setting up the legend and ticks.
#....................................................................... 
axis1.legend([nonSmokerPlot,tayls16Plot,medianRatePlot,upper68RatePlot,upper95RatePlot,rmatrixPlot,rdStanPlot],[r'NON-SMOKER$^{WEB}$','Talys 1.6','Median Rate','68% limit','95% limit','R-Matrix Plot','Random Spin Set'],loc=2,frameon = False)
pyplot.xticks([.2,.3,.4,.5,1,2,3],[ r'.2', r'.3', r'.4', r'.5', r'1', r'2', r'3'])


#pyplot.show()
pyplot.savefig(savefile)










