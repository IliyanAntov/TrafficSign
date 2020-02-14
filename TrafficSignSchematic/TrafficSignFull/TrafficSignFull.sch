EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Full traffic sign schematic"
Date "2020-02-15"
Rev "1"
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L CustomSymbols:BQ24650-MPPT-Controller U3
U 1 1 5E1C2763
P 9075 1400
F 0 "U3" H 9075 1600 50  0000 C CNN
F 1 "BQ24650 charge controller" H 9050 1200 50  0000 C CNN
F 2 "" H 9075 1400 50  0001 C CNN
F 3 "" H 9075 1400 50  0001 C CNN
	1    9075 1400
	1    0    0    -1  
$EndComp
$Comp
L Device:Solar_Cell SC1
U 1 1 5E1AF05D
P 8175 1450
F 0 "SC1" H 7975 1550 50  0000 C CNN
F 1 "10W" H 7975 1450 50  0000 C CNN
F 2 "" V 8175 1510 50  0001 C CNN
F 3 "~" V 8175 1510 50  0001 C CNN
	1    8175 1450
	1    0    0    -1  
$EndComp
Wire Wire Line
	8175 1250 8175 1200
Wire Wire Line
	8175 1200 8475 1200
Wire Wire Line
	8475 1200 8475 1350
Wire Wire Line
	8475 1350 8675 1350
Wire Wire Line
	8175 1550 8175 1600
Wire Wire Line
	8475 1600 8475 1450
Wire Wire Line
	8475 1450 8675 1450
Wire Wire Line
	10475 5975 10775 5975
Connection ~ 10475 5975
Wire Wire Line
	10475 5925 10475 5975
Wire Wire Line
	10475 5575 10775 5575
Connection ~ 10475 5575
Wire Wire Line
	10475 5625 10475 5575
$Comp
L Device:C C7
U 1 1 5E2FC6B7
P 10475 5775
F 0 "C7" H 10575 5825 50  0000 L CNN
F 1 "100nF" H 10575 5750 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 10513 5625 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/5920/" H 10475 5775 50  0001 C CNN
	1    10475 5775
	1    0    0    -1  
$EndComp
Wire Wire Line
	10475 4675 10775 4675
Connection ~ 10475 4675
Wire Wire Line
	10475 4625 10475 4675
Wire Wire Line
	10475 4275 10775 4275
Connection ~ 10475 4275
Wire Wire Line
	10475 4325 10475 4275
$Comp
L Device:C C6
U 1 1 5E2B96D7
P 10475 4475
F 0 "C6" H 10575 4525 50  0000 L CNN
F 1 "100nF" H 10575 4450 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 10513 4325 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/5920/" H 10475 4475 50  0001 C CNN
	1    10475 4475
	1    0    0    -1  
$EndComp
Text GLabel 4725 6600 2    50   Input ~ 0
SIM_RST
Text GLabel 4425 1100 0    50   Input ~ 0
SIM_RST
Wire Wire Line
	5175 2150 5200 2150
Wire Wire Line
	2550 4550 2700 4550
Connection ~ 2550 4550
Wire Wire Line
	2550 4600 2550 4550
Wire Wire Line
	2400 4550 2550 4550
Wire Wire Line
	2550 4250 2700 4250
Connection ~ 2550 4250
Wire Wire Line
	2550 4200 2550 4250
Wire Wire Line
	2400 4250 2550 4250
$Comp
L Device:C C5
U 1 1 5E5C89EE
P 2700 4400
F 0 "C5" H 2800 4450 50  0000 L CNN
F 1 "100n" H 2800 4375 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 2738 4250 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/5920/" H 2700 4400 50  0001 C CNN
	1    2700 4400
	1    0    0    -1  
$EndComp
$Comp
L Device:C C4
U 1 1 5E5BEE3A
P 2400 4400
F 0 "C4" H 2175 4450 50  0000 L CNN
F 1 "100n" H 2100 4375 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 2438 4250 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/5920/" H 2400 4400 50  0001 C CNN
	1    2400 4400
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0123
U 1 1 5E5B557C
P 2550 4600
F 0 "#PWR0123" H 2550 4350 50  0001 C CNN
F 1 "GND" H 2555 4427 50  0000 C CNN
F 2 "" H 2550 4600 50  0001 C CNN
F 3 "" H 2550 4600 50  0001 C CNN
	1    2550 4600
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0122
U 1 1 5E5ABDC2
P 2550 4200
F 0 "#PWR0122" H 2550 4050 50  0001 C CNN
F 1 "+5V" H 2565 4373 50  0000 C CNN
F 2 "" H 2550 4200 50  0001 C CNN
F 3 "" H 2550 4200 50  0001 C CNN
	1    2550 4200
	1    0    0    -1  
$EndComp
Wire Wire Line
	2875 6850 2875 6800
$Comp
L power:GND #PWR0121
U 1 1 5E2B082D
P 2875 6850
F 0 "#PWR0121" H 2875 6600 50  0001 C CNN
F 1 "GND" H 2880 6677 50  0000 C CNN
F 2 "" H 2875 6850 50  0001 C CNN
F 3 "" H 2875 6850 50  0001 C CNN
	1    2875 6850
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0120
U 1 1 5E56BC18
P 10775 5575
F 0 "#PWR0120" H 10775 5425 50  0001 C CNN
F 1 "+5V" H 10790 5748 50  0000 C CNN
F 2 "" H 10775 5575 50  0001 C CNN
F 3 "" H 10775 5575 50  0001 C CNN
	1    10775 5575
	1    0    0    -1  
