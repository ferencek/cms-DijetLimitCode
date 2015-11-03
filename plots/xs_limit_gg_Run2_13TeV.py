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
#syst = False

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
xs_obs_limits = array('d', [0.774406, 0.986218, 1.75866, 1.14641, 0.919007, 0.737969, 0.392757, 0.279419, 0.189352, 0.168139, 0.168823, 0.139586, 0.112821, 0.0966805, 0.0797317, 0.0730251, 0.0777934, 0.0925955, 0.0952212, 0.0900524, 0.0882402, 0.0900611, 0.0943155, 0.0976048, 0.100283, 0.0990596, 0.0922381, 0.0766865, 0.0552401, 0.0354419, 0.0256382, 0.0186629, 0.0145845, 0.0123074, 0.0112314, 0.0114168, 0.012173, 0.0127663, 0.0128261, 0.01233, 0.0118628, 0.0118075, 0.0121371, 0.01201, 0.0119846, 0.0117518, 0.0116898, 0.0114021, 0.0109518, 0.0103538, 0.00979565, 0.00930067, 0.00910024, 0.00945993, 0.00994439, 0.0105076])
xs_exp_limits = array('d', [1.135775, 0.8386765, 0.7627025, 0.6236365, 0.51727, 0.419236, 0.3993075, 0.3559885, 0.284311, 0.24024, 0.2280625, 0.1981365, 0.188856, 0.1642985, 0.152, 0.1254045, 0.1073285, 0.0990953, 0.0897164, 0.0791696, 0.0707024, 0.0635862, 0.0573578, 0.05032625, 0.04748195, 0.0424117, 0.03836, 0.0344605, 0.03161445, 0.02992775, 0.0272681, 0.0264569, 0.02613395, 0.024436, 0.0216682, 0.0210522, 0.0186031, 0.0181665, 0.0161242, 0.01440485, 0.01365405, 0.013109, 0.012854, 0.01212855, 0.010987, 0.009940435, 0.00973575, 0.00959334, 0.00972272, 0.009528715, 0.0094567, 0.00973143, 0.00959768, 0.009403555, 0.009493375, 0.009247495])

masses_exp = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0])
xs_exp_limits_1sigma = array('d', [0.464414728, 0.402541441, 0.375016009, 0.327198469, 0.299538912, 0.254727911, 0.225210637, 0.196159416, 0.16364538, 0.136830645, 0.139297504, 0.122819524, 0.115149546, 0.103313699, 0.0914524073, 0.0788361835, 0.0701621514, 0.0614813822, 0.0553636938, 0.0518491897, 0.0474456576, 0.0416284307, 0.0365145282, 0.0328329618, 0.0301622299, 0.0277540679, 0.0264419491, 0.0227258767, 0.0217140278, 0.0198371168, 0.0193182382, 0.01768646, 0.0178167349, 0.0163910119, 0.0145637995, 0.0139684523, 0.0128938364, 0.0126658508, 0.0113093651, 0.0108666156, 0.00969838355, 0.00935218465, 0.00905677475, 0.00840763859, 0.00798584756, 0.0078135435, 0.00749576603, 0.00751411143, 0.00738299827, 0.00722378507, 0.00736137237, 0.00733511469, 0.00741154107, 0.00735959292, 0.00748431964, 0.00751857641, 0.0130960433, 0.0146126132, 0.0135709432, 0.0136084552, 0.0142172099, 0.0144883921, 0.0139552567, 0.0136770352, 0.0137236453, 0.0142496246, 0.0142382188, 0.015696577, 0.0166347314, 0.0181713485, 0.0184536258, 0.0205465453, 0.0219712795, 0.0230231303, 0.0274832453, 0.0280216785, 0.0296997605, 0.0322942527, 0.0345115353, 0.0405471104, 0.0407107756, 0.0434485514, 0.045036077, 0.0505783909, 0.053509418, 0.0593379719, 0.0652839036, 0.0718149083, 0.0781309566, 0.09115154, 0.0969017776, 0.110345668, 0.129930899, 0.146250554, 0.160935013, 0.179918345, 0.191598028, 0.236679191, 0.265100093, 0.306772209, 0.344658339, 0.38593476, 0.432571275, 0.529936387, 0.606036842, 0.693655791, 0.836583159, 0.898056011, 1.19964432, 1.47965627, 1.93273453, 2.92027235])
xs_exp_limits_2sigma = array('d', [0.236215683, 0.229761196, 0.22672439, 0.214717193, 0.188859174, 0.163793428, 0.141622067, 0.127397701, 0.108980444, 0.0947379612, 0.0942755456, 0.0823872503, 0.0694469318, 0.0680394748, 0.0601460802, 0.0558078423, 0.0483144495, 0.0433223144, 0.0393819016, 0.0340634363, 0.0337815548, 0.0290718491, 0.0249910034, 0.0242319685, 0.0226487117, 0.0196489911, 0.0181905795, 0.016091039, 0.0151068859, 0.0147163619, 0.0146165038, 0.0132548031, 0.0125961108, 0.0117737399, 0.0116072955, 0.0105309512, 0.00896710446, 0.00918711368, 0.00851744707, 0.00818888335, 0.00799085592, 0.00763466277, 0.0072686012, 0.00719143859, 0.0064071679, 0.00664561681, 0.00640225508, 0.00615149239, 0.00589629471, 0.00587431482, 0.00621374162, 0.00608467911, 0.00595022064, 0.0057902385, 0.00642037836, 0.00642052485, 0.0191567348, 0.0188298687, 0.0194591855, 0.0186587068, 0.0212685131, 0.0202826475, 0.0198653257, 0.0189719638, 0.0190608164, 0.0188533391, 0.0195427145, 0.0215819507, 0.0225411655, 0.024602872, 0.0263120422, 0.0273107633, 0.0298801943, 0.0337559915, 0.0354187098, 0.0399195304, 0.0410829052, 0.0444920938, 0.0481263581, 0.0526463785, 0.0551641105, 0.0618380915, 0.0660708747, 0.0768814085, 0.0779338788, 0.0885582776, 0.094914248, 0.102109616, 0.10912541, 0.131516794, 0.14149284, 0.168660742, 0.170135015, 0.205664215, 0.219881045, 0.256570028, 0.300768148, 0.350844872, 0.386351233, 0.480558114, 0.536907746, 0.591362705, 0.686271782, 0.825270312, 0.970931368, 1.08394561, 1.27151336, 1.62031636, 1.91298503, 2.37309118, 3.30988656, 3.97130462])

