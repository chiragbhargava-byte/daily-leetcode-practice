class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        
        # return sorted(s) == sorted(t)


        # using hashMaps

        if len(s) != len(t) :
            return False

        hashS, hashT = {}, {}

        for char in range(len(s)):
            hashS[s[char]] = hashS.get(s[char], 0) + 1
            hashT[t[char]] = hashT.get(t[char], 0) + 1
        
        return hashS == hashT