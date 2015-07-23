#!/usr/bin/env python

import sys, os, subprocess, string, re
from ROOT import *
from array import array
import CMS_lumi


gROOT.SetBatch(kTRUE);
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetCanvasBorderMode(0)
gStyle.SetFrameBorderMode(0)
gStyle.SetCanvasColor(kWhite)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadRightMargin(0.05)
gStyle.SetPadTopMargin(0.05)
gStyle.SetPadBottomMargin(0.15)
gROOT.ForceStyle()

masses = array('d')
xs_obs_limits = array('d')
xs_exp_limits = array('d')
masses_exp = array('d')
xs_exp_limits_1sigma = array('d')
xs_exp_limits_1sigma_up = array('d')
xs_exp_limits_2sigma = array('d')
xs_exp_limits_2sigma_up = array('d')


syst = True
#syst = False

mass_min = 1300
mass_max = 5500

########################################################
## Uncomment this part if running the limit code


### for running the limit code
#for mass in range(mass_min,mass_max+100,100):

  #masses.append(float(mass))
  #masses_exp.append(float(mass))

  #cmd = "./stats " + str(int(mass)) + " gg | tee stats_" + str(int(mass)) + "_gg.log"
  #print "Running: " + cmd
  #proc = subprocess.Popen( cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
  #output = proc.communicate()[0]
  #if proc.returncode != 0:
    #print output
    #sys.exit(1)
  ##print output

  #outputlines = output.split("\n")

  #for line in outputlines:
    #if re.search("observed bound =", line):
      #xs_obs_limits.append(float(line.split()[6]))
    #if re.search("median:", line):
      #xs_exp_limits.append(float(line.split()[1]))
    #if re.search("1 sigma band:", line):
      #xs_exp_limits_1sigma.append(float(line.split()[4]))
      #xs_exp_limits_1sigma_up.append(float(line.split()[6]))
    #if re.search("2 sigma band:", line):
      #xs_exp_limits_2sigma.append(float(line.split()[4]))
      #xs_exp_limits_2sigma_up.append(float(line.split()[6]))

##------------------------------------------------------

### for reading the limit code log files
#for mass in range(mass_min,mass_max+100,100):

  #masses.append(float(mass))
  #masses_exp.append(float(mass))

  #log_file = open("stats_" + str(int(mass)) + "_gg.log",'r')
  #outputlines = log_file.readlines()
  #log_file.close()

  #for line in outputlines:
    #if re.search("observed bound =", line):
      #xs_obs_limits.append(float(line.split()[6]))
    #if re.search("median:", line):
      #xs_exp_limits.append(float(line.split()[1]))
    #if re.search("1 sigma band:", line):
      #xs_exp_limits_1sigma.append(float(line.split()[4]))
      #xs_exp_limits_1sigma_up.append(float(line.split()[6]))
    #if re.search("2 sigma band:", line):
      #xs_exp_limits_2sigma.append(float(line.split()[4]))
      #xs_exp_limits_2sigma_up.append(float(line.split()[6]))

##------------------------------------------------------

#for i in range(0,len(masses)):
  #masses_exp.append( masses[len(masses)-i-1] )
  #xs_exp_limits_1sigma.append( xs_exp_limits_1sigma_up[len(masses)-i-1] )
  #xs_exp_limits_2sigma.append( xs_exp_limits_2sigma_up[len(masses)-i-1] )


#print "masses =", masses
#print "xs_obs_limits =", xs_obs_limits
#print "xs_exp_limits =", xs_exp_limits
#print ""
#print "masses_exp =", masses_exp
#print "xs_exp_limits_1sigma =", xs_exp_limits_1sigma
#print "xs_exp_limits_2sigma =", xs_exp_limits_2sigma

##
########################################################

########################################################
## Comment out this part if running the limit code

