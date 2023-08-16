import textwrap

def wrap(string, max_width):
    result = []
    w = 0
    for s in string:
        w += 1
        result.append(s)
        if w == max_width:
            result.append('\n')
            w = 0 
    return "".join(result)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)