#!/usr/bin/env python
# -*- coding=utf-8 -*-

import time  as sysTime
from time import time

from util.geo.GeoUtil import GeoUtil
from util.io.FileUtil import FileUtil

import gevent
import gevent.monkey
gevent.monkey.patch_thread()
gevent.monkey.patch_socket()

from service.map.baidu.SnatcherService import BaiduMapSnatcherService
import logging
import logging.config
from setting import baidu_map_uadb_setting


from shapely.geometry import Polygon

logging.config.fileConfig(FileUtil().getLogConfigPath())
logger = logging.getLogger("ugc")

goodAkList = ["lWpbR5OCQYybppqci2kGYgFd", "WBw4kIepZzGp4kH5Gn3r0ACy", "ou5X9BBEMZtwvuSO4Ypfx2HB",
              "Qdgt7mclCrkFdPBizd3uUWsE","lWhyznAxPPYdanHLKZpjR272","e5UujacxFn50xo2RadnTEtly",
              "WEC1LKpjIWfCehFqGVPm6Dn6", "DW2CwL3B3271CiVyw7GdBsfR", "LPtK0OiWUItxFK6qd3m1FsRD",
              "oD8Okbi8FdRm5keKBvfHuR7H","K1bHzgxG2osaIiKyAAel57jQ",
              "MviPFAcx5I6f1FkRQlq6iTxc", "MviPFAcx5I6f1FkRQlq6iTxc","MviPFAcx5I6f1FkRQlq6iTxc"
             ]

# 数据库配置
dao_setting = baidu_map_uadb_setting

# 中国
polygon_target = Polygon(((108.533701, 21.550861), (109.269592, 21.240711), (109.821511, 21.413099), (109.536353, 20.964466),
                          (109.343182, 20.609772), (109.085619, 19.950084), (108.496906, 19.427295), (108.165755, 18.867771),
                          (109.784717, 17.601983), (110.594198, 18.587295), (111.2439, 19.749686), (110.719577, 20.531601),
                          (110.811563, 21.162871), (111.078324, 21.404286), (113.957501, 21.800021), (117.324207, 23.252826),
                          (119.844636, 25.268352), (122.590433, 30.245623), (121.92813, 32.362247), (120.456346, 34.430003),
                          (121.560184, 36.536529), (123.105557, 36.980639), (117.751944, 38.514484), (117.899122, 38.889325),
                          (118.248671, 38.975545), (118.579822, 38.874944), (121.146245, 40.72668), (121.698164, 40.768656),
                          (122.047713, 40.572537), (122.047713, 40.347691), (121.127848, 39.583242), (121.072656, 38.579502),
                          (122.434056, 39.068831), (124.402567, 39.810643), (126.941393, 41.436644), (128.817918, 41.71295),
                          (130.105729, 42.589116), (130.804826, 42.261985), (130.84162, 42.806247), (131.31995, 42.887474),
                          (131.301553, 44.482813), (131.11758, 44.850436), (132.037445, 45.202705), (133.012501, 44.98116),
                          (133.251666, 45.111586), (134.116339, 46.399379), (134.870628, 47.744231), (135.109793, 48.568976),
                          (131.411937, 47.806239), (130.768031, 48.115169), (131.025593, 48.360974), (130.657647, 48.642183),
                          (130.768031, 48.982407), (126.223899, 52.829883), (124.273785, 53.602875), (121.661369, 53.537167),
                          (120.631121, 53.317399), (119.932023, 52.807591), (120.042407, 52.449359), (119.122542, 50.496506),
                          (119.196131, 50.166769), (115.406288, 47.942397), (116.14218, 47.520382), (118.129088, 47.942397),
                          (119.085748, 47.545302), (119.932023, 46.716655), (118.570623, 46.868285), (116.767688, 46.539211),
                          (116.14218, 46.028999), (115.958207, 45.694795), (114.486424, 45.488126), (112.573105, 45.124612),
                          (112.094775, 45.202705), (111.211705, 44.627516), (111.064526, 43.673795), (104.588678, 42.104626),
                          (96.2731, 43.298713), (93.476711, 45.098557), (90.680321, 45.514002), (88.98777, 48.532332),
                          (82.217565, 47.094924), (79.421176, 44.784961), (79.789122, 42.43258), (76.183251, 40.94327),
                          (73.092506, 39.987775), (79.05323, 30.914198), (86.338559, 27.755075), (89.282127, 27.032511),
                          (92.225694, 26.768583), (98.480775, 27.164241), (97.229759, 23.960657), (99.437435, 21.778542),
                          (102.307413, 21.296561), (101.865878, 22.464245), (105.986872, 22.80582),(106.869943, 21.709787),
                          (107.642629, 21.399979), (107.642629, 21.399979)))

