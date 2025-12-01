import random
 
# Empty list
numbers = []
 
# Generate 5 random integers between 1 and 50
for i in range(5):
    num = random.choice(range(1, 51))  # pick any number from 1 to 50
    numbers.append(num)
 
print("Random Numbers:", numbers)
 
 
 