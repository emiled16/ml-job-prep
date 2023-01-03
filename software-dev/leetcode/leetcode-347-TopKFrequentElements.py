from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storage = dict()

        for number in nums:
            if number not in storage:
                storage[number] = 1
            else:
                storage[number] += 1
        
        result = []
        for i in range(k):
            max_key = max(storage, key=storage.get)
            result.append(max_key)
            storage.pop(max_key)
        return result

