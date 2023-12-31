class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        maxLengh = -1

        for index, value in enumerate(s):
            if value in seen:
                maxLengh = max((index - seen[value]) - 1, maxLengh)

            else:
                seen[value] = index

        return maxLengh