$EndComp
$Comp
L power:+4V #PWR0119
U 1 1 5E55845B
P 10775 4275
F 0 "#PWR0119" H 10775 4125 50  0001 C CNN
F 1 "+4V" H 10790 4448 50  0000 C CNN
F 2 "" H 10775 4275 50  0001 C CNN
F 3 "" H 10775 4275 50  0001 C CNN
	1    10775 4275
	1    0    0    -1  
$EndComp
Wire Wire Line
	5050 1850 5200 1850
$Comp
L power:+4V #PWR0117
U 1 1 5E526B11
P 5050 1850
F 0 "#PWR0117" H 5050 1700 50  0001 C CNN
F 1 "+4V" H 5050 2000 50  0000 C CNN
F 2 "" H 5050 1850 50  0001 C CNN
F 3 "" H 5050 1850 50  0001 C CNN
	1    5050 1850
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR0115
U 1 1 5E4CDF3C
P 7575 4075
F 0 "#PWR0115" H 7575 3925 50  0001 C CNN
F 1 "+12V" H 7590 4248 50  0000 C CNN
F 2 "" H 7575 4075 50  0001 C CNN
F 3 "" H 7575 4075 50  0001 C CNN
	1    7575 4075
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR0114
U 1 1 5E4C461B
P 7575 5375
F 0 "#PWR0114" H 7575 5225 50  0001 C CNN
F 1 "+12V" H 7590 5548 50  0000 C CNN
F 2 "" H 7575 5375 50  0001 C CNN
F 3 "" H 7575 5375 50  0001 C CNN
	1    7575 5375
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0113
U 1 1 5E49DEF5
P 7575 4675
F 0 "#PWR0113" H 7575 4425 50  0001 C CNN
F 1 "GND" H 7580 4502 50  0000 C CNN
F 2 "" H 7575 4675 50  0001 C CNN
F 3 "" H 7575 4675 50  0001 C CNN
	1    7575 4675
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0112
U 1 1 5E4944C4
P 10775 4675
F 0 "#PWR0112" H 10775 4425 50  0001 C CNN
F 1 "GND" H 10780 4502 50  0000 C CNN
F 2 "" H 10775 4675 50  0001 C CNN
F 3 "" H 10775 4675 50  0001 C CNN
	1    10775 4675
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0111
U 1 1 5E48ABD8
P 10775 5975
F 0 "#PWR0111" H 10775 5725 50  0001 C CNN
F 1 "GND" H 10780 5802 50  0000 C CNN
F 2 "" H 10775 5975 50  0001 C CNN
F 3 "" H 10775 5975 50  0001 C CNN
	1    10775 5975
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0110
U 1 1 5E4813F6
P 7575 5975
F 0 "#PWR0110" H 7575 5725 50  0001 C CNN
F 1 "GND" H 7580 5802 50  0000 C CNN
F 2 "" H 7575 5975 50  0001 C CNN
F 3 "" H 7575 5975 50  0001 C CNN
	1    7575 5975
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0109
U 1 1 5E476F4D
P 2250 1850
F 0 "#PWR0109" H 2250 1700 50  0001 C CNN
F 1 "+5V" H 2265 2023 50  0000 C CNN
F 2 "" H 2250 1850 50  0001 C CNN
F 3 "" H 2250 1850 50  0001 C CNN
	1    2250 1850
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0108
U 1 1 5E464023
P 2250 2150
F 0 "#PWR0108" H 2250 1900 50  0001 C CNN
F 1 "GND" H 2255 1977 50  0000 C CNN
F 2 "" H 2250 2150 50  0001 C CNN
F 3 "" H 2250 2150 50  0001 C CNN
	1    2250 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	1225 2000 1225 2400
Connection ~ 1225 2000
Wire Wire Line
	1225 2000 1625 2000
Wire Wire Line
	1225 2400 1225 2650
Connection ~ 1225 2400
Wire Wire Line
	1225 2400 1625 2400
Wire Wire Line
	1225 1200 1625 1200
Wire Wire Line
	1225 1200 1225 2000
$Comp
L power:GND #PWR0105
U 1 1 5E40D0CE
P 1225 2650
F 0 "#PWR0105" H 1225 2400 50  0001 C CNN
F 1 "GND" H 1230 2477 50  0000 C CNN
F 2 "" H 1225 2650 50  0001 C CNN
F 3 "" H 1225 2650 50  0001 C CNN
	1    1225 2650
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0104
U 1 1 5E3F8F53
P 4620 5000
F 0 "#PWR0104" H 4620 4850 50  0001 C CNN
F 1 "+5V" H 4620 5150 50  0000 C CNN
F 2 "" H 4620 5000 50  0001 C CNN
F 3 "" H 4620 5000 50  0001 C CNN
	1    4620 5000
	1    0    0    -1  
$EndComp
Wire Wire Line
	3525 3650 3525 3800
