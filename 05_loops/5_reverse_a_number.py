# Input a number
num = int(input("Enter a number: "))

reverse_num = 0
temp = num  # original number save

# Use loop to reverse the digits
while temp > 0:
    digit = temp % 10          
    reverse_num = reverse_num * 10 + digit
    temp = temp // 10          

# Print result
print("Reversed number:", reverse_num)
