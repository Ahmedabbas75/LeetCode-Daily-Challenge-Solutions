class Solution:
    def findErrorNums(self, nums):
        hashset = set(); soul = []
        size = len(nums); total = 0

        for num in nums:
            if num in hashset:
                soul.append(num)
            else:
                total+= num
                hashset.add(num)

        value = size * (size + 1) // 2
        soul.append(total - value)

        return soul
S = Solution()
print(S.findErrorNums(nums = [1,2,2,4]))
        