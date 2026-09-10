# Define a function called log_incident
# Parameters: incident_type (str), description (str)
#
# Your program should:
# 1. Open "incident_log.txt" in append mode ('a')
# 2. Write incident in format: "[TYPE] Description"
# 3. Add a newline after each entry
# 4. Close file properly (use with statement)
# Test with:
# log_incident("MALWARE", "Trojan detected on endpoint")
# log_incident("ACCESS", "Unauthorized login attempt")
# log_incident("NETWORK", "Port scan detected")
# Then read the file back and print all incidents

import os

base_dir = "C:/Users/danie/Desktop/Programmering PBA/EXTRA-Consignment-EK"
filename = "incident_log.txt"
full_path = os.path.join(base_dir, filename)

# Function takes 2 strings, Opens the file with the given path in append mode 'a' (so its write)
# and writes it with a formated string (made for readability)
# Closed to save and clear it from memory
def log_incident(incident_type: str, description: str):
    with open(full_path, 'a') as file:
        file.write(f"{incident_type}: {description}\n")
        file.close()

    # Reads the file from the path given. Opens it in Read mode 'r' and prints it.
    with open(full_path, 'r') as file:
        print(file.read())
        file.close()

# Test with:
# log_incident("MALWARE", "Trojan detected on endpoint")
# log_incident("ACCESS", "Unauthorized login attempt")
# log_incident("NETWORK", "Port scan detected")

print("Exercise 10: Writeing Incident Log")

with open(full_path, 'r') as file:
        print(file.read())
        file.close()