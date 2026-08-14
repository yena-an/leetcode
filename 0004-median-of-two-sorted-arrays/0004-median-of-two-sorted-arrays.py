class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        mid = (len(nums1) + len(nums2)) // 2 

        if (len(nums1) + len(nums2)) % 2 == 0:
            return (nums[mid] + nums[mid-1]) / 2.0
        elif (len(nums1) + len(nums2)) % 2 == 1:
            return nums[mid] 