# Input a number n
n = int(input("Enter a number: "))

# Sum of natural numbers (1 to n)
natural_sum = 0
for i in range(1, n + 1):
    natural_sum += i

# Sum of odd numbers
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        odd_sum += i

# Sum of even numbers
even_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i

# Print all three sums
print("Sum of natural numbers:", natural_sum)
print("Sum of odd numbers:", odd_sum)
print("Sum of even numbers:", even_sum)
