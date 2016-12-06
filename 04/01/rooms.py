#!/usr/bin/env python

from collections import Counter

# -*- coding: utf-8 -*-
#
#  untitled.py
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


def main(args):
    
    valid_sector = 0
    
    with open(args[1]) as f:
        rooms = f.readlines()
    
    rooms = [r.strip() for r in rooms]
    
    for r in rooms:
        
        #build a counter object
        cnt = Counter()
        
        #get the letters
        letters = ''.join(r.split('-')[:-1])
        
        #load the counter object with the letters and cnt
        for l in letters:
            cnt[l] += 1
        
        #find the top 25, sort it by most common and then alphabetical, and
        #return only the top 5
        top5 = ''.join([x[0] for x in sorted(cnt.most_common(25),\
            key=lambda x: (x[1],-ord(x[0])), reverse=True)][0:5])
        
        #split out the code and sector number
        sector,code = r.split('-')[-1].split('[')
        
        #if the top5 are equal to the code add in the sector number
        if top5 == code[:-1]:
            valid_sector += int(sector)
            
    print valid_sector    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
