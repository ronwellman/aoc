#!/usr/bin/env python
keypad = [['X','X','1','X','X'],
          ['X','2','3','4','X'],
          ['5','6','7','8','9'],
          ['X','A','B','C','X'],
          ['X','X','D','X','X']]

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
    
    output = []
    pattern = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
    x1 = 0
    y1 = 2
    
    with open(args[1]) as f:
        code = f.readlines()
    
    code =  [l.strip() for l in code]   
    
    for digit in code:
        
        for movement in digit:
            
            y2,x2 = pattern[movement]
            x2 = x1 + x2
            y2 = y1 + y2
            
                       
            if x2 < 0:
                x2 = 0
            if x2 > 4:
                x2 = 4
            if y2 < 0:
                y2 = 0
            if y2 > 4:
                y2 = 4
            
            #if an X was not found, set the new coordinates
            if keypad[y2][x2] != 'X':
                x1,y1 = x2,y2
            
        output.append(keypad[y1][x1])
    
    print ''.join(output)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
