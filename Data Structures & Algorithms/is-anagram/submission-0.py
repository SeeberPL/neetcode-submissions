class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = []
        for i in range(len(s)):
            letters.append(s[i])
        for i in range(len(t)):
            try:
                letters.remove(t[i])
            except:
                pass
        if len(letters) != 0:
            return False
        return True