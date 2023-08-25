# Random

import random
integer= random.randint(1, 10)
print(integer)

float = random.random()
print(float)

range = random.uniform(2.5, 5.5)
print(range)

fruits = ['apple', 'banana', 'orange']
fruit = random.choice(fruits)
print(fruit)

shuffled= random.sample(fruits, len(fruits))
print(shuffled)

random.shuffle(fruits)
print(fruits)