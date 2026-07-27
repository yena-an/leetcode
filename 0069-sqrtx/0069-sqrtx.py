class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        for i in range(50000):
            if i ** 2 > x:
                result = i - 1
                break

        return result