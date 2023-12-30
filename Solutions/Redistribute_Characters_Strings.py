class Solution:
    def makeEqual(self, words) -> bool:
        # Create an empty dictionary to store character frequencies
        char_frq = {}
        
        # Concatenate all words into a single string
        string_comping = "".join(words)
        
        # Iterate through each character in the concatenated string
        for char in string_comping:
            # Increment the character count in the dictionary
            char_frq[char] = char_frq.get(char, 0) + 1

        # Check each value in the character frequency dictionary
        for value in char_frq.values():
            # If the count of any character is not divisible by the number of words,
            # return False as it's not possible to make all words equal
            if value % len(words) != 0:
                return False
        
        # If all characters' counts are divisible by the number of words,
        # return True as it's possible to make all words equal
        return True
