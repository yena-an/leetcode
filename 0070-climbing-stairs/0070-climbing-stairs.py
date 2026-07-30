class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        result = 1

        for _ in range(n):
            i = result
            result = start + i
            start = i
        
        return result