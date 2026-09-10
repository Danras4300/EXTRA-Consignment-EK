splitter = "\n------------\n"


# Threat score from monitoring system

# Your program should classify the threat based on score ranges:
# CRITICAL (90+): Immediate action required
# HIGH (70-89): Investigate within 1 hour
# MEDIUM (40-69): Review within 24 hours
# LOW (20-39): Monitor
# INFORMATIONAL (below 20): No action needed
#
# Print the classification level and its action message
# Include the actual score value in your output
# Example: "Score 75: HIGH - Investigate within 1 hour"
def Thread(thread_score):
    if thread_score >= 90:
        print(f"CRITICAL {thread_score}: Immediate action required")
    elif thread_score >= 70:
        print(f"HIGH {thread_score}: Investigate within 1 hour")
    elif thread_score >= 40:
        print(f"MEDIUM {thread_score}: Review within 24 hours")
    elif thread_score >= 20:
        print(f"LOW {thread_score}: Monitor")
    else:
        print(f"INFORMATIONAL {thread_score}: No action needed")

print("Exercise 1: Thread Level Classifier")

Thread(92)
Thread(12)
Thread(54)
Thread(71)

print(splitter)


"""----------------------------"""


# Port number to analyze
# Your program should use match-case to classify:
# 22 → "SSH - Secure Shell"
# 80 → "HTTP - Web Traffic (Unencrypted)"
# 443 → "HTTPS - Secure Web Traffic"
# 3306 → "MySQL - Database"
# 3389 → "RDP - Remote Desktop"
# 53 → "DNS - Domain Name System"
# _ (default) → "Unknown Port"
#
# Print the port number and its classification

def port(port_number):
    match port_number:
        case 22:
            return("SSH - Secure Shell")
        case 80:
            return("HTTP - Web Traffic (Unencrypted)")
        case 443:
            return("HTTPS - Secure Web Traffic")
        case 3306:
            return("MySQL - Database")
        case 3389:
            return("RDP - Remote Desktop")
        case 53:
            return("DNS - Domain Name System")
        case _:
            return("Unknown Port")

print("Exercise 2: Port Classifier")

print(port(443))
print(port(3306))
print(port(346))
print(port(53))

print(splitter)


"""----------------------------"""


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

# while attempts < max_attempts:
#     login = input("Password: ")
#     if login == correct_password:
#         print("Login granted")
#         break
#     else:
#         attempts += 1

print(splitter)


"""----------------------------"""


# Network to scan: 192.168.1.1 to 192.168.1.20
# Your program should:
# 1. Use a for loop with range(1, 21)
# 2. Print "Scanning 192.168.1.X..." for each IP
# 3. For IPs ending in 5, 10, 15: print " → Device found!"
# 4. For IP ending in 13: print " → SUSPICIOUS DEVICE!" and break
# 5. Count total IPs scanned before breaking
def networkscan(network_to_scan: str, range_start: int, range_end: int, device_found: list, suspicious_device: list):
    network_range = range(range_start, range_end)
    # Device_found = [5, 10, 15]
    for scan in network_range:
        print(f"Scanning {network_to_scan}{scan}...")
        if scan in device_found:
            print(f"Device found!")
        elif scan in suspicious_device:
            print(f"SUSPICIOUS DEVICE!\nINVESTIGATE NOW!")
            break
    print(f"{scan} Scans were made")

print("Exercise 4: IP Scanner")
print("\nScan 1")
networkscan("192.168.1.", 1, 21, [5, 10, 15], [13])
print("\nScan 2")
networkscan("192.168.1.", 1, 21, [3, 7, 14, 17], [])

print(splitter)


"""----------------------------"""


security_logs = [
                "User login successful",
                "Test log entry",
                "Failed login attempt from 10.0.0.5",
                "System reboot",
                "Test connection",
                "Malware detected on endpoint",
                "Test data sync",
                "Unauthorized access attempt"
                ]
# Your program should:
# 1. Loop through all log entries
# 2. Use continue to skip any entry containing "Test"
# 3. Print remaining entries with line numbers
# 4. Count how many entries were processed (not skipped)
# 5. Count how many were skipped

def log_filter(log):
    entries_processed = 0
    entries_skipped = 0
    line_number = 0

    for entrie in log:
        line_number += 1
        # Checks if "Test" is in the given entrie, and skips if so
        if "Test" in entrie:
            entries_skipped += 1
            continue
        # Prints the remaining entries with the linenumber
        else:
            print(f"Line {line_number}: {entrie}")
            entries_processed += 1

    print(f"Entries processed: {entries_processed}\nEntries skipped: {entries_skipped}")

print("Exercise 5: Log Filter")
log_filter(security_logs)

print(splitter)


"""----------------------------"""


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

