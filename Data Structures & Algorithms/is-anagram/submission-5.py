class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        seen={}
        for word in list(s):
            if word not in seen:
                seen[word]=1
            else:seen[word]+=1
        
        for i in list(t):
            if i not in seen or seen[i]==0:
                return False
            else:
                seen[i]-=1
        return True