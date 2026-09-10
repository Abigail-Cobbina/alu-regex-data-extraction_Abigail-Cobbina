import re
import json

with open("../input/raw-text.txt", "r") as file:
    raw_text = file.read()

emails = re.findall(
    r'\b[\w.%+-]+@(?:alueducation\.com|alumni\.alueducation\.com|si\.alueducation\.com)\b',
    raw_text
)

card_numbers = re.findall(r'\b(?:\d[ -]?){13,19}\b', raw_text)

phone_numbers = re.findall(r'\+250\s\d{3}\s\d{3}\s\d{3}', raw_text)

urls = re.findall(r'https?://[^\s]+', raw_text)

def clean_card_number(card):
    return card.replace(" ", "").replace("-", "")

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

def mask_card_number(card):
    return "**** **** **** " + card[-4:]

cleaned_cards = []

for card in card_numbers:
    cleaned = clean_card_number(card)

    if luhn_check(cleaned):
        cleaned_cards.append(mask_card_number(cleaned))

output = {
    "emails": emails,
    "credit_cards": cleaned_cards,
    "phone_numbers": phone_numbers,
    "urls": urls
}

with open("../output/sample-output.json", "w") as file:
    json.dump(output, file, indent=4)
