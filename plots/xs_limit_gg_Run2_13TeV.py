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
gStyle.SetPadTopMargin(0.06)
gStyle.SetPadBottomMargin(0.14)
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
syst = False

mass_min = 1500
mass_max = 7000

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

masses = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0])
xs_obs_limits = array('d', [0.680896, 2.32953, 4.04889, 2.70984, 1.63131, 0.722975, 0.304211, 0.210821, 0.175022, 0.208804, 0.222049, 0.160221, 0.115233, 0.0943928, 0.0897623, 0.0975766, 0.104625, 0.115908, 0.123013, 0.13359, 0.145926, 0.15449, 0.164504, 0.177682, 0.188521, 0.183386, 0.171823, 0.138317, 0.0970859, 0.0596124, 0.0337915, 0.0220069, 0.016306, 0.014434, 0.0140258, 0.0149217, 0.0165609, 0.0178973, 0.0180645, 0.0178544, 0.0178232, 0.0184748, 0.0196399, 0.0203581, 0.0204475, 0.0198154, 0.0191383, 0.018142, 0.0166986, 0.0152962, 0.0139596, 0.0132503, 0.0122787, 0.0142038, 0.0140427, 0.014355])
xs_exp_limits = array('d', [1.36934, 1.186465, 1.02848, 0.846644, 0.718544, 0.5826205, 0.4870105, 0.4574365, 0.396259, 0.343479, 0.3105215, 0.2726215, 0.2406215, 0.2094135, 0.1969805, 0.1654515, 0.155856, 0.134224, 0.1171255, 0.106889, 0.0950857, 0.09192005, 0.07597055, 0.07110095, 0.06109135, 0.05340185, 0.05169885, 0.0466053, 0.04397075, 0.04178275, 0.0423906, 0.0378297, 0.0375223, 0.0340438, 0.0314429, 0.0272715, 0.02574655, 0.0242959, 0.02149465, 0.02048635, 0.0190695, 0.0179567, 0.01705655, 0.0158581, 0.01506845, 0.01450415, 0.01425475, 0.01388215, 0.01415945, 0.0140644, 0.0142503, 0.0146564, 0.0154837, 0.0140672, 0.0141344, 0.014604])

