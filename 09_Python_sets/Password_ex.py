password = input("Enter your password: ")

letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
digits = set("0123456789")
special = set("!@#$%^&*()-_=+[]{}/?|><.,;:'`~")
space = set(" ")

# Convert password into a set of characters
pwd_set = set(password)

# Check the password contents using set operations
has_letters = len(pwd_set & letters) > 0
has_digits = len(pwd_set & digits) > 0
has_special = len(pwd_set & special) > 0
has_space = len(pwd_set & space) > 0

print("\nPassword Analysis Report:")
print("-------------------------")

if has_letters:
    print("✔ Contains Letters")
else:
    print("✘ No Letters Found")

if has_digits:
    print("✔ Contains Numbers")
else:
    print("✘ No Numbers Found")

if has_special:
    print("✔ Contains Special Characters")
else:
    print("✘ No Special Characters Found")

if has_space:
    print("✘ Password contains spaces (not recommended)")
else:
    print("✔ No Spaces Found")

# Strength Evaluation
if has_letters and has_digits and has_special and not has_space and len(password) >= 8:
    print("\nStrength: 🟢 Strong Password 💪")
elif has_letters and has_digits:
    print("\nStrength: 🟡 Moderate Password 🙂")
else:
    print("\nStrength: 🔴 Weak Password 😟")
 