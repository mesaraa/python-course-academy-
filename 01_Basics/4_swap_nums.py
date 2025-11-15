# Take two numbers as input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# Print before swapping
print("Before swapping: a =", a, ", b =", b)
# Store one value 
temp = a
# Swap the variables
a = b
b = temp
# Print after swapping
print("After swapping: a =", a, ", b =", b)
