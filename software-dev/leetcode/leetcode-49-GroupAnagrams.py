from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = dict()
        for string in strs:
            key = self.getkey(string)
            if key in storage:
                storage[key].append(string)
            else: 
                storage[key] = [string]

        result = []
        for key in storage:
            result.append(storage[key])
        return result

    
    def isAnagram(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        return self.getkey(word1) == self.getkey(word2)


    @staticmethod
    def getkey(word: str) -> str:
        word = list(word.lower())
        word.sort()
        return "".join(word)
