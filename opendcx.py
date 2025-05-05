import serial
import time
from tools import *

SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 38400

class OpenDCX(object):
    def __init__(self, timing=False):
        self.timing = timing
        if self.timing:
            self.last_sent_command = time.time()
        with serial.Serial(SERIAL_PORT, BAUD_RATE, bytesize=serial.EIGHTBITS,
                           parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                           timeout=1) as ser:
            print("Remote Control Enable...")
            enable_remote = bytes([0xF0, 0x00, 0x20, 0x32, 0x00, 0x0E, 0x3F, 0x04, 0x00, 0xF7])
            ser.write(enable_remote)

    def send_command(self, function, num_params, address, parameternum, value):
        if self.timing:
            if self.last_sent_command-0.05 > time.time():
                self.last_sent_command = time.time()
            else:
                time.sleep(0.05)
        with serial.Serial(SERIAL_PORT, BAUD_RATE, bytesize=serial.EIGHTBITS,
                           parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                           timeout=1) as ser:
            valuehi, valuelo = to_sysex_14bit(value)
            ser.write(bytes([0xF0, 0x00, 0x20, 0x32, 0x00, 0x0E,
                             function, num_params,
                             address,
                             parameternum,
                             valuehi, valuelo,
                             0xF7]))

    def mute_channel(self, addr):
        self.send_command(0x20, 0x01, addr, 0x03, 1)

    def unmute_channel(self, addr):
        self.send_command(0x20, 0x01, addr, 0x03, 0)

    def set_gain(self, addr, gain):
        self.send_command(0x20, 0x01, addr, 0x02, gain)

    def set_highpass_filter(self, addr, filter_type, filter_frequency):
        self.send_command(0x20, 0x01, addr, 0x42, filter_type)
        self.send_command(0x20, 0x01, addr, 0x43, filter_frequency)

    def set_lowpass_filter(self, addr, filter_type, filter_frequency):
        self.send_command(0x20, 0x01, addr, 0x44, filter_type)
        self.send_command(0x20, 0x01, addr, 0x45, filter_frequency)

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

o = OpenDCX()

o.mute_channel(
    get_channel("a")
)
o.mute_channel(
    get_channel("b")
)
o.mute_channel(
    get_channel("c")
)

o.mute_channel(
    get_channel("1")
)
o.mute_channel(
    get_channel("2")
)
o.mute_channel(
    get_channel("3")
)
o.mute_channel(
    get_channel("4")
)
o.mute_channel(
    get_channel("5")
)
o.mute_channel(
    get_channel("6")
)

o.set_gain(
    get_channel("a"),
    db_to_gain_value(0)
)
o.set_gain(
    get_channel("b"),
    db_to_gain_value(0)
)
o.set_gain(
    get_channel("c"),
    db_to_gain_value(0)
)

o.set_gain(
    get_channel("1"),
    db_to_gain_value(0)
)
o.set_gain(
    get_channel("2"),
    db_to_gain_value(0)
)
o.set_gain(
    get_channel("3"),
    db_to_gain_value(0)
)
o.set_gain(
    get_channel("4"),
    db_to_gain_value(0)
)
o.set_gain(
    get_channel("5"),
    db_to_gain_value(0)
)
o.set_gain(
    get_channel("6"),
    db_to_gain_value(0)
)

o.set_highpass_filter(
    get_channel("1"),
    get_filter("but48"),
    hz_to_param(39)
)
o.set_lowpass_filter(
    get_channel("1"),
    get_filter("but48"),
    hz_to_param(105)
)
o.set_highpass_filter(
    get_channel("2"),
    get_filter("but48"),
    hz_to_param(39)
)
o.set_lowpass_filter(
    get_channel("2"),
    get_filter("but48"),
    hz_to_param(105)
)
o.set_highpass_filter(
    get_channel("3"),
    get_filter("but48"),
    hz_to_param(39)
)
o.set_lowpass_filter(
    get_channel("3"),
    get_filter("but48"),
    hz_to_param(105)
)

o.set_highpass_filter(
    get_channel("4"),
    get_filter("but48"),
    hz_to_param(90)
)
o.set_lowpass_filter(
    get_channel("4"),
    get_filter(0),
    hz_to_param(1)
)
o.set_highpass_filter(
    get_channel("5"),
    get_filter("but48"),
    hz_to_param(90)
)
o.set_lowpass_filter(
    get_channel("5"),
    get_filter(0),
    hz_to_param(1)
)
o.set_highpass_filter(
    get_channel("6"),
    get_filter(0),
    hz_to_param(1)
)
o.set_lowpass_filter(
    get_channel("6"),
    get_filter(0),
    hz_to_param(1)
)
#blinking_mutes(0.05)
