class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_frequency = 0
        result = 0
        lookup = {}

        for right in range(len(s)):
            # add the frequency lookup i.e. character frequency
            lookup[s[right]] = lookup.get(s[right],0)+1
            max_frequency = max(max_frequency,lookup[s[right]])

            # when the difference of window size and max frequency greater than
            # the target output then the window length must be reduced 
            while (right-left+1) - max_frequency > k:
                lookup[s[left]] -=1
                left +=1
            result = max(result,(right-left+1))
        return result


        