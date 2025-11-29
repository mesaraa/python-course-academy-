# Input principal, rate, and time
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time in Years: "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Print the interest
print("Simple Interest is:", simple_interest)