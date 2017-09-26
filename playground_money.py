# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 01:42:48 2017

@author: AB Sanyal

Money Playground
"""

#imports
import numpy as np
from amibi_money import *
from progbar import *
import matplotlib.pyplot as plt


#Constants
N = 1000
t_stop = 20

family = []
wealth_list = []

#Create initial population
for n in range( N ):
    family.append( amibi( np.random.randint( 0, 10 ) ) )

#Main Routine
t = 0
while ( t <= t_stop):

    wealth_list = []

    for a in family:
        wealth_list.append( a.money )

    plt.hist( wealth_list )
    plt.show()

    print( "\nCalculating at t = ", t )

    for a in family:

        progressbar( a.idno, 1, len( family ) )

        transferlist = family[ : ]
        transferlist.remove( a )
        b = np.random.choice( transferlist )
#        while ( b.money != 0 ):
#            b = np.random.choice( transferlist )

        if ( a.money > 0 ):
            a.money -= 1
            b.money += 1
    t += 1

#Accounting
wealth_list = []

for a in family:
    wealth_list.append( a.money )

plt.hist( wealth_list )
plt.show()