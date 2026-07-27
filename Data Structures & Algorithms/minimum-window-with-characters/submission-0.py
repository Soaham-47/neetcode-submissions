class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        window={}
        formed=0
        ans=(0,10**6)
        i,j=0,0
        while j<len(s):
            char=s[j]
            window[char]=1+window.get(char,0)
            if window[char]==need.get(char,0):
                formed+=1
            if formed==len(need):
                while window[s[i]]!=need.get(s[i],0):
                    window[s[i]]-=1
                    i+=1
                prevL,prevR=ans
                if j-i<prevR-prevL:
                    ans=(i,j)
                window[s[i]]-=1
                i+=1
                formed-=1
            j+=1
        l_idx,r_idx=ans
        if r_idx==10**6:
            return ""
        return s[l_idx:r_idx+1]

            








        
        
        

        