class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        third = len(piles) // 3
        piles = sorted(piles, reverse=True)[:-third] 
        # the last thrid after sorting is Bob's
        mine = 0
        for i in range(1,int(2 * third), 2): 
            mine += piles[i] # collecting our coin
        return mine
