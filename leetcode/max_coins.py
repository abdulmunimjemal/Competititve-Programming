# Improved Time Complexity Solution - Aug 16

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total_coins = 0
        n = len(piles)
        for i in range(n//3, n, 2):
            total_coins += piles[i]
        return total_coins


# PREVIOUS SOLUTIONS

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        third = len(piles) // 3
        piles = sorted(piles, reverse=True)[:-third] 
        # the last thrid after sorting is Bob's
        mine = 0
        for i in range(1,int(2 * third), 2): 
            mine += piles[i] # collecting our coin
        return mine
