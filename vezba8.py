#This program calculates the influence of Temperature on enzyme
#activity. I am using it to choose what is the best temperature
#for invertase. 

import numpy as np
import matplotlib.pyplot as plt

#Za vezbu 8

#Jedinica za Konstantu DNS-a [dm^3/mmol]
k_dns = 0.24
odnos = {}

#### GOING TO WORK ON THIS; AS EACH TEMPERATURE IN THIS case
### HAS ITS OWN SET OF VALUES CONNECTED TO IT
#class Temperatura():
#    def __init__(self, brzina, SAk):
#        self.brzina = brzina
#        self.SAk = SAk


def list_maker(x, z):
    """X is a list to which we are going to append values
    z is a string; essentially a type of parameter for which we want to
    take in values. pH, concentrantation, Apsorbance and similar """
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
    return round(slope, 3)

v = input("What's the volume of reaction mixture: ")

#Creates a list of all the times in which the reaction took place
#and we took the value of apsorbance.
t_values = list()
list_maker(t_values, 'time')
print(t_values)
#Temperatures at which we are looking at the reaction
T = list()
list_maker(T, 'Temperature')
print(T)
Cp = 0.002
#Zapreminska aktivnost koju mi racunamo jeste samo zapreminska aktivnost
#za zadatu reakcionu smesu

#Apsorbanca

for temperature in T:
    #Apsorbanca za zadatu temperaturu
    A = list()
    A = list_maker(A, 'Apsorbance for temperature {0} degrees'.format(temperature))
    conc = concentration(A)
    slope_value = slope(t_values, conc)
    odnos[temperature] = round(slope_value,4)

v_reakcije = {}
for key in odnos:
    v_reakcije[key] = odnos[key]*10**(-3)/60

SA = {}
for key in odnos:
    SA[key] = round(odnos[key]/Cp,6)

for key in sorted(odnos):
    print('Temp: {0}, Brzina: {1}, SA: {2}'.format(key, v_reakcije[key], SA[key]))
