# Input a number
num = int(input("Enter a number: "))

# Variables for sum and product
sum_digits = 0
product_digits = 1

# Use loop to extract digits (using % and //)
n = num
while n > 0:
    digit = n % 10          # last digit
    sum_digits += digit     # add to sum
    product_digits *= digit # multiply to product
    n //= 10                # remove last digit

# Print both values
print("Sum of digits:", sum_digits)
print("Product of digits:", product_digits)
