class Solution:
    def lengthOfLIS(self, nums) -> int:
        tempList = [nums[0]]
        
        for num in nums[1:]:
            if num > tempList[-1]:
                tempList.append(num)
            else:
                insert_position  = self.findInsertPosition(list = tempList, target = num)
                tempList[insert_position] = num

        return len(tempList)

    def findInsertPosition(self, list, target):
        left, right = 0, len(list) - 1

        while left < right:
            mid = left + (right - left) // 2

            if list[mid] < target:
                left = mid + 1

            else:
                right = mid

        return left

    
S = Solution()
print(S.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
        