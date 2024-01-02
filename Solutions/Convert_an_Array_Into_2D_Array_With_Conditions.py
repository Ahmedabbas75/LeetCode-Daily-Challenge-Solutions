class Solution:
    def findMatrix(self, nums):
        num_frq = {}; array = []

        for num in nums :
            if num in num_frq:
                num_frq[num] +=1
            else:
                num_frq[num] = 1

        while max(num_frq.values()) > 0:
            temp_arr = []

            for key, value in num_frq.items():
                if value :
                    temp_arr.append(key)
                    num_frq[key]-=1

            array.append(temp_arr)
            
        return array
 
        