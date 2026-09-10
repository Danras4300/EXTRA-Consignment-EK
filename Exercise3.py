# Correct password stored in system
correct_password = "Cyber2026!"
attempts = 0
max_attempts = 3
# Your program should:
# 1. Use a while loop to allow up to 3 attempts
# 2. Ask user for password input (use input() function)
# 3. Check if password matches correct_password
# 4. If correct: print "Access granted" and exit loop
# 5. If wrong: increment attempts, show remaining attempts
# 6. If max attempts reached: print "Account locked"

print("Exercise 3: Password Retry System")

while attempts < max_attempts:
    login = input("Password: ")
    if login == correct_password:
        print("Login granted")
        break
    else:
        attempts += 1