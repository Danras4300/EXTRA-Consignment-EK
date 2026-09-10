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