$Comp
L power:GND #PWR0103
U 1 1 5E3D329E
P 3675 3650
F 0 "#PWR0103" H 3675 3400 50  0001 C CNN
F 1 "GND" H 3680 3477 50  0000 C CNN
F 2 "" H 3675 3650 50  0001 C CNN
F 3 "" H 3675 3650 50  0001 C CNN
	1    3675 3650
	1    0    0    -1  
$EndComp
Text Label 4425 4700 0    50   ~ 0
TXD
Text Label 4425 4800 0    50   ~ 0
RXD
Text Label 4475 4600 0    50   ~ 0
2
Text Label 4475 4500 0    50   ~ 0
3
Text Label 4475 4400 0    50   ~ 0
4
Text Label 4475 4300 0    50   ~ 0
5
Text Label 4475 4200 0    50   ~ 0
6
Text Label 4475 4100 0    50   ~ 0
7
Wire Wire Line
	4125 5100 4875 5100
Wire Wire Line
	4125 5200 4875 5200
Text Label 4475 5600 0    50   ~ 0
A0
Text Label 4475 5500 0    50   ~ 0
A1
Text Label 4475 5400 0    50   ~ 0
A2
Text Label 4475 5300 0    50   ~ 0
A3
Text Label 4475 5200 0    50   ~ 0
A4
Text Label 4475 5100 0    50   ~ 0
A5
Wire Wire Line
	4525 5900 4525 6000
Wire Wire Line
	4525 6000 4825 6000
Wire Wire Line
	4125 5800 4525 5800
Wire Wire Line
	4525 5800 4525 5700
Wire Wire Line
	4525 5700 4825 5700
Wire Wire Line
	4125 6000 4475 6000
Wire Wire Line
	4475 6000 4475 6100
Wire Wire Line
	4475 6100 4875 6100
Text Label 4525 6600 0    50   ~ 0
8
Text Label 4525 6500 0    50   ~ 0
9
Text Label 4475 6400 0    50   ~ 0
10
Text Label 4475 6300 0    50   ~ 0
11
Text Label 4475 6200 0    50   ~ 0
12
Text Label 4475 6100 0    50   ~ 0
13
Wire Wire Line
	4125 6100 4425 6100
Wire Wire Line
	4425 6100 4425 6200
Wire Wire Line
	4425 6200 4875 6200
Wire Wire Line
	4125 6200 4375 6200
Wire Wire Line
	4375 6200 4375 6300
Wire Wire Line
	4375 6300 4725 6300
Wire Wire Line
	4125 6300 4325 6300
Wire Wire Line
	4325 6300 4325 6400
Wire Wire Line
	4325 6400 4725 6400
Wire Wire Line
	4125 6400 4275 6400
Wire Wire Line
	4275 6400 4275 6500
Wire Wire Line
	4275 6500 4725 6500
Wire Wire Line
	4125 6500 4225 6500
Wire Wire Line
	4225 6500 4225 6600
Text GLabel 4725 4600 2    50   Input ~ 0
R0
Text GLabel 4725 4500 2    50   Input ~ 0
G0
Text GLabel 4725 4400 2    50   Input ~ 0
B0
Wire Wire Line
	4125 4400 4725 4400
Wire Wire Line
	4125 4500 4725 4500
Wire Wire Line
	4125 4600 4725 4600
Text GLabel 4725 4300 2    50   Input ~ 0
R1
Text GLabel 4725 4200 2    50   Input ~ 0
G1
Text GLabel 4725 4100 2    50   Input ~ 0
B1
Wire Wire Line
	4125 4300 4725 4300
Wire Wire Line
	4125 4200 4725 4200
Wire Wire Line
	4125 4100 4725 4100
Text GLabel 4775 5600 2    50   Input ~ 0
A
Text GLabel 4775 5500 2    50   Input ~ 0
B
Text GLabel 4775 5400 2    50   Input ~ 0
C
Text GLabel 4775 5300 2    50   Input ~ 0
D
Wire Wire Line
	4125 5300 4775 5300
Wire Wire Line
	4125 5400 4775 5400
Wire Wire Line
	4125 5500 4775 5500
Wire Wire Line
	4125 5600 4775 5600
Text GLabel 4725 6300 2    50   Input ~ 0
CLK
Text GLabel 4725 6400 2    50   Input ~ 0
STB
Text GLabel 4725 6500 2    50   Input ~ 0
OE
$Comp
L Device:R R3
U 1 1 5E100EA7
P 4175 1850
F 0 "R3" H 4225 1900 50  0000 L CNN
F 1 "16k" H 4225 1825 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4105 1850 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/25851/" H 4175 1850 50  0001 C CNN
	1    4175 1850
	1    0    0    -1  
$EndComp
Wire Wire Line
	4100 1700 4175 1700
Wire Wire Line
	4505 5000 4620 5000
Wire Wire Line
	2925 6500 2875 6500
Wire Wire Line
	3625 6950 3625 6800
Wire Wire Line
	3525 6800 3525 6950
Wire Wire Line
	3525 6950 3625 6950
Connection ~ 3625 6950
Wire Wire Line
	4825 5700 4875 5700
Connection ~ 4825 5700
Wire Wire Line
	5325 5700 5175 5700
