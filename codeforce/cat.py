def is_it_cat(s: str, n: int):
    s = s.lower()
    
    if not s or s[0] != 'm' or s[-1] != 'w':
        return "NO"

    last = s[0]
    data = {'m': 'e',
            'e': 'o',
            'o': 'w',
            'w': ''}  # "last:next"
    
    for i in range(1,len(s)):
        if s[i] == last:
            continue
        else:
            if s[i] == data[last]:
                last = s[i]
                continue
            else:
                return 'NO'
    return "YES"
        
        
no = int(input())
tests = []
for i in range(no):
    d = int(input())
    data = input()
    tests.append((data,d))

for test in tests:
    print(is_it_cat(test[0], test[1]))
    
