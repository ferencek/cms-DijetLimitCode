#!/usr/bin/env python

import sys, os, subprocess, string, re
from ROOT import *
from array import array
import numpy as np
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

useTeV = True
#useTeV = False

masses = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7100.0, 7200.0])

xs_gg_obs_limits = array('d', [0.836478, 0.774447, 1.23998, 0.959869, 0.526238, 0.310743, 0.219122, 0.14414, 0.117179, 0.131122, 0.127128, 0.0906086, 0.104278, 0.117512, 0.122472, 0.120322, 0.121221, 0.113741, 0.102283, 0.0975416, 0.0961606, 0.0925603, 0.0792465, 0.0676229, 0.0701066, 0.0671454, 0.0527954, 0.0336437, 0.0224766, 0.0150056, 0.0121905, 0.0103843, 0.00921951, 0.00866013, 0.00924763, 0.0110804, 0.0127599, 0.0139334, 0.0141779, 0.013463, 0.0126392, 0.0119217, 0.0112133, 0.010475, 0.00967835, 0.00879789, 0.00802754, 0.00750105, 0.00693862, 0.00675818, 0.00620987, 0.00612767, 0.00588462, 0.00575895, 0.00572472, 0.00575174, 0.00590138, 0.00613816])
xs_gg_exp_limits = array('d', [0.807865, 0.749822, 0.636492, 0.501165, 0.442055, 0.373683, 0.308796, 0.274763, 0.2461, 0.21873, 0.197548, 0.159459, 0.144599, 0.12325, 0.112418, 0.101445, 0.092047, 0.0772591, 0.0728687, 0.0636055, 0.0546508, 0.0506898, 0.0467854, 0.0444067, 0.0383595, 0.0337996, 0.0299116, 0.0287613, 0.0256873, 0.0245892, 0.0222354, 0.0203452, 0.0190944, 0.0182157, 0.015392, 0.0142076, 0.0136367, 0.0126589, 0.012195, 0.0112466, 0.0102815, 0.00954721, 0.00920796, 0.00848258, 0.00804014, 0.00762756, 0.0071216, 0.00727543, 0.00694033, 0.00698688, 0.00702847, 0.0068209, 0.00682605, 0.00684432, 0.00685966, 0.00686981, 0.00704506, 0.00730533])

xs_qg_obs_limits = array('d', [0.602272, 0.64491, 0.865673, 0.616196, 0.343269, 0.212624, 0.140649, 0.103605, 0.0918694, 0.101727, 0.0892428, 0.0678928, 0.0825205, 0.0915746, 0.0943468, 0.0911699, 0.0866712, 0.0832746, 0.0744257, 0.0706772, 0.0713686, 0.065973, 0.0549593, 0.0506374, 0.0501734, 0.0443592, 0.0335244, 0.0213411, 0.0135937, 0.0100408, 0.00828029, 0.00734691, 0.00693662, 0.00679592, 0.00720566, 0.00848763, 0.00966361, 0.0100682, 0.0101104, 0.00961391, 0.00901056, 0.00843457, 0.00787787, 0.007268, 0.0068383, 0.0062159, 0.00564396, 0.00512824, 0.00467353, 0.00421974, 0.00397535, 0.00369705, 0.00362929, 0.00343399, 0.00331401, 0.00323391, 0.00324306, 0.00327224])
xs_qg_exp_limits = array('d', [0.604644, 0.474845, 0.431861, 0.371758, 0.309556, 0.251925, 0.210053, 0.196129, 0.167196, 0.158303, 0.131379, 0.108406, 0.100809, 0.0946049, 0.0795457, 0.0718638, 0.0629254, 0.0589563, 0.0533615, 0.047158, 0.0424394, 0.0381913, 0.0333004, 0.0309208, 0.0274924, 0.024903, 0.0237022, 0.0209057, 0.0194533, 0.0179081, 0.0165851, 0.0141789, 0.0139069, 0.0127362, 0.0119621, 0.0104715, 0.00996637, 0.00912483, 0.00839968, 0.0077472, 0.00685672, 0.00680356, 0.00636493, 0.0060644, 0.00583616, 0.00540399, 0.00510707, 0.00492442, 0.0046922, 0.00473624, 0.00445597, 0.00434573, 0.00420864, 0.00409594, 0.00399577, 0.00389151, 0.00387871, 0.00392686])

