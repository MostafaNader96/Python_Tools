#!/usr/bin/env python3.8

#AUTHOR: MOSTAFA NADER#

#PhoneBook Manual
  #Passing Arguments: 
    #Add:       For adding a new contact in the phonebook
    #Printall:  Printing all the saved contacts in the phonebook
    #Delete:    Deleting a certain contact by name from the phonebook
    #Search:    Searching for a certain contact by name from the phonebook
  
#Examples for running in the cmd:
    #PhoneBook.py Add
    #PhoneBook.py Printall
    #PhoneBook.py Delete
    #PhoneBook.py Search
    
#File phonebook.txt acts as a database for the contact not to be deleted even when the cmd is closed

import sys

args=sys.argv[1:]
pb={}

def phonebook():
  number=0
  f=open('phonebook.txt','r+')
  lines=f.readlines()
  if len(lines)==0:
    number=0
  else:
    for i in lines:
      number=number+1
  pb[number]={}
  
  if sys.argv[1]=="Add":
    name=input("Whats the name of the contact: ")
    phone=input("Whats the phone number of the contact: ")
    email=input("Whats the email of the contact: ")
    pb[number]['Name']=name
    pb[number]['Phone']=phone
    pb[number]['Email']=email 
    f.write(str(pb)+ "\n")
    f.close();
  
  if sys.argv[1]=="Printall":
    for i in lines:
      print(i)
      
  if sys.argv[1]=="Delete":
    delname=input("Whats the name of the contact you want to delete: ")
    f=open('phonebook.txt','w')
    for i in lines:
      if delname not in i:
        f.write(i)
  f.close()
    
  if sys.argv[1]=="Search":
    count=0
    sername=input("Whats the name of the contact you want to Search: ")
    for i in lines:
      if sername in i:
        count=count+1
        print(i)
    if count==0:
      print("Contact Enetered Is Not Found!!")

if __name__=="__main__":
  phonebook() 
  