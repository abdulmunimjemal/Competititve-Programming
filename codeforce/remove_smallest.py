def solve(a):
    a.sort() 
    n = len(a)
    for i in range(1, n):
        if abs(a[i] - a[i-1]) > 1:
            return "NO"
    return "YES"


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = solve(a)
    print(result)
