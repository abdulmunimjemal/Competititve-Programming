class Solution:
    def addSpaces(self, string: str, spaces: List[int]) -> str:
        result = ""
        spaces = spaces[::-1]
        i = 0
        for s in string:
            if spaces and i == spaces[-1]:
                result += ' '
                spaces.pop()
            result += s
            i += 1
        return result