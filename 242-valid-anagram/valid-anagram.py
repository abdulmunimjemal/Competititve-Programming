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
        freq_s = Counter(s)
        freq_t = Counter(t)
        return freq_s == freq_t
        
        return 
        