# Define a function called calculate_risk_score
# Parameters: vulnerabilities (int), open_ports (int), failed_logins (int)
# Formula: (vulnerabilities * 10) + (open_ports * 2) + (failed_logins * 5)
# Return: integer risk score
#
# Your program should:
# 1. Define the function with the formula above
# 2. Add type hints for parameters and return value
# 3. Test with: calculate_risk_score(3, 15, 8) # Should return 100
# Bonus: Add default parameter values of 0 for all parameters

def calculate_risk_score(vulnerabilities: int = 0, open_ports: int = 0, failed_logins: int = 0) -> int:
    return (vulnerabilities * 10) + (open_ports * 2) + (failed_logins * 5)

print("Exercise 7: Calculate Risk Score Function")
print(f"Test 1:{calculate_risk_score(3, 15, 8)}")
print(f"Test 1:{calculate_risk_score(3, 15)}")
print(f"Test 1:{calculate_risk_score(5, 7, 8)}")