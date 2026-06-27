class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        result = ""
        first = strs[0]

        for i in range(len(first)):
            curr = first[i]

            for j in strs:
                if i > len(j) - 1 or curr != j[i]:
                    return result
            
            result += curr

        return result 