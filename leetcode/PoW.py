class Solution:
    def myPow(self, x: float, n: int) -> float:
      def solver(b=x, e=abs(n)):
              if e == 0:
                  return 1
              elif e % 2 == 0:
                  return solver(b*b, e//2)
              else:
                  return b*solver(b*b, (e-1)//2)

      return float(solver()) if n >= 0 else 1/solver()

"""
BASED ON THE MATHEMATICAL REALTION

x^n = | x(x^2)^((n-1)/2) if n is odd
      | (x^2)^(n/2) if n is even
"""