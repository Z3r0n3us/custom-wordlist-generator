# Custom Wordlist Generator

## Overview

The **Custom Wordlist Generator** is a Python-based tool designed for penetration testers and security professionals to generate custom wordlists and passwords for use in brute-force attacks. This tool supports various features including leetspeak variations, custom character sets, password patterns, and random password generation.

## Features

- **Wordlist Generation**: Generate wordlists based on provided words and dates.
- **Leetspeak Variations**: Automatically generate leetspeak variations of provided words.
- **Custom Character Sets**: Include custom character sets (e.g., lowercase, uppercase, digits, special characters) in password generation.
- **Password Length Control**: Specify minimum, maximum, or exact lengths for passwords.
- **Password Patterns**: Generate passwords following specific patterns (e.g., start with uppercase, followed by digits).
- **Random Password Generation**: Generate completely random passwords based on the specified character sets and length.


## Docker Installation Option:  
https://github.com/Z3r0n3us/custom-wordlist-generator/blob/main/Docker/README.md

## Regular Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Z3r0n3us/custom-wordlist-generator.git
   cd custom-wordlist-generator
   
2. Set Up the Environment:

It's recommended to use a Python virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

## Usage
### Basic Wordlist Generation

Generate a wordlist from a list of words:
```
python wordlist_generator.py --words admin root password --output my_wordlist.txt
```

### Generate Random Passwords

Generate random passwords with specific character sets and lengths:

```
python wordlist_generator.py --random --charset lower,upper,digits --min-length 10 --max-length 15 --output random_passwords.txt
```

### Generate Wordlist with Leetspeak Variations

Generate a wordlist that includes leetspeak variations of the provided words:
```
python wordlist_generator.py --words password secret --leetspeak --output leetspeak_wordlist.txt
```

### Specify Exact Password Length

Generate passwords with an exact length:
```
python wordlist_generator.py --random --charset lower,upper,digits,special --length 12 --output exact_length_passwords.txt
```

###Using a Password Pattern

Generate passwords following a specific pattern:
```
python wordlist_generator.py --random --pattern "Uld" --output patterned_passwords.txt
```

Example pattern Uld: Uppercase, lowercase, digit.

### Help and Examples
To view all available options and examples, run:
```
python wordlist_generator.py --help
```

### Error Handling and Tips
If you do not provide the required arguments, the script will guide you on what to do:


### If no words or random flag is provided:


Error: You must provide at least one of the following:
  - A list of words with the --words option.
  - Use the --random flag to generate random passwords.
If --min-length is greater than --max-length:


Error: The minimum length cannot be greater than the maximum length.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue.


License
This project is licensed under the MIT License - see the LICENSE file for details.





