class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        result=[]
        i=0
        while i<n:
            j,k=i+1,n-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total==0:
                    result.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif total>0:
                    k-=1
                else:
                    j+=1
            while i+1<n and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return result 
                


        