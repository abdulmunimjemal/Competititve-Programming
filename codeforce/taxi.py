rules ="""
each car at most 4 passengers

each group should ride same taxi

but one taxi can get more than one group
"""


# group_sizes.sort()

from collections import Counter

n = int(input())
group_sizes = list(map(int, input().split()))

p = Counter(group_sizes)

taxi_count = p[4]
taxi_count += min(p[3], p[1])
taxi_count += (p[2] // 2)

if p[1] > p[3]:
    e = p[1] - p[3]
    if p[2] % 2:
        if e > 1:
            e -= 2
            taxi_count += 1
            if e % 4:
                taxi_count += (e//4)
                taxi_count += 1
            else:
                taxi_count += (e // 4)
        else:
            taxi_count +=1
    else:
        if e % 4:
            taxi_count += (e // 4)
            taxi_count += 1
        else:
            taxi_count += (e//4)
elif p[1] < p[3]:
    e = p[3] - p[1]
    if p[2] % 2:
        taxi_count += e
        taxi_count += 1
    else:
        taxi_count += e
elif p[2] % 2:
    taxi_count += 1

print(taxi_count)
                