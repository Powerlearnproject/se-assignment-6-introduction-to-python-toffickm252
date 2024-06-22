# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:05:48 2024

@author: Thinkpad
"""

# Create a list of numbers
numbers = [12, 59, 39, 62, 87]

# Accessing elements by index
last_number = numbers[-1]  # Accessing the last element (index -1)
print(f"last number: {last_number}")

# Looping through the list
print("Numbers in the list:")
for number in numbers:
  print(number)

# Modifying an element
numbers[0] = 10  # Replacing the first element (index 2) with 10
print("\nList after modification:", numbers)

# Create a dictionary
person = {
  "name": "Lisa",
  "age": 12,
  "city": "Kumasi"
}

# Accessing dictionary values by key
name = person["name"]
print(f"\nPerson's name: {name}")

# Adding a new key-value pair
person["occupation"] = "Student"
print(f"\nDictionary after adding occupation: {person}")

# Checking if a key exists
if "age" in person:
  print("\nThe 'age' key exists in the dictionary.")
