class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        left = 0
        char = set()

        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left += 1

            char.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length