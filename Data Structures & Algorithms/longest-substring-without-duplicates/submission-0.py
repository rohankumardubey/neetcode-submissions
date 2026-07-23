class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using two pointers approach 
        left = 0
        right = 0
        max_length = 0
        lookup = set()

        while right < len(s):
            if s[right] not in lookup:
                lookup.add(s[right])
                max_length = max(max_length,right-left+1)
                right +=1
            else:
                lookup.remove(s[left])
                left +=1
        return max_length
