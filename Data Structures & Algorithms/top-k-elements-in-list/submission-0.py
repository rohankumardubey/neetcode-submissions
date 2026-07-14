import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        max_heap = []
        result = []

        for num in nums:
            if num in lookup:
                lookup[num] +=1
            else:
                lookup[num] = 1
        
        for sets in lookup.items():
            heapq.heappush(max_heap,[-sets[1],-sets[0]])

        for index in range(0,k):
            result.append(-heapq.heappop(max_heap)[1])

        return result