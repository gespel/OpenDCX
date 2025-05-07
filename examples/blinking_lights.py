import time

from opendcx import OpenDCX


def blinking_mutes(sleep_time):
    opendcx = OpenDCX()
    while True:
        opendcx.unmute_channel(0x05)
        opendcx.mute_channel(0x06)
        time.sleep(sleep_time)
        opendcx.unmute_channel(0x06)
        opendcx.mute_channel(0x07)
        time.sleep(sleep_time)
        opendcx.unmute_channel(0x07)
        opendcx.mute_channel(0x08)
        time.sleep(sleep_time)
        opendcx.unmute_channel(0x08)
        opendcx.mute_channel(0x09)
        time.sleep(sleep_time)
        opendcx.unmute_channel(0x09)
        opendcx.mute_channel(0x0a)
        time.sleep(sleep_time)
        opendcx.unmute_channel(0x0a)
        opendcx.mute_channel(0x05)
        time.sleep(sleep_time)

blinking_mutes(0.05)