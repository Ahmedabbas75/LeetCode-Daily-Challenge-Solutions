class Solution:
    def groupAnagrams(self, strs):
        anagram = {}

        for word in strs:

            temp_word = ''.join(sorted(word))

            if temp_word in anagram:
                anagram[temp_word].append(word)

            else:
                anagram[temp_word] = [word]  

        return list(anagram.values())      

   