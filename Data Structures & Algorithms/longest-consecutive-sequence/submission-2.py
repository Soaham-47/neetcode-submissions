class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        ans=0
        for num in nums:
            temp=1
            k=num-1
            while k in st:
                temp+=1
                k-=1
            ans=max(ans,temp)
        return ans

                



        