score = 0

print("Quiz Game Start\n")

# Question 1
print("1. What is the capital of India?")
print("a) Mumbai  b) Delhi  c) Chennai")
ans = input("Enter your answer: ")
if ans == "b":
    score += 1

# Question 2
print("\n2. Which language is used for Python?")
print("a) Programming  b) Snake  c) Animal")
ans = input("Enter your answer: ")
if ans == "a":
    score += 1

# Question 3
print("\n3. What is 5 + 5?")
print("a) 5  b) 10  c) 15")
ans = input("Enter your answer: ")
if ans == "b":
    score += 1

print("\nYour final score is:", score)
