#!/usr/bin/python
import time
import datetime
from Adafruit_LED_Backpack import SevenSegment

segment = SevenSegment.SevenSegment(address=0x70)
# Continually update the time on a 4 char, 7-segment display
segment.begin()


def countdown(t):
    now = datetime.datetime.now()   
    second = now.second
    segment.clear()
    while t:
        mins, secs = divmod(t, 60)
        time.sleep(1)
        t -= 1
        segment.set_digit(0, int(mins / 10))     # Tens
        segment.set_digit(1, mins % 10)          # Ones
        # Set minutes
        segment.set_digit(2, int(secs / 10))   # Tens
        segment.set_digit(3, secs % 10)        # Ones
        # Toggle colon
        segment.set_colon(second % 2)              # Toggle colon at 1Hz
        # Write the display buffer to the hardware.  This must be called to
        # update the actual display LEDs.
        segment.write_display()

        # Wait a quarter second (less than 1 second to prevent colon blinking getting$
        # time.sleep(0.25)

    print('Fire in the hole!')

t = 120 # in seconds
countdown(t)
