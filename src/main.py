import re

with open("../input/raw-text.txt", "r") as file:
    raw_text = file.read()

print(raw_text)

emails = re.findall(
    r'\b[\w.%+-]+@(?:alueducation\.com|alumni\.alueducation\.com|si\.alueducation\.com)\b',
    raw_text
)
print(emails)

card_numbers = re.findall(r'\b(?:\d[ -]?){13,19}\b', raw_text)

print(card_numbers)

phone_numbers = re.findall(r'\+250\s\d{3}\s\d{3}\s\d{3}', raw_text)

print(phone_numbers)

urls = re.findall(r'https?://[^\s]+', raw_text)

print(urls)
