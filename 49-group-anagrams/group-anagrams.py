class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)
        for s in strs:
            sorted_word = ''.join(sorted(list(s)))
            hash_table[sorted_word].append(s)
        return hash_table.values()
            