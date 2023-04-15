# recursive
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return self.solve(n,k) + 1
    def solve(self, n: int, k: int) -> int:
        if (n==1):
          return 0
        return (self.solve(n-1, k) + k) % n



#Non recursive Time Complexity: O()
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
      friends = [i for i in range(1, n + 1)] 
      while len(friends) != 1: 
          if len(friends) < k:
              index = (k-1) % len(friends) 
          else:
              index = k - 1 
          friends.pop(index)
          friends = friends[index:] + friends[:index]
      return friends[0]