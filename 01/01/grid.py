#!/usr/bin/env python



# -*- coding: utf-8 -*-
#
#  grid.py
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


def change_direction(direction,movement):
    
    movement = movement[0]
    
    #find the result of Right/Left turns based on the original heading
    if direction  == 'N':
        if movement == 'L':
            return 'W'
        else:
            return 'E'
    elif direction == 'S':
        if movement == 'L':
            return 'E'
        else:
            return 'W'
    elif direction == 'E':
        if movement == 'L':
            return 'N'
        else:
            return 'S'
    else:
        if movement == 'L':
            return 'S'
        else:
            return 'N'


def record_distance(x,y,direction,movement):
    
    distance = int(movement[1:])
    
    #update position based on the direction being traveled
    if direction == 'N':
        y += distance
    elif direction == 'S':
        y -= distance
    elif direction == 'E':
        x += distance
    else:
        x -= distance
        
    return x,y
    
    
def main(args):
    
    x = 0
    y = 0
    
    #initially moving north
    direction='N'

    with open(args[1]) as f:
        grids = f.read()
    
    grids = [g.strip() for g in grids.split(',')]
    
    for movement in grids:
        
        #update direction
        direction = change_direction(direction,movement)
        
        #update position based on distance and direction
        x,y = record_distance(x,y,direction,movement)
    
    #find the non-direct (non-diagonal) distance between x and y
    print abs(x) + abs(y)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
