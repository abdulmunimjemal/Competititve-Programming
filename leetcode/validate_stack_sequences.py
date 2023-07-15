# using stack

def validateStackSequences(pushed: list, popped: list) -> bool:
    stack = []
    for i in range(len(pushed)):
        if pushed[i] == popped[j]:
            j += 1
            