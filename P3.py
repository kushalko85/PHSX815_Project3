#! /usr/bin/env python
import sys
import numpy as np
import pandas as pd
#from Random import Random
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import random
from scipy.stats import norm
from scipy.optimize import curve_fit
import matplotlib.mlab as mlab
from matplotlib.colors import LogNorm
 # read the user-provided seed from the command line (if there)
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed <number>] [-trial_b <number of trials for biased dice>] [-trial_n <number of fair trials for trial_b dice>]" % sys.argv[0])
        sys.exit(1)

    # default seed and trial from suspected dice
    seed = 3333
    trial_b = (25)
    trial_n = (100)
    p6 = (0.5)
# default slices to pull out of neymann construction
    prob1 = 0.9
    prob2 = 0.1
    prob3 = 0.2
    #Slice of the 2D Histogram
    Slice1 = []
    Slice2 = []
    Slice3 = []


    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]

    if '-trial_b' in sys.argv:
        p = sys.argv.index('-trial_b')
        trial_b = sys.argv[p+1]
        trial_b = int(sys.argv[p+1])

    if '-trial_n' in sys.argv:
        p = sys.argv.index('-trial_n')
        trial_n = sys.argv[p+1]
        trial_n = int(sys.argv[p+1])

    if '-p6' in sys.argv:
        p = sys.argv.index('-p6')
        p6 = float(sys.argv[p+1])

    if '-prob1' in sys.argv:
        p = sys.argv.index('-prob1')
        prob1 = float(sys.argv[p+1])

        
# make a gaussian distribution for outcome 6
#generate unfair outcomes from random numbers
listd=[1,2,3,4,5,6]
xxx=int(trial_b)
p1,p2,p3,p4,p5 = (1-p6)/5.,(1-p6)/5.,(1-p6)/5.,(1-p6)/5.,(1-p6)/5.
rolls_dist_100 = [random.choices(listd, weights =(p1,p2,p3,p4,p5,p6), k = xxx) for num_trials in range(trial_n)]
roll_dist_int = []
#print(rolls_dist_100)
for line_list in rolls_dist_100:
    for x in line_list:
        valuex= int(x)
        roll_dist_int.append(valuex)





# writing array in the file 
f = open("biased_dice.txt", "w")
np.savetxt(f,roll_dist_int)
f.close()

# making a dict and setting counter for each number as 0 and looping and adding # count
counter = {1:0,2:0,3:0,4:0,5:0,6:0}
for lst in roll_dist_int:
    if lst ==1:
        counter[1]=counter[1]+1
    if lst ==2:
        counter[2]=counter[2]+1
    if lst ==3:
        counter[3]=counter[3]+1
    if lst ==4:
        counter[4]=counter[4]+1
    if lst ==5:
        counter[5]=counter[5]+1
    if lst ==6:
        counter[6]=counter[6]+1

# Writing count in a file with header
with open("biased_dice_counter.txt","w") as counter_file:
    w = csv.writer(counter_file)
    w.writerow(["number", "count"])
    for key, val in counter.items():
        w.writerow([key, val])
    counter_file.close()


# Reading count file and converting into list by separating with ,    
file1 = open('biased_dice_counter.txt', 'r')
Lines = file1.readlines()[1:]
x_count=[]
y_count=[]
# Strips the newline character
for line in Lines:
    number,count = line.split(',')
    x_count.append(int(number))
    y_count.append(int(count))
    

#write unfair output of trials in a file 
g = open("ufair_dice.txt", "w")
np.savetxt(g,rolls_dist_100)
g.close()


file_test=open("ufair_dice.txt","r")
value_list=[]
for line in file_test:
    line=line.strip()
    for x in line:
        number = x
        value_list.append(number)
    


# Reading count file and converting into list by separating with ,    
file1 = open('ufair_dice.txt', 'r')
Lines = file1.readlines()
# Strips the newline character
line_count = 1
ufair_dice_table = {}
for line in Lines:
    six_count =0
    list_of_samples = list(line.split())
    for value in list_of_samples:
        if int(float(value))==6:
            six_count=six_count+1
    ufair_dice_table[line_count]=six_count
    line_count=1+line_count
    
#print(six_count)
    
# Writing count in a file with header
with open("ufair_dice_counter.txt","w") as ufair_counter_file:
    w = csv.writer(ufair_counter_file)
    w.writerow(["line_number", "six_count"])
    for key, val in ufair_dice_table.items():
        w.writerow([key, val])
    ufair_counter_file.close()



 
