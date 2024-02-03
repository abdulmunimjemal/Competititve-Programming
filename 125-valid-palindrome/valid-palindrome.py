class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove everything
        s = s.lower()
        s = re.sub(r"[^a-z0-9]+", '', s)
        return s == s[::-1]
        