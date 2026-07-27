class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq1=[0]*26
        for char in s1:
            freq1[ord(char)-ord('a')]+=1
        freq2=[0]*26
        for i in range(len(s1)-1):
            freq2[ord(s2[i])-ord('a')]+=1
        i,j=0,len(s1)-1
        while j<len(s2):
            freq2[ord(s2[j])-ord('a')]+=1
            if freq2==freq1:
                return True
            freq2[ord(s2[i])-ord('a')]-=1
            i+=1
            j+=1
        return False

                
        


        
        