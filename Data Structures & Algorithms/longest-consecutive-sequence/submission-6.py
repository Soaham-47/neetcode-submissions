class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        st=set(nums)
        ans=1
        for num in nums:
            if num-1 not in st:
                curr=num+1
                temp=1
                while curr in st:
                    curr+=1
                    temp+=1
                ans=max(ans,temp)
        return ans

                



        