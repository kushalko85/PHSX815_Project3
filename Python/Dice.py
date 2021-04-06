#! /usr/bin/env python
import sys
import numpy as np
import pandas as pd
from Random import Random
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import random
from scipy.optimize import curve_fit
 # read the user-provided seed from the command line (if there)
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed <number>] [-trial_b <number of trials for biased dice>] [-trial_n <number of fair trials for trial_b dice>]" % sys.argv[0])
        sys.exit(1)

    # default seed and trial from suspected dice
    seed = 3333
    trial_b = (250)
    trial_n = (1000)


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

#class instance for random class

random_number = Random(seed)
myx = []


for x in range(0,trial_b):
    faces = random_number.Category6()
    myx.append(int(faces))
    

# writing array in the file 
f = open("biased_dice.txt", "w")
np.savetxt(f,myx)
f.close()

# making a dict and setting counter for each number as 0 and looping and adding # count
counter = {1:0,2:0,3:0,4:0,5:0,6:0}
for lst in myx:
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

#plot in bar diagram

plt.bar(x_count,y_count)
plt.grid(True)
plt.title('Outcome of the suspected Dice from 250 trials')
plt.xlabel('Faces')
plt.ylabel('Counts')
plt.savefig("biased_plot.png")
plt.show()






#generate fair outcomes from random numbers
rolls_dist_100 = [[random.randint(1, 6) for rolls in range(trial_b)] for num_trials in range(trial_n)]
roll_dist_int = []
for line_list in rolls_dist_100:
    for x in line_list:
        valuex= int(x)
        roll_dist_int.append(valuex)



#write fair output of trials in a file 
g = open("fair_dice.txt", "w")
np.savetxt(g,rolls_dist_100)
g.close()


file_test=open("fair_dice.txt","r")
value_list=[]
for line in file_test:
    line=line.strip()
    for x in line:
        number = x
        value_list.append(number)
    


# Reading count file and converting into list by separating with ,    
file1 = open('fair_dice.txt', 'r')
Lines = file1.readlines()
# Strips the newline character
line_count = 1
fair_dice_table = {}
for line in Lines:
    six_count =0
    list_of_samples = list(line.split())
    for value in list_of_samples:
        if int(float(value))==6:
            six_count=six_count+1
    fair_dice_table[line_count]=six_count
    line_count=1+line_count
    

# Writing count in a file with header
with open("fair_dice_counter.txt","w") as fair_counter_file:
    w = csv.writer(fair_counter_file)
    w.writerow(["line_number", "six_count"])
    for key, val in fair_dice_table.items():
        w.writerow([key, val])
    fair_counter_file.close()



#read the saved file

fair_dice_count_file = open('fair_dice_counter.txt', 'r')
Lines = fair_dice_count_file.readlines()[1:]

# Strips the newline character

total_maxima = int(trial_n)

six_count_in_range={}
for i in range(1,total_maxima+1):
    six_count_in_this_range=0
    for line in Lines:
        if int(line.split(',')[1])==i:
            six_count_in_this_range+=1
    six_count_in_range[i]=six_count_in_this_range

    #print(six_count_in_range)

N=[]
V=[]
for key,value in six_count_in_range.items():
    N.append(key)
    V.append(value)

plt.bar(N,V)
plt.xlim(10,100)
def func(x, a, b, c):
    # a Gaussian distribution
    return a * np.exp(-(x-b)**2/(2*c**2))

popt, pcov = curve_fit(func, N, V,p0=(1,90,90))

a,b,c = tuple(popt)

quantile2s =  b - 2*c
#quantile1s =  b-c
#quantile0s =  b
#quantile1sp = b+c
quantile2sp = b+2*c


x = np.linspace(0, 250, 10000)
y = func(x, *popt)
width = 1/1.5
plt.plot(x + width/2, y, c='r', label ='fit:a-%5.3f, b = %5.3f, c = %5.3f' %tuple(popt))

plt.title('Number of Sixes Rolled in 10000 Trials')
plt.axvline(quantile2s,label="-2 $\sigma$",color="green",linestyle = "--")
plt.axvline(82,label="counts of Sixes for suspected trial",color="yellow",linestyle = "--")
plt.xlabel('Number of sixes rolled')
plt.ylabel('Counts')

#plt.axvline(quantile0s,label="median", color="blue",linestyle = "--")
#plt.axvline(quantile1sp,label="1 $\sigma$", color="yellow",linestyle = "--")
plt.axvline(quantile2sp,label="2 $\sigma$",color ="black",linestyle = "--")
plt.legend(loc='upper right', fontsize=7)
plt.show()









