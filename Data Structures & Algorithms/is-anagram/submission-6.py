class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        s_dict=defaultdict(int)
        t_dict=defaultdict(int)

        for word in s:
            s_dict[word]+=1
        for word in t:
            t_dict[word]+=1
        return t_dict==s_dict