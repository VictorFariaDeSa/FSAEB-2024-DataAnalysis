from TeamClass import *

cars = []

car1 =  Car(6  ,"Fórmula FEI"               , "Yamaha WR450F"           ,10,     False, 50.6, 51.6, 1530, 1150, 1250, 28.0, 168, "E100", 5)
car1.cost = Cost(22591, 22.4, 22.0, 23.8, 0, -6, 0, 62.2)
car1.design = Design(19.5, 18.1, 10.9, 13.7, 28.4, 25.0, 13.0,0,0, 128.6)
car1.business = Business(0,0,77.9)
car1.acceleration.runs = [4.300, None, None, 4.295]
car1.acceleration.cones = [0]*4
car1.acceleration.score = 62.83
car1.skidPad.runs = [[5.57, 5.88],[5.62, 5.53],[5.35, 5.47],[5.31, 5.47]]
car1.skidPad.cones = [0,1,1,0]
car1.skidPad.score = 75
car1.autoX.runs = [67.74,64.19,65.17,65.44]
car1.autoX.offCourses = [0,0,1,0]
car1.autoX.cones = [0]*4
car1.autoX.score = 119.75
car1.enduro = Enduro(1395.5, 20,0,0,0, 20.00)
car1.enduro.lap_times = [73.20, 70.22, 69.44, 68.86, 68.87, 90.73, 69.12, 76.65, 68.33, 68.10, 68.23, 68.47, 68.36, 66.32, 65.81, 66.42, 64.97, 64.39, 70.14, 68.87]
car1.efficiency = Efficiency(69.77, 20, 4.157, 71.3)
cars.append(car1)

car2 =  Car(4  ,"EESC-USP Formula SAE"      , "KTM DUKE 390"            ,10,     True , 50.0, 52.0, 1530, 1200, 1200, 30.0, 180, "E100", 6)
car2.cost = Cost(12660, 22.9, 27.5, 21.3, 31.0, -7, 0, 95.7)
car2.design = Design(27.6, 29.5, 16.9, 14.6, 29.6, 29.3, 23.5, 0, 0, 170.9)
car2.business = Business(0,0,64.7)
car2.acceleration.runs = [None]*4
car2.acceleration.cones = [0]*4
car2.acceleration.score = 0
car2.skidPad.runs = [None]*4
car2.skidPad.cones = [0]*4
car2.skidPad.score = 0
car2.autoX.runs = [None]*4
car2.autoX.offCourses = [0]*4
car2.autoX.cones = [0]*4
car2.autoX.score = 0
car2.enduro = Enduro(1683.8, 22,0,0,0, 176.24)
car2.enduro.lap_times = [78.01, 74.67, 79.25, 81.91, 68.78, 78.97, 69.92, 72.23, 91.58, 68.70, 84.12, 81.57, 73.54, 73.72, 71.32, 76.67, 70.81, 74.39, 80.69, 72.07, 82.68, 78.18]
car2.efficiency = Efficiency(76.53, 22,3.520, 91.8)
cars.append(car2)

car3 =  Car(5  ,"Formula UFSM"              , "Honda CBR 600 RR"        ,10,     False, 50.0, 51.8, 1525, 1180, 1200, 26.0, 203,  "E25", 4) 
car3.cost = Cost(12358, 17.4, 18.0, 13.8, 31.9, -22,0, 59.1)
car3.design = Design(14.4, 16.4, 13.5, 10.4, 22.0, 19.3, 19.8, 0, 0, 115.8)
car3.business = Business(0,0,78.7)
car3.acceleration.runs = [4.263,4.088, 4.112,4.075]
car3.acceleration.cones = [0]*4
car3.acceleration.score = 75.21
car3.skidPad.runs = [[5.94, 5.97],[5.84, 6.85],[5.97, 8.44],[5.69, 7.53]]
car3.skidPad.cones = [0,0,4,3]
car3.skidPad.score = 39.10
car3.autoX.runs = [77.16,69.96,71.79,70.76]
car3.autoX.offCourses = [0]*4
car3.autoX.cones = [0,0,0,1]
car3.autoX.score = 94.71
car3.enduro = Enduro(1640.0, 22, 2,0,0,191.16)
car3.enduro.lap_times = [83.82, 73.87, 72.40, 70.57, 72.20, 73.02, 70.65, 80.70, 74.57, 94.57, 77.44, 74.79, 71.91, 71.01, 70.34, 71.47, 72.83, 70.09, 70.69, 81.39, 69.43, 76.20]
car3.efficiency = Efficiency(74.73, 22,3.708, 49.3)
cars.append(car3)

car4 =  Car(11 ,"Poli Racing"               , "Yamaha YFZ 450R"         ,10,     True , 50.4, 49.7, 1530, 1200, 1150, 44.0, 203,   None, 19)
car4.cost = Cost(17537, 22.3, 17.5, 21.3, 15.8, -9,0, 67.9)
car4.design = Design(16.0, 18.7, 12.4, 12.9, 26.3, 19.3, 14.6, 0, -5, 115.2)
car4.business = Business(0,0,70.1)
car4.acceleration.runs = [4.897,None,None,None]
car4.acceleration.cones = [0]*4
car4.acceleration.score = 34.64
car4.skidPad.runs = [None]*4
car4.skidPad.cones = [0]
car4.skidPad.score = 0
car4.autoX.runs = [109.79,110.69,237.59,None]
car4.autoX.offCourses = [0]*4
car4.autoX.cones = [0]*4
car4.autoX.score = 6.5
car4.enduro = Enduro(79.5, 1,0,0, 120, 1.00)
car4.enduro.lap_times = [79.48]
cars.append(car4)