xs_qq_obs_limits = array('d', [0.445766, 0.531756, 0.660085, 0.462665, 0.259771, 0.176882, 0.11975, 0.0883606, 0.0911673, 0.091631, 0.0673097, 0.0576683, 0.0663765, 0.0715058, 0.0707653, 0.0679017, 0.0648869, 0.0605661, 0.0551873, 0.0536497, 0.0525322, 0.0449858, 0.0376862, 0.0386666, 0.0394637, 0.032315, 0.0210878, 0.0132809, 0.00920013, 0.00718502, 0.00635795, 0.00565515, 0.00524019, 0.00555239, 0.00664857, 0.00749758, 0.00812448, 0.00821765, 0.00778863, 0.0072654, 0.00689535, 0.00641743, 0.00594571, 0.00542539, 0.00487017, 0.00432282, 0.00385402, 0.00345907, 0.00325031, 0.0029336, 0.00266552, 0.00247031, 0.0023408, 0.00224978, 0.00218731, 0.0021452, 0.00214538, 0.0021549])
xs_qq_exp_limits = array('d', [0.477582, 0.401964, 0.363716, 0.289744, 0.23842, 0.210805, 0.184404, 0.156756, 0.133975, 0.116447, 0.101665, 0.0899399, 0.0785615, 0.07051, 0.059203, 0.0554069, 0.0494558, 0.0459754, 0.0401039, 0.0355165, 0.031371, 0.0280482, 0.0250272, 0.0237096, 0.0207305, 0.0191532, 0.0166698, 0.0160243, 0.0137829, 0.0132228, 0.0124812, 0.0118259, 0.010205, 0.00943852, 0.0084869, 0.00801166, 0.00735571, 0.00677923, 0.0063039, 0.00570682, 0.00525888, 0.0049462, 0.00463206, 0.00440061, 0.00415374, 0.00370666, 0.00357487, 0.00338426, 0.00335521, 0.00328086, 0.00321736, 0.003065, 0.0029891, 0.00288091, 0.00276867, 0.00267989, 0.0026509, 0.0026118])