Wire Wire Line
	4825 6000 4875 6000
Connection ~ 4825 6000
$Comp
L Device:R R4
U 1 1 5E2884D8
P 4175 2250
F 0 "R4" H 4225 2300 50  0000 L CNN
F 1 "20k" H 4225 2225 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4105 2250 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/3884/" H 4175 2250 50  0001 C CNN
	1    4175 2250
	1    0    0    -1  
$EndComp
$Comp
L Device:C C2
U 1 1 5E17AFFA
P 5025 6000
F 0 "C2" V 4975 6100 50  0000 C CNN
F 1 "22pF" V 5075 6150 50  0000 C CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 5063 5850 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/27466/" H 5025 6000 50  0001 C CNN
	1    5025 6000
	0    1    1    0   
$EndComp
$Comp
L Device:C C1
U 1 1 5E16B77E
P 5025 5700
F 0 "C1" V 4975 5800 50  0000 C CNN
F 1 "22pF" V 5075 5850 50  0000 C CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 5063 5550 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/27466/" H 5025 5700 50  0001 C CNN
	1    5025 5700
	0    1    1    0   
$EndComp
$Comp
L Device:Crystal Y1
U 1 1 5E152994
P 4825 5850
F 0 "Y1" V 4725 5600 50  0000 L CNN
F 1 "16MHz" V 4825 5450 50  0000 L CNN
F 2 "Crystal:Crystal_HC49-U_Vertical" H 4825 5850 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/27238/" H 4825 5850 50  0001 C CNN
	1    4825 5850
	0    1    1    0   
$EndComp
NoConn ~ 4875 5100
NoConn ~ 4875 5200
NoConn ~ 4875 6100
NoConn ~ 4875 6200
Wire Wire Line
	5175 6000 5325 6000
$Comp
L power:GND #PWR0102
U 1 1 5E2916ED
P 5325 6050
F 0 "#PWR0102" H 5325 5800 50  0001 C CNN
F 1 "GND" H 5330 5877 50  0000 C CNN
F 2 "" H 5325 6050 50  0001 C CNN
F 3 "" H 5325 6050 50  0001 C CNN
	1    5325 6050
	1    0    0    -1  
$EndComp
Wire Wire Line
	5325 6050 5325 6000
Connection ~ 5325 6000
Wire Wire Line
	5325 6000 5325 5700
$Comp
L power:+5V #PWR0101
U 1 1 5E2B9136
P 3875 6950
F 0 "#PWR0101" H 3875 6800 50  0001 C CNN
F 1 "+5V" H 3890 7123 50  0000 C CNN
F 2 "" H 3875 6950 50  0001 C CNN
F 3 "" H 3875 6950 50  0001 C CNN
	1    3875 6950
	1    0    0    -1  
$EndComp
Wire Wire Line
	3625 6950 3875 6950
Wire Wire Line
	4125 5900 4525 5900
$Comp
L MCU_Microchip_ATmega:ATmega328P-PU U1
U 1 1 5DF560CB
P 3525 5300
F 0 "U1" H 2975 5150 50  0000 R CNN
F 1 "ATmega328P-PU" H 2975 5250 50  0000 R CNN
F 2 "Package_DIP:DIP-28_W7.62mm" H 3525 5300 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/ATmega328_P%20AVR%20MCU%20with%20picoPower%20Technology%20Data%20Sheet%2040001984A.pdf" H 3525 5300 50  0001 C CNN
	1    3525 5300
	1    0    0    1   
$EndComp
$Comp
L Device:CP COUT1
U 1 1 5DFA6ACC
P 9975 4475
F 0 "COUT1" H 10075 4475 50  0000 L CNN
F 1 "16V/470uF" H 10000 4375 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm" H 10013 4325 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/36876/" H 9975 4475 50  0001 C CNN
	1    9975 4475
	1    0    0    -1  
$EndComp
Connection ~ 2350 1850
Wire Wire Line
	2350 1850 2250 1850
Wire Wire Line
	2350 1950 2350 1850
Connection ~ 2350 2150
Wire Wire Line
	2350 2150 2250 2150
Wire Wire Line
	2350 2050 2350 2150
Wire Wire Line
	2450 2150 2350 2150
Wire Wire Line
	2450 2050 2350 2050
Wire Wire Line
	2450 1950 2350 1950
Wire Wire Line
	2450 1850 2350 1850
$Comp
L Connector_Generic:Conn_01x04 J2
U 1 1 5E3512ED
P 2650 1950
F 0 "J2" H 2600 2300 50  0000 L CNN
F 1 "LED matrix power" H 2450 2200 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-396_A-41791-0004_1x04_P3.96mm_Vertical" H 2650 1950 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/25223/" H 2650 1950 50  0001 C CNN
	1    2650 1950
	1    0    0    -1  
$EndComp
$Comp
L Device:CP CIN2
U 1 1 5E3391F1
P 7975 5675
F 0 "CIN2" H 7675 5725 50  0000 L CNN
F 1 "35V/680uF" H 7425 5625 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm" H 8013 5525 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/44664/" H 7975 5675 50  0001 C CNN
	1    7975 5675
	1    0    0    -1  
