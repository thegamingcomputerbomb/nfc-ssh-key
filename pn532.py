"""
This example shows connecting to the PN532 with SPI.
After initialization, try waving various 13.56MHz RFID cards over it!
"""

import board
import busio
import time
from paramiko import SSHClient
from digitalio import DigitalInOut
from digitalio import Direction
#
# NOTE: pick the import that matches the interface being used
#
from adafruit_pn532.spi import PN532_SPI

# SPI connection:
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs_pin = DigitalInOut(board.D5)
pn532 = PN532_SPI(spi, cs_pin, debug=False)

#door emulation leds
door_unlocked = DigitalInOut(board.D4)
door_unlocked.direction = Direction.OUTPUT
key_denied = DigitalInOut(board.D18)
key_denied.direction = Direction.OUTPUT

ic, ver, rev, support = pn532.get_firmware_version()
print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

# Configure PN532 to communicate with MiFare cards
pn532.SAM_configuration()

print('Waiting for RFID/NFC card...')
while True: #loop the following lines forever
    # Check if a card is available to read
    uid = pn532.read_passive_target(timeout=0.5)
    # Try again if no card is available.
    if uid is None:
        continue
    #print('Found card with UID:', [hex(i) for i in uid])
    print (uid)
    match = False
    keys = []
    with open("/keys.txt", "r") as keyfile:
        keys = keyfile.readlines()
    for i in keys:
        if uid == eval(i.strip()):
            match = True
            door_unlocked.value = True
            time.sleep(15)
            door_unlocked.value = False
            #add code to send ssh signal to door
            break
    if not match:
        key_denied.value = True
        time.sleep(15)
        key_denied.value = False
    