if syst:
  xs_gg_obs_limits = array('d', [2.0615, 1.94582, 2.06492, 1.62597, 1.05113, 0.619752, 0.409027, 0.278679, 0.223427, 0.231844, 0.213956, 0.17448, 0.182167, 0.187449, 0.181862, 0.17469, 0.163485, 0.151662, 0.139721, 0.129114, 0.120302, 0.11357, 0.100043, 0.0874448, 0.081939, 0.0751703, 0.0658594, 0.0515029, 0.0351077, 0.0223095, 0.0158919, 0.0128366, 0.0113868, 0.0106171, 0.0108656, 0.0121578, 0.0134528, 0.0142962, 0.0143024, 0.0139918, 0.0132415, 0.0124992, 0.0118243, 0.0110701, 0.0101539, 0.00942484, 0.00875206, 0.00818491, 0.00757354, 0.00701268, 0.0064779, 0.00638241, 0.00611084, 0.00592149, 0.0057839, 0.00583632, 0.00589959, 0.00615538])
  xs_gg_exp_limits = array('d', [2.35524, 1.718395, 1.428665, 1.09346, 0.8535145, 0.6807505, 0.5645625, 0.4462245, 0.3892175, 0.338744, 0.296201, 0.261048, 0.227171, 0.203175, 0.18259, 0.1602235, 0.14302, 0.125324, 0.1061265, 0.09317755, 0.0843383, 0.07174945, 0.064988, 0.05691025, 0.0509401, 0.0453084, 0.04059635, 0.0373627, 0.0317369, 0.0300091, 0.0270188, 0.02477945, 0.0223704, 0.0199402, 0.0187306, 0.01701985, 0.0151752, 0.01351145, 0.01255925, 0.01157715, 0.0106024, 0.009756425, 0.00934829, 0.00875005, 0.00851081, 0.008080615, 0.00765728, 0.007629135, 0.007262815, 0.007117835, 0.007197575, 0.00695401, 0.006931495, 0.00696994, 0.00698784, 0.007031325, 0.007249375, 0.00743711])

  xs_qg_obs_limits = array('d', [1.3959, 1.44829, 1.31726, 1.00642, 0.637327, 0.378596, 0.248195, 0.179449, 0.156801, 0.157078, 0.140802, 0.123014, 0.126673, 0.129163, 0.12916, 0.123556, 0.115661, 0.10677, 0.097489, 0.090278, 0.0860718, 0.0789864, 0.0697045, 0.0619197, 0.0574263, 0.0508895, 0.0431843, 0.0315208, 0.0207677, 0.0137897, 0.0105188, 0.00888977, 0.00784571, 0.00769529, 0.00820165, 0.00918646, 0.0099582, 0.0102429, 0.0102928, 0.00988389, 0.00943999, 0.00886349, 0.0083116, 0.00767947, 0.00708125, 0.00644123, 0.00599399, 0.00549601, 0.0049915, 0.00448342, 0.00424979, 0.00392172, 0.00367954, 0.00349917, 0.00334032, 0.00325643, 0.00322229, 0.00324652])
  xs_qg_exp_limits = array('d', [1.5228, 1.141925, 0.9300815, 0.689262, 0.546956, 0.444851, 0.362029, 0.3022745, 0.2590265, 0.2264055, 0.202871, 0.173006, 0.1562905, 0.140351, 0.126195, 0.1108165, 0.09769975, 0.0839188, 0.07267645, 0.06334305, 0.0558337, 0.05026125, 0.04454515, 0.0396875, 0.03530295, 0.0312174, 0.0287047, 0.02557055, 0.0228086, 0.020473, 0.01940965, 0.01746235, 0.01593015, 0.01452195, 0.01314315, 0.0118794, 0.0107423, 0.009848545, 0.00888611, 0.00831464, 0.00746645, 0.006944, 0.00649144, 0.00627163, 0.006093345, 0.005412895, 0.005109905, 0.00507699, 0.00489189, 0.0046593, 0.00453367, 0.004363205, 0.0042402, 0.004188755, 0.004090695, 0.00398848, 0.00398725, 0.00402766])

  xs_qq_obs_limits = array('d', [0.895858, 0.965575, 0.900752, 0.697496, 0.423405, 0.26049, 0.181675, 0.132657, 0.125319, 0.119397, 0.0987246, 0.0877885, 0.0911367, 0.0928461, 0.0908348, 0.0858027, 0.0808088, 0.0741853, 0.0681326, 0.0642383, 0.060582, 0.0544358, 0.0476643, 0.0443734, 0.0423859, 0.037657, 0.0311503, 0.0211091, 0.0130474, 0.00900213, 0.00728843, 0.00637582, 0.00597609, 0.00623773, 0.00705963, 0.00787881, 0.0082644, 0.00835833, 0.00805248, 0.00763612, 0.00711483, 0.00660508, 0.00613461, 0.00565583, 0.00512362, 0.00461948, 0.00412781, 0.00375494, 0.00339019, 0.003035, 0.00278894, 0.00257018, 0.00243658, 0.00227797, 0.00219318, 0.00215883, 0.00214122, 0.0021581])
  xs_qq_exp_limits = array('d', [0.9946315, 0.8051145, 0.627147, 0.475644, 0.374002, 0.304605, 0.2522265, 0.208702, 0.183822, 0.161106, 0.1410845, 0.123595, 0.1101135, 0.0996241, 0.0878194, 0.0777768, 0.0679316, 0.05905805, 0.0536272, 0.0459997, 0.0409238, 0.0364848, 0.0330868, 0.0286179, 0.0252488, 0.02282465, 0.02144215, 0.0180953, 0.0170692, 0.0151538, 0.01402765, 0.01239115, 0.01140105, 0.01064755, 0.00952408, 0.00845977, 0.00801375, 0.007042805, 0.006565405, 0.00586786, 0.00550331, 0.00508579, 0.00470573, 0.00448573, 0.00417389, 0.003885045, 0.0036984, 0.00356998, 0.003465925, 0.00331277, 0.0031561, 0.003022025, 0.00295003, 0.00287352, 0.002794315, 0.002722985, 0.002670735, 0.00265583])

massesTh = array('d', [1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0,6100.0,6200.0,6300.0,6400.0,6500.0,6600.0,6700.0,6800.0,6900.0,7000.0,7100.0,7200.0,7300.0,7400.0,7500.0,7600.0,7700.0,7800.0,7900.0,8000.0,8100.0,8200.0,8300.0,8400.0,8500.0,8600.0,8700.0,8800.0,8900.0,9000.0])

