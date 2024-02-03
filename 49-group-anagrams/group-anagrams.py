class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = dict()
        for s in strs:
            freq = Counter(s)
            hashable_freq = tuple(sorted(freq.items()))
            if hashable_freq in hash_table:
                hash_table[hashable_freq].append(s)
            else:
                hash_table[hashable_freq] = [s]
        return hash_table.values()
            