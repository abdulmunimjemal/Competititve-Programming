class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = [((point[0]**2 + point[1]**2)**0.5, point) for point in points]
        # Let us keept the distance and point in tuples then store those tuples in the lsit
        d.sort() # built in sorting function to sort
        return [point for distance, point in d[:k]]  # return list of the points up to kth element from the sorted list