car5 =  Car(2  ,"Mauá Racing"               , "Triumph Daytona 675 R"   ,10,     False, 50.2, 51.1, 1530, 1200, 1200, 31.0, 207,   None, 7) 
car5.cost = Cost(17598, 21.7, 25.0, 19.4, 15.6, -21,0, 60.7)
car5.design = Design(21.9, 20.4, 15.4, 8.8, 17.7, 17.2, 18.4, -30, 0, 89.7)
car5.business = Business(0,0,84.8)
car5.acceleration.runs = [3.892, None, None, None]
car5.acceleration.cones = [0]*4
car5.acceleration.score = 86.57
car5.skidPad.runs = [[44.19, 5.72],[5.72, 5.75],[6.00, 5.71],[5.54, 5.37]]
car5.skidPad.cones = [2,0,0,0]
car5.skidPad.score = 70.30
car5.autoX.runs = [67.09,65.13,None,None]
car5.autoX.offCourses = [0]*4
car5.autoX.cones = [0]*4
car5.autoX.score = 119.95
car5.enduro = Enduro(864.4, 11,0,0,0,11.00)
car5.enduro.lap_times = [79.03, 81.32, 77.24, 74.30, 75.03, 77.46, 79.05, 79.41, 80.08, 81.08, 80.44]
cars.append(car5)

car6 =  Car(1  ,"Fórmula Cefast"            , "Honda CBR 600RR"         ,10,     True , 50.7, 52.6, 1540, 1210, 1210, 33.0, 210,  "E25", 1) 
car6.cost = Cost(14497, 23.1, 24.0, 23.1, 25.3, -8, 0, 87.5)
car6.design = Design(28.1, 28.4, 18.2, 14.7, 29.6, 29.7, 24.2, 0, 0, 172.9)
car6.business = Business(0,0,87.8)
car6.acceleration.runs = [5.079, 4.604, 3.854, 3.840]
car6.acceleration.cones = [0]*4
car6.acceleration.score = 90
car6.skidPad.runs = [[5.91, 6.12],[5.78, 5.91],[5.59, 5.50],[5.62, 5.69]]
car6.skidPad.cones = [0,0,0,0]
car6.skidPad.score = 64.05
car6.autoX.runs = [63.12,73.64,65.79,65.24]
car6.autoX.offCourses = [0,0,0,0]
car6.autoX.cones = [1,3,0,0]
car6.autoX.score = 120
car6.enduro = Enduro(1546.7, 22, 1,0,0,230.00)
car6.enduro.lap_times = [69.88, 67.69, 66.05, 72.50, 68.80, 65.82, 68.56, 67.17, 71.48, 70.74, 68.81, 72.93, 71.02, 69.78, 75.90, 73.12, 71.96, 70.50, 72.01, 69.74, 70.75, 73.53]
car6.efficiency = Efficiency(70.40, 22, 3.298, 66.6)
cars.append(car6)

car7 =  Car(22 ,"V8 Racing Team"            , "Honda CBR 600 RR"        ,10,     False, 50.8, 47.3, 1535, 1215, 1165, 38.0, 214, "E100", 13) 
car7.cost = Cost(12306, 13.9, 17.5, 12.5, 32.1, -24, 0, 52.0)
car7.design = Design(5.9, 7.6, 4.8, 2.6, 15.2, 11.9, 5.9, 0, 0, 53.9)
car7.business = Business(0,-5,40.1)
car7.acceleration.runs = [4.366, 4.129, 4.482, 4.112]
car7.acceleration.cones = [0]*4
car7.acceleration.score = 73.03
car7.skidPad.runs = [[None,None],[5.82, 5.75],[7.56, 7.19],[6.44, 6.35]]
car7.skidPad.cones = [0,1,0,2]
car7.skidPad.score = 41.59
car7.autoX.runs = [77.95,124.06,92.99,83.68]
car7.autoX.offCourses = [0,0,0,1]
car7.autoX.cones = [0,0,0,1]
car7.autoX.score = 59.79
car7.enduro = Enduro(1877.1, 22, 2, 3,0, 94.51)
car7.enduro.lap_times = [106.04, 112.72, 92.39, 90.18, 87.49, 88.68, 118.64, 84.84, 87.19, 82.53, 88.81, 84.65, 119.67, 76.78, 76.21, 78.36, 81.66, 78.08, 75.68, 74.23, 76.34, 79.92]
car7.efficiency = Efficiency(88.23, 22, 5.419, 34.3)
cars.append(car7)

