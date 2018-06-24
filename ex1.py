#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 10:17:36 2018

@author: sachin
"""


print "Hello  Program file ex1.py"

try: 
    x = input("Enter first number : ")
    y = input("Enter second number : ")
    res = x/y
    print "Result of Division",res
except ZeroDivisionError,e:    
    print "ZDE:Zero div error",e
    
except NameError,e:    
    print "NE:Name Error",e 
except TypeError,e:    
    print "TE:Type Error",e     
    
except Exception :    
    print "Default:This is default exception",e 
    

else:
    print "else block is executed  no error in program"

finally:
    print "Finally this will get executed all times"