class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencies = [(word,Counter(word)) for word in strs]
        hash_table = dict()
        for frequency in frequencies:
            word, freq = frequency
            hashable_freq = tuple(sorted(freq.items()))
            if hashable_freq in hash_table:
                hash_table[hashable_freq].append(word)
            else:
                hash_table[hashable_freq] = [word]
        return hash_table.values()
        