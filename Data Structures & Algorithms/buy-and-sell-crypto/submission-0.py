class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        i,j=0,1
        ans=0
        while j<n:
            if prices[i]>=prices[j]:
                i=j
            else:
                profit=prices[j]-prices[i]
                ans=max(ans,profit)
            j+=1
        return ans



            




        