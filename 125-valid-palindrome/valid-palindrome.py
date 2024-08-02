class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation + ' ')).lower()
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] != s[j]: return False
            i, j = i+1, j-1
        return True
        