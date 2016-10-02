from random import normalvariate
import matplotlib.pyplot as plt

def generate_data(n):
    ''' (number) -> array
#     
    Returns an array of n-many epsilon values taken from
    the standard normal distribution.    
    '''
    
    epsilon_values = []
    for i in range(n):
        e = normalvariate(0, 1)
        epsilon_values.append(e)
    return epsilon_values

data = generate_data(100)
plt.plot(data, 'b-')
plt.show()