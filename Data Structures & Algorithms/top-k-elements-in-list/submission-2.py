class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        heap=[(-value,key) for key,value in freq.items()]
        heapq.heapify(heap)
        ans=[]
        while k!=0:
            x,y=heapq.heappop(heap)
            ans.append(y)
            k-=1
        return ans

        