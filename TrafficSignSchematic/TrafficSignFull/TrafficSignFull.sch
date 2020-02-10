EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
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
	10200 6000 10500 6000
Connection ~ 10200 6000
Wire Wire Line
	10200 5950 10200 6000
Wire Wire Line
	10200 5600 10500 5600
Connection ~ 10200 5600
Wire Wire Line
	10200 5650 10200 5600
$Comp
L Device:C C7
U 1 1 5E2FC6B7
P 10200 5800
F 0 "C7" H 10300 5850 50  0000 L CNN
F 1 "100n" H 10300 5775 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 10238 5650 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/5920/" H 10200 5800 50  0001 C CNN
	1    10200 5800
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
F 1 "100n" H 10575 4450 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 10513 4325 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/5920/" H 10475 4475 50  0001 C CNN
	1    10475 4475
	1    0    0    -1  
$EndComp
Text GLabel 4550 6300 2    50   Input ~ 0
SIM_RST
Text GLabel 4750 1900 0    50   Input ~ 0
SIM_RST
Wire Wire Line
	5175 2100 5200 2100
Wire Wire Line
	2375 4250 2525 4250
Connection ~ 2375 4250
Wire Wire Line
	2375 4300 2375 4250
Wire Wire Line
	2225 4250 2375 4250
Wire Wire Line
	2375 3950 2525 3950
Connection ~ 2375 3950
Wire Wire Line
	2375 3900 2375 3950
Wire Wire Line
	2225 3950 2375 3950
$Comp
L Device:C C5
U 1 1 5E5C89EE
P 2525 4100
F 0 "C5" H 2625 4150 50  0000 L CNN
F 1 "100n" H 2625 4075 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 2563 3950 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/5920/" H 2525 4100 50  0001 C CNN
	1    2525 4100
	1    0    0    -1  
$EndComp
$Comp
L Device:C C4
U 1 1 5E5BEE3A
P 2225 4100
F 0 "C4" H 2000 4150 50  0000 L CNN
F 1 "100n" H 1925 4075 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 2263 3950 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/5920/" H 2225 4100 50  0001 C CNN
	1    2225 4100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0123
U 1 1 5E5B557C
P 2375 4300
F 0 "#PWR0123" H 2375 4050 50  0001 C CNN
F 1 "GND" H 2380 4127 50  0000 C CNN
F 2 "" H 2375 4300 50  0001 C CNN
F 3 "" H 2375 4300 50  0001 C CNN
	1    2375 4300
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0122
U 1 1 5E5ABDC2
P 2375 3900
F 0 "#PWR0122" H 2375 3750 50  0001 C CNN
F 1 "+5V" H 2390 4073 50  0000 C CNN
F 2 "" H 2375 3900 50  0001 C CNN
F 3 "" H 2375 3900 50  0001 C CNN
	1    2375 3900
	1    0    0    -1  
$EndComp
Wire Wire Line
	2700 6550 2700 6500
$Comp
L power:GND #PWR0121
U 1 1 5E2B082D
P 2700 6550
F 0 "#PWR0121" H 2700 6300 50  0001 C CNN
F 1 "GND" H 2705 6377 50  0000 C CNN
F 2 "" H 2700 6550 50  0001 C CNN
F 3 "" H 2700 6550 50  0001 C CNN
	1    2700 6550
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0120
U 1 1 5E56BC18
P 10500 5600
F 0 "#PWR0120" H 10500 5450 50  0001 C CNN
F 1 "+5V" H 10515 5773 50  0000 C CNN
F 2 "" H 10500 5600 50  0001 C CNN
F 3 "" H 10500 5600 50  0001 C CNN
	1    10500 5600
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
	5050 1800 5200 1800