xsAxi = array('d', [0.1849E+03,0.1236E+03,0.8473E+02,0.5937E+02,0.4235E+02,0.3069E+02,0.2257E+02,0.1680E+02,0.1263E+02,0.9577E+01,0.7317E+01,0.5641E+01,0.4374E+01,0.3411E+01,0.2672E+01,0.2103E+01,0.1658E+01,0.1312E+01,0.1041E+01,0.8284E+00,0.6610E+00,0.5294E+00,0.4250E+00,0.3417E+00,0.2752E+00,0.2220E+00,0.1792E+00,0.1449E+00,0.1172E+00,0.9487E-01,0.7686E-01,0.6219E-01,0.5033E-01,0.4074E-01,0.3298E-01,0.2671E-01,0.2165E-01,0.1755E-01,0.1422E-01,0.1152E-01,0.9322E-02,0.7539E-02,0.6092E-02,0.4917E-02,0.3965E-02,0.3193E-02,0.2568E-02,0.2062E-02,0.1653E-02,0.1323E-02,0.1057E-02,0.8442E-03,0.6728E-03,0.5349E-03,0.4242E-03,0.3357E-03,0.2644E-03,0.2077E-03,0.1627E-03,0.1271E-03,0.9891E-04,0.7686E-04,0.5951E-04,0.4592E-04,0.3530E-04,0.2704E-04,0.2059E-04,0.1562E-04,0.1180E-04,0.8882E-05,0.6657E-05,0.4968E-05,0.3693E-05,0.2734E-05,0.2016E-05,0.1481E-05,0.1084E-05,0.7903E-06,0.5744E-06,0.4160E-06,0.3007E-06])
xsDiquark = array('d', [0.5824E+02,0.4250E+02,0.3172E+02,0.2411E+02,0.1862E+02,0.1457E+02,0.1153E+02,0.9211E+01,0.7419E+01,0.6019E+01,0.4912E+01,0.4031E+01,0.3323E+01,0.2750E+01,0.2284E+01,0.1903E+01,0.1590E+01,0.1331E+01,0.1117E+01,0.9386E+00,0.7900E+00,0.6658E+00,0.5618E+00,0.4745E+00,0.4010E+00,0.3391E+00,0.2869E+00,0.2428E+00,0.2055E+00,0.1740E+00,0.1473E+00,0.1246E+00,0.1055E+00,0.8922E-01,0.7544E-01,0.6376E-01,0.5385E-01,0.4546E-01,0.3834E-01,0.3231E-01,0.2720E-01,0.2288E-01,0.1922E-01,0.1613E-01,0.1352E-01,0.1132E-01,0.9463E-02,0.7900E-02,0.6584E-02,0.5479E-02,0.4551E-02,0.3774E-02,0.3124E-02,0.2581E-02,0.2128E-02,0.1750E-02,0.1437E-02,0.1177E-02,0.9612E-03,0.7833E-03,0.6366E-03,0.5160E-03,0.4170E-03,0.3360E-03,0.2700E-03,0.2162E-03,0.1725E-03,0.1372E-03,0.1087E-03,0.8577E-04,0.6742E-04,0.5278E-04,0.4114E-04,0.3192E-04,0.2465E-04,0.1894E-04,0.1448E-04,0.1101E-04,0.8322E-05,0.6253E-05,0.4670E-05])
xsWprime = array('d', [0.8811E+01,0.6024E+01,0.4216E+01,0.3010E+01,0.2185E+01,0.1610E+01,0.1200E+01,0.9043E+00,0.6875E+00,0.5271E+00,0.4067E+00,0.3158E+00,0.2464E+00,0.1932E+00,0.1521E+00,0.1201E+00,0.9512E-01,0.7554E-01,0.6012E-01,0.4792E-01,0.3827E-01,0.3059E-01,0.2448E-01,0.1960E-01,0.1571E-01,0.1259E-01,0.1009E-01,0.8090E-02,0.6483E-02,0.5193E-02,0.4158E-02,0.3327E-02,0.2660E-02,0.2125E-02,0.1695E-02,0.1351E-02,0.1075E-02,0.8546E-03,0.6781E-03,0.5372E-03,0.4248E-03,0.3353E-03,0.2642E-03,0.2077E-03,0.1629E-03,0.1275E-03,0.9957E-04,0.7757E-04,0.6027E-04,0.4670E-04,0.3610E-04,0.2783E-04,0.2140E-04,0.1641E-04,0.1254E-04,0.9561E-05,0.7269E-05,0.5510E-05,0.4167E-05,0.3143E-05,0.2364E-05,0.1774E-05,0.1329E-05,0.9931E-06,0.7411E-06,0.5523E-06,0.4108E-06,0.3055E-06,0.2271E-06,0.1687E-06,0.1254E-06,0.9327E-07,0.6945E-07,0.5177E-07,0.3863E-07,0.2888E-07,0.2162E-07,0.1622E-07,0.1218E-07,0.9156E-08,0.6893E-08])
xsZprime = array('d', [0.5027E+01,0.3398E+01,0.2353E+01,0.1663E+01,0.1196E+01,0.8729E+00,0.6450E+00,0.4822E+00,0.3638E+00,0.2769E+00,0.2123E+00,0.1639E+00,0.1272E+00,0.9933E-01,0.7789E-01,0.6134E-01,0.4848E-01,0.3845E-01,0.3059E-01,0.2440E-01,0.1952E-01,0.1564E-01,0.1256E-01,0.1010E-01,0.8142E-02,0.6570E-02,0.5307E-02,0.4292E-02,0.3473E-02,0.2813E-02,0.2280E-02,0.1848E-02,0.1499E-02,0.1216E-02,0.9864E-03,0.8002E-03,0.6490E-03,0.5262E-03,0.4264E-03,0.3453E-03,0.2795E-03,0.2260E-03,0.1826E-03,0.1474E-03,0.1188E-03,0.9566E-04,0.7690E-04,0.6173E-04,0.4947E-04,0.3957E-04,0.3159E-04,0.2516E-04,0.2001E-04,0.1587E-04,0.1255E-04,0.9906E-05,0.7795E-05,0.6116E-05,0.4785E-05,0.3731E-05,0.2900E-05,0.2247E-05,0.1734E-05,0.1334E-05,0.1022E-05,0.7804E-06,0.5932E-06,0.4492E-06,0.3388E-06,0.2544E-06,0.1903E-06,0.1417E-06,0.1051E-06,0.7764E-07,0.5711E-07,0.4186E-07,0.3055E-07,0.2223E-07,0.1612E-07,0.1164E-07,0.8394E-08])
xsRSG = array('d', [0.8673E+01,0.5261E+01,0.3306E+01,0.2139E+01,0.1420E+01,0.9639E+00,0.6666E+00,0.4691E+00,0.3349E+00,0.2424E+00,0.1774E+00,0.1312E+00,0.9793E-01,0.7373E-01,0.5591E-01,0.4269E-01,0.3279E-01,0.2533E-01,0.1966E-01,0.1532E-01,0.1200E-01,0.9422E-02,0.7426E-02,0.5870E-02,0.4652E-02,0.3696E-02,0.2942E-02,0.2346E-02,0.1874E-02,0.1499E-02,0.1200E-02,0.9625E-03,0.7724E-03,0.6202E-03,0.4983E-03,0.4005E-03,0.3220E-03,0.2589E-03,0.2082E-03,0.1673E-03,0.1345E-03,0.1080E-03,0.8669E-04,0.6953E-04,0.5573E-04,0.4462E-04,0.3568E-04,0.2850E-04,0.2273E-04,0.1810E-04,0.1439E-04,0.1142E-04,0.9042E-05,0.7147E-05,0.5635E-05,0.4433E-05,0.3479E-05,0.2722E-05,0.2125E-05,0.1653E-05,0.1282E-05,0.9914E-06,0.7639E-06,0.5866E-06,0.4489E-06,0.3423E-06,0.2599E-06,0.1966E-06,0.1481E-06,0.1112E-06,0.8308E-07,0.6183E-07,0.4584E-07,0.3384E-07,0.2489E-07,0.1823E-07,0.1330E-07,0.9672E-08,0.7008E-08,0.5059E-08,0.3645E-08])

