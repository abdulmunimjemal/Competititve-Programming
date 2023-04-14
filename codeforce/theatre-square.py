import math

n, m, a = map(int, input().split(' ')) # accepting input
# to cover horizontally
h = math.ceil(n/a)
# vertically 
v = math.ceil(m/a)

print(h * v) # h * v will give the total required stones