class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        prev={}
        if len(s)!=len(t):
            return False
        for ch in s:
            prev[ch]=prev.get(ch,0)+1
        for ch in t :
            if ch not in prev or prev[ch]==0:
                return False
            prev[ch]-=1
        return True


        