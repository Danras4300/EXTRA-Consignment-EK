# Define a function called check_security_config
# Parameters: firewall_enabled (bool), antivirus_updated (bool), encryption_on (bool)
# Return: True if ALL three are True, False otherwise
#
# Your function should:
# 1. Take three boolean parameters
# 2. Return True only if all three are enabled
# 3. Print a warning message if any check fails

def check_security_config(firewall_enabled, antivirus_updated, encryption_on):
    return True if firewall_enabled and antivirus_updated and encryption_on else False




# Test your function with:
print("Exercise 6: Log Filter")
if check_security_config(True, True, True): # Should return True
    print(f"Test 1: Succes")
else:
    print(f"Test 1: Failed")

if not check_security_config(True, False, True): # Should return False
    print(f"Test 2: Succes")
else:
    print(f"Test 1: Failed")

if not check_security_config(False, False, False): # Should return False
    print(f"Test 1: Succes")
else:
    print(f"Test 1: Failed")  