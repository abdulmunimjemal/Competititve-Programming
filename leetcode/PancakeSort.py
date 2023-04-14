class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips, length  = [], len(arr)
        for i in range(length, 0, -1):
            place = arr.index(i)
            if place == i - 1:
                continue
            if place != 0:
                flips.append(place + 1)
                arr[:place+1] = arr[:place+1][::-1]
            flips.append(i)
            arr[:i] = arr[:i][::-1]
        return flips