$EndComp
Text Notes 7625 4675 0    50   ~ 0
IN-
Text Notes 7625 4075 0    50   ~ 0
IN+
Text Notes 7625 5975 0    50   ~ 0
IN-
Text Notes 7625 5375 0    50   ~ 0
IN+
Text Notes 10525 4675 0    50   ~ 0
OUT-
Text Notes 10525 4275 0    50   ~ 0
OUT+
Text Notes 10525 5575 0    50   ~ 0
OUT+
Text Notes 10525 5975 0    50   ~ 0
OUT-
Wire Wire Line
	9975 5325 9975 5575
Wire Wire Line
	9225 5375 9225 5325
Wire Wire Line
	9975 5325 9225 5325
$Comp
L Device:L L2
U 1 1 5E20713A
P 9675 5575
F 0 "L2" V 9865 5575 50  0000 C CNN
F 1 "33uH" V 9774 5575 50  0000 C CNN
F 2 "Inductor_SMD:L_Bourns_SDR1806" H 9675 5575 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/15514/" H 9675 5575 50  0001 C CNN
	1    9675 5575
	0    -1   -1   0   
$EndComp
Connection ~ 9975 5975
Wire Wire Line
	9975 5975 10475 5975
Connection ~ 9975 5575
Wire Wire Line
	9975 5575 10475 5575
Connection ~ 9375 5975
Wire Wire Line
	9975 5975 9975 5925
Wire Wire Line
	9375 5975 9975 5975
Wire Wire Line
	9825 5575 9975 5575
Wire Wire Line
	9975 5575 9975 5625
Wire Wire Line
	7975 5525 7975 5375
Wire Wire Line
	7975 5375 8225 5375
Connection ~ 7975 5375
Wire Wire Line
	7575 5375 7975 5375
Connection ~ 7975 5975
Connection ~ 8725 5975
Wire Wire Line
	9375 5975 8725 5975
Wire Wire Line
	9375 5925 9375 5975
Wire Wire Line
	9375 5575 9525 5575
Connection ~ 9375 5575
Wire Wire Line
	9375 5575 9375 5625
$Comp
L Device:D_Schottky D2
U 1 1 5E207114
P 9375 5775
F 0 "D2" V 9329 5854 50  0000 L CNN
F 1 "100V/5A" V 9420 5854 50  0000 L CNN
F 2 "Diode_THT:D_DO-27_P12.70mm_Horizontal" H 9375 5775 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/9381/" H 9375 5775 50  0001 C CNN
	1    9375 5775
	0    1    1    0   
$EndComp
Wire Wire Line
	9225 5575 9375 5575
Wire Wire Line
	7575 5975 7975 5975
Wire Wire Line
	7975 5825 7975 5975
Connection ~ 8175 5975
Wire Wire Line
	7975 5975 8175 5975
Wire Wire Line
	8175 5575 8175 5975
Wire Wire Line
	8175 5975 8725 5975
Wire Wire Line
	8175 5575 8225 5575
Wire Wire Line
	8725 5775 8725 5975
$Comp
L Device:CP COUT2
U 1 1 5E2070F5
P 9975 5775
F 0 "COUT2" H 10075 5775 50  0000 L CNN
F 1 "25V/330uF" H 10000 5675 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm" H 10013 5625 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/7086/" H 9975 5775 50  0001 C CNN
	1    9975 5775
	1    0    0    -1  
$EndComp
$Comp
L Regulator_Switching:LM2596S-5 VR2
U 1 1 5E1D68D4
P 8725 5475
F 0 "VR2" H 8725 5842 50  0000 C CNN
F 1 "LM2596S-5" H 8725 5751 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:TO-263-5_TabPin3" H 8775 5225 50  0001 L CIN
F 3 "https://store.comet.bg/Catalogue/Product/16565/" H 8725 5475 50  0001 C CNN
	1    8725 5475
	1    0    0    -1  
$EndComp
$Comp
L Device:L L1
U 1 1 5E02F62B
P 9675 4275
F 0 "L1" V 9865 4275 50  0000 C CNN
F 1 "33uH" V 9774 4275 50  0000 C CNN
F 2 "Inductor_SMD:L_Bourns_SDR1806" H 9675 4275 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/15514/" H 9675 4275 50  0001 C CNN
	1    9675 4275
	0    -1   -1   0   
$EndComp
Wire Wire Line
	7175 4925 8725 4925
Wire Wire Line
	8725 4925 8725 4675
Connection ~ 8975 3575
Wire Wire Line
	9975 3575 9975 4275
Wire Wire Line
	8975 3575 9975 3575
Wire Wire Line
	8975 3575 8925 3575
Wire Wire Line
	8975 3225 8975 3575
Wire Wire Line
	8925 3225 8975 3225
Connection ~ 9975 4675
Wire Wire Line
	9975 4675 10475 4675
Connection ~ 9975 4275
Wire Wire Line
	9975 4275 10475 4275
Connection ~ 9375 4675
Wire Wire Line
	9975 4675 9975 4625
Wire Wire Line
	9375 4675 9975 4675
Wire Wire Line
	9825 4275 9975 4275
Wire Wire Line
	9975 4275 9975 4325
Wire Wire Line
	7975 4225 7975 4075
Wire Wire Line
	7975 4075 8225 4075
