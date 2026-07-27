class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp={}
        ans=0
        i,j=0,0
        while j<len(s):
            if mp.get(s[j],0)>0:
                while i<j and s[i]!=s[j]:
                    mp[s[i]]-=1
                    i+=1
                mp[s[i]]-=1
                i+=1
            else:
                ans=max(ans,j-i+1)
            mp[s[j]]=1
            j+=1
        return ans

        

        