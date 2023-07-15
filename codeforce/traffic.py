rules = """
r,y,g

every n second
"""

no = int(input())

while no > 0:
    n = int(input())
    c, s = input().split()
    s += s
    
    cnt = 0
    maxv = 0
    flag = 0
    
    for i in range(len(s)):
        if s[i] == c:
            flag = 1
        if s[i] == 'g':
            flag = 0
            maxv = max(maxv, cnt)
            cnt = 0
        if flag == 1:
            cnt += 1
    
    print(maxv)
    t -= 1
