# Input values
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()
verification = input("Is your account verified? (yes/no): ").strip().lower()

# 1. Empty Field Check
if username == "" or password == "":
    print("Error: Username and password cannot be empty!")

# 2. Password Length Check
elif len(password) < 8:
    print("Error: Password must be at least 8 characters long!")

# 3. Admin Access (verified)
elif username == "admin" and password == "admin123" and verification == "yes":
    print("Welcome, Admin! Full access granted.")

# 4. Admin but NOT verified
elif username == "admin" and password == "admin123" and verification == "no":
    print("Login successful, but please verify your account.")

# 5. Regular User Access
elif username == "user" and password == "password123" and verification == "yes":
    print("Welcome, User! Access granted.")

# 6. Invalid Credentials
else:
    print("Invalid credentials. Access denied.")
