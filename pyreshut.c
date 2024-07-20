/* 
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
 */
#include <unistd.h>
#define REBOOT 0x1234567 
#define POWER_OFF 0x4321FEDC 

void shutdown(){
  sync();   
  reboot(POWER_OFF); 
  }


void reboot_machine(){
  sync();
  reboot(REBOOT);
}


