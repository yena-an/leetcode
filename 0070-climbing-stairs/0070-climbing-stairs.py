class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # def Fibonacci(n):
        #     if n == 0 or n == 1:
        #         return 1
        #     return Fibonacci(n-1) + Fibonacci(n-2)
         
        # return Fibonacci(n)
        a, b = 1, 1

        for num in range(2, n + 1):
            a, b = b, a + b
            
        return b