$Comp
L power:+4V #PWR0117
U 1 1 5E526B11
P 5050 1800
F 0 "#PWR0117" H 5050 1650 50  0001 C CNN
F 1 "+4V" H 5050 1950 50  0000 C CNN
F 2 "" H 5050 1800 50  0001 C CNN
F 3 "" H 5050 1800 50  0001 C CNN
	1    5050 1800
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0116
U 1 1 5E4EA9BE
P 4175 2400
F 0 "#PWR0116" H 4175 2150 50  0001 C CNN
F 1 "GND" H 4175 2250 50  0000 C CNN
F 2 "" H 4175 2400 50  0001 C CNN
F 3 "" H 4175 2400 50  0001 C CNN
	1    4175 2400
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
P 7300 5400
F 0 "#PWR0114" H 7300 5250 50  0001 C CNN
F 1 "+12V" H 7315 5573 50  0000 C CNN
F 2 "" H 7300 5400 50  0001 C CNN
F 3 "" H 7300 5400 50  0001 C CNN
	1    7300 5400
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
P 10500 6000
F 0 "#PWR0111" H 10500 5750 50  0001 C CNN
F 1 "GND" H 10505 5827 50  0000 C CNN
F 2 "" H 10500 6000 50  0001 C CNN
F 3 "" H 10500 6000 50  0001 C CNN
	1    10500 6000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0110
U 1 1 5E4813F6
P 7300 6000
F 0 "#PWR0110" H 7300 5750 50  0001 C CNN
F 1 "GND" H 7305 5827 50  0000 C CNN
F 2 "" H 7300 6000 50  0001 C CNN
F 3 "" H 7300 6000 50  0001 C CNN
	1    7300 6000
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
P 4445 4700
F 0 "#PWR0104" H 4445 4550 50  0001 C CNN
F 1 "+5V" H 4445 4850 50  0000 C CNN
F 2 "" H 4445 4700 50  0001 C CNN
F 3 "" H 4445 4700 50  0001 C CNN
	1    4445 4700
	1    0    0    -1  
$EndComp
Wire Wire Line
	3350 3350 3350 3500
$Comp
L power:GND #PWR0103
U 1 1 5E3D329E
P 3500 3350
F 0 "#PWR0103" H 3500 3100 50  0001 C CNN
F 1 "GND" H 3505 3177 50  0000 C CNN
F 2 "" H 3500 3350 50  0001 C CNN
F 3 "" H 3500 3350 50  0001 C CNN
	1    3500 3350
	1    0    0    -1  
$EndComp
Text Label 4250 4400 0    50   ~ 0
TXD
Text Label 4250 4500 0    50   ~ 0
RXD
Text Label 4300 4300 0    50   ~ 0
2
Text Label 4300 4200 0    50   ~ 0
3
Text Label 4300 4100 0    50   ~ 0
4
Text Label 4300 4000 0    50   ~ 0
5
Text Label 4300 3900 0    50   ~ 0
6
Text Label 4300 3800 0    50   ~ 0
7
Wire Wire Line
	3950 4800 4700 4800
Wire Wire Line
	3950 4900 4700 4900
Text Label 4300 5300 0    50   ~ 0
A0
Text Label 4300 5200 0    50   ~ 0
A1
Text Label 4300 5100 0    50   ~ 0
A2
Text Label 4300 5000 0    50   ~ 0
A3
Text Label 4300 4900 0    50   ~ 0
A4
Text Label 4300 4800 0    50   ~ 0
A5
Wire Wire Line
	4350 5600 4350 5700
Wire Wire Line
	4350 5700 4650 5700
Wire Wire Line
	3950 5500 4350 5500
Wire Wire Line
	4350 5500 4350 5400
Wire Wire Line
	4350 5400 4650 5400
Wire Wire Line
	3950 5700 4300 5700
Wire Wire Line
	4300 5700 4300 5800
Wire Wire Line
	4300 5800 4700 5800
Text Label 4350 6300 0    50   ~ 0
8
Text Label 4350 6200 0    50   ~ 0
9
Text Label 4300 6100 0    50   ~ 0
10
Text Label 4300 6000 0    50   ~ 0
11
Text Label 4300 5900 0    50   ~ 0
12
Text Label 4300 5800 0    50   ~ 0
13
Wire Wire Line
	3950 5800 4250 5800
Wire Wire Line
	4250 5800 4250 5900
Wire Wire Line
	4250 5900 4700 5900