print(splitter)


"""----------------------------"""


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

print(splitter)


"""----------------------------"""


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

print(splitter)


"""----------------------------"""


# First, create a file called "alerts.txt" with these lines:
# Login failed from 192.168.1.50
# Malware detected on workstation-05
# System update completed
# Suspicious outbound traffic detected
# Your program should:
# 1. Use pathlib to get current working directory
# 2. Create filepath using Path.cwd().joinpath("alerts.txt")
# 3. Open file with "with" statement
# 4. Read and print each line
# 5. Count total lines read
# 6. Print lines containing "detected" or "failed“

import os
base_dir = "C:/Users/danie/Desktop/Programmering PBA/EXTRA-Consignment-EK"
filename = "alerts.txt"
full_path = os.path.join(base_dir, filename)

# Works if the terminal is in the correct dir
# with open("alerts.txt") as file:
#     print(file2.read())

print("Exercise 9: Reading Security Alerts from File")

# Works by path making
count = 0
with open(full_path) as file:
    # Reading file, using splitlines to split at linebreaks
    # to make a list instead of one string
    content = file.read().splitlines()


    print("Printing lines with line number:")
    for line in content:
        count += 1
        print(f"{count}: {line}")


    print("\nPrinting lines with detected or failed:")
    for line in content:
        if "failed" in line or "detected" in line:
            print(line)

    #Closing file to free it from memory
    file.close()
print(f"\nlines counted: {count}")

print(splitter)


"""----------------------------"""


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

# import os

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

print(splitter)


"""----------------------------"""


# Part 1: Create helper functions
# Function 1: is_critical_event(event_type) -> bool
# Returns True if event_type is "MALWARE", "BREACH", or "INTRUSION"
#
# Function 2: generate_alert_id() -> str
# Returns a string like "ALT-001", incrementing each call
# Hint: Use a global counter variable
#
# Function 3: process_event(event_type, source_ip, description) -> dict
# Returns a dictionary with keys: alert_id, event_type, source_ip,
# description, is_critical
# Part 2: Process multiple events
# Your program should:
# 1. Loop through events list
# 2. Use process_event() to create alert dictionary for each
# 3. Store all alerts in a list
# 4. Count critical vs non-critical alerts
# 5. Print all critical alerts with their alert_id
# Part 3: Save to file
# Write all critical alerts to "critical_alerts.txt"
# Format: "[ALERT_ID] TYPE from IP: Description“
# import os

events = [
("LOGIN_FAIL", "192.168.1.100", "Failed authentication"),
("MALWARE", "192.168.1.105", "Ransomware detected"),
("UPDATE", "10.0.0.1", "System patch applied"),
("INTRUSION", "203.0.113.5", "Unauthorized access attempt")
]

Alert_count = 0

# Checks if an event is critcal based on what event type it is
def is_critical_event(event_type) -> bool:
    return True if event_type == "MALWARE" or event_type == "BREACH" or event_type == "INTRUSION" else False

# generates a alert id based on the global count of Alert_count and returns it as a string (as determined)
# And in the format ALT-[id]
def generate_alert_id() -> str:
    global Alert_count
    Alert_count += 1
    return(f"ALT-{Alert_count}")

# Returns a dict for each alert
def process_event(event_type, source_ip, description) -> dict:
    return {"alert_id": generate_alert_id(), "event_type": event_type, "source_ip": source_ip, "description": description, "is_critical": is_critical_event(event_type)}

# Alert list resets after every use
Alerts = []

# Takes an alert in the form of a tuble in the events list
# grabs the diffrent information from by indexing and runs the append tool to append a dict to the Alerts list
for event in events:
    event_type, source_ip, description = event[0], event[1], event[2]
    Alerts.append(process_event(event_type, source_ip, description))

# Used for debuging print every dict in Alerts list, one by one
# for x in Alerts:
#     print(x)

# Counts how many critical and non critical alert there is based on the item under "is_critical" key in the alert dict
def count_alerts():
    # Counts
    critical_alerts = 0
    non_critical_alerts = 0
    for alert in Alerts:
        # greps the item under this key
        if alert["is_critical"]:
            critical_alerts += 1
            # Used for debuging prints the alert with items from each alert dict
            # print(f"CRITICAL: ID - {alert["alert_id"]}, {alert["event_type"]}, {alert["source_ip"]}: {alert["description"]}")
        else:
            non_critical_alerts += 1
    # Prints the counts
    print(f"Non Critical alerts: {non_critical_alerts}")
    print(f"Critical Alerts: {critical_alerts}")

# path making for part 3
base_dir = "C:/Users/danie/Desktop/Programmering PBA/EXTRA-Consignment-EK"
filename = "critical_alerts.txt"
full_path = os.path.join(base_dir, filename)    

