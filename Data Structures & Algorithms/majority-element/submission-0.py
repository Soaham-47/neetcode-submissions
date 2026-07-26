class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countS={}
        for num in nums:
            countS[num]=countS.get(num,0)+1
        
        for k in countS:
            if countS[k]>len(nums)/2:
                return k
        return 0

    
        