Wire Wire Line
	3950 5900 4200 5900
Wire Wire Line
	4200 5900 4200 6000
Wire Wire Line
	4200 6000 4550 6000
Wire Wire Line
	3950 6000 4150 6000
Wire Wire Line
	4150 6000 4150 6100
Wire Wire Line
	4150 6100 4550 6100
Wire Wire Line
	3950 6100 4100 6100
Wire Wire Line
	4100 6100 4100 6200
Wire Wire Line
	4100 6200 4550 6200
Wire Wire Line
	3950 6200 4050 6200
Wire Wire Line
	4050 6200 4050 6300
Text GLabel 4550 4300 2    50   Input ~ 0
R0
Text GLabel 4550 4200 2    50   Input ~ 0
G0
Text GLabel 4550 4100 2    50   Input ~ 0
B0
Wire Wire Line
	3950 4100 4550 4100
Wire Wire Line
	3950 4200 4550 4200
Wire Wire Line
	3950 4300 4550 4300
Text GLabel 4550 4000 2    50   Input ~ 0
R1
Text GLabel 4550 3900 2    50   Input ~ 0
G1
Text GLabel 4550 3800 2    50   Input ~ 0
B1
Wire Wire Line
	3950 4000 4550 4000
Wire Wire Line
	3950 3900 4550 3900
Wire Wire Line
	3950 3800 4550 3800
Text GLabel 4600 5300 2    50   Input ~ 0
A
Text GLabel 4600 5200 2    50   Input ~ 0
B
Text GLabel 4600 5100 2    50   Input ~ 0
C
Text GLabel 4600 5000 2    50   Input ~ 0
D
Wire Wire Line
	3950 5000 4600 5000
Wire Wire Line
	3950 5100 4600 5100
Wire Wire Line
	3950 5200 4600 5200
Wire Wire Line
	3950 5300 4600 5300
Text GLabel 4550 6000 2    50   Input ~ 0
CLK
Text GLabel 4550 6100 2    50   Input ~ 0
STB
Text GLabel 4550 6200 2    50   Input ~ 0
OE
$Comp
L Device:R R3
U 1 1 5E100EA7
P 4175 1800
F 0 "R3" H 4225 1850 50  0000 L CNN
F 1 "10k" H 4225 1775 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4105 1800 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/25851/" H 4175 1800 50  0001 C CNN
	1    4175 1800
	1    0    0    -1  
$EndComp
Wire Wire Line
	4100 1650 4175 1650
Wire Wire Line
	4330 4700 4445 4700
Wire Wire Line
	2750 6200 2700 6200
Wire Wire Line
	3450 6650 3450 6500
Wire Wire Line
	3350 6500 3350 6650
Wire Wire Line
	3350 6650 3450 6650
Connection ~ 3450 6650
Wire Wire Line
	4650 5400 4700 5400
Connection ~ 4650 5400
Wire Wire Line
	5150 5400 5000 5400
Wire Wire Line
	4650 5700 4700 5700
Connection ~ 4650 5700
$Comp
L Device:R R4
U 1 1 5E2884D8
P 4175 2200
F 0 "R4" H 4225 2250 50  0000 L CNN
F 1 "20k" H 4225 2175 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4105 2200 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/3884/" H 4175 2200 50  0001 C CNN
	1    4175 2200
	1    0    0    -1  
$EndComp
Wire Wire Line
	4175 2400 4175 2350
$Comp
L Device:C C2
U 1 1 5E17AFFA
P 4850 5700
F 0 "C2" V 4800 5800 50  0000 C CNN
F 1 "22pF" V 4900 5850 50  0000 C CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 4888 5550 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/27466/" H 4850 5700 50  0001 C CNN
	1    4850 5700
	0    1    1    0   
$EndComp
$Comp
L Device:C C1
U 1 1 5E16B77E
P 4850 5400
F 0 "C1" V 4800 5500 50  0000 C CNN
F 1 "22pF" V 4900 5550 50  0000 C CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 4888 5250 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/27466/" H 4850 5400 50  0001 C CNN
	1    4850 5400
	0    1    1    0   
