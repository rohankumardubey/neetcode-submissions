class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for index,num in enumerate(nums):
            difference = target - num
            if difference in lookup:
                return [lookup[difference],index]
            
            lookup[num] = index

        return None 