Connection ~ 7975 4075
Wire Wire Line
	7575 4075 7975 4075
Connection ~ 7975 4675
Connection ~ 8725 4675
Wire Wire Line
	9375 4675 8725 4675
Wire Wire Line
	9375 4625 9375 4675
Wire Wire Line
	9375 4275 9525 4275
Connection ~ 9375 4275
Wire Wire Line
	9375 4275 9375 4325
$Comp
L Device:D_Schottky D1
U 1 1 5DFADDFD
P 9375 4475
F 0 "D1" V 9329 4554 50  0000 L CNN
F 1 "100V/5A" V 9420 4554 50  0000 L CNN
F 2 "Diode_THT:D_DO-27_P12.70mm_Horizontal" H 9375 4475 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/9381/" H 9375 4475 50  0001 C CNN
	1    9375 4475
	0    1    1    0   
$EndComp
Wire Wire Line
	9225 4275 9375 4275
Wire Wire Line
	7175 3575 7175 4925
Wire Wire Line
	8225 3575 7175 3575
Connection ~ 8575 3575
Wire Wire Line
	8575 3575 8625 3575
Wire Wire Line
	8575 3575 8575 3725
Wire Wire Line
	8525 3575 8575 3575
Wire Wire Line
	9225 3725 8575 3725
Wire Wire Line
	9225 4075 9225 3725
Wire Wire Line
	7575 4675 7975 4675
Wire Wire Line
	7975 4525 7975 4675
Connection ~ 8175 4675
Wire Wire Line
	7975 4675 8175 4675
Wire Wire Line
	8175 4275 8175 4675
Wire Wire Line
	8175 4675 8725 4675
Wire Wire Line
	8175 4275 8225 4275
Wire Wire Line
	8725 4475 8725 4675
$Comp
L Device:C CFF1
U 1 1 5DFA831C
P 8775 3225
F 0 "CFF1" V 8523 3225 50  0000 C CNN
F 1 "10nF" V 8614 3225 50  0000 C CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 8813 3075 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/5919/" H 8775 3225 50  0001 C CNN
	1    8775 3225
	0    1    1    0   
$EndComp
$Comp
L Device:CP CIN1
U 1 1 5DFA53B3
P 7975 4375
F 0 "CIN1" H 7675 4425 50  0000 L CNN
F 1 "35V/680uF" H 7425 4325 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm" H 8013 4225 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/44664/" H 7975 4375 50  0001 C CNN
	1    7975 4375
	1    0    0    -1  
$EndComp
$Comp
L TrafficSignPCB-rescue:SIM800L-SIM800L U2
U 1 1 5DF831F1
P 5800 2050
F 0 "U2" H 5500 2650 60  0000 C CNN
F 1 "SIM800L" H 5600 2550 60  0000 C CNN
F 2 "SIM800:Sim800L" H 6100 1900 60  0001 C CNN
F 3 "https://img.filipeflop.com/files/download/Datasheet_SIM800L.pdf" H 6100 1900 60  0001 C CNN
	1    5800 2050
	1    0    0    -1  
$EndComp
NoConn ~ 6450 2300
NoConn ~ 6450 2200
NoConn ~ 6450 2100
NoConn ~ 6450 2000
NoConn ~ 6450 1900
NoConn ~ 6450 1800
$Comp
L Device:R R2
U 1 1 5DF907CE
P 8775 3575
F 0 "R2" V 8568 3575 50  0000 C CNN
F 1 "2.21k/1%" V 8659 3575 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 8705 3575 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/5041342/" H 8775 3575 50  0001 C CNN
	1    8775 3575
	0    1    1    0   
$EndComp
$Comp
L Device:R R1
U 1 1 5DF8F28A
P 8375 3575
F 0 "R1" V 8168 3575 50  0000 C CNN
F 1 "1k/1%" V 8259 3575 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 8305 3575 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/6406/" H 8375 3575 50  0001 C CNN
	1    8375 3575
	0    1    1    0   
$EndComp
$Comp
L Regulator_Switching:LM2596S-ADJ VR1
U 1 1 5E041BCD
P 8725 4175
F 0 "VR1" H 8725 4542 50  0000 C CNN
F 1 "LM2596S-ADJ" H 8725 4451 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:TO-263-5_TabPin3" H 8775 3925 50  0001 L CIN
F 3 "https://store.comet.bg/Catalogue/Product/16564/" H 8725 4175 50  0001 C CNN
	1    8725 4175
	1    0    0    -1  
$EndComp
Text GLabel 1525 1500 0    50   Input ~ 0
CLK
Text GLabel 1525 1400 0    50   Input ~ 0
STB
Text GLabel 1525 1300 0    50   Input ~ 0
OE
Wire Wire Line
	1525 2700 1625 2700
Wire Wire Line
	1525 2600 1625 2600
Wire Wire Line
	1525 2500 1625 2500
Wire Wire Line
	1525 2300 1625 2300
Wire Wire Line
	1525 2200 1625 2200
Wire Wire Line
	1525 2100 1625 2100
Wire Wire Line
	1525 1900 1625 1900
Wire Wire Line
	1525 1800 1625 1800
Wire Wire Line
	1525 1700 1625 1700
Wire Wire Line
	1525 1600 1625 1600