car8 =  Car(17 ,"Formula SAE UFMG"          , "Honda CB 600F"           ,10,     True , 51.3, 51.4, 1550, 1150, 1150, 33.4, 217,  "E25", 2) 
car8.cost = Cost(13643, 23.1, 23.0, 20.0, 27.9, -12,0, 82.0)
car8.design = Design(18.9, 24.8, 12.5, 12.6, 22.7, 20.7, 17.8, 0, 0, 130.0)
car8.business = Business(0,0,80.8)
car8.acceleration.runs = [4.174, 4.234, 4.120, 4.142]
car8.acceleration.cones = [0]*4
car8.acceleration.score = 72.57
car8.skidPad.runs = [[6.19, 6.00],[5.62, 5.71],[None,None],[5.78, 5.90]]
car8.skidPad.cones = [0,1,0,0]
car8.skidPad.score = 48.51
car8.autoX.runs = [70.56,65.83,66.75,70.75]
car8.autoX.offCourses = [0]*4
car8.autoX.cones = [0,0,2,1]
car8.autoX.score =  116.08
car8.enduro = Enduro(1623.8, 22, 2,0, 65, 172.94)
car8.enduro.lap_times = [92.04, 73.44, 76.83, 71.08, 69.69, 68.65, 69.37, 66.65, 70.82, 71.53, 74.21, 75.90, 76.06, 74.21, 73.93, 77.68, 76.94, 73.31, 73.57, 72.00, 75.60, 74.30]
car8.efficiency = Efficiency(76.95, 22, 3.782, 45.0)
cars.append(car8)

car9 =  Car(8  ,"FSAE Unicamp"              , "Yamaha MT07"             ,10,     True , 50.1, 48.7, 1528, 1200, 1200, 29.5, 220,  "E25", 3) 
car9.cost = Cost(14457, 18.5, 23.5, 13.8, 25.4, -18, 0, 63.2)
car9.design = Design(27.2, 27.9, 16.1, 14.4, 29.8, 29.6, 22.9, 0, 0, 168.0)
car9.business = Business(0,0,89.7)
car9.acceleration.runs = [4.459, 4.419, 4.330, 4.314]
car9.acceleration.cones = [0]*4
car9.acceleration.score = 61.82
car9.skidPad.runs = [[5.82, 5.53],[5.59, 5.59],[6.43, 6.66],[6.06, 6.10]]
car9.skidPad.cones = [0]*4
car9.skidPad.score = 61.04
car9.autoX.runs = [77.58,73.52,108.76,68.25]
car9.autoX.offCourses = [0]*4
car9.autoX.cones = [0]*4
car9.autoX.score = 103.24
car9.enduro = Enduro(1684.1, 22, 1, 0, 120, 134.48)
car9.enduro.lap_times = [89.94, 80.52, 75.71, 74.95, 74.27, 81.32, 73.08, 76.02, 73.82, 74.17, 75.09, 78.36, 75.32, 74.72, 72.58, 73.38, 86.70, 75.44, 73.68, 72.46, 76.12, 78.47]
car9.efficiency = Efficiency(82.10, 22, 3.056, 58.6)
cars.append(car9)

car10 = Car(23 ,"Apuama Racing"             , "Honda CB 600F"           ,10,     False, 51.2, 47.8, 1535, 1200, 1220, 31.4, 228,   None, 23) 
car10.cost = Cost(13556, 13.9, 8.5, 11.9, 28.2, -34, 0, 28.5)
car10.design = Design(19.7, 7.3, 5.7, 9.9, 21.7, 18.0, 10.3, 0, 0, 92.6)
car10.business = Business(0,0,58.1)
car10.acceleration.runs = [None]*4
car10.acceleration.cones = [0]*4
car10.acceleration.score = 0
car10.skidPad.runs = [None]*4
car10.skidPad.cones = [0]
car10.skidPad.score = 0
car10.autoX.runs = [None]*4
car10.autoX.offCourses = [0]*4
car10.autoX.cones = [0]*4
car10.autoX.score = 0
cars.append(car10)

car11 = Car(16 ,"Fórmula UFPB"              , "Yamaha XT660R"           ,13,     False, 49.9, 50.6, 1555, 1220, 1220, 34.5, 232,  "E25", 12) 
car11.cost = Cost(11497, 20.4, 17.5, 11.9, 34.6, -29, 0, 55.4)
car11.design = Design(12.8, 17.3, 10.6, 9.2, 21.8, 15.6, 12.0, 0, -5, 94.2)
car11.business = Business(0,0,71.1)
car11.acceleration.runs = [4.918,4.950,5.072,6.070]
car11.acceleration.cones = [0]*4
car11.acceleration.score = 33.78
car11.skidPad.runs = [[8.25, 7.65],[6.81, 6.82],[None,None],[5.81, 5.78]]
car11.skidPad.cones = [0,2,0,0]
car11.skidPad.score = 48.21
car11.autoX.runs = [70.96,69.73,74.00,70.62]
car11.autoX.offCourses = [1,0,0,0]
car11.autoX.cones = [3,5,3,1]
car11.autoX.score = 82.22
car11.enduro = Enduro(1250.7, 15, 3,0,0, 15.00)
car11.enduro.lap_times = [80.49, 76.24, 75.70, 75.76, 82.05, 78.30, 76.93, 85.98, 78.33, 82.35, 80.59, 89.76, 83.22, 84.80, 126.23]
car11.efficiency = Efficiency(83.78, 15, 2.062, 57.6)
cars.append(car11)

