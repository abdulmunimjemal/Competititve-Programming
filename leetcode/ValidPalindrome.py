class Solution:
    def isPalindrome(self, s: str) -> bool:
        def helper(s):
            result = ''
            for i in s.lower():
                if i.isalnum():
                    result += i 
            return result
        string = helper(s)
        return string == string[::-1]