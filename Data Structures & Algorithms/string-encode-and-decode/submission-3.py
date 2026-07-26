class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=[]
        for s in strs:
            ans.append(str(len(s)))
            ans.append('|')
            ans.append(s)
        return ''.join(ans)

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            l=0
            while s[i]!='|':
                l=l*10+int(s[i])
                i+=1
            i+=1
            subS=[]
            while l!=0:
                subS.append(s[i])
                l-=1
                i+=1
            ans.append(''.join(subS))
        return ans

            
            

                
        