car12 = Car(42 ,"Escuderia UFSAE"           , "Honda CB 600F"           ,13,     False, 50.9, 44.9, 1600, 1391, 1337, 39.0, 233,   None, 33) 
car12.cost = Cost(14566, 8.6, 1.0, 4.4, 25.1, -30, -10, 0.0)
car12.design = Design(1.5, 4.9, 5.9, 1.9, 0.2, 3.2, 0, -60, -20, 0.0)
car12.business = Business(0,0,86.1)
car12.acceleration.runs = [None]*4
car12.acceleration.cones = [0]*4
car12.acceleration.score = 0
car12.skidPad.runs = [None]*4
car12.skidPad.cones = [0]
car12.skidPad.score = 0
car12.autoX.runs = [None]*4
car12.autoX.offCourses = [0]*4
car12.autoX.cones = [0]*4
car12.autoX.score = 0
cars.append(car12)

car13 = Car(14 ,"Protto UFSC Motorsport"    , "Yamaha XT660R"           ,10,     True , 50.2, 52.1, 1535, 1250, 1250, 32.0, 236,  "E25", 17) 
car13.cost = Cost(12767, 16.4, 15.0, 12.5, 30.7, -10, 0, 64.6)
car13.design = Design(5.4, 17.9, 9.1, 4.1, 3.6, 10.0, 11.0, 0, -25, 35.9)
car13.business = Business(0,0,81.5)
car13.acceleration.runs = [27.075, None, None, None]
car13.acceleration.cones = [0]*4
car13.acceleration.score = 4.5
car13.skidPad.runs = [None]*4
car13.skidPad.cones = [0]
car13.skidPad.score = 0
car13.autoX.runs = [85.61,76.98,83.35,78.22]
car13.autoX.offCourses = [0]*4
car13.autoX.cones = [0]*4
car13.autoX.score = 63.67
car13.enduro = Enduro(1227.4, 15, 1,0,0,15.00)
car13.enduro.lap_times = [84.83, 79.38, 80.43, 78.11, 79.37, 88.57, 82.62, 80.21, 81.11, 82.27, 82.54, 89.10, 84.78, 78.81, 77.30]
car13.efficiency = Efficiency(81.96, 15, 1.955, 65.3)
cars.append(car13)

car14 = Car(27 ,"TEC Racing Formula SAE"    , "Honda CB 600F"           ,13,     False, 48.7, 50.4, 1554, 1479, 1385, 30.0, 239,   None, 29) 
car14.cost = Cost(12783, 14.0, 13.5, 15.6, 30.6, -29, 0, 44.7)
car14.design = Design(5.3, 9.6, 5.0, 7.3, 7.0, 9.9, 7.1, -30, -5, 16.2)
car14.business = Business(0,-10,38)
car14.acceleration.runs = [None]*4
car14.acceleration.cones = [0]*4
car14.acceleration.score = 0
car14.skidPad.runs = [None]*4
car14.skidPad.cones = [0]
car14.skidPad.score = 0
car14.autoX.runs = [None]*4
car14.autoX.offCourses = [0]*4
car14.autoX.cones = [0]*4
car14.autoX.score = 0
cars.append(car14)

car15 = Car(7  ,"RS Racing UFRGS"           , "Yamaha XJ6N"             ,10,     False, 49.7, 55.1, 1550, 1200, 1200, 39.5, 240,   None, 26) 
car15.cost = Cost(13830, 13.9, 12.0, 10.6, 27.4, -26, 0, 37.9)
car15.design = Design(2.3, 5.9, 5.7, 3.4, 7.9, 10.9, 5.0, 0, 0, 41.0)
car15.business = Business(0,0,33.7)
car15.acceleration.runs = [None]*4
car15.acceleration.cones = [0]*4
car15.acceleration.score = 0
car15.skidPad.runs = [None]*4
car15.skidPad.cones = [0]
car15.skidPad.score = 0
car15.autoX.runs = [None]*4
car15.autoX.offCourses = [0]*4
car15.autoX.cones = [0]*4
car15.autoX.score = 0
car15.enduro = Enduro(106.4, 1,0,0,0,1.00)
car15.enduro.lap_times = [106.38]
cars.append(car15)

car16 = Car(12 ,"Fórmula UTFPR"             , "Yamaha YZF-R3"           ,13,     True , 50.1, 50.7, 1525, 1190, 1140, 37.4, 240,   None, 16) 
car16.cost = Cost(12389, 16.1, 25.0, 18.1, 31.9, -14, 0, 77.1)
car16.design = Design(6.4, 10.2, 6.6, 3.9, 7.0, 11.7, 6.1, 0, -5, 47.0)
car16.business = Business(0,0,94.3)
car16.acceleration.runs = [9.131,9.206,5.998,4.801]
car16.acceleration.cones = [0]*4
car16.acceleration.score = 38.66
car16.skidPad.runs = [[6.78,6.00],[None,None],[8.56, 7.34],[7.66, 6.94]]
car16.skidPad.cones = [0]*4
car16.skidPad.score = 17.70
car16.autoX.runs = [None,None,80.87,74.72]
car16.autoX.offCourses = [0]*4
car16.autoX.cones = [0,0,1,0]
car16.autoX.score = 73.04
car16.enduro = Enduro(692.2, 9, 2,0, 120, 9.00)
car16.enduro.lap_times = [87.16, 79.28, 79.57, 77.20, 79.10, 78.04, 75.84, 70.68, 69.37]
cars.append(car16)