masses = array('d', [1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0])
xs_obs_limits = array('d', [5.90412, 24.8042, 18.3176, 7.17719, 4.19916, 1.98404, 1.19833, 1.46079, 1.71165, 1.33612, 1.17315, 1.14401, 1.44153, 1.62837, 1.36941, 1.34004, 1.42824, 1.44795, 1.35705, 1.10115, 0.828976, 0.660172, 0.458337, 0.385381, 0.355388, 0.332631, 0.310094, 0.302969, 0.293327, 0.274843, 0.254422, 0.234144, 0.222194, 0.228776, 0.234352, 0.238696, 0.237315, 0.233928, 0.230453, 0.230717, 0.223965, 0.216521, 0.210162])
xs_exp_limits = array('d', [9.79282, 7.62507, 6.703235, 5.51467, 4.74207, 3.671345, 3.194125, 2.82396, 2.235, 2.025325, 1.747005, 1.608285, 1.37957, 1.14505, 1.008255, 0.8711925, 0.8048135, 0.7139645, 0.6407455, 0.58749, 0.5356085, 0.507517, 0.474179, 0.4520175, 0.4212405, 0.400004, 0.3629105, 0.3306745, 0.2973345, 0.2781095, 0.263274, 0.2599575, 0.2412745, 0.222197, 0.2122655, 0.2033305, 0.188874, 0.186582, 0.18188, 0.171405, 0.1658715, 0.169089, 0.1615145])

masses_exp = array('d', [1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0])
xs_exp_limits_1sigma = array('d', [4.25269701, 3.5814807, 3.12437044, 2.87295598, 2.524546, 2.25136398, 1.94684076, 1.75983907, 1.45069696, 1.37914387, 1.18551872, 1.06788417, 0.919481943, 0.778911719, 0.655908731, 0.616409289, 0.545025364, 0.504277479, 0.458636845, 0.430695501, 0.405511081, 0.369503799, 0.343968719, 0.325385351, 0.296381838, 0.27495425, 0.255083737, 0.246075969, 0.229335582, 0.220690087, 0.21055097, 0.202712537, 0.193381576, 0.1849071, 0.161190497, 0.156253169, 0.150726081, 0.151102573, 0.148482896, 0.142830458, 0.141133437, 0.1414601, 0.139885441, 0.214788948, 0.222304556, 0.22769444, 0.22653568, 0.245063735, 0.25124408, 0.258628903, 0.269333267, 0.283539933, 0.323472124, 0.346914222, 0.366784086, 0.385603267, 0.401571736, 0.432047538, 0.476397509, 0.513771899, 0.562343783, 0.617472894, 0.69430656, 0.739033163, 0.780014976, 0.848377924, 0.93703286, 0.954776487, 1.06456712, 1.21852308, 1.42441245, 1.61429439, 1.91318415, 2.10268397, 2.52811108, 3.02916001, 3.26131476, 3.84564242, 4.81602732, 5.49044447, 6.43498751, 8.67315715, 10.7377752, 13.4014049, 15.7384751, 21.7225561])
xs_exp_limits_2sigma = array('d', [2.5722479, 2.2851025, 1.95863055, 1.68005806, 1.54218572, 1.4140722, 1.30817114, 1.13901616, 0.976131144, 0.960673715, 0.91121753, 0.777026061, 0.608712259, 0.543462454, 0.49370271, 0.47831404, 0.435547004, 0.414351898, 0.396581195, 0.348773331, 0.328403935, 0.305661154, 0.277716293, 0.261595371, 0.246864899, 0.239033684, 0.219345929, 0.210573487, 0.183215142, 0.171339318, 0.171534889, 0.155856939, 0.153927138, 0.15140098, 0.142513697, 0.13759286, 0.134954175, 0.13348332, 0.131868257, 0.130153194, 0.131165257, 0.130454527, 0.129498781, 0.287066032, 0.29774787, 0.314671997, 0.306965212, 0.328498813, 0.343953141, 0.353773202, 0.361704286, 0.376417367, 0.452584538, 0.469860758, 0.508702085, 0.521346451, 0.570153744, 0.613432555, 0.666742248, 0.72248531, 0.808388934, 0.87628648, 0.948912422, 1.02316046, 1.14984979, 1.22707052, 1.25639907, 1.43007469, 1.68651432, 1.77035394, 2.19060321, 2.63146467, 2.9343295, 3.27797507, 3.81838354, 4.25540585, 4.82752339, 5.78027958, 6.97663754, 8.68026272, 10.6078858, 13.0445512, 15.7489113, 18.9823185, 24.5480007, 34.1899871])

