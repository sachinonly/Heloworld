#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os, sys, stat
os.chmod('samplefile.txt', 774)
try:
    fd = open ("samplefile.txt","w")
    touch "touch.txt"
    print "Openining samplefile.txt for read file name is:", fd.name
    fd.append ("File contents added from script ")
    fd.seek(0,0)
    for x in fd.readlines():
        
        print " First 5 char", fd.tell(),fd.read()
except IOError, e:
    print "errror", e
    
