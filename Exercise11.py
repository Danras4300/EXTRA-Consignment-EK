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

import os

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