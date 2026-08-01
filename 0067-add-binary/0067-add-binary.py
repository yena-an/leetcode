class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1 
        carry = 0
        current = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            current = 0
            if i>= 0:
                current += int(a[i])
                i -= 1
            if j >= 0:
                current += int(b[j])
                j -= 1
            current += carry
            carry = current // 2 
            result.append(str(current % 2))
        
        return "".join(reversed(result))