masses_exp = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0])
xs_exp_limits_1sigma = array('d', [0.569050608, 0.548935315, 0.47674635, 0.451325057, 0.401160272, 0.358784491, 0.283620088, 0.261065595, 0.224521379, 0.214688387, 0.190342142, 0.1736525, 0.143898984, 0.133325258, 0.12361176, 0.108360232, 0.0949897317, 0.090893969, 0.0762866494, 0.0717036264, 0.0621067904, 0.0570105487, 0.0498135814, 0.0472185499, 0.0383576263, 0.0351599474, 0.0314535397, 0.0307498075, 0.0297008904, 0.0278336101, 0.0279092178, 0.0259267914, 0.0255668096, 0.0251262764, 0.0219441143, 0.0195344206, 0.0174980703, 0.0165161126, 0.015421505, 0.0148845455, 0.0142676075, 0.0138017056, 0.0131424989, 0.0126011576, 0.01189881, 0.0111541504, 0.0113326772, 0.0112849821, 0.0112467786, 0.0111099766, 0.0111644504, 0.0117030662, 0.011970723, 0.011511892, 0.0118214984, 0.0120147536, 0.0201660138, 0.0191849236, 0.0194298575, 0.0213217191, 0.0201073292, 0.0205017485, 0.0186424642, 0.0201745645, 0.0198200881, 0.0202208341, 0.0206065167, 0.0229200261, 0.0232355906, 0.0242195875, 0.0260447991, 0.0284852776, 0.0301585984, 0.0318721103, 0.0343863371, 0.0373003385, 0.0434198682, 0.0442735168, 0.0507389938, 0.0542180138, 0.0545072066, 0.0639324655, 0.0639781086, 0.0692641188, 0.0753736824, 0.0814181063, 0.084853799, 0.0992977106, 0.111389211, 0.121029902, 0.143528639, 0.151350148, 0.163108287, 0.176892731, 0.214035562, 0.247644326, 0.265001272, 0.30607141, 0.364238435, 0.426429201, 0.446460683, 0.549963185, 0.61496169, 0.67439832, 0.814289032, 0.933115018, 1.06033995, 1.31692774, 1.59043822, 2.02751826, 2.80076553, 3.61359083])
xs_exp_limits_2sigma = array('d', [0.327266015, 0.295198917, 0.285281018, 0.28188633, 0.248670176, 0.238154171, 0.187361611, 0.158353904, 0.1345829, 0.142075651, 0.127096263, 0.116260564, 0.101395631, 0.0993632056, 0.0794804284, 0.0726312279, 0.060537635, 0.0649783562, 0.0571688132, 0.0485825097, 0.0439187079, 0.0424340726, 0.0351505086, 0.0321446193, 0.028996006, 0.0254366847, 0.0223320839, 0.0233480731, 0.020121411, 0.020730032, 0.0208932213, 0.0189121677, 0.017939093, 0.0180456086, 0.017607539, 0.0156699636, 0.0142017787, 0.0137335075, 0.0126674381, 0.0124533489, 0.0118813747, 0.011424812, 0.0104367963, 0.010160146, 0.00941866105, 0.0090434907, 0.00909195284, 0.00912291502, 0.00933518471, 0.00928596268, 0.00922665464, 0.00961364434, 0.0100311684, 0.00977851357, 0.0100142204, 0.0104111374, 0.0265320192, 0.026630516, 0.0261236976, 0.0288470946, 0.0303907794, 0.0283292594, 0.0276417146, 0.0280004941, 0.0268713383, 0.0285039525, 0.0275435363, 0.0314805999, 0.0315686554, 0.0344520037, 0.037053891, 0.0397396799, 0.0429884742, 0.0469136656, 0.0523720203, 0.0518632573, 0.0589102716, 0.0671958109, 0.0749018786, 0.0738175624, 0.0797559633, 0.0937397204, 0.0901896397, 0.103311938, 0.108711808, 0.116699034, 0.117725857, 0.141587573, 0.165447489, 0.169775663, 0.203548436, 0.21563157, 0.239464776, 0.28113409, 0.312025442, 0.345953053, 0.381190623, 0.43077701, 0.489627385, 0.603848336, 0.663976957, 0.783027493, 0.944173915, 1.16312001, 1.25226, 1.51980433, 1.47793306, 2.05175324, 2.51818929, 3.21715916, 4.16123123, 6.51807865])

