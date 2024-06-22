# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 10:28:28 2024

@author: Thinkpad
"""

def read_file(file_path):
  
  try:
    # Open the file in read mode
    with open(file_path, 'r') as file:
      # Read all content into a variable
      content = file.read()
      # Print the content
      print(content)
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")


file_path = 'C:/Users/Thinkpad/OneDrive/Desktop/plp-file-read-from.txt'
read_file(file_path)