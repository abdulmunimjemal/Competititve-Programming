t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    div = list(map(int, input().split()))
    div.sort(reverse = True)
    count, divs = 0, 2
    i = 0
    while divs < n and i < len(div):
        divs += div[i] - 1
        i += 1
        count += 1
    if divs >= n:
        print(count)
    else:
        print(-1)