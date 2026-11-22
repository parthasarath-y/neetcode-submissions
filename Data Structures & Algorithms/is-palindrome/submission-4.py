import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean= re.sub("\W","",s.lower())
        return clean == clean[::-1]