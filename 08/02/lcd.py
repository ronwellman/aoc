#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lcd.py
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

def draw_rect(lcd,dim):
    x,y = dim.split('x')
    
    #light up the pixels
    for row in range(int(y)):
        for col in range(int(x)):
            lcd[row][col] = '#'

def shift_row(lcd,y,num):
    
    y = int(y)
    num=int(num)
    
    #build a temp row
    row = ['']*50
    
    #shift positions right and copy old list into the new list
    for x,p in enumerate(lcd[y]):
        row[(x+num)%50] = p
    
    lcd[y] = row
    
    
    
def shift_col(lcd,x,num):
    
    #convert
    x = int(x)
    num = int(num)
    
    #create new col
    col = ['']*6
    
    #shift positions and copy values from old col into new
    for n,row in enumerate(lcd):
        col[(n+num)%6] = row[x]
        
    for n,p in enumerate(col):
        lcd[n][x] = p
    

def count_pixels(lcd):
    
    cnt = 0
    cnt2 = 0
    
    #move through the lcd and count the #s
    for row in lcd:
        row = [x for x in row if x == '#']
        cnt += len(row)
    return cnt
    
def main(args):
    
    with open(args[1]) as f:
        inst = f.readlines()
    
    lcd = []
    for row in range(6):
        lcd.append([' ']*50)
        
    inst = [x.strip() for x in inst]
    
    #check command and modify lcd by reference
    for cmd in inst:
        cmd = cmd.split()
        if cmd[0] == 'rect':
            draw_rect(lcd,cmd[1])
        if cmd[0] == 'rotate' and cmd[1] == 'row':
            shift_row(lcd,cmd[2].split('=')[-1],cmd[-1])
        if cmd[0] == 'rotate' and cmd[1] == 'column':
            shift_col(lcd,cmd[2].split('=')[-1],cmd[-1])
    
    #print out the lcd
    for row in lcd:
        print row
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
