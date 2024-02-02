class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        # using dictionary to keep number
        alphabet = {letter: 0 for letter in string.ascii_lowercase}
        for i in range(len(s)):
            alphabet[s[i]] += 1
            alphabet[t[i]] -= 1
        return not any(alphabet.values())
        