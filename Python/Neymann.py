import numpy as np
import matplotlib.pyplot as plt

N_meas = 50
N_exp = 100
true_value_l = []
meas_value_l = []

#loop over parameters
for i in range (1,100):
    true_value = float(i)/10.
    for j in range(0,N_exp):
        meas_value = 0.
        for k in range(0,N_meas):

            x = np.random.normal(true_value,0.2)
            meas_value = meas_value + x 

        meas_value = float(meas_value)/float(N_meas)
        meas_value_l.append(float(meas_value))
        true_value_l.append(float(true_value))


#Plotting stuffs
plt.figure()
plt.scatter(true_value_l,meas_value_l)
plt.xlabel('True Value of ' + r'$\mu$'+r'$\rightarrow$')
plt.ylabel('Measured Value of '  + r'$\mu$' + r'$\rightarrow$')
plt.title('Neyman Construction for Normal distribution')
plt.show()
