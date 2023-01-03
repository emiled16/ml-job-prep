from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        suffixes = []
        for i, number in enumerate(nums):
            prefixes.append(number if i == 0 else number*prefixes[i-1])
        nums.reverse()
        for i, number in enumerate(nums):
            suffixes.append(number if i == 0 else number*suffixes[i-1])
        suffixes.reverse()

        result = []
 
        for index in range(len(nums)):
            if index == 0:
                result.append(suffixes[index+1])
            elif index == len(nums)-1:
                result.append(prefixes[index-1])
            else:
                number = prefixes[index-1] * suffixes[index+1]
                result.append(number)

        return result
