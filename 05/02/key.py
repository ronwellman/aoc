#!/usr/bin/env python

import hashlib

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
    
    door_id = 'ffykfhsq'
    door_code = [' '] * 8
    found = 0
    cnt = 0
    
    while found < 8:
        
        #get hash
        h = hashlib.md5(door_id + str(cnt)).hexdigest()
        
        #look for leading zeros and update door_code
        if h[0:5] == '00000' and h[5].isdigit() and int(h[5]) <= 7 and door_code[int(h[5])] == ' ':
            door_code[int(h[5])] = h[6]
            found += 1
            print('{0:<40} {1}').format(door_code, cnt)
        
        #update counter
        cnt += 1
    print '---------------'
    print ''.join(door_code)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
