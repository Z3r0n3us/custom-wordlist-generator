import argparse
import random
from itertools import permutations

# Define the character sets
CHAR_SETS = {
    'lower': 'abcdefghijklmnopqrstuvwxyz',
    'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'digits': '0123456789',
    'special': '!@#$%^&*()_+-=[]{}|;:,.<>?/'
}

# Function to parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Generate custom wordlists and passwords for penetration testing.")
    parser.add_argument('-w', '--words', nargs='+', help="List of words to include in the wordlist.")
    parser.add_argument('-d', '--dates', nargs='+', help="List of dates (e.g., birthdays, anniversaries).")
    parser.add_argument('-l', '--leetspeak', action='store_true', help="Apply leetspeak variations.")
    parser.add_argument('-o', '--output', type=str, default='wordlist.txt', help="Output file name.")
    parser.add_argument('-c', '--charset', type=str, default='lower,upper,digits,special',
                        help="Character sets to include (options: lower, upper, digits, special).")
    parser.add_argument('-min', '--min-length', type=int, default=8,
                        help="Minimum length of passwords.")
    parser.add_argument('-max', '--max-length', type=int, default=12,
                        help="Maximum length of passwords.")
    parser.add_argument('-len', '--length', type=int, help="Exact length of the passwords.")
    parser.add_argument('-p', '--pattern', type=str, help="Pattern for generating passwords (e.g., 'Uld' for Upper, lower, digit).")
    parser.add_argument('-r', '--random', action='store_true', help="Generate random passwords.")
    return parser.parse_args()

# Function to generate leetspeak variations
def generate_leetspeak(word):
    leet_dict = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}
    return ''.join(leet_dict.get(c, c) for c in word.lower())

# Function to generate wordlist based on words and leetspeak option
def generate_wordlist(words, leetspeak=False):
    wordlist = set()
    for word in words:
        wordlist.add(word)
        if leetspeak:
            wordlist.add(generate_leetspeak(word))
    # Add permutations
    for p in permutations(words, 2):
        wordlist.add(''.join(p))
    return wordlist

# Function to apply pattern to generated password
def apply_pattern(password, pattern):
    pattern_dict = {'U': 'upper', 'l': 'lower', 'd': 'digits', 's': 'special'}
    new_password = []
    for p in pattern:
        new_password.append(random.choice(CHAR_SETS[pattern_dict[p]]))
    return ''.join(new_password) + password[len(pattern):]

# Function to generate passwords based on charset, length, and pattern
def generate_passwords(charset, min_length, max_length, exact_length=None, pattern=None, randomize=False):
    available_chars = ''.join(CHAR_SETS[c] for c in charset.split(','))
    passwords = set()
    
    if exact_length:
        min_length = max_length = exact_length
    
    if randomize:
        for _ in range(100):  # Generate 100 random passwords
            length = random.randint(min_length, max_length)
            passwords.add(''.join(random.choice(available_chars) for _ in range(length)))
    else:
        for length in range(min_length, max_length + 1):
            password = ''.join(random.choices(available_chars, k=length))
            if pattern:
                password = apply_pattern(password, pattern)
            passwords.add(password)
    
    return passwords

# Function to write the wordlist to a file
def write_wordlist_to_file(wordlist, output_file):
    with open(output_file, 'w') as f:
        for word in sorted(wordlist):
            f.write(f"{word}\n")

# Main function to handle input arguments and generate the wordlist/passwords
if __name__ == "__main__":
    args = parse_args()
    
    # Validate input arguments and provide hints if necessary
    if not args.words and not args.random:
        print("Error: You must provide at least one of the following:")
        print("  - A list of words with the --words option.")
        print("  - Use the --random flag to generate random passwords.")
        print("\nExamples:")
        print("  python wordlist_generator.py --words admin root password")
        print("  python wordlist_generator.py --random")
        exit(1)
    
    if args.min_length > args.max_length:
        print("Error: The minimum length cannot be greater than the maximum length.")
        print("Please check your --min-length and --max-length options.")
        exit(1)
    
    wordlist = set()
    
    if args.words:
        wordlist = generate_wordlist(args.words, leetspeak=args.leetspeak)
    
    if args.random:
        password_list = generate_passwords(args.charset, args.min_length, args.max_length, exact_length=args.length, pattern=args.pattern, randomize=True)
        wordlist.update(password_list)
    
    if wordlist:
        write_wordlist_to_file(wordlist, args.output)
        print(f"Wordlist saved to {args.output}")
    else:
        print("No words or passwords generated. Please provide words with --words or use the --random option.")
