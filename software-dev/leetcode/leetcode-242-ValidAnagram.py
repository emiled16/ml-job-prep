class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        storage = dict()

        for letter in s:
            if letter not in storage:
                storage[letter] = 1
            else:
                storage[letter]+=1
            
        for letter in t:
            if letter not in storage:
                return False
            else:
                storage[letter]-=1

        for key in storage:
            if storage[key] != 0:
                return False
    
        return True

