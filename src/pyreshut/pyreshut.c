/* 
Pyreshut 1.0
Coded by: ViCoder32

    Simple for reboot or
    shutdown pc with using C language.
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


