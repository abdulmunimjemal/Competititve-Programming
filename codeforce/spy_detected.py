t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Length of the array
    arr = list(map(int, input().split()))  # Elements of the array

    # Find the index of the element that is not equal to others
    if arr[0] != arr[1]:
        if arr[0] == arr[2]:
            print(2)
        else:
            print(1)
    else:
        for i in range(2, n):
            if arr[i] != arr[0]:
                print(i+1)
                break
