#! /usr/bin/python
"""
Pyreshut 1.0
Coded by: ViCoder32

    Simple or even primitive library for reboot or
    shutdown pc with using low-level code on my
    favourite C. In next version I will update this
    library and add new functional, but while it`s 
    basic kit for control most low level your pc, 
    I don`t know why nobody written library, which
    I written for 1 hour with beer and berserk on 
    monitor. Fuck, 45 strings in python file, 
    and 38 strings in C file

"""
from ctypes import CDLL
import sys

def shutdown():
    src = CDLL("./pyreshut.so")
    src.shutdown()





def reboot():
    src = CDLL("./pyreshut.so")
    src.reboot_machine()




def debug_menu():
    if "off" in sys.argv:
        shutdown()
    elif "reboot" in sys.argv:
        reboot()
  
if __name__ == '__main__':
    pass



