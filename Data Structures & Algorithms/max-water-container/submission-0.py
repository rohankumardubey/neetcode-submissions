class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxValue = float("-INF")

        left,right = 0,len(heights)-1

        while left < right:
            area = (right-left) * min(heights[left],heights[right])
            maxValue = max(area,maxValue)

            if heights[left] > heights[right]:
                right -=1
            else:
                left +=1
                
        return maxValue

        