if syst:
  masses = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0])
  xs_obs_limits = array('d', [1.96856, 2.43822, 2.76583, 2.04621, 1.46395, 1.12298, 0.726003, 0.487341, 0.338475, 0.292971, 0.269578, 0.239681, 0.202668, 0.169284, 0.139073, 0.128541, 0.121525, 0.132959, 0.130894, 0.124102, 0.120602, 0.11783, 0.116425, 0.116592, 0.115549, 0.110867, 0.10454, 0.0942745, 0.0782696, 0.0566834, 0.0380103, 0.0260337, 0.0189558, 0.0150787, 0.0133684, 0.0128971, 0.0130313, 0.0131463, 0.0130563, 0.012868, 0.0125073, 0.0124197, 0.0125219, 0.012125, 0.0121815, 0.0119257, 0.0119576, 0.0117623, 0.0114172, 0.0108835, 0.0104712, 0.00997223, 0.00965398, 0.00993409, 0.0101813, 0.0105714])
  xs_exp_limits = array('d', [2.67522, 2.19755, 1.82921, 1.39324, 1.052685, 0.825972, 0.67222, 0.5580595, 0.485295, 0.414629, 0.3724995, 0.320681, 0.2813525, 0.2604625, 0.223714, 0.1877485, 0.1655965, 0.1459175, 0.1230215, 0.114149, 0.1020235, 0.09069065, 0.082192, 0.0730009, 0.06256325, 0.0540863, 0.04947105, 0.0445009, 0.0404743, 0.0381551, 0.0349583, 0.0320151, 0.0287547, 0.02631, 0.02377695, 0.0221527, 0.0209546, 0.0186064, 0.01734865, 0.01645255, 0.0146564, 0.0141953, 0.01339455, 0.0122686, 0.01170885, 0.0109162, 0.0104373, 0.0103499, 0.01008445, 0.01021665, 0.0102788, 0.00998176, 0.009929745, 0.00994015, 0.0100449, 0.009597815])

  masses_exp = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0])
  xs_exp_limits_1sigma = array('d', [1.07201312, 1.08719513, 1.05248198, 0.834065279, 0.691127858, 0.531985306, 0.433610938, 0.370410232, 0.315600826, 0.283652947, 0.241739922, 0.214784845, 0.201225323, 0.174648649, 0.157083755, 0.139232261, 0.122344449, 0.103825399, 0.0930486325, 0.0829739357, 0.0694770768, 0.0655549536, 0.0553736814, 0.05065505, 0.0448847864, 0.0379434578, 0.0344611915, 0.0302602602, 0.027670956, 0.02661256, 0.0239503866, 0.021905424, 0.0206880441, 0.018896005, 0.0175439734, 0.0159282432, 0.0147729228, 0.0132091722, 0.0124999547, 0.0118302038, 0.0109070502, 0.0101000732, 0.00951027721, 0.00909984213, 0.00853298033, 0.00795007624, 0.00779069406, 0.00763883927, 0.0076071425, 0.00756272622, 0.00774491661, 0.00777012544, 0.0079133207, 0.0075171157, 0.00761048388, 0.0075369317, 0.0134980341, 0.0140488748, 0.013952496, 0.0141447961, 0.014869186, 0.0148224661, 0.0145316746, 0.0148844341, 0.0155311905, 0.0158981802, 0.0165546582, 0.0172103103, 0.0186255461, 0.0192174104, 0.0205203032, 0.0217692874, 0.0241080199, 0.0259388816, 0.0284868372, 0.0295753544, 0.0322893384, 0.0363142366, 0.039471016, 0.0406775016, 0.0468536404, 0.04997596, 0.0559823594, 0.0577035098, 0.0647627972, 0.0719171374, 0.0809174612, 0.0893341969, 0.103561422, 0.114762248, 0.127928185, 0.144791511, 0.169488334, 0.186838688, 0.220974894, 0.240098972, 0.273267325, 0.327222151, 0.38258364, 0.419181091, 0.481391931, 0.549479364, 0.622810723, 0.692031928, 0.842227535, 0.986825913, 1.2456825, 1.54560863, 2.08121788, 2.80990347, 3.76365714, 4.91862158])
  xs_exp_limits_2sigma = array('d', [0.589695698, 0.655743652, 0.628241151, 0.537769475, 0.454548025, 0.350905181, 0.307671727, 0.262897006, 0.23399669, 0.199379662, 0.168088895, 0.150048464, 0.141434262, 0.129306819, 0.114084653, 0.0995558094, 0.0871603979, 0.0762839311, 0.0705735059, 0.0559718529, 0.0547636829, 0.0461803473, 0.0425468626, 0.0373210949, 0.031165793, 0.0282037309, 0.0252042573, 0.0218942568, 0.0200060166, 0.018765164, 0.0184829894, 0.0166108677, 0.0148532425, 0.0139244197, 0.0124747541, 0.011517601, 0.0112590572, 0.00991631962, 0.00969775306, 0.00973110508, 0.00887372138, 0.00827161708, 0.00752794236, 0.00727467541, 0.00692951303, 0.00640452012, 0.00636803336, 0.00601427438, 0.00591545513, 0.00603815722, 0.005960942, 0.0059571166, 0.00581198855, 0.0059990937, 0.0060190636, 0.00628591439, 0.0196332716, 0.0199003842, 0.019382447, 0.0192122683, 0.020548208, 0.0202452272, 0.0210012428, 0.0209354892, 0.0224225237, 0.0247699996, 0.0254279068, 0.0249722372, 0.027257437, 0.0287069726, 0.0292534292, 0.0305221874, 0.0340665411, 0.0357128688, 0.0377122202, 0.041532597, 0.0448033598, 0.0529550505, 0.0600616506, 0.0616092292, 0.0700114618, 0.0650206306, 0.075391559, 0.0873569498, 0.0911474392, 0.1003411686, 0.112741889, 0.129046839, 0.138369705, 0.172206681, 0.18843674, 0.191190553, 0.230028525, 0.255356806, 0.287716212, 0.331221251, 0.370530806, 0.453348718, 0.502356898, 0.571777652, 0.6387958, 0.755486349, 0.864371351, 1.00043786, 1.22756601, 1.35955321, 1.73122819, 2.15009558, 2.93206243, 3.80237853, 5.1609406, 6.8508778])