# 苏州工业园区
# polygon_target = Polygon(((120.699452, 31.455197), (120.717274, 31.248457), (120.652884, 31.284016), (120.634487, 31.351144),
#                           (120.660358, 31.371865), (120.720724, 31.391595), (120.739696, 31.38765), (120.74602, 31.410828),
#                           (120.802362, 31.436959), (120.832258, 31.441888), (120.836282, 31.391595), (120.85123, 31.370385),
#                           (120.866752, 31.356572), (120.884575, 31.317586), (120.855829, 31.285003), (120.817885, 31.300802),
#                           (120.805811, 31.285497), (120.81616, 31.273152), (120.810411, 31.271671), (120.785689, 31.270683),
#                           (120.763843, 31.238084), (120.743721, 31.235614), (120.743721, 31.235614)))

# 徐州市
# polygon_target = Polygon(((118.640238, 34.339068), (118.628904, 34.348954), (118.639826, 34.350447), (118.642418, 34.362114), (118.650849, 34.364886), (118.653043, 34.384957), (118.669444, 34.390129), (118.680267, 34.400743), (118.680679, 34.406359), (118.675344, 34.413375), (118.677586, 34.425333), (118.6633, 34.426762), (118.661843, 34.432634), (118.655366, 34.432758), (118.651455, 34.446057), (118.6408, 34.445753), (118.614557, 34.452644), (118.602433, 34.450008), (118.592127, 34.425547), (118.585011, 34.422699), (118.581081, 34.422918), (118.578584, 34.429219), (118.567055, 34.434778), (118.539264, 34.441414), (118.530823, 34.446091), (118.510376, 34.436364), (118.496426, 34.426064), (118.496308, 34.421872), (118.472751, 34.412822), (118.459277, 34.418168), (118.451839, 34.416768), (118.441116, 34.41961), (118.435893, 34.426695), (118.428627, 34.429494), (118.422239, 34.425969), (118.419918, 34.437051), (118.414963, 34.44186), (118.411244, 34.433388), (118.399866, 34.431973), (118.388906, 34.42601), (118.386353, 34.420958), (118.361247, 34.422971), (118.358784, 34.428799), (118.327388, 34.427693), (118.325123, 34.434635), (118.320462, 34.429336), (118.298882, 34.431258), (118.295681, 34.418997), (118.285266, 34.417372), (118.284014, 34.410439), (118.249002, 34.411505), (118.247394, 34.407853), (118.237603, 34.404728), (118.226753, 34.41201), (118.224205, 34.385345), (118.210847, 34.383693), (118.209343, 34.387248), (118.196093, 34.38694), (118.194159, 34.396527), (118.189603, 34.39636), (118.185827, 34.385597), (118.176982, 34.387357), (118.175439, 34.393943), (118.182366, 34.408139), (118.181518, 34.419529), (118.185399, 34.431566), (118.184301, 34.459392), (118.162393, 34.470828), (118.154045, 34.476587), (118.155317, 34.478537), (118.14664, 34.48099), (118.147955, 34.485588), (118.139526, 34.489085), (118.1502, 34.503966), (118.171573, 34.510811), (118.175899, 34.518374), (118.172907, 34.521018), (118.174426, 34.525977), (118.191152, 34.550427), (118.178948, 34.553011), (118.179672, 34.555858), (118.153047, 34.556549), (118.147395, 34.559658), (118.148983, 34.565427), (118.143863, 34.568895), (118.13924, 34.561466), (118.133108, 34.560541), (118.120605, 34.566754), (118.085199, 34.575839), (118.088536, 34.58616), (118.10486, 34.594546), (118.121335, 34.620032), (118.121433, 34.62528), (118.107261, 34.632355), (118.108064, 34.638448), (118.10095, 34.642373), (118.10939, 34.653591), (118.106538, 34.657329), (118.089139, 34.662272), (118.06402, 34.660886), (118.060521, 34.656732), (118.048041, 34.661665), (118.035189, 34.661443), (118.03543, 34.66529), (118.027438, 34.665843), (118.025296, 34.652738), (118.014346, 34.652922), (118.01401, 34.66159), (118.00395, 34.662537), (117.995508, 34.667754), (117.996394, 34.673852), (117.991384, 34.675765), (117.958925, 34.677613), (117.948886, 34.670256), (117.916671, 34.675988), (117.909336, 34.649982), (117.885983, 34.650951), (117.881508, 34.656523), (117.870045, 34.651057), (117.862154, 34.651677), (117.855762, 34.653434), (117.853017, 34.659073), (117.840652, 34.653503), (117.836461, 34.660453), (117.827674, 34.652627), (117.817416, 34.650556), (117.806073, 34.652991), (117.8066, 34.656263), (117.800488, 34.657391), (117.800281, 34.631602), (117.806182, 34.62655), (117.806383, 34.615432), (117.798069, 34.576963), (117.803328, 34.563701), (117.800411, 34.552571), (117.805999, 34.52601), (117.796191, 34.524587), (117.771952, 34.538187), (117.726002, 34.550653), (117.691194, 34.553585), (117.68853, 34.535181), (117.664723, 34.504349), (117.653702, 34.498504), (117.645266, 34.503294), (117.640992, 34.497445), (117.630446, 34.49314), (117.626651, 34.497041), (117.616027, 34.496523), (117.606353, 34.478045), (117.595602, 34.467619), (117.576905, 34.468717), (117.568228, 34.477449), (117.554739, 34.480749), (117.545078, 34.472436), (117.519566, 34.478456), (117.500859, 34.478776), (117.494175, 34.472236), (117.491144, 34.490469), (117.471665, 34.490712), (117.461521, 34.508632), (117.445005, 34.521919), (117.446208, 34.525821), (117.432955, 34.531159), (117.42671, 34.543793), (117.409599, 34.552934), (117.408739, 34.575276), (117.383137, 34.589386), (117.372533, 34.584243), (117.35836, 34.59002), (117.350499, 34.587865), (117.342499, 34.580909), (117.326062, 34.57892), (117.322656, 34.57473), (117.306613, 34.572501), (117.293597, 34.577131), (117.28615, 34.564396), (117.279748, 34.561712), (117.276876, 34.539188), (117.27326, 34.535724), (117.280365, 34.525702), (117.268405, 34.519036), (117.2809, 34.51715), (117.279839, 34.508112), (117.266065, 34.504264), (117.272334, 34.483773), (117.262391, 34.483241), (117.255088, 34.493063), (117.248682, 34.486469), (117.25219, 34.481512), (117.261761, 34.478738), (117.262296, 34.468124), (117.259691, 34.465547), (117.255935, 34.469917), (117.250599, 34.468043), (117.251087, 34.465076), (117.259093, 34.464971), (117.252536, 34.456654), (117.240434, 34.460335), (117.230095, 34.458222), (117.214723, 34.462173), (117.2192, 34.469902), (117.194252, 34.502073), (117.187447, 34.49809), (117.182327, 34.49891), (117.163287, 34.527808), (117.166632, 34.565678), (117.151749, 34.593477), (117.144632, 34.620778), (117.138112, 34.630996), (117.133826, 34.654179), (117.102324, 34.653722), (117.083744, 34.642936), (117.072943, 34.653232), (117.068693, 34.663272), (117.067868, 34.681651), (117.076377, 34.697681), (117.098142, 34.709234), (117.07088, 34.732707), (117.07165, 34.748066), (117.066454, 34.756511), (117.055214, 34.760636), (117.056589, 34.775557), (117.04795, 34.784527), (117.026028, 34.795971), (116.993153, 34.803642), (116.973423, 34.842783), (116.972352, 34.881024), (116.952267, 34.896699), (116.922805, 34.897928), (116.903001, 34.909214), (116.887468, 34.914059), (116.867221, 34.932031), (116.852709, 34.930116), (116.818482, 34.934218), (116.792789, 34.946008), (116.787854, 34.922701), (116.763402, 34.923561), (116.743872, 34.930234), (116.726256, 34.93228), (116.711602, 34.941536), (116.700217, 34.937843), (116.631863, 34.939504), (116.621221, 34.934863), (116.61049, 34.925144), (116.567351, 34.91449), (116.555112, 34.914696), (116.475565, 34.900825), (116.466061, 34.905414), (116.453253, 34.903727), (116.447218, 34.890887), (116.417712, 34.864271), (116.419468, 34.847025), (116.41613, 34.834426), (116.420438, 34.822363), (116.410602, 34.812006), (116.409323, 34.801574), (116.412758, 34.775675), (116.408604, 34.768068), (116.412818, 34.754649), (116.372285, 34.755895), (116.369088, 34.750302), (116.36856, 34.743492), (116.374914, 34.73749), (116.375009, 34.73174), (116.369934, 34.729946), (116.370356, 34.721127), (116.37744, 34.720177), (116.385107, 34.724791), (116.388923, 34.723762), (116.391872, 34.711026), (116.400074, 34.710676), (116.399744, 34.705648), (116.392225, 34.701085), (116.391511, 34.693015), (116.382419, 34.686962), (116.388336, 34.668934), (116.374462, 34.65486), (116.37716, 34.649394), (116.391086, 34.645294), (116.395647, 34.640324), (116.399917, 34.647806), (116.436696, 34.65681), (116.44474, 34.631499), (116.462164, 34.626001), (116.474347, 34.616308), (116.479281, 34.620482), (116.485737, 34.620766), (116.486073, 34.613334), (116.498038, 34.591274), (116.497135, 34.583681), (116.504641, 34.57308), (116.511763, 34.570902), (116.514482, 34.564577), (116.532304, 34.559709), (116.527385, 34.554185), (116.529327, 34.547868), (116.554167, 34.548067), (116.558998, 34.550445), (116.578105, 34.527868), (116.591972, 34.51825), (116.601867, 34.517266), (116.605616, 34.50597), (116.578247, 34.503082), (116.575877, 34.499313), (116.579935, 34.493127), (116.625532, 34.494048), (116.670358, 34.478281), (116.708023, 34.477043), (116.732473, 34.480256), (116.759264, 34.472398), (116.784483, 34.45633), (116.785265, 34.444779), (116.796268, 34.434651), (116.798782, 34.426712), (116.824825, 34.411634), (116.84206, 34.396345), (116.849238, 34.396135), (116.853438, 34.401427), (116.877512, 34.400366), (116.879006, 34.411432), (116.93534, 34.407307), (116.975893, 34.394813), (116.967499, 34.370895), (116.99088, 34.361883), (116.989124, 34.347224), (116.97681, 34.331764), (116.977182, 34.324229), (116.982779, 34.316739), (116.979355, 34.301656), (116.983248, 34.29685), (116.978884, 34.291378), (116.984764, 34.288662), (116.991709, 34.278527), (117.005332, 34.272091), (117.00867, 34.263994), (117.012762, 34.262503), (117.02351, 34.267196), (117.027521, 34.249197), (117.034459, 34.246256), (117.043475, 34.252591), (117.051888, 34.253577), (117.051532, 34.230512), (117.064932, 34.230761), (117.045128, 34.207406), (117.0339, 34.184692), (117.039012, 34.184449), (117.033465, 34.173667), (117.044943, 34.17327), (117.053669, 34.157144), (117.06157, 34.160763), (117.072448, 34.15723), (117.076014, 34.149235), (117.102113, 34.148954), (117.108728, 34.136442), (117.137963, 34.1329), (117.14353, 34.124809), (117.138367, 34.117461), (117.126836, 34.113006), (117.125746, 34.108826), (117.153123, 34.103888), (117.162964, 34.105112), (117.156716, 34.089684), (117.171611, 34.089047), (117.199333, 34.074459), (117.213613, 34.074575), (117.214376, 34.080656), (117.218672, 34.080736), (117.231191, 34.07041), (117.263553, 34.071903), (117.264416, 34.077977), (117.288555, 34.082729), (117.295731, 34.080282), (117.296344, 34.072586), (117.318889, 34.070956), (117.326846, 34.088932), (117.349792, 34.08706), (117.359527, 34.094744), (117.364134, 34.094914), (117.364388, 34.089997), (117.378784, 34.084097), (117.382906, 34.078749), (117.378428, 34.063672), (117.401289, 34.058621), (117.401688, 34.052104), (117.40656, 34.051699), (117.407036, 34.033471), (117.427062, 34.025253), (117.438733, 34.026504), (117.443148, 34.031716), (117.463134, 34.032776), (117.466055, 34.041711), (117.481135, 34.047718), (117.485547, 34.054705), (117.503483, 34.05443), (117.512315, 34.058713), (117.514617, 34.066131), (117.527738, 34.066151), (117.545718, 34.054821), (117.544033, 34.048008), (117.552788, 34.04005), (117.550484, 34.013455), (117.563414, 34.009864), (117.563319, 34.002209), (117.572276, 34.001726), (117.570343, 33.987508), (117.574258, 33.984471), (117.593049, 33.989043), (117.597093, 33.995407), (117.59438, 34.003335), (117.605606, 34.004468), (117.617848, 34.012442), (117.617071, 34.017436), (117.627497, 34.022457), (117.613749, 34.028356), (117.617004, 34.036008), (117.628759, 34.034159), (117.638296, 34.025135), (117.648789, 34.02435), (117.650029, 34.013809), (117.670747, 34.005828), (117.676917, 34.000052), (117.675709, 33.986165), (117.667669, 33.976814), (117.670062, 33.96352), (117.680506, 33.952259), (117.676898, 33.938546), (117.697308, 33.928467), (117.703458, 33.918293), (117.708964, 33.895012), (117.723179, 33.88691), (117.730813, 33.888115), (117.731473, 33.894286), (117.735939, 33.896969), (117.752559, 33.897244), (117.764631, 33.890637), (117.762458, 33.869179), (117.75903, 33.869217), (117.761808, 33.854824), (117.752697, 33.829816), (117.75974, 33.817491), (117.759377, 33.808816), (117.748381, 33.78367), (117.748702, 33.766971), (117.74224, 33.760802), (117.741743, 33.753609), (117.732347, 33.75269), (117.731548, 33.748928), (117.742749, 33.729136), (117.751932, 33.724721), (117.753289, 33.716915), (117.761058, 33.717024), (117.800674, 33.740254), (117.830654, 33.744541), (117.839459, 33.738143), (117.843549, 33.742067), (117.860347, 33.741866), (117.904091, 33.725172), (117.907949, 33.725836), (117.906399, 33.736059), (117.910335, 33.741863), (117.923912, 33.741611), (117.936231, 33.733315), (117.959665, 33.735703), (117.963487, 33.762662), (117.975845, 33.76669), (117.980413, 33.756434), (118.008654, 33.751455), (118.017255, 33.751955), (118.018666, 33.754967), (118.054735, 33.757139), (118.080231, 33.771802), (118.107224, 33.771476), (118.127297, 33.767802), (118.147409, 33.755366), (118.17517, 33.755832), (118.177422, 33.765147), (118.185128, 33.769257), (118.177031, 33.79222), (118.166292, 33.79793), (118.166016, 33.801104), (118.168313, 33.809761), (118.175485, 33.816472), (118.174198, 33.826784), (118.190282, 33.822524), (118.193717, 33.826819), (118.191259, 33.850448), (118.182376, 33.850454), (118.181135, 33.870786), (118.174731, 33.887021), (118.157173, 33.904187), (118.149961, 33.929912), (118.135789, 33.957836), (118.126602, 33.960524), (118.123599, 33.954968), (118.126105, 33.947234), (118.117755, 33.94135), (118.112643, 33.94119), (118.10562, 33.947961), (118.092218, 33.947856), (118.09185, 33.971801), (118.079138, 33.971626), (118.068633, 33.97721), (118.059644, 33.977962), (118.049307, 33.989397), (118.039329, 33.992604), (118.035064, 34.00406), (118.038772, 34.005481), (118.03666, 34.013034), (118.043951, 34.017354), (118.060713, 34.015768), (118.070043, 34.026607), (118.068179, 34.037565), (118.073352, 34.040697), (118.067536, 34.045102), (118.065759, 34.051299), (118.070279, 34.060025), (118.055179, 34.098508), (118.019738, 34.089588), (118.01217, 34.097371), (118.01507, 34.105714), (118.003224, 34.111538), (118.001337, 34.121589), (118.005593, 34.145879), (118.016939, 34.145041), (118.02368, 34.148703), (118.062069, 34.154916), (118.070647, 34.158766), (118.067092, 34.163237), (118.077936, 34.177369), (118.090285, 34.171399), (118.093148, 34.161612), (118.104579, 34.15596), (118.105346, 34.148177), (118.109089, 34.145747), (118.12734, 34.14986), (118.15091, 34.141187), (118.15945, 34.145313), (118.160929, 34.154182), (118.156499, 34.161984), (118.160631, 34.166042), (118.183811, 34.162509), (118.195993, 34.168568), (118.218352, 34.167384), (118.244267, 34.130547), (118.255142, 34.129508), (118.259198, 34.131728), (118.305678, 34.118587), (118.395465, 34.122558), (118.443932, 34.110497), (118.461444, 34.111705), (118.482099, 34.102172), (118.488854, 34.103994), (118.511162, 34.113659), (118.52056, 34.121764), (118.512298, 34.125813), (118.51153, 34.130101), (118.516324, 34.154463), (118.513434, 34.155317), (118.51281, 34.164058), (118.516447, 34.168212), (118.525822, 34.174384), (118.566876, 34.171903), (118.566392, 34.195697), (118.57803, 34.225538), (118.579996, 34.239572), (118.57037, 34.244889), (118.567578, 34.254351), (118.572862, 34.279467), (118.580999, 34.284651), (118.578386, 34.30444), (118.597973, 34.313851), (118.630157, 34.311357), (118.631444, 34.314002), (118.6391, 34.313635), (118.640238, 34.339068)))