car17 = Car(3  ,"Zeus Formula SAE"          , "Yamaha XJ6"              ,13,     False, 49.5, 50.9, 1525, 1200, 1200, 29.0, 242,  "E25", 8) 
car17.cost = Cost(11030, 19.2, 13.5, 17.5, 36.1, -19, 0, 67.3)
car17.design = Design(4.0, 16.6, 9.2, 5.7, 5.4, 9.2, 6.1, 0, 0, 56.1)
car17.business = Business(0,0,25.1)
car17.acceleration.runs = [4.744,4.945,4.618,4.520]
car17.acceleration.cones = [0]*4
car17.acceleration.score = 51.41
car17.skidPad.runs = [[6.53, 6.84],[6.16, 6.22],[6.41, 6.44],[6.13, 6.21]]
car17.skidPad.cones = [3,0,0,0]
car17.skidPad.score = 27.96
car17.autoX.runs = [84.44,79.31,80.11,74.48]
car17.autoX.offCourses = [0]*4
car17.autoX.cones = [0]*4
car17.autoX.score = 74.04
car17.enduro = Enduro(1719.6, 22, 8,0,0,157.83)
car17.enduro.lap_times = [91.16, 81.73, 77.84, 89.49, 76.40, 83.34, 76.96, 78.13, 77.16, 75.42, 75.70, 79.44, 81.05, 78.62, 75.75, 76.95, 77.11, 72.68, 74.67, 74.39, 81.89, 79.72]
car17.efficiency = Efficiency(78.89, 22, 3.130, 60.2)
cars.append(car17)

car18 = Car(15 ,"Fórmula Del-Racing"        , "Honda C B600F"           ,13,     False, 49.2, 50.4, 1550, 1200, 1200, 38.0, 247,   None, 15) 
car18.cost = Cost(11744, 20.3, 22.0, 13.8, 33.9, -32, 0, 58.0)
car18.design = Design(8.6, 7.2, 12.1, 7.1, 17.6, 16.3, 5.9, 0, 0, 74.7)
car18.business = Business(0,0,79.6)
car18.acceleration.runs = [4.763,4.543,5.126,5.805]
car18.acceleration.cones = [0]*4
car18.acceleration.score = 50.31
car18.skidPad.runs = [[6.34, 5.81],[6.13, 6.03],[6.75, 5.85],[6.07, 5.72]]
car18.skidPad.cones = [0,0,2,0]
car18.skidPad.score = 42.43
car18.autoX.runs = [76.83,75.73,78.75,72.49]
car18.autoX.offCourses = [1,1,0,0]
car18.autoX.cones = [1,1,0,0]
car18.autoX.score = 82.85
car18.enduro = Enduro(989.4, 11,0, 1,0,11.00)
car18.enduro.lap_times = [91.47, 82.80, 82.01, 79.79, 78.68, 82.44, 77.74, 78.86, 77.90, 79.22, 198.50]
cars.append(car18)

car19 = Car(20 ,"Unesp Racing"              , "Minarelli 660"           ,13,     False, 50.8, 50.7, 1550, 1240, 1240, 48.7, 247,  "E25", 20) 
car19.cost = Cost(12686, 18.4, 25.0, 10.6, 30.9, -32, 0, 52.9)
car19.design = Design(11.6, 16.9, 9.0, 5.3, 16.8, 4.0, 10.0, 0, -10, 63.5)
car19.business = Business(0,0,65)
car19.acceleration.runs = [4.973,None,None,None]
car19.acceleration.cones = [0]*4
car19.acceleration.score = 31.56
car19.skidPad.runs = [[6.91,6.89],[7.03, 7.87],None,None]
car19.skidPad.cones = [0,5,0,0]
car19.skidPad.score = 3.5
car19.autoX.runs = [81.81,77.85,81.43,97.80]
car19.autoX.offCourses = [0,2,3,3]
car19.autoX.cones = [5,7,2,4]
car19.autoX.score = 13.68
car19.enduro = Enduro(1957.1, 20, 58, 6, 21,20.00)
car19.enduro.lap_times = [102.60, 118.81, 93.98, 100.59, 119.54, 157.60, 107.69, 105.45, 102.58, 101.03, 112.60, 94.37, 124.87, 102.35, 104.18, 97.33, 103.72, 107.82, 112.55, 107.43]
car19.efficiency = Efficiency(110.70, 20, 2.552, 39.6)
cars.append(car19)

car20 = Car(25 ,"UTFast F-SAE Racing"       , "Kawasaki Ninja 300"      ,13,     False, 51.1, 47.4, 1535, 1200, 1200, 55.0, 253,   None, 24) 
car20.cost = Cost(9778, 14.9, 5.0, 11.9, 40.0, -16, 0, 55.8)
car20.design = Design(4.5, 12.7, 5.7, 3.4, 1.2, 14.7, 5.2, 0, 0, 47.4)
car20.business = Business(0,0,56.9)
car20.acceleration.runs = [None]*4
car20.acceleration.cones = [0]*4
car20.acceleration.score = 0
car20.skidPad.runs = [None]*4
car20.skidPad.cones = [0]
car20.skidPad.score = 0
car20.autoX.runs = [None]*4
car20.autoX.offCourses = [0]*4
car20.autoX.cones = [0]*4
car20.autoX.score = 0
cars.append(car20)

