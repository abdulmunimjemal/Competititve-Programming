t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    zero = 0
    mx = 0

    for i in range(n):
        if a[i] == 0:
            zero += 1
            mx = max(zero, mx)
        else:
            mx = max(zero, mx)
            zero = 0

    print(mx)
