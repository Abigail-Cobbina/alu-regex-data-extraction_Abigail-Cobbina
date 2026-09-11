#I imported regex and JSON tools, then read the raw text file into raw_text.
import re
import json

with open("../input/raw-text.txt", "r") as file:
    raw_text = file.read()

#This is used to extract valid ALU emails from raw text which includes official, alumni and SI domains. 
emails = re.findall(
    r'\b[\w.%+-]+@(?:alueducation\.com|alumni\.alueducation\.com|si\.alueducation\.com)\b',
    raw_text
)

#This is used to extract possible 13 to 19 digit credit-card numbers and the Luhn check below validates them.
card_numbers = re.findall(r'\b(?:\d[ -]?){13,19}\b', raw_text)

#I extracted Rwandan phone numbers using the +250 country code, spaces and the required digits.
phone_numbers = re.findall(r'\+250\s\d{3}\s\d{3}\s\d{3}', raw_text)

#This extracts URLs starting with http:// or https://, allowing the "s" to be optional and matching all characters until a space.
urls = re.findall(r'https?://[^\s]+', raw_text)

#This removes spaces and hyphens from a possible card number so that it can be checked as one continuous number.
def clean_card_number(card):
    return card.replace(" ", "").replace("-", "")

#I used the Luhn algorithm to check whether a card number passes the standard checksum used by many payment cards.
def luhn_check(card):
    total = 0
    reverse_digits = card[::-1]

    for i, digit in enumerate(reverse_digits):
        number = int(digit)

        if i % 2 == 1:
            number = number * 2

            if number > 9:
                number = number - 9

        total = total + number

    return total % 10 == 0

#This validates possible card numbers, keeps only those that pass the Luhn check, and masks valid cards before storing them.
def mask_card_number(card):
    return "**** **** **** " + card[-4:]

cleaned_cards = []

for card in card_numbers:
    cleaned = clean_card_number(card)

    if luhn_check(cleaned):
        cleaned_cards.append(mask_card_number(cleaned))
#This stores the extracted information in a structured dictionary, masks card numbers, and saves the results as a JSON file.
output = {
    "emails": emails,
    "credit_cards": cleaned_cards,
    "phone_numbers": phone_numbers,
    "urls": urls
}

with open("../output/sample-output.json", "w") as file:
    json.dump(output, file, indent=4)
