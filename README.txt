#PINOUT FOR RASPBERRY PI 3 B+
+----------------------------+
|()2#################40() +---+
|  1#################39   |USB|
|#D    Pi B+ / Pi 2 +-+   +---+
|#I   \/  +--+      | |   +---+
|#S  ()() |  | CAM  +-+   |USB|
|#P   ()  +--+  #         +---+  
|#Y             #        +----+
|        +----+ # +-+    | NET|
|()+---+ |    | # |A|  ()+----+
+--|PWR|-|HDMI|---|V|--------+
   +---+ +----+   +-+           [ ] = not used / ignore for this project
				[*] = used
              
	           Pin 1 Pin2
                +3V3 [ ] [ ] +5V
      SDA1 / GPIO  2 [ ] [*] +5V (PN532)
      SCL1 / GPIO  3 [ ] [*] GND (PN532)
ACCESS GRANTED LED + [*] [ ] GPIO 14 / TXD0
ACCESS GRANTED LED - [*] [ ] GPIO 15 / RXD0
             GPIO 17 [ ] [*] ACCESS DENIED LED +
             GPIO 27 [ ] [*] ACCESS DENIED LED -
             GPIO 22 [ ] [ ] GPIO 23
                +3V3 [ ] [ ] GPIO 24
        MOSI (PN532) [*] [ ] GND
        MISO (PN532) [*] [ ] GPIO 25
         SCK (PN532) [*] [ ] GPIO  8 / CE0#
                 GND [ ] [ ] GPIO  7 / CE1#
     ID_SD / GPIO  0 [ ] [ ] GPIO  1 / ID_SC
        SSEL (PN532) [*] [ ] GND
             GPIO  6 [ ] [ ] GPIO 12
             GPIO 13 [ ] [ ] GND
      MISO / GPIO 19 [ ] [ ] GPIO 16 / CE2#
             GPIO 26 [ ] [ ] GPIO 20 / MOSI
                 GND [ ] [ ] GPIO 21 / SCLK
                  Pin 39 Pin 40

#IMPORTANt!!!
Add keys.txt to root level of the filesystem that will be running the program.

#TODO
1.Add SSH functionality