$EndComp
$Comp
L Device:Crystal Y1
U 1 1 5E152994
P 4650 5550
F 0 "Y1" V 4550 5300 50  0000 L CNN
F 1 "16MHz" V 4650 5150 50  0000 L CNN
F 2 "Crystal:Crystal_HC49-U_Vertical" H 4650 5550 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/27238/" H 4650 5550 50  0001 C CNN
	1    4650 5550
	0    1    1    0   
$EndComp
NoConn ~ 4700 4800
NoConn ~ 4700 4900
NoConn ~ 4700 5800
NoConn ~ 4700 5900
Wire Wire Line
	5000 5700 5150 5700
$Comp
L power:GND #PWR0102
U 1 1 5E2916ED
P 5150 5750
F 0 "#PWR0102" H 5150 5500 50  0001 C CNN
F 1 "GND" H 5155 5577 50  0000 C CNN
F 2 "" H 5150 5750 50  0001 C CNN
F 3 "" H 5150 5750 50  0001 C CNN
	1    5150 5750
	1    0    0    -1  
$EndComp
Wire Wire Line
	5150 5750 5150 5700
Connection ~ 5150 5700
Wire Wire Line
	5150 5700 5150 5400
$Comp
L power:+5V #PWR0101
U 1 1 5E2B9136
P 3700 6650
F 0 "#PWR0101" H 3700 6500 50  0001 C CNN
F 1 "+5V" H 3715 6823 50  0000 C CNN
F 2 "" H 3700 6650 50  0001 C CNN
F 3 "" H 3700 6650 50  0001 C CNN
	1    3700 6650
	1    0    0    -1  
$EndComp
Wire Wire Line
	3450 6650 3700 6650
Wire Wire Line
	3950 5600 4350 5600
$Comp
L MCU_Microchip_ATmega:ATmega328P-PU U1
U 1 1 5DF560CB
P 3350 5000
F 0 "U1" H 2800 4850 50  0000 R CNN
F 1 "ATmega328P-PU" H 2800 4950 50  0000 R CNN
F 2 "Package_DIP:DIP-28_W7.62mm" H 3350 5000 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/ATmega328_P%20AVR%20MCU%20with%20picoPower%20Technology%20Data%20Sheet%2040001984A.pdf" H 3350 5000 50  0001 C CNN
	1    3350 5000
	1    0    0    1   
$EndComp
$Comp
L Device:CP COUT1
U 1 1 5DFA6ACC
P 9975 4475
F 0 "COUT1" H 10093 4521 50  0000 L CNN
F 1 "470uF" H 10093 4430 50  0000 L CNN
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
P 7700 5700
F 0 "CIN2" H 7400 5750 50  0000 L CNN
F 1 "680uF" H 7350 5650 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm" H 7738 5550 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/44664/" H 7700 5700 50  0001 C CNN
	1    7700 5700
	1    0    0    -1  
$EndComp
Text Notes 7625 4675 0    50   ~ 0
IN-
Text Notes 7625 4075 0    50   ~ 0
IN+
Text Notes 7350 6000 0    50   ~ 0
IN-
Text Notes 7350 5400 0    50   ~ 0
IN+
Text Notes 10525 4675 0    50   ~ 0
OUT-
Text Notes 10525 4275 0    50   ~ 0
OUT+
Text Notes 10250 5600 0    50   ~ 0
OUT+
Text Notes 10250 6000 0    50   ~ 0
OUT-
Wire Wire Line
	9700 5350 9700 5600
Wire Wire Line
	8950 5400 8950 5350
Wire Wire Line
	9700 5350 8950 5350
$Comp
L Device:L L2
U 1 1 5E20713A
P 9400 5600
F 0 "L2" V 9590 5600 50  0000 C CNN
F 1 "33uH" V 9499 5600 50  0000 C CNN
F 2 "Inductor_SMD:L_Bourns_SDR1806" H 9400 5600 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/15514/" H 9400 5600 50  0001 C CNN
	1    9400 5600
	0    -1   -1   0   
$EndComp
Connection ~ 9700 6000
Wire Wire Line
	9700 6000 10200 6000
