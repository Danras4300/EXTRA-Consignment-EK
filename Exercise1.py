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