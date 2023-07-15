t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = []
    
    for _ in range(n):
        s.append(input())

    ans = 1
    for i in range(1, n):
        ans += (s[i] == s[0])

    print(ans)
