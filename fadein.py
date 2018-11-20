# program: fadein.py
# author: Akshyata
# course: CS827 (Computer Audio)
# date: November 19th 2018
# student ID: 200394002
# description: This program takes in a file mysteryTones.dat as input and gives back a output.dat file as the output. 
#              Both the .dat files are PCM encoded files.

# importing all the relevant libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import matplotlib.pyplot as plt

# Providing the path for the input .dat file.
data = pd.read_csv("C:/Users/AKSHITA/Desktop/computer Audio/Assignment 3/MysteryTones.dat", header=None, delimiter=r"\s+")

x = data[0]
y = data[1]
xarray = []
yarray = []

# the lists are filled by reading the coloumn contents
for i in range(0,int(len(x))):
   xarray.append(float(x.iloc[i]))
   yarray.append(float(y.iloc[i]))   

f = open("output.dat", "w")


# add header required for pcm file

f.write("; Sample Rate "+str(44100)+"\n")
f.write("; Channels 1"+"\n")

# simple fadein filter/effect
# Taking two variables factor and fnew.These are the multiplicative factors. 
# factor is initially assigned a value 1. fnew is initialised by total number of samples in input file.
# the amplitude values are multiplied with the factors.
# this factor when multiplied to the amplitudes will give the fading-in wave.

factor = 1
fnew = 113776
yarray[0] = 0
f.write(str(xarray[0])+"   "+str(((yarray[0]))))
for i in range(1,int(len(xarray))):
   f.write(str(xarray[i])+"   "+str(((yarray[i]))*(factor/fnew))+"\n")
   factor = factor + 1
f.close() 
