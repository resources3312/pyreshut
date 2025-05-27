#! /usr/bin/python
"""
Pyreshut 1.1
Coded by: ViCoder32

    Simple library for reboot or
    shutdown pc with using C language.

"""
from ctypes import CDLL
import sys


class powerController:
    def __init__(self):
        self.src = CDLL("./pyreshut.so")
    
    def shutdown(self)
        self.src.shutdown()

    def reboot():
        self.src.reboot_machine()




def debugMenu():
    power = powerController()
    match sys.argv[1]:
        case "shutdown": power.shutdown()
        case "reboot": power.reboot()


if __name__ == '__main__': pass
