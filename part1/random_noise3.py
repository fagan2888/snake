from random import normalvariate, uniform
import matplotlib.pyplot as plt

def generate_data(n, generator_type):
    ''' (number, random) -> array
    
    Returns an array of n-many epsilon values taken from
    the distribution specified by generator type.
    '''
    
    epsilon_values = []
    for i in range(n):
        e = uniform(0, 1) if generator_type == 'U' else normalvariate(0, 1)
        epsilon_values.append(e)
    return epsilon_values

data = generate_data(100, 'U')
plt.plot(data, 'b-')
plt.show()