Wire Wire Line
	1525 1500 1625 1500
Wire Wire Line
	1525 1400 1625 1400
Wire Wire Line
	1625 1300 1525 1300
Text GLabel 1525 1600 0    50   Input ~ 0
D
Text GLabel 1525 1700 0    50   Input ~ 0
C
Text GLabel 1525 1800 0    50   Input ~ 0
B
Text GLabel 1525 1900 0    50   Input ~ 0
A
Text GLabel 1525 2100 0    50   Input ~ 0
B1
Text GLabel 1525 2200 0    50   Input ~ 0
G1
Text GLabel 1525 2300 0    50   Input ~ 0
R1
Text GLabel 1525 2500 0    50   Input ~ 0
B0
Text GLabel 1525 2600 0    50   Input ~ 0
G0
Text GLabel 1525 2700 0    50   Input ~ 0
R0
$Comp
L Connector_Generic:Conn_01x16 J1
U 1 1 5DF93F79
P 1825 2000
F 0 "J1" H 1743 975 50  0000 C CNN
F 1 "LED matrix data" H 1743 1066 50  0000 C CNN
F 2 "Connector_IDC:IDC-Header_2x08_P2.54mm_Vertical" H 1825 2000 50  0001 C CNN
F 3 "~" H 1825 2000 50  0001 C CNN
	1    1825 2000
	1    0    0    1   
$EndComp
Wire Wire Line
	3525 3650 3675 3650
Wire Wire Line
	8175 1600 8475 1600
Wire Wire Line
	4725 4800 4125 4800
Wire Wire Line
	4125 4700 4725 4700
Wire Wire Line
	5050 2250 5200 2250
$Comp
L power:GND #PWR0118
U 1 1 5E53B52D
P 5050 2250
F 0 "#PWR0118" H 5050 2000 50  0001 C CNN
F 1 "GND" H 5050 2100 50  0000 C CNN
F 2 "" H 5050 2250 50  0001 C CNN
F 3 "" H 5050 2250 50  0001 C CNN
	1    5050 2250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4875 2150 4750 2150
Text GLabel 4750 2150 0    50   Input ~ 0
SIM_TX
Text GLabel 4100 1700 0    50   Input ~ 0
SIM_RX
Wire Wire Line
	4175 2050 5200 2050
Connection ~ 4175 2050
Wire Wire Line
	4175 2050 4175 2100
Wire Wire Line
	4175 2000 4175 2050
Wire Notes Line
	1000 875  3200 875 
Wire Notes Line
	3200 875  3200 2950
Wire Notes Line
	3200 2950 1000 2950
Wire Notes Line
	1000 2950 1000 875 
Text Notes 2075 1025 0    75   Italic 15
Visualization Block
Wire Wire Line
	4225 6600 4725 6600
Text GLabel 4725 4700 2    50   Input ~ 0
SIM_RX
Text GLabel 4725 4800 2    50   Input ~ 0
SIM_TX
$Comp
L Device:R R6
U 1 1 5E6F86C9
P 5025 2150
F 0 "R6" V 5060 2330 50  0000 C CNN
F 1 "10k" V 4980 2330 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4955 2150 50  0001 C CNN
F 3 "~" H 5025 2150 50  0001 C CNN
	1    5025 2150
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4125 5000 4205 5000
$Comp
L Device:R R5
U 1 1 5E122269
P 4355 5000
F 0 "R5" V 4205 4995 50  0000 C CNN
F 1 "10k" V 4275 5000 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4285 5000 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/25851/" H 4355 5000 50  0001 C CNN
	1    4355 5000
	0    1    1    0   
$EndComp
Wire Notes Line
	3725 975  3725 2675
Wire Notes Line
	3725 2675 6625 2675
Wire Notes Line
	6625 2675 6625 975 
Wire Notes Line
	6625 975  3725 975 
Text Notes 5350 1125 0    75   Italic 15
Communication Block
Wire Wire Line
	5175 1750 5200 1750
Wire Wire Line
	5175 1650 5175 1750
$Comp
L Device:Antenna AE1
U 1 1 5E0362F2
P 5175 1450
F 0 "AE1" H 5100 1700 50  0000 L CNN
F 1 "Antenna" H 5025 1600 50  0000 L CNN
F 2 "Connector_Coaxial:SMA_Amphenol_901-144_Vertical" H 5175 1450 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/51344/" H 5175 1450 50  0001 C CNN
	1    5175 1450
	1    0    0    -1  
$EndComp
Wire Notes Line
	2025 3475 2025 7125
Wire Notes Line
	2025 7125 5475 7125
Wire Notes Line
	5475 3475 2025 3475
Wire Notes Line
	5475 7125 5475 3475
Text Notes 4600 3650 0    75   Italic 15
Control Block
$Comp
L Device:C C3
U 1 1 5E57F981
P 2875 6650
F 0 "C3" H 2650 6700 50  0000 L CNN
F 1 "100n" H 2575 6625 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 2913 6500 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/5920/" H 2875 6650 50  0001 C CNN
	1    2875 6650
	1    0    0    -1  
$EndComp
Wire Notes Line
	7050 6300 10950 6300
Wire Notes Line
	10950 6300 10950 2350
