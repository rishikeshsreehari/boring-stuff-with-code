# List of Abbreviations from a Document

The code.py reads a doc file and checks for any abbreviations present in the document. The code can be used to create
a list of acronyms from a large document. The output printed is sorted along with the number and any duplicates are ignored. 

The existing code uses a regular expression that looks for capital letters inside parentheses and is defined using the variable abbreviation_pattern.
The regular expression  r'\(([A-Z]+)\)' denotes:

- r' ... ' denotes a raw string literal in Python. This prevents any special characters within the string from being interpreted as escape sequences.
- \( and \) are used to match literal parentheses '(' and ')' respectively. Since parentheses have special meaning in regular expressions (they are used for grouping), we must escape them with a backslash to match them literally.
- [A-Z] represents a character class that matches any uppercase letter from 'A' to 'Z'. This part of the pattern is enclosed within square brackets, indicating that we're looking for a single character from the specified range.
- + means to match one or more occurrences of the preceding character class (uppercase letters). This ensures that we match sequences of consecutive uppercase letters.
- ( ... ) is used to create a capturing group. This means that the part of the text that matches the pattern within the parentheses will be extracted and returned as a match.

Modify accordingly to find other types of text.
