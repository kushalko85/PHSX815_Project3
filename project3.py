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
    trial_b = (250)
    trial_n = (1000)
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
#f = open("biased_dice.txt", "w")
#np.savetxt(f,roll_dist_int)
#f.close()

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

#plot in bar diagram

plt.bar(x_count,y_count)
plt.grid(True)
plt.title('Outcome of the side 6 from ' + str(trial_b) + ' dice in ' + str(trial_n) + ' experiments')
plt.xlabel('Faces')
plt.ylabel('Counts')
plt.savefig("biased_plot.png")
plt.show()





        

#write unfair output of trials in a file 
#g = open("ufair_dice.txt", "w")
#np.savetxt(g,rolls_dist_100)
#g.close()


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
#with open("ufair_dice_counter.txt","w") as ufair_counter_file:
    #w = csv.writer(ufair_counter_file)
    #w.writerow(["line_number", "six_count"])
    #for key, val in ufair_dice_table.items():
        #w.writerow([key, val])
    #ufair_counter_file.close()



#read the saved file
gauss = []
ufair_dice_count_file = open('ufair_dice_counter.txt', 'r')
lines = ufair_dice_count_file.readlines()[1:]
for l in lines:
    gauss.append(int(l.rstrip().split(",")[1]))


# best fit of data
(mu, sigma) = norm.fit(gauss)

# the histogram of the data
n, bins, patches = plt.hist(gauss, 10, density = True, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=2)

#plot
plt.xlabel('No. of outcome 6 in '+ str(trial_b) + ' dice in ' + str(trial_n) + ' experiments' )
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ outcome\ 6:}\ \mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))
plt.grid(True)

plt.show()


# best fit uncertainities and MLE calculation

Nmeas, Nexp = trial_b,trial_n
#sigma = 10.0
mu_bst = []
mu_tru = []

for i in range(0,Nmeas):
    mu_tru_value = float(i)*1.
    p6 = mu_tru_value / Nmeas
    diff = (1-p6)/5.
    p1 = diff
    p2 = diff
    p3 = diff
    p4 = diff
    p5 = diff
    
    for e in range(Nexp):
        #mu_bst_value = 0.0
        sixes = 0
        for m in range(Nmeas):
            listd = [1,2,3,4,5,6]
            x = random.choices(listd, weights =(p1,p2,p3,p4,p5,p6), k =1)
            #print(x)
            if (x==[6]):
                sixes = sixes + 1
        #print(sixes)
        p6s = float(sixes)
                
        mu_bst.append(p6s)
        mu_tru.append(mu_tru_value)
        
        if (abs(p6-prob1) < 0.00000008):
            Slice1.append(p6s)
        if (abs(p6-prob2) < 0.00000008):
            Slice2.append(p6s)

#print(p6s)
                

# Measured & True Parameters for mean in 2D
fig, ax = plt.subplots()
hist_mean = plt.hist2d(mu_tru, mu_bst, bins = 100,norm = LogNorm())   
plt.xlabel(r"$\mu_{T}$")
plt.ylabel(r"$\mu_{M}$")
plt.title(r"2D Histogram of Measured & True $\mu$ ")
plt.grid(color = 'g', alpha = 0.4, linestyle = 'dashed', linewidth = 0.3)
plt.colorbar(hist_mean[3], ax = ax)
plt.show()






#slice fits
(mu1,sigma1) = norm.fit(Slice1)
(mu2,sigma2) = norm.fit(Slice2)
(mu3,sigma3) = norm.fit(Slice3)
weightss = np.ones_like(Slice1) / len(Slice1)
#Slice1 plot
plt.figure()
n1,bins1, patches1 = plt.hist(Slice1,5,weights=weightss, density = True, facecolor='green')
y1 = mlab.normpdf(bins1, mu1, sigma1)
l1 = plt.plot(bins1, y1, "r", linewidth=2)
#plt.show()

left1, right1 = plt.xlim([0,250])
bottom1, top1 = plt.ylim()
plt.text(left1+.05*(right1-left1), .9*top1, "$\\mu$ = %.3f" %(mu1), fontweight="bold")
plt.text(left1+.05*(right1-left1), .85*top1, "$\\sigma$ = %.3f" %(sigma1), fontweight="bold")
plt.title("Neymann Slice for $P_{6}$ = %.2f " %(prob1))
plt.xlabel("Estimated Average")
plt.ylabel("Probability")
plt.show()

### Histogram of $\mu_{measured}$ and Errors ###
data = np.array(mu_bst)
dt, binEdges = np.histogram(data, bins = 50)
bincenters = 0.5*(binEdges[1:] + binEdges[:-1])
Stdevn = np.sqrt(dt)
plt.bar(bincenters, dt, linewidth = 4, color = 'g', alpha = 0.5, yerr = Stdevn)
plt.xlabel(r'$\mu$ values')
plt.ylabel(r"$Frequency$")
plt.title(r'Histogram of measured $\mu_{M}$ and their errors')
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dashed', linewidth = 0.7)
plt.show()


#Histogram for pull
pullofmu = (np.asarray(mu_bst) - np.asarray(mu_tru))/(sigma)
plt.hist(pullofmu, 40, color = 'g', alpha = 0.5,  density = True)

mu0, sigma0 = norm.fit(pullofmu)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu0, sigma0)
widet = sigma0
wideth = round(widet,3)
mu7=round(mu0,3)

plt.text(2, .6, '$\mu$ = ' + str(mu7))
plt.text(2, .4, '$\sigma$ = ' + str(wideth))
plt.plot(x, p, 'k--', linewidth = 1)
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dotted', linewidth = 0.7)
plt.xlabel(r'$\mu$')
plt.ylabel(r"Frequency")
plt.title(r'Histogram for pull on $\mu$ Parameter')
plt.legend()
plt.show()

