import re

# Sample text
text = """
1. abc123
2. 456xyz 
3. a_b c!
4. 789abcxyz 
5. abc xyz 
6. no_digits_here
"""

# Digits and Non-Digits
digits_pattern = r'\d'
non_digits_pattern = r'\D'

# Word and Non-Word Characters
word_characters_pattern = r'\w'
non_word_characters_pattern = r'\W'

# Whitespace and Non-Whitespace Characters
whitespace_characters_pattern = r'\s'
non_whitespace_characters_pattern = r'\S'

# String Start and End
start_with_abc_pattern = r'\babc\w*'
end_with_xyz_pattern = r'xyz\s*$'

# Finding all matches
digits_matches = re.findall(digits_pattern, text)
non_digits_matches = re.findall(non_digits_pattern, text)
word_characters_matches = re.findall(word_characters_pattern, text)
non_word_characters_matches = re.findall(non_word_characters_pattern, text)
whitespace_characters_matches = re.findall(whitespace_characters_pattern, text)
non_whitespace_characters_matches = re.findall(non_whitespace_characters_pattern, text)

lines = text.strip().split('\n')
start_with_abc_matches = [line for line in lines if re.findall(start_with_abc_pattern, line)]
end_with_xyz_matches = [line for line in lines if re.findall(end_with_xyz_pattern, line)]


# Output results
print("Digits:", digits_matches)
print("Non-Digits:", non_digits_matches)
print("Word Characters:", word_characters_matches)
print("Non-Word Characters:", non_word_characters_matches)
print("Whitespace Characters:", whitespace_characters_matches)
print("Non-Whitespace Characters:", non_whitespace_characters_matches)
print("Lines starting with 'abc':", start_with_abc_matches)
print("Lines ending with 'xyz':", end_with_xyz_matches)