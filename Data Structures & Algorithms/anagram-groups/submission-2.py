class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[[strs[0]]]
        def isAnagram(a,b):
            return Counter(a)==Counter(b)
        for i in range(1,len(strs)):
            word=strs[i]
            flag=False
            for j in range(len(result)):
                if isAnagram(word,result[j][0]):
                    flag=True
                    result[j].append(word)
                    break
            if not flag:
                result.append([word])
        return result
            


        
        