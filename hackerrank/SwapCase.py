def swap_case(s):
    result = []
    for i in s:
        if i.islower():
            result.append(i.upper())
        else:
            result.append(i.lower())
    return "".join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)