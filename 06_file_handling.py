# file_handling.py

import os

# 1. Write to a file
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python!\n")
    file.write("Learning File Handling.")

print("File written successfully.")


# 2. Read a file
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("\nFile content:")
print(content)


# 3. Append new content
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("\nNew line added.")

print("\nAfter append:")

with open("data.txt", "r", encoding="utf-8") as file:
    print(file.read())


# 4. Read line by line
print("\nLine by line:")

with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


# 5. Check if file exists
if os.path.exists("data.txt"):
    print("\nFile exists!")
else:
    print("\nFile does not exist.")


# 6. File information
if os.path.exists("data.txt"):
    size = os.path.getsize("data.txt")
    print("File size:", size, "bytes")


# 7. Handle missing file
try:
    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("\nError: File not found!")


# 8. JSON file handling
import json

user = {
    "name": "Rohan",
    "age": 24,
    "skills": ["Python", "JavaScript", "React"]
}

# Save dictionary as JSON
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent=4)

print("\nJSON saved.")


# Read JSON back into Python
with open("user.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("JSON data:")
print(data)
print("Name:", data["name"])
print("Skills:", data["skills"])