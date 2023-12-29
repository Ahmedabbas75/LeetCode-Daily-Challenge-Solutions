class Solution(object):
    def reverse(self, x):

        # check "x" greater than 0 or not
        sign = -1 if x < 0 else 1

        # convert "x" to string and revers digits
        x = str(abs(x))[::-1]

        # create variable final "result"
        result  = int(x) * sign

        # return needed output
        return result if  (2 ** 31) - 1 > result >= (-2 ** 31) else 0
 

        