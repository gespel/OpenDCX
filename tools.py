import math

def db_to_gain_value(db):
    return (db + 15) * 10

def get_filter(name):
    if name == "but6":
        return 0x01
    elif name == "but12":
        return 0x02
    elif name == "bes12":
        return 0x03
    elif name == "lr12":
        return 0x04
    elif name == "but18":
        return 0x05
    elif name == "but24":
        return 0x06
    elif name == "bes24":
        return 0x07
    elif name == "lr24":
        return 0x08
    elif name == "but48":
        return 0x09
    elif name == "lr48":
        return 0x0A
    else:
        return 0x00

def get_channel(name):
    if name == "a":
        return 0x01
    elif name == "b":
        return 0x02
    elif name == "c":
        return 0x03
    elif name == "sum":
        return 0x04
    elif name == "1":
        return 0x05
    elif name == "2":
        return 0x06
    elif name == "3":
        return 0x07
    elif name == "4":
        return 0x08
    elif name == "5":
        return 0x09
    elif name == "6":
        return 0x0A

def to_sysex_14bit(value):
    valuehi = (value >> 7) & 0x7F
    valuelo = value & 0x7F
    return valuehi, valuelo

def hz_to_param(hz: float) -> int:
    log_min = math.log10(20)
    log_max = math.log10(20000)
    log_hz  = math.log10(hz)

    normalized = (log_hz - log_min) / (log_max - log_min)
    param_value = int(round(normalized * 320))
    return param_value-1
