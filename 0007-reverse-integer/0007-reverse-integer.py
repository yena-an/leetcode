class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        
        if x[0] == "-":
            x = "-" + x[1:][::-1]
        else:
            x = x[::-1]
        
        x = int(x)
        
        if x < -2**31 or x > 2**31 - 1:
            return 0
        else:
            return x