if syst:
  masses = array('d', [1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0])
  xs_obs_limits = array('d', [6.5388, 25.3099, 21.3927, 9.40168, 4.96007, 2.29408, 1.38732, 1.50147, 1.68523, 1.40833, 1.24679, 1.21808, 1.42811, 1.59275, 1.44016, 1.42188, 1.47216, 1.4937, 1.43758, 1.26953, 1.06583, 0.906498, 0.659773, 0.504959, 0.436788, 0.379415, 0.337783, 0.318595, 0.302804, 0.287377, 0.268775, 0.244895, 0.232776, 0.241318, 0.239077, 0.238428, 0.23798, 0.235695, 0.233228, 0.232629, 0.226054, 0.222463, 0.216499])
  xs_exp_limits = array('d', [10.0367, 7.655415, 6.584175, 5.5488, 4.62124, 4.14456, 3.76115, 3.07871, 2.65414, 2.317055, 2.047445, 1.795945, 1.57297, 1.33652, 1.14401, 1.00681, 0.938574, 0.8439625, 0.727921, 0.683078, 0.617896, 0.5927655, 0.546331, 0.511499, 0.4521155, 0.4194385, 0.3840845, 0.3620595, 0.322148, 0.3009535, 0.2935945, 0.2854585, 0.273496, 0.2426835, 0.220393, 0.213165, 0.199981, 0.194173, 0.189593, 0.1799155, 0.174718, 0.172585, 0.164677])

  masses_exp = array('d', [1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0])
  xs_exp_limits_1sigma = array('d', [5.00694924, 3.69544881, 3.36520391, 3.06477088, 2.60730294, 2.45077444, 2.22643462, 1.92165832, 1.70419968, 1.5256961, 1.32510548, 1.16700595, 1.04371948, 0.857683948, 0.760721308, 0.700839992, 0.623124684, 0.605864663, 0.540834402, 0.494476778, 0.457070137, 0.407260297, 0.390568961, 0.363424486, 0.333222171, 0.304065655, 0.282319439, 0.269429114, 0.245884904, 0.233522348, 0.221294027, 0.213882609, 0.207042758, 0.187732261, 0.166617816, 0.163322872, 0.158007969, 0.15496617, 0.151804963, 0.146959174, 0.143744926, 0.144222945, 0.141113813, 0.218529834, 0.226339109, 0.240077182, 0.245245202, 0.259811091, 0.270414612, 0.280118132, 0.294368724, 0.311511448, 0.33919149, 0.3783383, 0.404890193, 0.416130745, 0.422772566, 0.45456063, 0.510637218, 0.541158074, 0.594206855, 0.652433755, 0.773730442, 0.780183167, 0.850731717, 0.947092726, 1.00264412, 1.07141514, 1.22008592, 1.4092104, 1.58760984, 1.83987232, 2.10447726, 2.38191602, 2.91680625, 3.27501796, 3.73505286, 4.22755648, 5.02740885, 5.85121618, 6.85456188, 9.1299558, 10.7618088, 13.2240972, 15.218662, 19.9517756])
  xs_exp_limits_2sigma = array('d', [2.98869941, 2.5247419, 2.2350229, 1.88388024, 1.77369824, 1.595637, 1.497473, 1.34306436, 1.220122, 1.03785578, 0.898167293, 0.867067565, 0.713178576, 0.602401562, 0.544852444, 0.509533032, 0.472183924, 0.441762896, 0.420956127, 0.379053628, 0.369621233, 0.338672517, 0.322098868, 0.288520962, 0.268057913, 0.248870815, 0.233230343, 0.22217494, 0.189642302, 0.182107124, 0.176629553, 0.16315061, 0.160255962, 0.150677297, 0.142521556, 0.139115798, 0.1374949, 0.133595188, 0.133826982, 0.131541732, 0.131691623, 0.129393856, 0.12825799, 0.301250733, 0.314797001, 0.337061795, 0.334089845, 0.353311585, 0.364530621, 0.384834561, 0.38959623, 0.439910716, 0.477982365, 0.567150067, 0.601072105, 0.576770517, 0.628173094, 0.663930452, 0.740854198, 0.802932519, 0.86640174, 0.929986665, 1.05396016, 1.06295319, 1.25658882, 1.44540071, 1.3856858, 1.52291287, 1.71445802, 2.05304602, 2.29123416, 2.7300816, 3.40691982, 3.46011142, 4.33784829, 4.89352042, 5.53895713, 6.47243132, 7.33632668, 8.68559658, 10.2299192, 13.5078942, 16.5231688, 19.8060837, 23.7110938, 32.3846684])