Connection ~ 9700 5600
Wire Wire Line
	9700 5600 10200 5600
Connection ~ 9100 6000
Wire Wire Line
	9700 6000 9700 5950
Wire Wire Line
	9100 6000 9700 6000
Wire Wire Line
	9550 5600 9700 5600
Wire Wire Line
	9700 5600 9700 5650
Wire Wire Line
	7700 5550 7700 5400
Wire Wire Line
	7700 5400 7950 5400
Connection ~ 7700 5400
Wire Wire Line
	7300 5400 7700 5400
Connection ~ 7700 6000
Connection ~ 8450 6000
Wire Wire Line
	9100 6000 8450 6000
Wire Wire Line
	9100 5950 9100 6000
Wire Wire Line
	9100 5600 9250 5600
Connection ~ 9100 5600
Wire Wire Line
	9100 5600 9100 5650
$Comp
L Device:D_Schottky D2
U 1 1 5E207114
P 9100 5800
F 0 "D2" V 9054 5879 50  0000 L CNN
F 1 "100V/5A" V 9145 5879 50  0000 L CNN
F 2 "Diode_THT:D_DO-27_P12.70mm_Horizontal" H 9100 5800 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/9381/" H 9100 5800 50  0001 C CNN
	1    9100 5800
	0    1    1    0   
$EndComp
Wire Wire Line
	8950 5600 9100 5600
Wire Wire Line
	7300 6000 7700 6000
Wire Wire Line
	7700 5850 7700 6000
Connection ~ 7900 6000
Wire Wire Line
	7700 6000 7900 6000
Wire Wire Line
	7900 5600 7900 6000
Wire Wire Line
	7900 6000 8450 6000
Wire Wire Line
	7900 5600 7950 5600
Wire Wire Line
	8450 5800 8450 6000
$Comp
L Device:CP COUT2
U 1 1 5E2070F5
P 9700 5800
F 0 "COUT2" H 9818 5846 50  0000 L CNN
F 1 "330uF" H 9818 5755 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm" H 9738 5650 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/7086/" H 9700 5800 50  0001 C CNN
	1    9700 5800
	1    0    0    -1  
$EndComp
$Comp
L Regulator_Switching:LM2596S-5 VR2
U 1 1 5E1D68D4
P 8450 5500
F 0 "VR2" H 8450 5867 50  0000 C CNN
F 1 "LM2596S-5" H 8450 5776 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:TO-263-5_TabPin3" H 8500 5250 50  0001 L CIN
F 3 "https://store.comet.bg/Catalogue/Product/16565/" H 8450 5500 50  0001 C CNN
	1    8450 5500
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
Wire Wire Line
	8575 3225 8625 3225
Wire Wire Line
	8575 3575 8575 3225
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
F 1 "680uF" H 7625 4325 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm" H 8013 4225 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/44664/" H 7975 4375 50  0001 C CNN
	1    7975 4375
	1    0    0    -1  
$EndComp
$Comp
L TrafficSignPCB-rescue:SIM800L-SIM800L U2
U 1 1 5DF831F1
P 5800 2000
F 0 "U2" H 5500 2600 60  0000 C CNN
F 1 "SIM800L" H 5600 2500 60  0000 C CNN
F 2 "SIM800:Sim800L" H 6100 1850 60  0001 C CNN
F 3 "https://img.filipeflop.com/files/download/Datasheet_SIM800L.pdf" H 6100 1850 60  0001 C CNN
	1    5800 2000
	1    0    0    -1  
$EndComp
NoConn ~ 6450 2250
NoConn ~ 6450 2150
NoConn ~ 6450 2050
NoConn ~ 6450 1950
NoConn ~ 6450 1850
NoConn ~ 6450 1750
$Comp
L Device:R R2
U 1 1 5DF907CE
P 8775 3575
F 0 "R2" V 8568 3575 50  0000 C CNN
F 1 "2.2k/1%" V 8659 3575 50  0000 C CNN
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
	3350 3350 3500 3350
Wire Wire Line
	8175 1600 8475 1600