if syst:
  masses = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0])
  xs_obs_limits = array('d', [18.0287, 15.6733, 8.6325, 3.91811, 2.1875, 1.69301, 2.13894, 2.80253, 2.79607, 2.63993, 2.65454, 2.58143, 2.36525, 1.83277, 1.27788, 1.03022, 1.11398, 1.13528, 1.05868, 0.910854, 0.720537, 0.592423, 0.492657, 0.397243, 0.311835, 0.251862, 0.207095, 0.18806, 0.184561, 0.177655, 0.169964, 0.166488, 0.155208, 0.159438, 0.162678, 0.164746, 0.166951, 0.167498, 0.164833, 0.162225, 0.156879, 0.153625, 0.146906, 0.139942, 0.13422, 0.128718, 0.125957, 0.125876, 0.124731, 0.125308, 0.132913, 0.135618, 0.13851, 0.142256, 0.145583, 0.149747])
  xs_exp_limits = array('d', [10.4422, 8.9131, 7.47655, 6.2181, 5.2968, 4.500395, 3.855925, 3.167, 2.69755, 2.292435, 1.940255, 1.683285, 1.418775, 1.24041, 1.11487, 0.9766635, 0.844834, 0.7089375, 0.625544, 0.5524985, 0.5503275, 0.4784735, 0.4144995, 0.402687, 0.3619335, 0.3407565, 0.3199655, 0.2868715, 0.260819, 0.241752, 0.219856, 0.2151445, 0.202777, 0.1877995, 0.1729915, 0.1606085, 0.1550125, 0.144495, 0.141409, 0.137229, 0.1342635, 0.131153, 0.127747, 0.12215, 0.1202925, 0.1166245, 0.117466, 0.1217755, 0.121739, 0.121855, 0.1236985, 0.125862, 0.1290245, 0.132092, 0.13631, 0.140493])

  masses_exp = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0])
  xs_exp_limits_1sigma = array('d', [6.21123476, 5.26774792, 4.36130257, 3.92517088, 3.62367304, 3.1688113, 2.71086825, 2.22266038, 1.87066821, 1.6134789, 1.35538591, 1.14366417, 0.973090906, 0.880815864, 0.780716373, 0.672944018, 0.583737785, 0.486137268, 0.436473526, 0.391914933, 0.375144287, 0.334171995, 0.295714159, 0.277061038, 0.263978496, 0.24036933, 0.218494429, 0.210549895, 0.1860362, 0.175329411, 0.164290302, 0.15017127, 0.15097111, 0.139251541, 0.129000335, 0.121852994, 0.114884839, 0.112090308, 0.107497497, 0.104425647, 0.101918181, 0.0985768604, 0.0967240176, 0.0978627275, 0.0964360191, 0.0948344489, 0.0964151674, 0.0993765189, 0.101031698, 0.104074866, 0.103545774, 0.106127594, 0.109081025, 0.112095849, 0.115649523, 0.119279916, 0.178622177, 0.173040947, 0.170098988, 0.166666883, 0.163844335, 0.161533796, 0.165038406, 0.164566366, 0.163415196, 0.162356946, 0.156588746, 0.163000724, 0.167001067, 0.172389747, 0.178661832, 0.183550924, 0.193918855, 0.198610202, 0.197859598, 0.227741346, 0.235231649, 0.248077328, 0.262762694, 0.308964994, 0.302282313, 0.322546232, 0.364378886, 0.375145427, 0.412668625, 0.469653668, 0.504513639, 0.539266796, 0.594023462, 0.588069243, 0.687031341, 0.784097076, 0.832520944, 0.923402771, 1.08663353, 1.25484349, 1.45501727, 1.65018378, 1.86366904, 2.09552459, 2.45080602, 2.89172908, 3.36528267, 3.76500412, 4.43536148, 5.56642359, 6.57651434, 7.48619724, 9.20909846, 11.7407675, 13.4752294, 18.1688591])
  xs_exp_limits_2sigma = array('d', [4.13138985, 3.21887024, 2.74955129, 2.70920042, 2.34549972, 2.0751619, 1.76364209, 1.66353852, 1.35870571, 1.19483766, 1.02480137, 0.839703034, 0.699227499, 0.656588448, 0.556879603, 0.501896998, 0.435314986, 0.368385357, 0.312124235, 0.310869604, 0.289678626, 0.255802094, 0.238445697, 0.214639598, 0.198199573, 0.184097747, 0.165507971, 0.161417087, 0.150125485, 0.132436442, 0.129053316, 0.127601918, 0.120263858, 0.10776226, 0.104534027, 0.0966922096, 0.0953319424, 0.0933798708, 0.0896073309, 0.0885899154, 0.0884077286, 0.0871315166, 0.0864900831, 0.0852969915, 0.0845176672, 0.0843281709, 0.0867340028, 0.0880801375, 0.090515376, 0.0931598802, 0.0934007325, 0.0962620894, 0.0990598081, 0.101685524, 0.104850065, 0.108589081, 0.247903628, 0.24249601, 0.237021659, 0.233242629, 0.22865918, 0.228457345, 0.232357986, 0.228886816, 0.231171531, 0.224348404, 0.215377259, 0.230353995, 0.237969484, 0.24534997, 0.248604114, 0.256775158, 0.259767017, 0.268449538, 0.278327136, 0.318409261, 0.316953385, 0.358192821, 0.370259557, 0.427721484, 0.453463059, 0.454163746, 0.49550195, 0.518073945, 0.614585016, 0.655984169, 0.692087759, 0.727687211, 0.80751574, 0.808281262, 0.939624131, 1.03679852, 1.19514181, 1.32925097, 1.4809772, 1.75900633, 1.94401271, 2.19141083, 2.7067759, 2.81269465, 3.17864731, 3.93668574, 4.45634077, 4.99311173, 6.16222264, 8.22243635, 9.26108307, 10.6994382, 13.016748, 17.0977239, 21.9691376, 24.3170575])

