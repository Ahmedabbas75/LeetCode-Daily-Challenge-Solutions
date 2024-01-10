class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowel = {'a', 'e', 'i', 'o', 'u'}
        count, temp, left = 0, 0, 0

        for right in range(len(s)):

            if s[right] in vowel :
                temp+= 1 

            if (right - left + 1) > k:
                temp-= 1 if s[left] in vowel else 0
                left+=1

            count = max(count, temp)
        
        return count
             