#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  triangles.py
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
    valid = 0
    
    with open(args[1]) as f:
        triangles = f.readlines()
        
    triangles = [t.strip() for t in triangles]
    
    for t in triangles:
        
        #load triangle sides into x,y,x
        x,y,z = t.split()
        
        #sort them to ensure the largets number is in z
        x,y,z = sorted([int(x),int(y),int(z)])
        
        #ballpark check for valid triagles says that z has to be less than x+y
        if (x+y) > z:
            valid += 1
            
    print valid
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
