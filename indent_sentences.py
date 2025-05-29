import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'entropy_text.txt')
output_path = os.path.join(script_dir, 'entropy_text_indented.txt')

# Read the original text
with open(input_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Add a tab after every period that ends a sentence (period followed by space and capital letter)
# This regex finds a period, then a space, then a capital letter, and inserts a tab before the capital letter
indented_text = re.sub(r'\. ([A-Z])', r'.\n\1', text)

# Write the result to a new file (to preserve the original)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(indented_text)

print('Indented text written to entropy_text_indented.txt') 