#!/usr/bin/env python

from collections import Counter
import string

#build a dictionary for the alphabet for easy lookup
ascii = string.ascii_lowercase
alpha = {}

for x in range(26):
    alpha[ascii[x]] = x
    
    
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

#shift cypher using the sector number
def decrypt_room(enc_name, sector):
    
    dec_name = []
    
    for enc_word in enc_name:
        dec_word = ''
        
        for l in enc_word:
            #find the value (0-26) of the letter, add in the sector, mod by 26,
            #and then find the letter that lines up with that number
            dec_word += ascii[(alpha[l] + sector) % 26]
        
        dec_name.append(dec_word)
    
    return ' '.join(dec_name)
    

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
        sector = int(sector)
        
        #if the top5 are equal to the code decrypt it
        if top5 == code[:-1]:
            
            #decrypt the names using a shift cypher based on sector number
            decrypted_rm = decrypt_room(r.split('-')[:-1],int(sector))
            
            #look for entries that contain the word pole as in northpole
            if 'pole' in decrypted_rm:
                print decrypted_rm, sector
            
  
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
