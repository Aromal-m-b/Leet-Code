from string import ascii_lowercase, ascii_uppercase

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_occurrence = {}
        last_occurrence = {}
        for index, char in enumerate(word):
            if char not in first_occurrence:
                first_occurrence[char] = index
            last_occurrence[char] = index
        special_char_count = sum(
            lowercase_char in last_occurrence 
            and uppercase_char in first_occurrence 
            and last_occurrence[lowercase_char] < first_occurrence[uppercase_char]
            for lowercase_char, uppercase_char in zip(ascii_lowercase, ascii_uppercase)
        )
      
        return special_char_count