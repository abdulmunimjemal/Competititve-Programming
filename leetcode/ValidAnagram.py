# Approach one (better:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for x in 'abcdefghijklmnopqrstuvwxzy':
            if s.count(x) != t.count(x):
                return False
        return True

# Approach two:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)