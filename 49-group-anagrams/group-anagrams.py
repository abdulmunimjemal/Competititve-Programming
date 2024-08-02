class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)
        return hashmap.values()


        