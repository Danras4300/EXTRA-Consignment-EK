# Define a function called safe_divide
# Parameters: numerator, denominator
# Return: result of division or None if error occurs
#
# Your program should:
# 1. Use try/except to catch ZeroDivisionError
# 2. If division by zero: print error message, return None
# 3. If successful: return the result
# 4. Use finally to print "Division attempt complete"

def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return("None, divided by zero isn't possible")
    except:
        return("None, Another error happened")

# Test with:
print("Exercise 8: Safe division")

print(safe_divide(10, 2)) # Should return 5.0
print(safe_divide(10, 0)) # Should return None with error message
print(safe_divide(10, "a"))