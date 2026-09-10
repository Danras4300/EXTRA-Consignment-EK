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