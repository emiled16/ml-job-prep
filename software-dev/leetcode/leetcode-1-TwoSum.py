from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = dict()

        for index in range(len(nums)):
            if nums[index] in storage:
                return [storage[nums[index]], index]
            else:
                storage[target-nums[index]] = index
                