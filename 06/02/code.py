#!/usr/bin/env python

from collections import Counter

# -*- coding: utf-8 -*-
#
#  code.py
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
def get_most_common(code,x):
    cnt = Counter()
    print x
    for l in code:
        
        cnt[l[x]] += 1
    #returns the least common letter
    return cnt.most_common()[-1][0][0]

def main(args):
    
    with open(args[1]) as f:
        code = f.readlines()
        
    code = [x.strip() for x in code]
    message = ''
    for x in range(len(code[0])):
        message += get_most_common(code,x)
    
    print message
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
