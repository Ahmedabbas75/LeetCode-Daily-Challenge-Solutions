class Solution:
    def twoSum(self, numbers, target: int):
        hasTable = {}

        for index, value in enumerate(numbers):
            if (target - value) in hasTable:
                return [hasTable[(target - value)] + 1, index + 1]
            
            else:
                hasTable[value] = index















       
        