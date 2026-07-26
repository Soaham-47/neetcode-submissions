class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0
        n=len(heights)
        i,j=0,n-1
        while i<j:
            area=(j-i)*min(heights[i],heights[j])
            ans=max(ans,area)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return ans
        