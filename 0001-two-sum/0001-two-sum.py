class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, n in enumerate(nums):
            if target - n in dict:
                return [dict[target-n], i]
            dict[n] = i