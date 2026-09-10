# Part 1: Create threat data
# Create a file "threat_intel.json" with this structure: DONE

# Part 2: Read and analyze
# Your program should:
# 1. Read the JSON file
# 2. Count total threats
# 3. Count threats by severity level (create a dictionary)
# 4. Find all unique source IPs (use a set)
# 5. Print all "high" or "critical" threats with their IDs
# Part 3: Add new threat
# Create a new threat dictionary:
new_threat = {
"threat_id": "THR-004",
"type": "ransomware",
"severity": "critical",
"indicators": ["encrypt.exe", "ransom.note"],
"source_ips": ["10.0.0.50"]
}

# Add it to the threats list and write back to JSON file
# Use indent=2 for readable formatting
import json
import os

base_dir = "C:/Users/danie/Desktop/Programmering PBA/EXTRA-Consignment-EK"
filename = "threat_intel.json"
full_path = os.path.join(base_dir, filename) 

# Reads json file and saves it as json_data
with open(full_path) as file:
    json_data = file.read()
    file.close()

# Count for all threats
threat_count = 0
# Dictionary over alle severity counts
severity = {"low": 0, "medium": 0, "high": 0, "critical": 0,}
# List over source ips from threats
source_ips = []


python_data = json.loads(json_data)
for event in python_data["threats"]:
    threat_count += 1
    # Adds one to the severity count for the given severity
    severity[event['severity']] += 1
    source_ips.extend(event['source_ips'])

    if event['severity'] == 'high' or event['severity'] == 'critical':
        print("threat")
        print(f"{event['threat_id']} {event['type']} from {event['source_ips']} - Severity: {event['severity']}")


# this removes dublicates from the list
# happens because all keys in a dict must be unique and therefore by making alle list items to keys
# Dublicates will be removed
ips = dict.fromkeys(source_ips)
source_ips = list(ips)
print("ips and severities")
print(source_ips)
print(severity)

# Since python_data["threats"] is a list we can append the new threat (dictionary)
# Then convert the python data back to json and overwrite the file with the new data
# The overwriting is commented out to not repeat the same
# python_data["threats"].append(new_threat)
# json_data = json.dumps(python_data, indent=2)
# with open(full_path, 'w') as file:
#     file.write(json_data)
#     file.close()

with open(full_path, 'r') as file:
    print(file.read())
    file.close()