# opens file in append mode and appends critical alerts in the wished format and closes file at end
def write_critical():
    with open(full_path, 'a') as file:
        for alert in Alerts:
            if alert["is_critical"]:
                file.write(f"{alert["alert_id"]} {alert["event_type"]} from {alert["source_ip"]}: {alert["description"]}\n")
        file.close()

# Reads file for debuging and criteria control
with open(full_path, 'r') as file:
    print(file.read())
    file.close()

# Count
count_alerts()
# Write is only needed the first time and therefore commented out
# write_critical()


print(splitter)


"""----------------------------"""


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

print(splitter)


"""----------------------------"""

# Part 1: Create sample data
# Create "security_report.csv" with these columns:
# timestamp, event_type, severity, source_ip, destination_ip, action_taken
# Sample data (write this to CSV):
# [
# ["2026-03-27 08:15:00", "login_failed", "medium", "192.168.1.50", "10.0.0.1", "blocked"],
# ["2026-03-27 08:20:00", "malware", "critical", "192.168.1.105", "10.0.0.5", "quarantined"],
# ["2026-03-27 08:25:00", "port_scan", "high", "203.0.113.10", "10.0.0.1", "blocked"],
# ["2026-03-27 08:30:00", "login_success", "low", "192.168.1.20", "10.0.0.1", "allowed"],
# ["2026-03-27 08:35:00", "data_exfil", "critical", "192.168.1.105", "8.8.8.8", "blocked"]
# ]

# Part 2: Write CSV file
# Your program should:
# 1. Use csv.writer to create the file
# 2. Write header row
# 3. Write all data rows
# Part 3: Read and analyze CSV
# Your program should:
# 1. Use csv.reader or csv.DictReader to read the file
# 2. Count events by severity (create severity_counts dict)
# 3. Find all unique source IPs that were blocked
# 4. Count total critical events
# 5. Create a list of all malware and data_exfil events
# Part 4: Generate summary report
# Write a new CSV file "summary_report.csv" with:
# severity, count
# Example:
# critical, 2
# high, 1
# medium, 1
# low, 1

import csv
# import os

base_dir = "C:/Users/danie/Desktop/Programmering PBA/EXTRA-Consignment-EK"
filename = "security_report.csv"
full_path = os.path.join(base_dir, filename)

fields = ["Timestamp", "Event_type", "Severity", "Source_ip", "Destination_ip", "Action_taken"]

rows = [
["2026-03-27 08:15:00", "login_failed", "medium", "192.168.1.50", "10.0.0.1", "blocked"],
["2026-03-27 08:20:00", "malware", "critical", "192.168.1.105", "10.0.0.5", "quarantined"],
["2026-03-27 08:25:00", "port_scan", "high", "203.0.113.10", "10.0.0.1", "blocked"],
["2026-03-27 08:30:00", "login_success", "low", "192.168.1.20", "10.0.0.1", "allowed"],
["2026-03-27 08:35:00", "data_exfil", "critical", "192.168.1.105", "8.8.8.8", "blocked"]
]

# with open(full_path, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(fields)
#     csvwriter.writerows(rows)
#     csvfile.close()

fields_file = []
rows_file = []

with open(full_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields_file = next(csvreader)
    for row in csvreader:
        rows_file.append(row)
    csvfile.close()

for row in rows_file:
    if rows == []:
        continue
    else:
        for col in row:
            print(col, end=" ")
        print("\n")

# Dictionary over alle severity counts
severity = {"low": 0, "medium": 0, "high": 0, "critical": 0,}
# List over source ips from threats
source_ips_blocked = []
# list of malware and data exfil events
malware_data_exfil = []


# This checks if a event has blocked in action taken and appends the ip to ips blocked
# malware or data_exfil as event type and appends to malware_data_exfil
for rows in rows_file:
    if rows == []:
        continue
    else:
        severity[rows[2]] += 1
        if rows[5] == "blocked":
            source_ips_blocked.append(rows[3])
        if rows[1] == "malware" or rows[1] == "data_exfil":
            malware_data_exfil.append(rows)

# this removes dublicates from the list
# happens because all keys in a dict must be unique and therefore by making alle list items to keys
# Dublicates will be removed
ips = dict.fromkeys(source_ips)
source_ips = list(ips)
print("ips and severities")
print(source_ips_blocked)
print(severity)

print("\nMalware and data exfil")
for row in malware_data_exfil:
        for col in row:
            print(col, end=" ")
        print("\n")


base_dir = "C:/Users/danie/Desktop/Programmering PBA/EXTRA-Consignment-EK"
filename = "summary_report.csv"
full_path = os.path.join(base_dir, filename)

# Make a with statement to open the new csv file and write a dict
