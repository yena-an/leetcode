class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_digits = map(str, digits)

        num = int("".join(str_digits))
        num += 1

        return [int(x) for x in str(num)]
        