car21 = Car(13 ,"Cheetah Racing"            , "Yamaha MT-07"            ,10,     True , 49.1, 48.5, 1540, 1250, 1200, 35.5, 254, "E100", 11) 
car21.cost = Cost(17050, 19.3, 7.0, 13.8, 17.3, -21, 0, 36.4)
car21.design = Design(15.6, 18.1, 6.2, 3.9, 14.5, 20.6, 10.9, 0, 0, 89.7)
car21.business = Business(0,0,54.1)
car21.acceleration.runs = [4.596,4.646,4.682,4.547]
car21.acceleration.cones = [0]*4
car21.acceleration.score = 50.12
car21.skidPad.runs = [[7.37, 6.75],[6.75, 7.15],[9.50, 7.69],[6.75,None]]
car21.skidPad.cones = [3,1,0,1]
car21.skidPad.score = 3.5
car21.autoX.runs = [80.47,74.29,None,None]
car21.autoX.offCourses = [0,2,0,0]
car21.autoX.cones = [1,2,0,0]
car21.autoX.score = 43.06
car21.enduro = Enduro(1887.2, 22, 5, 1,0,101.19)
car21.enduro.lap_times = [86.84, 82.18, 84.02, 84.66, 93.84, 94.22, 85.45, 86.29, 86.63, 82.43, 81.72, 93.20, 116.37, 86.83, 82.28, 81.62, 88.03, 80.18, 81.49, 81.29, 84.35, 93.24]
car21.efficiency = Efficiency(87.14, 22, 3.167, 88.6)
cars.append(car21)

car22 = Car(10 ,"UFPR Fórmula"              , "Kawasaki ER-6n"          ,10,     True , 50.7, 50.2, 1530, 1200, 1200, 35.0, 256,  "E25", 14) 
car22.cost = Cost(10692, 12.7, 11.5, 13.1, 37.1, -27, 0, 47.4)
car22.design = Design(4.9, 13.9, 8.8, 5.9, 12.8, 12.9, 11.3, 0, -5, 65.5)
car22.business = Business(0,0,21.3)
car22.acceleration.runs = [5.235,7.892,4.574,7.644]
car22.acceleration.cones = [0]*4
car22.acceleration.score = 48.84
car22.skidPad.runs = [[6.15, 6.28],[6.10, 6.47],[6.47, 6.63],[6.25, None]]
car22.skidPad.cones = [0]*4
car22.skidPad.score = 25.77
car22.autoX.runs = [72.7,70.46,76.56,72.02]
car22.autoX.offCourses = [0]*4
car22.autoX.cones = [0]*4
car22.autoX.score = 92.29
car22.enduro = Enduro(1924.9, 22, 1,0, 120,66.86)
car22.enduro.lap_times = [93.26, 90.12, 90.77, 87.93, 86.86, 81.10, 83.40, 85.72, 82.08, 82.65, 86.21, 101.48, 91.26, 87.16, 82.44, 86.34, 83.76, 91.50, 89.94, 89.28, 87.89, 83.82]
car22.efficiency = Efficiency(93.04, 22, 3.358, 39.2)
cars.append(car22)

car23 = Car(26 ,"Buffalo de Formula SAE"    , "Honda CB 600F"           ,13,     False, 50.3, 52.8, 1650, 1300, 1300, 47.0, 257,   None, 25) 
car23.cost = Cost(11885, 22.3, 5.0, 14.4, 33.4, -15, 0, 60.1)
car23.design = Design(1.3, 6.6, 2.2, 3.4, 10.4, 7.8, 7.4, 0, -25, 14.1)
car23.business = Business(0,-5,48.1)
car23.acceleration.runs = [5.809,6.210,5.494,4.801]
car23.acceleration.cones = [0]*4
car23.acceleration.score = 38.66
car23.skidPad.runs = [[7.75,None],[7.56, 7.06],None,None]
car23.skidPad.cones = [0]*4
car23.skidPad.score = 3.5
car23.autoX.runs = [101.41,90.60,None,None]
car23.autoX.offCourses = [1,0,0,0]
car23.autoX.cones = [0]*4
car23.autoX.score = 17.16
car23.enduro = Enduro(211.4, 2,0,0,0,2.00)
car23.enduro.lap_times = [108.16, 103.28]
cars.append(car23)

car24 = Car(9  ,"Fórmula CEM IC"            , "Yamaha XT 660"           ,13,     False, 50.2, 49.4, 1540, 1250, 1230, 45.0, 263,  "E25", 10) 
car24.cost = Cost(12433, 20.1, 11.0, 13.8, 31.7, -33, 0, 43.6)
car24.design = Design(14.6, 14.2, 5.0, 7.5, 12.3, 10.9, 10.7, 0, -10, 65.2)
car24.business = Business(0,0,83)
car24.acceleration.runs = [5.386,5.330,None,None]
car24.acceleration.cones = [0]*4
car24.acceleration.score = 18.30
car24.skidPad.runs = [[7.75, 6.65],[6.81, 6.72],[7.28, 6.38],[6.56, 6.03]]
car24.skidPad.cones = [0,0,2,0]
car24.skidPad.score = 22
car24.autoX.runs = [79.38,None,83.81,75.13]
car24.autoX.offCourses = [0,0,1,0]
car24.autoX.cones = [0]*4
car24.autoX.score = 71.27
car24.enduro = Enduro(1915.5, 22,0, 1,0, 96.07)
car24.enduro.lap_times = [101.47, 88.49, 89.60, 84.88, 87.26, 103.72, 82.07, 81.49, 83.63, 92.76, 84.84, 119.41, 84.85, 85.31, 87.14, 88.49, 82.73, 83.46, 78.74, 82.98, 80.11, 82.05]
car24.efficiency = Efficiency(87.98, 22, 2.008, 100.0)
cars.append(car24)

