#!/usr/bin/env python

import re

# -*- coding: utf-8 -*-
#
#  ipv7.py
#  
#  Copyright 2016 ron <ron.wellman01@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def find_abba(i):
    maximum = len(i)
    
    #slide along the entire input
    for x in range(len(i)):
        
        #ensure there is still at least 4 characters left in the input
        if maximum - x >= 4:
            
            #the last two characters should be the inverse of the first two characters
            #but the inner characters should not be the same as the outer characters
            if i[x:x+2] == i[x+2:x+4][::-1] and i[x+1] != i[x]:
                return True
    
    #if pattern was not found, return false
    return False

def test_abba(address):
    
    #regex pattern to find all the bracketed sections
    bracket = re.compile(r'(\[\S*?\])')
    
    #test brackets 1st to fail fast
    brackets = bracket.findall(address)

    for b in brackets:
        
        #check each of the bracketed sections 1 by 1 and fail fast
        if find_abba(b):
            return False
    
    #now attempt to find the abba pattern in the remaining sections of the address
    for section in [b for b in bracket.split(address) if '[' not in b]:
        
        if find_abba(section):
            return True
    
    return False

def main(args):
    
    valid = 0
    
    with open(args[1]) as f:
        addresses = f.readlines()
    
    addresses = [x.strip() for x in addresses]
    
    #test each address and update the valid counter
    for addr in addresses:
        
        if test_abba(addr):
            valid += 1
        
    print valid
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
