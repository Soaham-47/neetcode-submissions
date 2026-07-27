class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        freq={}
        l,r=0,0
        ans=0
        while r<n:
            freq[s[r]]=freq.get(s[r],0)+1
            while (r-l+1)-max(freq.values())>k:
                freq[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans
            
            
            




        

        