car25 = Car(24 ,"FEB Racing"                , "Honda CB 600F"           ,13,     False, 49.7, 47.3, 1535, 1200, 1150, 37.6, 264,   None, 22) 
car25.cost = Cost(14049, 13.1, 6.5, 6.9, 26.7, -25, 0, 28.2)
car25.design = Design(16.1, 13.3, 4.8, 7.2, 8.6, 13.6, 10.4, 0, 0, 74.0)
car25.business = Business(0,0,90.6)
car25.acceleration.runs = [None]*4
car25.acceleration.cones = [0]*4
car25.acceleration.score = 0
car25.skidPad.runs = [None]*4
car25.skidPad.cones = [0]
car25.skidPad.score = 0
car25.autoX.runs = [None]*4
car25.autoX.offCourses = [0]*4
car25.autoX.cones = [0]*4
car25.autoX.score = 0
cars.append(car25)

car26 = Car(48 ,"UFU Racing"                , "Honda CB 600F"           ,13,     False, 51.2, 49.1, 1200, 1011, 937 , 46.0, 267,   None, 41) 
car26.cost = Cost(9937, 16.9, 3.5, 6.3, 39.5, -40, 0, 26.2)
car26.design = Design(1.8, 3.3, 2.0, 6.5, 1.8, 1.8, 1.5, -30, -20, 0.0)
car26.business = Business(0,0,23.3)
car26.acceleration.runs = [None]*4
car26.acceleration.cones = [0]*4
car26.acceleration.score = 0
car26.skidPad.runs = [None]*4
car26.skidPad.cones = [0]
car26.skidPad.score = 0
car26.autoX.runs = [None]*4
car26.autoX.offCourses = [0]*4
car26.autoX.cones = [0]*4
car26.autoX.score = 0
cars.append(car26)

car27 = Car(21 ,"Fênix Racing"              , "Honda CB 600F"           ,13,     True , 50.4, 47.5, 1540, 1240, 1230, 33.0, 274,  "E25", 18) 
car27.cost = Cost(11401, 16.6, 12.0, 15.6, 34.9, -12, 0, 67.1)
car27.design = Design(7.6, 16.3, 8.1, 3.8, 11.5, 13.1, 7.6, 0, -5, 63.0)
car27.business = Business(0,0,82.6)
car27.acceleration.runs = [5.998,6.035,4.9]
car27.acceleration.cones = [0]*4
car27.acceleration.score = 34.51
car27.skidPad.runs = [[7.16, 6.97],[6.34, 6.28],None,None]
car27.skidPad.cones = [0]*4
car27.skidPad.score = 21.31
car27.autoX.runs = [97.78,None,None,None]
car27.autoX.offCourses = [0]*4
car27.autoX.cones = [0]*4
car27.autoX.score = 6.5
car27.enduro = Enduro(1647.4, 16, 2,0,0,16.00)
car27.enduro.lap_times = [114.45, 113.74, 107.48, 108.95, 103.07, 107.57, 101.28, 105.70, 107.37, 103.37, 99.66, 100.22, 98.73, 91.85, 94.71, 93.28]
car27.efficiency = Efficiency(103.21, 16, 3.358, 12.0)
cars.append(car27)

car28 = Car(19 ,"FSAE Carcará"              , "Yamaha XT660R"           ,13,     False, 49.7, 48.2, 1550, 1300, 1200, 49.6, 276,   None, 21) 
car28.cost = Cost(16165, 20.1, 13.0, 6.3, 20.1, -19, 0, 40.5)
car28.design = Design(12.7, 6.2, 6.8, 6.2, 12.9, 17.6, 5.9, 0, -5, 63.4)
car28.business = Business(0,0,89.9)
car28.acceleration.runs = [None]*4
car28.acceleration.cones = [0]*4
car28.acceleration.score = 0
car28.skidPad.runs = [None]*4
car28.skidPad.cones = [0]
car28.skidPad.score = 0
car28.autoX.runs = [None]*4
car28.autoX.offCourses = [0]*4
car28.autoX.cones = [0]*4
car28.autoX.score = 0
cars.append(car28)

car29 = Car(18 ,"Icarus UFRJ de Formula SAE", "Honda CB 600F"           ,13,     False, 50.5, 51.6, 1540, 1170, 1170, 46.0, 280,  "E25", 9) 
car29.cost = Cost(15345, 20.1, 25.5, 22.5, 22.6, -14, 0, 76.7)
car29.design = Design(14.3, 15.4, 11.7, 11.4, 19.1, 17.1, 14.9, 0, -15, 88.9)
car29.business = Business(0,0,86.9)
car29.acceleration.runs = [5.992,5.938,4.452,4.638]
car29.acceleration.cones = [0]*4
car29.acceleration.score = 54.74
car29.skidPad.runs = [[5.97, 6.00],[5.90, 5.81],[6.03, 5.90],[5.78, 5.91]]
car29.skidPad.cones = [0]*4
car29.skidPad.score = 45.28
car29.autoX.runs = [82.96,75.06,73.24,69.06]
car29.autoX.offCourses = [0]*4
car29.autoX.cones = [0]*4
car29.autoX.score = 99.13
car29.enduro = Enduro(1410.6, 19, 0,1,0,19.00)
car29.enduro.lap_times = [77.85, 73.21, 71.71, 73.38, 72.01, 79.61, 71.93, 70.74, 70.73, 70.44, 70.81, 80.20, 74.55, 75.13, 99.01, 75.57, 74.44, 75.40, 73.94]
car29.efficiency = Efficiency(75.30, 19, 4.124, 28.8)
cars.append(car29)

