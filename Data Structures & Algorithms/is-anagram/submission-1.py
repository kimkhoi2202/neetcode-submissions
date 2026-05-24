class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_array = list(s)
        for i in t:
            if i in s_array:
                s_array.remove(i)
            else:
                return False
        if s_array:
            return False
        return True