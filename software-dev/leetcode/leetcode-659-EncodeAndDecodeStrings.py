class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, s):
        # write your code here
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
