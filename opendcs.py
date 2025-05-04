import serial
import time

SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 38400

def mute_channel(addr):
    mute_input_a = bytes([0xF0, 0x00, 0x20, 0x32, 0x00, 0x0E,
                      0x20, 0x01,  # function + 1 param
                      addr,        # channel 1 (Input A)
                      0x03,        # parameternum: mute
                      0x00, 0x01,  # value: 1 (on)
                      0xF7])
    with serial.Serial(SERIAL_PORT, BAUD_RATE, bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                    timeout=1) as ser:
        ser.write(mute_input_a)

def unmute_channel(addr):
    unmute_input_a = bytes([0xF0, 0x00, 0x20, 0x32, 0x00, 0x0E,
                      0x20, 0x01,  # function + 1 param
                      addr,        # channel 1 (Input A)
                      0x03,        # parameternum: mute
                      0x00, 0x00,  # value: 1 (on)
                      0xF7])
    with serial.Serial(SERIAL_PORT, BAUD_RATE, bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                    timeout=1) as ser:
        ser.write(unmute_input_a)

def blinking_mutes():
    while True:
        unmute_channel(0x05)
        mute_channel(0x06)
        time.sleep(0.1)
        unmute_channel(0x06)
        mute_channel(0x07)
        time.sleep(0.1)
        unmute_channel(0x07)
        mute_channel(0x08)
        time.sleep(0.1)
        unmute_channel(0x08)
        mute_channel(0x09)
        time.sleep(0.1)
        unmute_channel(0x09)
        mute_channel(0x0a)
        time.sleep(0.1)
        unmute_channel(0x0a)
        mute_channel(0x05)
        time.sleep(0.1)

enable_remote = bytes([0xF0, 0x00, 0x20, 0x32, 0x00, 0x0E, 0x3F, 0x04, 0x00, 0xF7])

while True:
    with serial.Serial(SERIAL_PORT, BAUD_RATE, bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                    timeout=1) as ser:
        print("Sende: Remote Control Enable...")
        ser.write(enable_remote)
    blinking_mutes()
