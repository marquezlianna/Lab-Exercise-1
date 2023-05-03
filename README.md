# decryption


# Decryption using Python 

This is a simple Python program that decrypts an input string based on certain rules, and then displays the output using Pyfiglet library. The decryption rules are as follows:

- `*` is replaced with `a`
- `&` is replaced with `e`
- `#` is replaced with `i`
- `+` is replaced with `o`
- `!` is replaced with `u`

## Requirements

- Python 3.x
- Pyfiglet library

## Usage

1. Clone or download the project from GitHub
2. Open the terminal or command prompt
3. Navigate to the project directory
4. Run the following command:

```
python decrypt.py
```

5. Enter your input string when prompted
6. The decrypted output will be displayed in the terminal

## Sample Output

```
What is your input string? th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g
                                                  
The Plain Text:  the quick brown fox jumps over the lazy dog.
```

The output is first displayed in ASCII art using the Bubble font from Pyfiglet, and then printed in cyan color using the ANSI escape code `\33[96m`.
