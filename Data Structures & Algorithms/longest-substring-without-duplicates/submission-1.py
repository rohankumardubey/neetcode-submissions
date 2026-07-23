class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using the sliding window 
        left = 0
        max_length = 0

        lookup = set()

        for right in range(len(s)):
            # duplicate occured condition
            while s[right] in lookup:
                lookup.remove(s[left])
                left +=1

            # non duplicate track
            lookup.add(s[right])
            max_length = max(max_length,right-left+1)
        
        return max_length