massesString = array('d', [1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0,6100.0,6200.0,6300.0,6400.0,6500.0,6600.0,6700.0,6800.0,6900.0,7000.0,7100.0,7200.0,7300.0,7400.0,7500.0,7600.0,7700.0,7800.0,7900.0,8000.0,8100.0,8200.0,8300.0,8400.0,8500.0,8600.0,8700.0,8800.0,8900.0,9000.0,9100.,9200.,9300.,9400.,9500.,9600.,9700.,9800.,9900.,10000.])
xsString = array('d', [8316.184311558545,5312.93137758767,3435.0309937336524,2304.4139502741305,1569.8115447896687,1090.9516635659693,770.901859690924,551.9206062572061,399.69535383507633,293.77957451762086,218.15126842827823,162.87634729465125,123.17685479653694,93.63530805932386,71.53697229809124,55.37491301647483,42.75271508357369,33.36378355470234,26.06619302090876,20.311817606835643,16.1180931789545,12.768644973921226,10.142660425967444,8.057990848043234,6.400465846290908,5.115134438331436,4.132099789492928,3.3193854239538734,2.6581204529344302,2.157554604919995,1.7505176068913348,1.4049155245498584,1.140055677916783,0.9253251132104159,0.7522038169131606,0.6119747371392215,0.49612321727328523,0.40492020959456737,0.33091999402250655,0.27017917021492555,0.2201693919322846,0.17830700070267996,0.14564253802358157,0.11940534430331146,0.09694948234356839,0.0793065371847468,0.06446186373361917,0.05282660618352478,
                       0.0428516302310620888,0.0348997638039910363,0.0283334766442618227,0.0231416918363592127,0.0187417921340763783,0.0153501307395115115,0.0124396534127133717,0.0100542205744949455,0.0081744954858627415,0.0066338099362915941,0.0053365711503318145,0.00430912459914657443,0.00346381039244064343,0.00278602671711227174,0.00225154342228859257,0.0018082930150063248,0.00143929440338502119,0.0011581373956044489,0.00091869589873893118,0.00073410823691329855,0.00058669382997948734,0.0004661568745858897,0.000368716655469570365,0.000293168485206959169,0.000230224535021638668,0.000182317101888465142,0.000143263359883433282,0.000112630538527214965,0.000088189175598406759,0.000068708474367442343,0.000053931726669273556,0.0000416417855733682702,0.0000326529676755488658,0.0000254365480426201587,0.0000198410151166864761,0.0000154034425617473576,0.0000119095554601641413,9.2537574320108232e-6,7.2155417437856749e-6,5.6130924422251982e-6,4.36634755605624901e-6,3.39717456406994868e-6,2.6766018046173896e-6])

