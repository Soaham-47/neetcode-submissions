class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if mp.get(rem,-1)!=-1:
                return [mp[rem],i]
            mp[nums[i]]=i
        return []

        