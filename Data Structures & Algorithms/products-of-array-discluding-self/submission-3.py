class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[1]*n
        prefix=1
        for i in range(n-1):
            prefix*=nums[i]
            result[i+1]=prefix
        postfix=1
        for i in range(n-1,0,-1):
            postfix*=nums[i]
            result[i-1]=result[i-1]*postfix
        return result






        