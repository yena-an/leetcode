class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        length = len(columnTitle)
        result = 0

        for i, char in enumerate(columnTitle):
            result += (ord(char) - 64) * 26 ** (length - 1 - i)

        return result
        