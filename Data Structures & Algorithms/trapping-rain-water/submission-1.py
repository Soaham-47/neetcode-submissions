class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxL=[0]*n
        maxR=[0]*n
        maxi=-1
        for i in range(1,n):
            if height[i-1]>maxi:
                maxi=height[i-1]
            maxL[i]=maxi
        maxi=-1
        for i in range(n-2,-1,-1):
            if height[i+1]>maxi:
                maxi=height[i+1]
            maxR[i]=maxi
        ans=0
        for i in range(n):
            amount=min(maxL[i],maxR[i])-height[i]
            if amount>0:
                ans+=amount
        return ans




        