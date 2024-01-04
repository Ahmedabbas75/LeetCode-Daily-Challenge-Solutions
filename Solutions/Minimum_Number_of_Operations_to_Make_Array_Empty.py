class Solution:
    def minOperations(self, nums) -> int:

        num_freq = {} 
        operations = 0

        for num in nums:
            if num in num_freq:
                num_freq[num]+=1
            else:
                num_freq[num] = 1

        """
           One way to optimize above code is by using "collections.Counter", 
           which is a built-in Python tool specifically designed for counting frequencies.
           code :
                from collections import Counter
                num_freq = Counter(nums)
        """

        for value in num_freq.values():
            if value == 1: 
                return -1
            
            quotient, remainder = divmod(value, 3)
            if remainder == 0 : 
                operations+= quotient + remainder
            else: 
                operations += quotient + 1

        return operations