class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vowels = {'a', 'e', 'i', 'o', 'u'}
        count, length = 0, len(s)
        for index, value in enumerate(s.lower()):
            if index >= length // 2 and value in vowels:
                count+= 1
            
            if index < length // 2 and value in vowels:
                count-= 1
                
        return bool(count)
                
S = Solution()
print(S.halvesAreAlike(s = "book"))         
               