massesQstar = array('d', [1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0,6100.0,6200.0,6300.0,6400.0,6500.0,6600.0,6700.0,6800.0,6900.0,7000.0,7100.0,7200.0,7300.0,7400.0,7500.0,7600.0,7700.0,7800.0,7900.0,8000.0,8100.0,8200.0,8300.0,8400.0,8500.0,8600.0,8700.0,8800.0,8900.0,9000.0])
xsQstar = array('d', [0.4101E+03,0.2620E+03,0.1721E+03,0.1157E+03,0.7934E+02,0.5540E+02,0.3928E+02,0.2823E+02,0.2054E+02,0.1510E+02,0.1121E+02,0.8390E+01,0.6328E+01,0.4807E+01,0.3674E+01,0.2824E+01,0.2182E+01,0.1694E+01,0.1320E+01,0.1033E+01,0.8116E+00,0.6395E+00,0.5054E+00,0.4006E+00,0.3182E+00,0.2534E+00,0.2022E+00,0.1616E+00,0.1294E+00,0.1038E+00,0.8333E-01,0.6700E-01,0.5392E-01,0.4344E-01,0.3503E-01,0.2827E-01,0.2283E-01,0.1844E-01,0.1490E-01,0.1205E-01,0.9743E-02,0.7880E-02,0.6373E-02,0.5155E-02,0.4169E-02,0.3371E-02,0.2725E-02,0.2202E-02,0.1779E-02,0.1437E-02,0.1159E-02,0.9353E-03,0.7541E-03,0.6076E-03,0.4891E-03,0.3935E-03,0.3164E-03,0.2541E-03,0.2039E-03,0.1635E-03,0.1310E-03,0.1049E-03,0.8385E-04,0.6699E-04,0.5347E-04,0.4264E-04,0.3397E-04,0.2704E-04,0.2151E-04,0.1709E-04,0.1357E-04,0.1077E-04,0.8544E-05,0.6773E-05,0.5367E-05,0.4251E-05,0.3367E-05,0.2666E-05,0.2112E-05,0.1673E-05,0.1326E-05])

