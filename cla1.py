#!/usr/bin/env python2
# -*- coding: utf-8 -*-
print "Hello  Program file cla0.py"

import sys
import os
name = os.name
print "The operating system name is", name
if name == 'posix':
    os.system('clear')
elif name == 'nt' or name == 'dos':
    os.system('cls')
else:
    print("\n" * 30)

print "Total number of command line arguments are:",len(sys.argv)
print "List  of command line arguments are:",sys.argv
print "First Value  of command line arguments are:",sys.argv[0]
print "Tyoe   of command line arguments are:",type(sys.argv[0])

#print "Sum int of arg1 and arg 2   of command line arguments are:", int(sys.argv[1]) + int (sys.argv[2])
print "Sum eval   of command line arguments are:",eval(sys.argv[1]) +  eval(sys.argv[2])

y = len(sys.argv)

for x in range(1,y):
    print "Parameter at postition %s is %s" %(x,sys.argv[x])  

os.system('clear')

print "****** WHILE LOOP Example ************"

print "This will now be same in while loop to do sum"

i=1
result = 0

while (i < len(sys.argv)):
    print "Command Line argument for %s is %s"  %(i,sys.argv[i])
    result += int(sys.argv[i])
    i+=1  
    
print "Sum is %s"  %(result)
    
   
#for index,y in enumerate(sys.argv):
#    z = "Parameter at position %s  is %s" % (index,y)
#    print z    