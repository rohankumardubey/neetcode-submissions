class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        nums.sort()

        longest = 1
        current_longest = 1

        for index in range(1,len(nums)):
            if nums[index] == nums[index-1]:
                continue
            
            if nums[index] == nums[index-1]+1:
                current_longest +=1
            else:
                current_longest = 1
            
            longest = max(longest,current_longest)
        
        return longest




