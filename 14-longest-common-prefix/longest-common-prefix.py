class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest_string = min(map(len, strs))

        common = ""

        for i in range(shortest_string):
            current_common = ""
            for word in strs:
                if current_common == "": current_common = word[i]
                if word[i] != current_common:
                    return common
            common += current_common
        return common


            