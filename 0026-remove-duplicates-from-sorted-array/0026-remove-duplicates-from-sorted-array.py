class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        deleted = []

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                deleted.append(nums[i])
        
        for j in deleted:
            nums.remove(j)

