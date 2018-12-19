#Calculating the optimal pH for a certain enzyme

import numpy as np
import matplotlib.pyplot as plt

#Jedinica za Konstantu DNS-a [dm^3/mmol]
k_dns = 0.24
odnos = {}

def list_maker(x, z):
    """x predstavlja listu u kojoj ce biti ubacene date vrednosti.
    dok z predstavlja string, kako bi znali tacno koje vrednosti da ubacimo. """
    while True:
        y = input('Enter the value of {0}: '.format(z))
        if len(y) == 0:
            return x
        x.append(y)

def concentration(x):
    """Takes on the list of different apsorbances and gives back the concentration"""
    conc = list()
    for value in x:
        conc.append(round(float(value)/0.24, 4))
    return conc

def slope(x,y):
    """This program essentially calculates the value of the slope
    based on the values for conenctration and time. In fact this
    function can be used for any slope, however in our case we will
    use it for conc = f(t)"""
    x = np.array(x)
    y = np.array(y)
    slope =  np.linalg.lstsq(x.reshape(-1,1), y) [0][0]
    return round(slope, 6)

v = input("What's the volume of reaction mixture: ")

#Creates a list of all the times in which the reaction took place
#and we took the value of apsorbance.
#t_values = list()
#list_maker(t_values, 'time')
t_values = [5, 10, 15]
#Creates the list of all the pHs.
ph_values = [3.6, 4.5, 6.0 , 7.0, 8.0]
#Koncentracija enzima u reakcionoj smesi
Cp = 0.002
slopes = {}

for value in ph_values:
    #Apsorbanca za zadatu temperaturu
    A = list()
    A = list_maker(A, 'apsorbanca za ph {0}'.format(value))
    conc = concentration(A)
    slope_value = slope(t_values, conc)
    slopes[value] = round(slope_value,6)

v_reakcije = {}
for key in slopes:
    v_reakcije[key] = slopes[key]*10**(-3)/60


SA = {}
for key in slopes:
    SA[key] = slopes[key]/Cp

for key in sorted(slopes):
    print('pH: {0}, Brzina: {1}, SA: {2}'.format(key, v_reakcije[key], SA[key]))
