class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for key, value in counts.items():
            if value > len(nums) // 2:
                return key