##
########################################################

massesS8 = array('d', [1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0])
xsS8 = array('d', [5.15E+02,2.93E+02,1.73E+02,1.11E+02,6.68E+01,4.29E+01,2.86E+01,1.90E+01,1.30E+01,8.71E+00,6.07E+00,4.32E+00,2.99E+00,2.14E+00,1.53E+00,1.09E+00,8.10E-01,5.83E-01,4.38E-01,3.25E-01,2.43E-01,1.78E-01,1.37E-01,1.03E-01,7.66E-02,5.76E-02,4.46E-02,3.42E-02,2.60E-02,1.94E-02,1.50E-02,1.20E-02,9.12E-03,6.99E-03,5.47E-03,4.19E-03,3.21E-03,2.53E-03,1.90E-03,1.50E-03,1.18E-03,9.13E-04,7.07E-04,5.60E-04,4.35E-04,3.36E-04,2.59E-04,2.09E-04,1.59E-04,1.21E-04,9.38E-05])

xs_max = 2e+01
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
graph_exp_2sigma.GetYaxis().SetRangeUser(1e-03,1e+02)
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
CMS_lumi.lumi_sqrtS = "1769 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.15
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis()

c.SetLogy()
c.SaveAs('xs_limit_DijetLimitCode_gg' + ('_NoSyst' if not syst else '') + '_Run2_13TeV_DATA_1769_invpb.eps')