Wire Wire Line
	4550 4500 3950 4500
Wire Wire Line
	3950 4400 4550 4400
Wire Wire Line
	5175 1900 5200 1900
Wire Wire Line
	4875 1900 4750 1900
Wire Wire Line
	5050 2200 5200 2200
$Comp
L power:GND #PWR0118
U 1 1 5E53B52D
P 5050 2200
F 0 "#PWR0118" H 5050 1950 50  0001 C CNN
F 1 "GND" H 5050 2050 50  0000 C CNN
F 2 "" H 5050 2200 50  0001 C CNN
F 3 "" H 5050 2200 50  0001 C CNN
	1    5050 2200
	1    0    0    -1  
$EndComp
Wire Wire Line
	4875 2100 4750 2100
Text GLabel 4750 2100 0    50   Input ~ 0
SIM_TX
Text GLabel 4100 1650 0    50   Input ~ 0
SIM_RX
Wire Wire Line
	4175 2000 5200 2000
Connection ~ 4175 2000
Wire Wire Line
	4175 2000 4175 2050
Wire Wire Line
	4175 1950 4175 2000
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
	4050 6300 4550 6300
Text GLabel 4550 4400 2    50   Input ~ 0
SIM_RX
Text GLabel 4550 4500 2    50   Input ~ 0
SIM_TX
$Comp
L Device:R R6
U 1 1 5E6F86C9
P 5025 2100
F 0 "R6" V 5060 2280 50  0000 C CNN
F 1 "10k" V 4980 2280 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4955 2100 50  0001 C CNN
F 3 "~" H 5025 2100 50  0001 C CNN
	1    5025 2100
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R7
U 1 1 5E295091
P 5025 1900
F 0 "R7" V 5060 2080 50  0000 C CNN
F 1 "10k" V 4980 2080 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4955 1900 50  0001 C CNN
F 3 "~" H 5025 1900 50  0001 C CNN
	1    5025 1900
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3950 4700 4030 4700
$Comp
L Device:R R5
U 1 1 5E122269
P 4180 4700
F 0 "R5" V 4030 4695 50  0000 C CNN
F 1 "10k" V 4100 4700 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4110 4700 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/25851/" H 4180 4700 50  0001 C CNN
	1    4180 4700
	0    1    1    0   
$EndComp
Wire Notes Line
	3725 1025 3725 2675
Wire Notes Line
	3725 2675 6625 2675
Wire Notes Line
	6625 2675 6625 1025
Wire Notes Line
	6625 1025 3725 1025
Text Notes 5350 1175 0    75   Italic 15
Communication Block
Wire Wire Line
	5175 1700 5200 1700
Wire Wire Line
	5175 1600 5175 1700
$Comp
L Device:Antenna AE1
U 1 1 5E0362F2
P 5175 1400
F 0 "AE1" H 5100 1650 50  0000 L CNN
F 1 "Antenna" H 5025 1550 50  0000 L CNN
F 2 "Connector_Coaxial:SMA_Amphenol_901-144_Vertical" H 5175 1400 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/51344/" H 5175 1400 50  0001 C CNN
	1    5175 1400
	1    0    0    -1  
$EndComp
Wire Notes Line
	1850 3175 1850 6825
Wire Notes Line
	1850 6825 5300 6825
Wire Notes Line
	5300 3175 1850 3175
Wire Notes Line
	5300 6825 5300 3175
Text Notes 4425 3350 0    75   Italic 15
Control Block
$Comp
L Device:C C3
U 1 1 5E57F981
P 2700 6350
F 0 "C3" H 2475 6400 50  0000 L CNN
F 1 "100n" H 2400 6325 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 2738 6200 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/5920/" H 2700 6350 50  0001 C CNN
	1    2700 6350
	1    0    0    -1  
$EndComp
Wire Notes Line
	7050 2250 7050 6300
Wire Notes Line
	7050 6300 10950 6300
Wire Notes Line
	10950 6300 10950 2250
