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
#  

def flip_seq(word):
    
    return word[1] + word[0] + word[1]

def find_seq(i):
    maximum = len(i)
    matches = []
    
    #slide along the entire input
    for x in range(len(i)):
        
        #ensure there is still at least 4 characters left in the input
        if maximum - x >= 3:
            
            #1st char should match 3rd but not second
            if i[x] == i[x+2] and i[x] != i[x+1]:
                matches.append(i[x:x+3])
    
    return matches

def test_seq(address):
    address = address.upper()
    
    #regex pattern to find all the bracketed sections
    bracket = re.compile(r'(\[\S*?\])')
    
    #test brackets 1st to fail fast
    brackets = bracket.findall(address)
    matches = []
    
    #find all the patterns within the brackets
    for b in brackets:
        
        #load up all the patterns in a list
        for m in find_seq(b):
            matches.append(m)
    
    #now attempt to find the flipped pattern in the remaining sections of the address
    for section in [b for b in bracket.split(address) if '[' not in b]:
        
        for p in matches:
            
            if flip_seq(p) in section:
                return True
    
    return False

def main(args):
    
    valid = 0
    
    with open(args[1]) as f:
        addresses = f.readlines()
    
    addresses = [x.strip() for x in addresses]
    
    #test each address and update the valid counter
    for addr in addresses:
        
        if test_seq(addr):
            valid += 1
        
    print valid
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
