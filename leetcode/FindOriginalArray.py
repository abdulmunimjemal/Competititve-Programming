import collections

class Solution:
    def findOriginalArray(self, changed):
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        c = collections.Counter(changed)

        original  = []

        for num in changed:
            if num in c and c[num] >= 1: 
                c[num] -= 1
                if (num * 2) in c and c[(num*2)] >= 1:
                    original.append(num)
                    c[num*2] -= 1
            if len(original) == len(changed) // 2:
                return original
        return []
