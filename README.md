# PHSX815_Project3

## This is my repository for Project3

p3.py will simulate the dice rolls, fit and save the output in .txt file.
project3.py will read the .txt files, fit and estimate the MLE parameter \mu and then generates different plots to visualize the uncertainty of our estimation.

## Example usage
 First run `python3 P3.py -p6 0.3 -trial_b 250  -trial_n 10 -prob1 0.7` 
 Then run `python3 project3.py -p6 0.3 -trial_b 250  -trial_n 10 -prob1 0.7` Please use same parameters otherwise project3.py will return to default values. 

-p6 corresponds to the weight of the outcome 6 for the dice simulation. <br>
-trial_b corresponds to the number of dice rolls to be performed in each trial/experiment .  <br>
-trial_n corresponds to the number of experiment for the given number of dice rolls specified by -trial_b .  <br>
-prob1 corresponds to the weight of the outcome 6 for which we want to take the slice from the Neyman construct.  <br>


  
