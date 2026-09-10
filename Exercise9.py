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