car30 = Car(29 ,"Iron Racers"               , "Honda CB 600F"           ,13,     False, 50.8, 48.6, 1586, 1479, 1474, 50.0, 281,   None, 31) 
car30.cost = Cost(17593, 21.0, 9.0, 8.8, 15.6, -39, 0, 15.4)
car30.design = Design(2.9, 6.1, 2.9, 3.0, 4.0, 4.0, 2.9, 0, -15, 10.6)
car30.business = Business(0,0,46.6)
car30.acceleration.runs = [None]*4
car30.acceleration.cones = [0]*4
car30.acceleration.score = 0
car30.skidPad.runs = [None]*4
car30.skidPad.cones = [0]
car30.skidPad.score = 0
car30.autoX.runs = [None]*4
car30.autoX.offCourses = [0]*4
car30.autoX.cones = [0]*4
car30.autoX.score = 0
cars.append(car30)

car31 = Car(34 ,"KRT UFBA"                  , "Yamaha XT660"            ,14.3,   False, 49.9, 44.7, 1540, 1200, 1150, 43.7, 287,   None, 36) 
car31.cost = Cost(13116, 19.5, 13.0, 10.6, 29.6, -44, 0, 28.7)
car31.design = Design(4.4, 7.8, 5.0, 3.8, 8.7, 15.1, 8.1, -90, -10, 0.0)
car31.business = Business(0,0,73.9)
car31.acceleration.runs = [None]*4
car31.acceleration.cones = [0]*4
car31.acceleration.score = 0
car31.skidPad.runs = [None]*4
car31.skidPad.cones = [0]
car31.skidPad.score = 0
car31.autoX.runs = [None]*4
car31.autoX.offCourses = [0]*4
car31.autoX.cones = [0]*4
car31.autoX.score = 0
car31.enduro = Enduro(292.6, 2, 3, 1,0,2.00)
car31.enduro.lap_times = [149.77, 146.80]
cars.append(car31)

car32 = Car(30 ,"Optimus FSAE UFG"          , "Yamaha XT 660R"          ,13,     False, 50.9, 42.2, 1610, 1310, 1307, 30.0, 294,   None, 32)
car32.cost = Cost(14513, 8.4, 3.5, 11.9, 25.2, -28, 0, 21.0)
car32.design = Design(3.0, 4.7, 4.2, 2.0, 0.5, 3.9, 0, 0, -5, 13.4)
car32.business = Business(0,0,32.4)
car32.acceleration.runs = [None]*4
car32.acceleration.cones = [0]*4
car32.acceleration.score = 0
car32.skidPad.runs = [None]*4
car32.skidPad.cones = [0]
car32.skidPad.score = 0
car32.autoX.runs = [None]*4
car32.autoX.offCourses = [0]*4
car32.autoX.cones = [0]*4
car32.autoX.score = 0
cars.append(car32)

car33 = Car(38 ,"PUCPR Racing"              , "Yamaha XJ6 N"            ,13,     False, 50.6, 50.2, 1727, 1475, 1469, 54.0, 306,   None, 27) 
car33.cost = Cost(21878, 9.4, 13.0, 6.9, 2.2, -41, 0, 0.0)
car33.design = Design(0.8, 4.2, 1.5, 2.4, 3.0, 4.4, 2.9, 0, -5, 14.2)
car33.business = Business(0,0,95.5)
car33.acceleration.runs = [None]*4
car33.acceleration.cones = [0]*4
car33.acceleration.score = 0
car33.skidPad.runs = [None]*4
car33.skidPad.cones = [0]
car33.skidPad.score = 0
car33.autoX.runs = [None]*4
car33.autoX.offCourses = [0]*4
car33.autoX.cones = [0]*4
car33.autoX.score = 0
cars.append(car33)

car34 = Car(32 ,"Sátirus"                   , "Honda CB 650F"           ,13,     False, 50.4, 45.9, 1570, 1200, 1220, 31.4, 331,   None, 39)
car34.cost = Cost(10811, 9.2, 5.0, 6.3, 36.8, -46, 0, 11.3)
car34.design = Design(0, 4.1, 1.3, 1.5, 4.7, 0.6, 2.9, -30, -35, 0.0)
car34.business = Business(0,0,55.2)
car34.acceleration.runs = [None]*4
car34.acceleration.cones = [0]*4
car34.acceleration.score = 0
car34.skidPad.runs = [None]*4
car34.skidPad.cones = [0]
car34.skidPad.score = 0
car34.autoX.runs = [None]*4
car34.autoX.offCourses = [0]*4
car34.autoX.cones = [0]*4
car34.autoX.score = 0
cars.append(car34)