"""
调用百度PlaceAPI爬取数据
"""
class PlaceService(object):
    def __init__(self):
        print "Constructor "

    def fetchPlace(self, index, bounds):
        # 最后一个token为企业号
        if index > len(goodAkList)-1:
            token = goodAkList[-1]
        else:
            token = goodAkList[index]
        snatcherService = BaiduMapSnatcherService(dao_setting["host"], dao_setting["db"], dao_setting["user"], dao_setting["password"], token)
        logger.debug('current index %s' % index)
        # 常用大类
        keywords = ["美食", "宾馆", "酒店", "购物", "汽车服务", "生活服务", "结婚", "丽人", "金融", "休闲娱乐", "运动健身", "医疗",
                    "旅游景点", "生活服务", "汽车服务", "教育", "培训机构", "交通设施", "房地产", "自然地物", "行政区划", "政府机构",
                    "公司企业", "门址", "道路", "交通线"]
        # 民政局-地名普查所需类型
        keywords = ["星级酒店", "购物中心", "家居建材", "集市", "批发市场", "邮局", "墓地陵园", "度假村", "农家院", "采摘园",
                    "文化宫", "电影院", "音乐厅", "剧院", "体育场馆", "医院", "疗养院", "旅游景点","学校","图书馆",
                    "飞机场","机场出入口","火车站","地铁站","长途汽车站","房地产",
                    "自然地物","行政区划","政府机构", "门址", "道路", "交通线"]
        # for keyword in keywords:
        #     logger.debug("keyword: %s " % keyword)
        #     snatcherService.fetchPlace(polygon_target,bounds[0], bounds[1], bounds[2], bounds[3], keyword,tableName="Place_SuZhou_GYYQ")
        #     # sysTime.sleep(1)
        #     pass

        # 从文件中读取关键字进行爬取
        f = open('keywords.txt', 'r')
        for line in f.readlines():
            logger.debug("keyword: %s " % line)
            snatcherService.fetchPlace(polygon_target,bounds[0], bounds[1], bounds[2], bounds[3], line,tableName="Place_Xuzhou")
        logger.debug("Process %s done" % index)

    def fetchPlaceDetail(self,index,bounds):
        if index > len(goodAkList)-1:
            token = goodAkList[-1]
        else:
            token = goodAkList[index]
        snatcherService = BaiduMapSnatcherService(dao_setting["host"], dao_setting["db"], dao_setting["user"], dao_setting["password"], token)
        logger.debug('current index %s' % index)
        logger.debug('current bounds:'+str(bounds))
        snatcherService.fetchPlaceDetail(bounds[0], bounds[1], bounds[2], bounds[3],"医院")
        logger.debug("Process %s done" % index)

    def normalRequest(self):
        # 南海区桂城街道
        bounds = [113.129391, 22.98257, 113.261335, 23.072904]
        # 偏移测试
        bounds[0] -= 0.02
        self.fetchPlace(0, bounds)

    def concurrentRequest(self):
        # 南海区
        envelope=polygon_target.envelope
        bounds=list(envelope.bounds)

        # 偏移测试
        bounds[0] -= 0.02
        parts = 4
        # 区域长度分4份，将生成16个区域
        boundsList = GeoUtil().getBoundsList(bounds, parts)

        threads = []
        for index in range(0, len(boundsList), 1):
            print 'current bounds ...%s ' % index
            subBounds = boundsList[index]

            # 将extent转换成polygon
            coords=GeoUtil().getPolygonByExtent(subBounds)
            coords=tuple(coords)
            isIntersects=Polygon((coords)).intersects(polygon_target)
            if isIntersects:
                threads.append(gevent.spawn(self.fetchPlace, index, subBounds))
        gevent.joinall(threads)

    '''
    多线程爬取poi点的详细信息
    '''
    def mutiSearchPlace(self):
        envelope=polygon_target.envelope
        bounds=list(envelope.bounds)
        # 偏移测试
        bounds[0] -= 0.02
        parts = 50
        # 区域长度分4份，将生成16个区域
        boundsList = GeoUtil().getBoundsList(bounds, parts)
        threads = []
        # 将区域分成块，并按照每16个协程一个循环进行数据获取
        for index in range(0, len(boundsList)/16+1, 1):
            for threadIndex in range(index*16,(index+1)*16):
                if threadIndex < len(boundsList):
                    print 'current bounds ...%s ' % threadIndex
                    subBounds = boundsList[threadIndex]
                    # 将extent转换成polygon
                    coords=GeoUtil().getPolygonByExtent(subBounds)
                    coords=tuple(coords)
                    isIntersects=Polygon((coords)).intersects(polygon_target)
                    if isIntersects:
                        threads.append(gevent.spawn(self.fetchPlaceDetail, threadIndex%16, subBounds))
            gevent.joinall(threads)


if __name__ == '__main__':
    # python E:\PythonWorkspace\ugc\ugc.aggregator\src\main\scripts\PlaceService.py
    ts = time()
    service = PlaceService()
    # service.concurrentRequest()
    service.mutiSearchPlace()
    print 'Took %s' % format(time() - ts)
