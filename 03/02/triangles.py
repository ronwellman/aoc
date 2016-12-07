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
        
    triangles = [t.strip().split() for t in triangles]
    
    x = []
    y = []
    z = []
    
    #break columns into different lists
    for t in triangles:
        x.append(int(t[0]))
        y.append(int(t[1]))
        z.append(int(t[2]))
    
    #triangles are referenced in groups of 3 by column not by row
    for i in range(0,len(x),3):
        
        #build and sort triangles
        t1 = sorted([x[i],x[i+1],x[i+2]])
        t2 = sorted([y[i],y[i+1],y[i+2]])
        t3 = sorted([z[i],z[i+1],z[i+2]])
        
        #test if they are valid sides
        if (t1[0]+t1[1]) > t1[2]:
            valid += 1
        if (t2[0]+t2[1]) > t2[2]:
            valid += 1
        if (t3[0]+t3[1]) > t3[2]:
            valid += 1
    
    
    print valid
       
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
