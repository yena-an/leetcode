class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0

        i = 0
        while i < len(s):
            if i < len(s) - 1 and value.get(s[i]) < value.get(s[i+1]):
                result += (value.get(s[i+1]) - value.get(s[i]))
                i += 2
            else:
                result += value.get(s[i])
                i += 1
        
        return result

