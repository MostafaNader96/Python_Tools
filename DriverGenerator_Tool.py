import os



def create():
  name=input("Please enter the name of the driver")
  os.mkdir(name+'_Driver')
  os.chdir('./'+name+'_Driver')
  a=open(name+'_config.h','w')
  b=open(name+'_register.h','w')
  c=open(name+'_private.h','w')
  d=open(name+'_interface.h','w')
  e=open(name+'_program.c','w')
  a.close()
  b.close()
  c.close()
  d.close()
  e.close()
  
  f=open(name+'_program.c','r+')
  
  f.write('#include "'+name+'_config.h"'+'\n')
  f.write('#include "'+name+'interface.h"'+'\n')
  f.write('#include "'+name+'private.h"'+'\n')
  f.write('#include "'+name+'register.h"'+'\n')
  f.close()

  
  
  
  
  
  
create()