from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        num_set = set(nums)
        max_length = -1
        for number in nums:
            if number-1 not in num_set:
                length = 1
                while number + length in num_set:
                    length+=1
                max_length = max(max_length, length)
        return max_length

