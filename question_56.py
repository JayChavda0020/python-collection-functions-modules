#  How will you set the starting value in generating random numbers? 

# The seed() method is used to initialize the random number generator.

import random

random.seed(5)
print(random.randint(1,10))

random.seed(5)
print(random.randint(1,10))