$Comp
L Connector_Generic:Conn_01x04 J3
U 1 1 5E26C348
P 9850 2775
F 0 "J3" H 9800 3125 50  0000 L CNN
F 1 "Power input" H 9700 3025 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-396_A-41791-0004_1x04_P3.96mm_Vertical" H 9850 2775 50  0001 C CNN
F 3 "https://store.comet.bg/Catalogue/Product/25223/" H 9850 2775 50  0001 C CNN
	1    9850 2775
	1    0    0    -1  
$EndComp
Wire Wire Line
	9650 2675 9550 2675
Wire Wire Line
	9650 2775 9550 2775
Wire Wire Line
	9650 2875 9550 2875
Wire Wire Line
	9650 2975 9550 2975
Wire Wire Line
	9550 2875 9550 2975
Wire Wire Line
	9550 2975 9450 2975
Connection ~ 9550 2975
Wire Wire Line
	9550 2775 9550 2675
Wire Wire Line
	9550 2675 9450 2675
Connection ~ 9550 2675
$Comp
L power:GND #PWR0106
U 1 1 5E43D1EE
P 9450 2975
F 0 "#PWR0106" H 9450 2725 50  0001 C CNN
F 1 "GND" H 9455 2802 50  0000 C CNN
F 2 "" H 9450 2975 50  0001 C CNN
F 3 "" H 9450 2975 50  0001 C CNN
	1    9450 2975
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR0107
U 1 1 5E463591
P 9450 2675
F 0 "#PWR0107" H 9450 2525 50  0001 C CNN
F 1 "+12V" H 9465 2848 50  0000 C CNN
F 2 "" H 9450 2675 50  0001 C CNN
F 3 "" H 9450 2675 50  0001 C CNN
	1    9450 2675
	1    0    0    -1  
$EndComp
Text Notes 10175 2425 0    75   Italic 15
Power Block
Text GLabel 7375 3100 0    50   Input ~ 0
BAT-
Text GLabel 7375 2625 0    50   Input ~ 0
BAT+
Wire Wire Line
	7625 3100 7625 3075
Connection ~ 7625 3100
Wire Wire Line
	7625 3100 7375 3100
Connection ~ 7625 2625
Wire Wire Line
	7625 2625 7375 2625
Wire Notes Line
	10950 2250 7050 2250
Wire Wire Line
	7625 3125 7625 3100
$Comp
L power:GND #PWR0124
U 1 1 5E1818BD
P 7625 3125
F 0 "#PWR0124" H 7625 2875 50  0001 C CNN
F 1 "GND" H 7700 2950 50  0000 R CNN
F 2 "" H 7625 3125 50  0001 C CNN
F 3 "" H 7625 3125 50  0001 C CNN
	1    7625 3125
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_DIP_x01 SW1
U 1 1 5E329055
P 7975 2625
F 0 "SW1" H 7975 2892 50  0000 C CNN
F 1 "Power switch" H 7975 2801 50  0000 C CNN
F 2 "" H 7975 2625 50  0001 C CNN
F 3 "~" H 7975 2625 50  0001 C CNN
	1    7975 2625
	1    0    0    -1  
$EndComp
Wire Wire Line
	8275 2625 8375 2625
Wire Wire Line
	7675 2625 7625 2625
$Comp
L power:+12V #PWR0125
U 1 1 5E174F0C
P 8375 2625
F 0 "#PWR0125" H 8375 2475 50  0001 C CNN
F 1 "+12V" H 8275 2800 50  0000 L CNN
F 2 "" H 8375 2625 50  0001 C CNN
F 3 "" H 8375 2625 50  0001 C CNN
	1    8375 2625
	1    0    0    -1  
$EndComp
Wire Wire Line
	7625 2625 7625 2675
$Comp
L Device:Battery BT1
U 1 1 5E200195
P 7625 2875
F 0 "BT1" H 7350 2925 50  0000 L CNN
F 1 "12V" H 7350 2825 50  0000 L CNN
F 2 "" V 7625 2935 50  0001 C CNN
F 3 "~" V 7625 2935 50  0001 C CNN
	1    7625 2875
	1    0    0    -1  
$EndComp
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
$EndSCHEMATC
