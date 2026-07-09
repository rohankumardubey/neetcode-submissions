class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup = [0]*26

        for index in s:
            lookup[ord(index) - ord('a')]+=1

        for index in t:
            lookup[ord(index) - ord('a')]-=1

        for index in lookup:
            if index != 0:
                return False

        return True
        