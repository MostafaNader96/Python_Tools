import os

#This Tool takes a Driver's name as an input from the user and generates five files in a directory:
#Name_config.h
#Name_register.h
#Name_private.h
#Name_interface.h
#Name_program.c
#The program.c file contains the other four files included inside it as #define "name_xxxx.h"

def CreateDriver():
  
  name=input("Please Enter The Name Of The Driver: ")
  
  os.mkdir(name+'_Driver')
  os.chdir('./'+name+'_Driver')
  
  ConfigFile=open(name+'_config.h','w')
  RegisterFile=open(name+'_register.h','w')
  PrivateFile=open(name+'_private.h','w')
  InterfaceFile=open(name+'_interface.h','w')
  ProgramFile=open(name+'_program.c','w')
  
  ConfigFile.close()
  RegisterFile.close()
  PrivateFile.close()
  InterfaceFile.close()
  ProgramFile.close()
  
  ProgramFile=open(name+'_program.c','r+')
  
  ProgramFile.write('#include "'+name+'_config.h"'+'\n')
  ProgramFile.write('#include "'+name+'_interface.h"'+'\n')
  ProgramFile.write('#include "'+name+'_private.h"'+'\n')
  ProgramFile.write('#include "'+name+'_register.h"'+'\n')
  ProgramFile.close()

  
CreateDriver()