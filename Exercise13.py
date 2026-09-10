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

import os
import csv

# Path for security report file
base_dir = "C:/Users/danie/Desktop/Programmering PBA/EXTRA-Consignment-EK"
filename = "security_report.csv"
full_path = os.path.join(base_dir, filename)

# Information to write to the first csv file
fields = ["Timestamp", "Event_type", "Severity", "Source_ip", "Destination_ip", "Action_taken"]

rows = [
["2026-03-27 08:15:00", "login_failed", "medium", "192.168.1.50", "10.0.0.1", "blocked"],
["2026-03-27 08:20:00", "malware", "critical", "192.168.1.105", "10.0.0.5", "quarantined"],
["2026-03-27 08:25:00", "port_scan", "high", "203.0.113.10", "10.0.0.1", "blocked"],
["2026-03-27 08:30:00", "login_success", "low", "192.168.1.20", "10.0.0.1", "allowed"],
["2026-03-27 08:35:00", "data_exfil", "critical", "192.168.1.105", "8.8.8.8", "blocked"]
]

""" This is commented out to not repeat the same line in the CSV file"""
# with open(full_path, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(fields)
#     csvwriter.writerows(rows)
#     csvfile.close()

# Lists made to append lists with data from csv files in the read system below
fields_file = []
rows_file = []

# Reads the csv file by using the csv library
with open(full_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields_file = next(csvreader)
    for row in csvreader:
        rows_file.append(row)
    csvfile.close()

# Prints each row from the csv file
for row in rows_file:
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
ips = dict.fromkeys(source_ips_blocked)
source_ips = list(ips)
print("ips and severities")
print(source_ips_blocked)
print(severity)

# This prints files that are event type malware or data exfil
print("\nMalware and data exfil")
for row in malware_data_exfil:
        for col in row:
            print(col, end=" ")
        print("\n")

# Path for new csv summary file
base_dir = "C:/Users/danie/Desktop/Programmering PBA/EXTRA-Consignment-EK"
filename = "summary_report.csv"
full_path = os.path.join(base_dir, filename)

# lists made for part 4, to write in a new csv file
fields = ["severity", "count"]
severity_for_csv = []

# This takes the severity count dictionary and makes it into a list formated as: [severity, count]
# And imbeds the list in the list severity_for_csv, so it's in a format that can be used as rows in csv
for sev in severity:
    temp_list = []
    temp_list.append(sev)
    temp_list.append(severity[sev])
    severity_for_csv.append(temp_list)

# Writes to a new csv file called summary_report

# with open(full_path, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(fields)
#     csvwriter.writerows(severity_for_csv)
#     csvfile.close()