##
########################################################

massesS8 = array('d', [1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0])
xsS8 = array('d', [5.15E+02,2.93E+02,1.73E+02,1.11E+02,6.68E+01,4.29E+01,2.86E+01,1.90E+01,1.30E+01,8.71E+00,6.07E+00,4.32E+00,2.99E+00,2.14E+00,1.53E+00,1.09E+00,8.10E-01,5.83E-01,4.38E-01,3.25E-01,2.43E-01,1.78E-01,1.37E-01,1.03E-01,7.66E-02,5.76E-02,4.46E-02,3.42E-02,2.60E-02,1.94E-02,1.50E-02,1.20E-02,9.12E-03,6.99E-03,5.47E-03,4.19E-03,3.21E-03,2.53E-03,1.90E-03,1.50E-03,1.18E-03,9.13E-04,7.07E-04,5.60E-04,4.35E-04,3.36E-04,2.59E-04,2.09E-04,1.59E-04,1.21E-04,9.38E-05])

xs_max = 2.5e+01
idx = 0

for i, xs in enumerate(xsS8):
  if xs < xs_max:
    idx = i
    break

graph_xsS8 = TGraph(len(massesS8[idx:-1]),massesS8[idx:-1],xsS8[idx:-1])
graph_xsS8.SetLineWidth(3)
graph_xsS8.SetLineStyle(8)
graph_xsS8.SetLineColor(6)

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.GetXaxis().SetTitle("gg resonance mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma #times #it{B} #times #it{A} [pb]")
graph_exp_2sigma.GetYaxis().SetTitleOffset(1.1)
graph_exp_2sigma.GetYaxis().SetRangeUser(3e-03,1e+02)
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
graph_obs.SetLineWidth(3)
#graph_obs.SetLineStyle(1)
graph_obs.SetLineColor(1)


c = TCanvas("c", "",800,800)
c.cd()

graph_exp_2sigma.Draw("AF")
graph_exp_1sigma.Draw("F")
graph_exp.Draw("L")
graph_obs.Draw("LP")
graph_xsS8.Draw("L")

legend = TLegend(.55,.50,.90,.70)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.035)
legend.SetHeader('95% CL upper limits')
legend.AddEntry(graph_obs,"Observed","lp")
legend.AddEntry(graph_exp,"Expected","lp")
legend.AddEntry(graph_exp_1sigma,"#pm 1#sigma","F")
legend.AddEntry(graph_exp_2sigma,"#pm 2#sigma","F")
legend.Draw()

legendTh = TLegend(.55,.80,.90,.84)
legendTh.SetBorderSize(0)
legendTh.SetFillColor(0)
legendTh.SetFillStyle(0)
legendTh.SetTextFont(42)
legendTh.SetTextSize(0.035)
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
CMS_lumi.lumi_sqrtS = "974 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.15
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis()

c.SetLogy()
c.SaveAs('xs_limit_DijetLimitCode_gg' + ('_NoSyst' if not syst else '') + '_Run2_13TeV_DATA_974_invpb.eps')