Text Notes 10175 2525 0    75   Italic 15
Power Block
Wire Notes Line
	10950 2350 7050 2350
Text GLabel 9750 1225 2    50   Input ~ 0
BAT+
Text GLabel 9750 1550 2    50   Input ~ 0
BAT-
Wire Wire Line
	9475 1450 9600 1450
Wire Wire Line
	9600 1450 9600 1550
Wire Wire Line
	9600 1550 9750 1550
Wire Wire Line
	9475 1350 9600 1350
Wire Wire Line
	9600 1350 9600 1225
Wire Wire Line
	9600 1225 9750 1225
Wire Notes Line
	7875 925  7875 1725
Wire Notes Line
	7875 1725 10075 1725
Wire Notes Line
	10075 1725 10075 925 
Wire Notes Line
	10075 925  7875 925 
Text Notes 9275 1075 0    75   Italic 15
Charge Block
Text GLabel 7525 3225 0    50   Input ~ 0
BAT-
Text GLabel 7525 2750 0    50   Input ~ 0
BAT+
Wire Wire Line
	7775 3225 7775 3200
Connection ~ 7775 3225
Wire Wire Line
	7775 3225 7525 3225
Connection ~ 7775 2750
Wire Wire Line
	7775 2750 7525 2750
Wire Wire Line
	7775 3250 7775 3225
$Comp
L power:GND #PWR0124
U 1 1 5E1818BD
P 7775 3250
F 0 "#PWR0124" H 7775 3000 50  0001 C CNN
F 1 "GND" H 7850 3075 50  0000 R CNN
F 2 "" H 7775 3250 50  0001 C CNN
F 3 "" H 7775 3250 50  0001 C CNN
	1    7775 3250
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_DIP_x01 SW1
U 1 1 5E329055
P 8125 2750
F 0 "SW1" H 8125 3017 50  0000 C CNN
F 1 "Power switch" H 8125 2926 50  0000 C CNN
F 2 "" H 8125 2750 50  0001 C CNN
F 3 "~" H 8125 2750 50  0001 C CNN
	1    8125 2750
	1    0    0    -1  
$EndComp
Wire Wire Line
	8425 2750 8525 2750
Wire Wire Line
	7825 2750 7775 2750
$Comp
L power:+12V #PWR0125
U 1 1 5E174F0C
P 8525 2750
F 0 "#PWR0125" H 8525 2600 50  0001 C CNN
F 1 "+12V" H 8425 2925 50  0000 L CNN
F 2 "" H 8525 2750 50  0001 C CNN
F 3 "" H 8525 2750 50  0001 C CNN
	1    8525 2750
	1    0    0    -1  
$EndComp
Wire Wire Line
	7775 2750 7775 2800
$Comp
L Device:Battery BT1
U 1 1 5E200195
P 7775 3000
F 0 "BT1" H 7500 3050 50  0000 L CNN
F 1 "12V/14Ah" H 7275 2950 50  0000 L CNN
F 2 "" V 7775 3060 50  0001 C CNN
F 3 "~" V 7775 3060 50  0001 C CNN
	1    7775 3000
	1    0    0    -1  
$EndComp
Wire Wire Line
	8575 3575 8575 3225
Wire Wire Line
	8575 3225 8625 3225
Wire Notes Line
	7050 2350 7050 6300
$Comp
L Device:R R7
U 1 1 5E490DB1
P 4500 1250
F 0 "R7" H 4550 1300 50  0000 L CNN
F 1 "16k" H 4550 1225 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4430 1250 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/25851/" H 4500 1250 50  0001 C CNN
	1    4500 1250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4425 1100 4500 1100
$Comp
L Device:R R8
U 1 1 5E490DB8
P 4500 1650
F 0 "R8" H 4550 1700 50  0000 L CNN
F 1 "20k" H 4550 1625 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4430 1650 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/3884/" H 4500 1650 50  0001 C CNN
	1    4500 1650
	1    0    0    -1  
$EndComp
Wire Wire Line
	4500 1400 4500 1450
Wire Wire Line
	4750 1450 4500 1450
Connection ~ 4500 1450
Wire Wire Line
	4500 1450 4500 1500
Wire Wire Line
	4750 1950 5200 1950
Wire Wire Line
	4175 2450 4175 2400
$Comp
L power:GND #PWR0116
U 1 1 5E4EA9BE
P 4175 2450
F 0 "#PWR0116" H 4175 2200 50  0001 C CNN
F 1 "GND" H 4175 2300 50  0000 C CNN
F 2 "" H 4175 2450 50  0001 C CNN
F 3 "" H 4175 2450 50  0001 C CNN
	1    4175 2450
	1    0    0    -1  
$EndComp
Wire Wire Line
	4500 1850 4500 1800
$Comp
L power:GND #PWR0106
U 1 1 5E490DAB
P 4500 1850
F 0 "#PWR0106" H 4500 1600 50  0001 C CNN
F 1 "GND" H 4500 1700 50  0000 C CNN
F 2 "" H 4500 1850 50  0001 C CNN
F 3 "" H 4500 1850 50  0001 C CNN
	1    4500 1850
	1    0    0    -1  
$EndComp
Wire Wire Line
	4750 1450 4750 1950
$EndSCHEMATC
