#!/usr/bin/env python

#keep track of where we have been
coords = [(0,0)]
collision = []

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
    
    #find new direction based on previous direction and current turn
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

    #based on direction increment/decrement x or y
    if direction == 'N':
        y2 = 1
        x2 = 0
    elif direction == 'S':
        y2 = -1
        x2 = 0
    elif direction == 'E':
        x2 = 1
        y2 = 0
    else:
        x2 = -1
        y2 = 0
        
    #record each of the coordinates one by one and look for collisions
    for m in range(distance):
        
        #calc new coords
        y += 1 * y2
        x += 1 * x2
        
        if (x,y) in coords:
                
            #if coordinate already exists we have been here before indicating 
            #the true position of the HQ break as there is no reason to 
            #continue the loop 
            collision.append((x,y))
            break
        else:
            
            #record current position
            coords.append((x,y))
    
    return x,y
    



    
def main(args):
    
    x = 0
    y = 0
    
    direction='N'
    
    #get and format input
    with open(args[1]) as f:
        grids = f.read()
    
    grids = [g.strip() for g in grids.split(',')]
    
    #loop through movements
    for movement in grids:
        
        #determine new direction
        direction = change_direction(direction,movement)
        
        #record coordinates moved in the coord list
        x,y = record_distance(x,y,direction,movement)
        
        #if a collision was recorded, break out of the loop
        if len(collision) != 0:
            break
    
    #find the non-direct (non-diagonal) distance between x and y        
    print abs(x) + abs(y)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
