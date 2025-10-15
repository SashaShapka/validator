# Identity Validator

This project provides a flexible validation framework for checking whether a given input is a valid **phone number** or **email address**. It supports strategy-based validation using both external libraries and regular expressions.

## Features

- Validates Ukrainian and Russian phone numbers.
- Validates email addresses using both syntax and deliverability checks.
- Pluggable strategy pattern for different validation logics.
- CLI interface using `argparse`.

## Installation

```bash
pip install -r requirements.txt
Usage

Run from terminal:

python main.py -v "+380501234567" -t phone
python main.py -v "example@gmail.com" -t mail
```
## Requirements
- phonenumbers
- email-validator