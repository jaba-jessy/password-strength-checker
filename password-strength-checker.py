import re

print("===== PASSWORD STRENGTH CHECKER =====")

password = input("Enter your password: ")

strength = 0

if len(password) >= 8:
    strength += 1

if re.search(r"[A-Z]", password):
    strength += 1

if re.search(r"[a-z]", password):
    strength += 1

if re.search(r"[0-9]", password):
    strength += 1

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1

print("\nPassword Analysis")
print("----------------------")

if strength <= 2:
    print("Password Strength: WEAK")
elif strength <= 4:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: STRONG")
