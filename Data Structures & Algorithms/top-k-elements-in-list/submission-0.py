class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countS={}
        res=[]
        for num in nums:
            countS[num]=countS.get(num,0)+1

        for _ in range(k):
            max_key=None
            max_value=float('-inf')
            for key in countS:
                if countS[key]>max_value:
                    max_value=countS[key]
                    max_key=key
            res.append(max_key) 
            del countS[max_key]   
        return res 