##
########################################################

massesS8 = array('d', [1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0])
xsS8 = array('d', [5.46E+02,3.12E+02,1.85E+02,1.12E+02,7.19E+01,4.59E+01,3.02E+01,2.01E+01,1.37E+01,9.46E+00,6.55E+00,4.64E+00,3.27E+00,2.36E+00,1.70E+00,1.24E+00,9.11E-01,6.69E-01,4.97E-01,3.71E-01,2.78E-01,2.07E-01,1.55E-01,1.19E-01,9.26E-02,7.08E-02,5.43E-02,4.15E-02,3.22E-02,2.50E-02,1.92E-02,1.51E-02,1.19E-02,9.25E-03,7.35E-03,5.86E-03,4.53E-03,3.66E-03,2.91E-03,2.33E-03,1.86E-03,1.45E-03,1.12E-03,8.75E-04,6.90E-04,5.55E-04,4.47E-04,3.63E-04,2.92E-04,2.37E-04,1.97E-04])

graph_xsS8 = TGraph(len(massesS8),massesS8,xsS8)
graph_xsS8.SetLineWidth(3)
graph_xsS8.SetLineStyle(8)
graph_xsS8.SetLineColor(6)

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.GetXaxis().SetTitle("gg resonance mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_exp_2sigma.GetYaxis().SetRangeUser(1e-02,1e+03)
#graph_exp_2sigma.GetXaxis().SetNdivisions(1005)

graph_exp_1sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_1sigma)
graph_exp_1sigma.SetFillColor(kGreen+1)

graph_exp = TGraph(len(masses),masses,xs_exp_limits)
#graph_exp.SetMarkerStyle(24)
graph_exp.SetLineWidth(3)
graph_exp.SetLineStyle(2)
graph_exp.SetLineColor(4)

graph_obs = TGraph(len(masses),masses,xs_obs_limits)
graph_obs.SetMarkerStyle(20)
graph_obs.SetLineWidth(2)
#graph_obs.SetLineStyle(1)
graph_obs.SetLineColor(1)


c = TCanvas("c", "",800,800)
c.cd()

graph_exp_2sigma.Draw("AF")
graph_exp_1sigma.Draw("F")
graph_exp.Draw("L")
graph_obs.Draw("LP")
graph_xsS8.Draw("L")

legend = TLegend(.50,.55,.80,.73)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader('95% CL upper limits' + ('' if syst else ' (stat. only)'))
legend.AddEntry(graph_obs,"Observed (pseudo-data)","lp")
legend.AddEntry(graph_exp,"Expected","lp")
legend.AddEntry(graph_exp_1sigma,"#pm 1#sigma","F")
legend.AddEntry(graph_exp_2sigma,"#pm 2#sigma","F")
legend.Draw()

legendTh = TLegend(.50,.80,.80,.84)
legendTh.SetBorderSize(0)
legendTh.SetFillColor(0)
legendTh.SetFillStyle(0)
legendTh.SetTextFont(42)
legendTh.SetTextSize(0.03)
legendTh.AddEntry(graph_xsS8,"S8","l")
legendTh.Draw()

#l1 = TLatex()
#l1.SetTextAlign(12)
#l1.SetTextFont(42)
#l1.SetNDC()
#l1.SetTextSize(0.04)
#l1.SetTextSize(0.04)
#l1.DrawLatex(0.18,0.40, "CMS Preliminary")
#l1.DrawLatex(0.18,0.32, "#intLdt = 1 fb^{-1}")
#l1.DrawLatex(0.19,0.27, "#sqrt{s} = 13 TeV")

#draw the lumi text on the canvas
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "37 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis()

c.SetLogy()
c.SaveAs('xs_limit_DijetLimitCode_gg' + ('_NoSyst' if not syst else '') + '_Run2_13TeV_DATA_37_invpb.eps')
