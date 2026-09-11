# Data Extraction and Secure Validation Assignment

## What is this project about?

In this project, I used **Python and Regular Expressions (Regex)** to find useful information inside a raw text file. The program extracts four types of information which include: Email addresses, Credit-card numbers, Rwandan phone numbers and Website URLs. It then checks the credit-card numbers and protects them by hiding most of the digits.

## Project Structure

```text
alu-regex-data-extraction_Abigail-Cobbina/
├── input/
│   └── raw-text.txt
├── src/
│   └── main.py
├── output/
│   └── sample-output.json
└── README.md
```

* **input/** contains the raw text that the program reads.
* **src/** contains the Python program.
* **output/** contains the extracted results in JSON format.
* **README.md** explains the project.

## How to Run This

First, you need Python 3 installed.

1. Open the terminal.

2. Go into the `src` folder by typing this in the terminal and pressing the Enter key: 
```bash
cd src
```

3. Run the program using:

```bash
python3 main.py
```

The results are saved in:

```text
../output/sample-output.json
```

## How the Regex Works

The program uses different Regex patterns for each type of data:

* **Email:** accepts official ALU, ALU alumni, and ALU SI email addresses.
* **Credit card:** finds possible card numbers containing 13–19 digits, with optional spaces or hyphens.
* **Phone:** finds Rwandan phone numbers beginning with `+250`.
* **URL:** finds website addresses beginning with `http://` or `https://`.

## Validation and Security

The raw text is treated as **untrusted input** because it could contain incorrect, malformed, or harmful data.

* Invalid formats are ignored instead of being treated as valid data.
* Credit-card numbers are additionally checked using the Luhn algorithm.
* Valid credit-card numbers are masked before being placed in the output so the full payment-card number is not exposed.
* Email addresses are included in the output because email extraction is a required part of the assignment. In a real system, access to extracted email data should be limited to what is necessary.
* The program does not execute code found inside the raw text.
* Regex helps with validation, but **Regex alone is not a complete security system**.

## Example Output

```json
{
    "emails": [
        "ama.cobbina@alueducation.com"
    ],
    "credit_cards": [
        "**** **** **** 1111"
    ],
    "phone_numbers": [
        "+250 123 456 789"
    ],
    "urls": [
        "https://www.alueducation.com"
    ]
}
```

