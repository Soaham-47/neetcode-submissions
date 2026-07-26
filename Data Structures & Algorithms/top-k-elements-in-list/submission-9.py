class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        freq={}
        ans=[]
        counts=[[] for _ in range(n+1)]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for key,value in freq.items():
            counts[value].append(key)
        for i in range(n,-1,-1):
            for num in counts[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans
        return []
                

        