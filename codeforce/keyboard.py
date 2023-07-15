direction = input()  # Direction of shifting
sequence = input()  # Sequence of characters

keyboard = {
    'q': 'q', 'w': 'w', 'e': 'e', 'r': 'r', 't': 't', 'y': 'y', 'u': 'u', 'i': 'i', 'o': 'o', 'p': 'p',
    'a': 'a', 's': 's', 'd': 'd', 'f': 'f', 'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l', ';': ';',
    'z': 'z', 'x': 'x', 'c': 'c', 'v': 'v', 'b': 'b', 'n': 'n', 'm': 'm', ',': ',', '.': '.', '/': '/'
}

if direction == 'L':
    for i in range(len(sequence)):
        sequence = sequence[:i] + keyboard[sequence[i-1]] + sequence[i+1:]
    sequence = sequence[1:]  # Remove the first character
else:
    for i in range(len(sequence)-1, -1, -1):
        sequence = sequence[:i+1] + keyboard[sequence[i+1]] + sequence[i+2:]
    sequence = sequence[:-1]  # Remove the last character

print(sequence)
