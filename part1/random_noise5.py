from random import normalvariate, uniform
import matplotlib.pyplot as plt

def generate_data(n, generator_type):
    ''' (number, random) -> array
    
    Returns an array of n-many epsilon values taken from
    the distribution specified by generator type.
    
    This is the most simplified version of random noise.
    We use list comprehension to generate the list of random draws.
    '''
    
    epsilon_values = [generator_type(0, 1) for i in range(n)]
    return epsilon_values

data = generate_data(100, uniform)
plt.plot(data, 'b-')
plt.show()
