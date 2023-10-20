class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        high = float('-inf')
        sum_val = 0
        for num in nums:
            sum_val += num
            if sum_val > high:
                high = sum_val
            if sum_val < 0:
                sum_val = 0
        return high
        
