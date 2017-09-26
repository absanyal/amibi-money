# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 20:17:26 2017

@author: AB Sanyal

A module form of the progressbar that can be reused anywhere.
"""

#imports
import sys
from itertools import cycle

sym_list = cycle( [ "(  ", " | ", "  )", " | " ] )

progress_symbol = "#"

def progressbar( v, v_min, v_max ):

    pc = int( ( v - v_min ) / ( v_max - v_min ) * 100 ) #percentage completed

    counter = int( pc / 10 )

    symbol = next( sym_list )

    message = "Progress: " + symbol + " " + progress_symbol * counter + " " + str( pc ) + " %"
    sys.stdout.write( '\r' + message )

    if ( v >= v_max ):
        done = "Progress: Done!"
        sys.stdout.write( '\r' + " " * len( message ) )
        sys.stdout.write( '\r' + done )