massesS8 = array('d', [1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0])
xsS8 = array('d', [5.15E+02,2.93E+02,1.73E+02,1.11E+02,6.68E+01,4.29E+01,2.86E+01,1.90E+01,1.30E+01,8.71E+00,6.07E+00,4.32E+00,2.99E+00,2.14E+00,1.53E+00,1.09E+00,8.10E-01,5.83E-01,4.38E-01,3.25E-01,2.43E-01,1.78E-01,1.37E-01,1.03E-01,7.66E-02,5.76E-02,4.46E-02,3.42E-02,2.60E-02,1.94E-02,1.50E-02,1.20E-02,9.12E-03,6.99E-03,5.47E-03,4.19E-03,3.21E-03,2.53E-03,1.90E-03,1.50E-03,1.18E-03,9.13E-04,7.07E-04,5.60E-04,4.35E-04,3.36E-04,2.59E-04,2.09E-04,1.59E-04,1.21E-04,9.38E-05])

xs_max = 2e+01
idx = 0

for i, xs in enumerate(xsAxi):
  if xs < xs_max:
    idx = i
    break

if useTeV:
  masses = array('d',(np.array(masses.tolist())/1000.).tolist())
  masses_exp = array('d',(np.array(masses_exp.tolist())/1000.).tolist())
  massesTh = array('d',(np.array(massesTh.tolist())/1000.).tolist())
  massesS8 = array('d',(np.array(massesS8.tolist())/1000.).tolist())
  massesString = array('d',(np.array(massesString.tolist())/1000.).tolist())
  massesQstar = array('d',(np.array(massesQstar.tolist())/1000.).tolist())

graph_xsAxi = TGraph(len(massesTh[idx:-1]),massesTh[idx:-1],xsAxi[idx:-1])
graph_xsAxi.SetLineWidth(3)
graph_xsAxi.SetLineStyle(3)
graph_xsAxi.SetLineColor(63)

for i, xs in enumerate(xsDiquark):
  if xs < xs_max:
    idx = i
    break

graph_xsDiquark = TGraph(len(massesTh[idx:-1]),massesTh[idx:-1],xsDiquark[idx:-1])
graph_xsDiquark.SetLineWidth(3)
graph_xsDiquark.SetLineStyle(9)
graph_xsDiquark.SetLineColor(42)

graph_xsWprime = TGraph(len(massesTh),massesTh,xsWprime)
graph_xsWprime.SetLineWidth(3)
graph_xsWprime.SetLineStyle(7)
graph_xsWprime.SetLineColor(46)

graph_xsZprime = TGraph(len(massesTh),massesTh,xsZprime)
graph_xsZprime.SetLineWidth(3)
graph_xsZprime.SetLineStyle(5)
graph_xsZprime.SetLineColor(38)

graph_xsRSG = TGraph(len(massesTh),massesTh,xsRSG)
graph_xsRSG.SetLineWidth(3)
graph_xsRSG.SetLineStyle(4)
graph_xsRSG.SetLineColor(30)

for i, xs in enumerate(xsString):
  if xs < xs_max:
    idx = i
    break

graph_xsString = TGraph(len(massesString[idx:-1]),massesString[idx:-1],xsString[idx:-1])
graph_xsString.SetLineWidth(3)
graph_xsString.SetLineStyle(8)
graph_xsString.SetLineColor(9)

for i, xs in enumerate(xsQstar):
  if xs < xs_max:
    idx = i
    break

graph_xsQstar = TGraph(len(massesQstar[idx:-1]),massesQstar[idx:-1],xsQstar[idx:-1])
graph_xsQstar.SetLineWidth(3)
graph_xsQstar.SetLineStyle(2)
graph_xsQstar.SetLineColor(1)

for i, xs in enumerate(xsS8):
  if xs < xs_max:
    idx = i
    break

graph_xsS8 = TGraph(len(massesS8[idx:-1]),massesS8[idx:-1],xsS8[idx:-1])
graph_xsS8.SetLineWidth(3)
graph_xsS8.SetLineStyle(6)
graph_xsS8.SetLineColor(6)


graph_exp_gg = TGraph(len(masses),masses,xs_gg_exp_limits)
graph_exp_gg.SetMarkerStyle(24)
graph_exp_gg.SetMarkerColor(TColor.GetColor("#006600"))
graph_exp_gg.SetLineWidth(3)
#graph_exp_gg.SetLineStyle(2)
graph_exp_gg.SetLineColor(TColor.GetColor("#006600"))
#graph_exp_gg.GetXaxis().SetTitle("Resonance mass [GeV]")
#graph_exp_gg.GetYaxis().SetTitle("#sigma #times #it{B} #times #it{A} [pb]")
#graph_exp_gg.GetYaxis().SetTitleOffset(1.1)
#graph_exp_gg.GetYaxis().SetRangeUser(1e-02,1e+03)

