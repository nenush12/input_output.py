# 1. Program that takes name and age
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old.")

# 2. Program that takes two numbers and prints their sum
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}")

# 3. Program that reads a file and counts words
filename = input("Enter filename to count words: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        print(f"Number of words: {len(words)}")
except FileNotFoundError:
    print("File not found!")

# 4. Program that writes sentence to file in reverse
sentence = input("Enter a sentence: ")
reverse_sentence = sentence[::-1]
output_file = input("Enter output filename: ")
with open(output_file, 'w') as file:
    file.write(reverse_sentence)
print(f"Sentence reversed and saved to {output_file}")

# 5. Program that reads CSV and converts to dictionary
import csv
csv_file = input("Enter CSV filename: ")
try:
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
        print("CSV converted to dictionary:")
        for row in data:
            print(dict(row))
except FileNotFoundError:
    print("CSV file not found!")

# 6. Script to monitor log file for keyword
import time
import os

log_file = input("Enter log file to monitor: ")
keyword = input("Enter keyword to alert on: ")

if not os.path.exists(log_file):
    print("Log file not found!")
    exit()

print(f"Monitoring {log_file} for '{keyword}'... Press Ctrl+C to stop")

try:
    # Get initial file size
    file_size = os.path.getsize(log_file)
    
    while True:
        current_size = os.path.getsize(log_file)
        
        if current_size > file_size:
            # File has been modified
            with open(log_file, 'r') as file:
                file.seek(file_size)  # Move to where we left off
                new_content = file.read()
                
                if keyword in new_content:
                    print(f"ALERT: Keyword '{keyword}' found!")
                    print(f"New content: {new_content}")
                
                file_size = current_size
        
        time.sleep(2)  # Check every 2 seconds
        
except KeyboardInterrupt:
    print("\nMonitoring stopped.")


