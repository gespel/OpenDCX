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

    def set_input_source(self, addr, input_source):
        self.send_command(0x20, 0x01, addr, 0x41, input_source)




