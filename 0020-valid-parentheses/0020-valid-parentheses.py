class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {")":"(", "]":"[", "}":"{"}
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack or stack.pop() != pairs[char]:
                    return False
            
        return not stack