# Input a string
text = input("Enter a string: ")

# Print first character
print("First character:", text[0])

# Print last character
print("Last character:", text[-1])

# Print middle character (use len() to find middle index)
middle_index = len(text) // 2
print("Middle character:", text[middle_index])
