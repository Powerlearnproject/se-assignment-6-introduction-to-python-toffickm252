# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 10:39:04 2024

@author: Thinkpad
"""

def write_to_file(file_path, data):
  """
  This function writes a list of strings to a file.
  """
  try:
    # Open the file in write mode
    with open(file_path, 'w') as file:
      # Write each element in the list to the file, followed by a newline
      for item in data:
        file.write(f"{item}\n")
  except (IOError, TypeError) as e:
    print(f"Error writing to file: {e}")

# Sample list of strings to write
data = ["BILIRUBIN LEVEL DETECTION OF NEONATAL JAUNDICE USING COLOR SENSOR IN PHOTOTHERAPY"]

# Replace 'path/to/your/file.txt' with the desired output file path
file_path = 'C:/Users/Thinkpad/OneDrive/Desktop/plp-file-read-from.txt'
write_to_file(file_path, data)

print(f"Successfully wrote data to {file_path}")
print(file_path)