graph_obs_gg = TGraph(len(masses),masses,xs_gg_obs_limits)
graph_obs_gg.SetMarkerStyle(24)
graph_obs_gg.SetMarkerColor(TColor.GetColor("#006600"))
graph_obs_gg.SetLineWidth(3)
#graph_obs_gg.SetLineStyle(1)
graph_obs_gg.SetLineColor(TColor.GetColor("#006600"))
graph_obs_gg.GetXaxis().SetTitle("Resonance mass [GeV]")
if useTeV:
  graph_obs_gg.GetXaxis().SetTitle("Resonance mass [TeV]")
graph_obs_gg.GetYaxis().SetTitle("#sigma #times #it{B} #times #it{A} [pb]")
graph_obs_gg.GetYaxis().SetTitleOffset(1.1)
graph_obs_gg.GetYaxis().SetRangeUser(1e-03,1e+02)

graph_exp_qg = TGraph(len(masses),masses,xs_qg_exp_limits)
graph_exp_qg.SetMarkerStyle(20)
graph_exp_qg.SetMarkerColor(2)
graph_exp_qg.SetLineWidth(3)
#graph_exp_qg.SetLineStyle(2)
graph_exp_qg.SetLineColor(2)

graph_obs_qg = TGraph(len(masses),masses,xs_qg_obs_limits)
graph_obs_qg.SetMarkerStyle(20)
graph_obs_qg.SetMarkerColor(2)
graph_obs_qg.SetLineWidth(3)
#graph_obs_qg.SetLineStyle(1)
graph_obs_qg.SetLineColor(2)

graph_exp_qq = TGraph(len(masses),masses,xs_qq_exp_limits)
graph_exp_qq.SetMarkerStyle(26)
graph_exp_qq.SetMarkerColor(4)
graph_exp_qq.SetLineWidth(3)
#graph_exp_qq.SetLineStyle(2)
graph_exp_qq.SetLineColor(4)

graph_obs_qq = TGraph(len(masses),masses,xs_qq_obs_limits)
graph_obs_qq.SetMarkerStyle(26)
graph_obs_qq.SetMarkerColor(4)
graph_obs_qq.SetLineWidth(3)
#graph_obs_qq.SetLineStyle(1)
graph_obs_qq.SetLineColor(4)


c = TCanvas("c", "",800,800)
c.cd()

graph_obs_gg.Draw("ALP")
graph_obs_qg.Draw("LP")
graph_obs_qq.Draw("LP")
graph_xsString.Draw("L")
graph_xsQstar.Draw("L")
graph_xsAxi.Draw("L")
graph_xsDiquark.Draw("L")
graph_xsS8.Draw("L")
graph_xsWprime.Draw("L")
graph_xsZprime.Draw("L")
graph_xsRSG.Draw("L")

legend = TLegend(.65,.48,.95,.60)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetMargin(0.20)
legend.SetHeader('95% CL upper limits')
legend.AddEntry(graph_exp_gg,"gluon-gluon","lp")
legend.AddEntry(graph_exp_qg,"quark-gluon","lp")
legend.AddEntry(graph_exp_qq,"quark-quark","lp")
legend.Draw()

legendTh = TLegend(.63,.64,.98,.90)
legendTh.SetBorderSize(0)
legendTh.SetFillColor(0)
legendTh.SetFillStyle(0)
legendTh.SetTextFont(42)
legendTh.SetTextSize(0.03)
legendTh.SetMargin(0.20)
legendTh.AddEntry(graph_xsString,"String","l")
legendTh.AddEntry(graph_xsDiquark,"Scalar diquark","l")
legendTh.AddEntry(graph_xsQstar,"Excited quark","l")
legendTh.AddEntry(graph_xsAxi,"Axigluon/coloron","l")
legendTh.AddEntry(graph_xsS8,"Color octet scalar","l")
legendTh.AddEntry(graph_xsWprime,"W'","l")
legendTh.AddEntry(graph_xsZprime,"Z'","l")
legendTh.AddEntry(graph_xsRSG,"RS graviton","l")
legendTh.Draw()

#draw the lumi text on the canvas
#CMS_lumi.extraText = "Preliminary"
CMS_lumi.extraText = ""
CMS_lumi.lumi_sqrtS = "2.4 fb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.15
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis()

c.SetLogy()
c.SaveAs('xs_limit_DijetLimitCode_summary' + ('_NoSyst' if not syst else '') + '_Run2_13TeV_DATA_2445_invpb.eps')
