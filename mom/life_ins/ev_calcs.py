
import numpy as np
import matplotlib.pyplot as plt

c_age = 68.
life_expectancy = 79.

# payout $4k
p = 4000.

# plan cost is $23 per month
c = 23.
c_per_yr = c*12.


#### Calcs

# yrs till net outcome is 0
end_t = p / c_per_yr

# Make a range
t = np.arange(1.,end_t,0.1)
age = c_age + t

net = p - t*c_per_yr

plt.figure(0)
plt.plot( age, net )
plt.axvline(x=life_expectancy, color='r', linestyle='--')
plt.grid(True)
plt.xlabel('Age (yrs)')
plt.ylabel('Net Payment ($)')
plt.title('Unadjusted Net Payment of Insurance vs Age')
#plt.show()
plt.savefig('unad_payout.png')



# Adjust for inflation effect on payout
inflation = 0.02
real_payout_value = p * np.exp( -inflation * t )

plt.figure(1)
plt.plot( age, real_payout_value )
plt.axvline(x=life_expectancy, color='r', linestyle='--')
plt.grid(True)
plt.xlabel('Age (yrs)')
plt.ylabel('Real Value of Payout')
plt.title('Adjusted Real Value of Payment of Insurance vs Age')
#plt.show()
plt.savefig('ad_payout_value.png')


# Adjust for inflation effect on payout 
real_payout = real_payout_value - t*c_per_yr

plt.figure(2)
plt.plot( age, real_payout )
plt.axvline(x=life_expectancy, color='r', linestyle='--')
plt.grid(True)
plt.xlabel('Age (yrs)')
plt.ylabel('Real Value of Payout')
plt.title('Adjusted Real Value of Payment of Insurance vs Age')
#plt.show()
plt.savefig('real_payout.png')

