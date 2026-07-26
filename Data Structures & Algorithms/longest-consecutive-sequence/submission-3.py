class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        st=set(nums)
        ans=1
        for num in nums:
            temp=1
            k=num-1
            while k in st:
                temp+=1
                k-=1
            ans=max(ans,temp)
        return ans

                



        