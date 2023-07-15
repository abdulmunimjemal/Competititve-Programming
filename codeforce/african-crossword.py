import sys

def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def lcm(a, b):
    return (a // math.gcd(a, b)) * b

def sortbysec(arr):
    return sorted(arr, key=lambda x: x[1])

def maxfreqof(nums):
    count = 0
    ans = 0
    for n in nums:
        if count == 0:
            ans = n
        if n == ans:
            count += 1
        else:
            count -= 1
    return ans

def MEX(V):
    i = 0
    for j in V:
        if j != i:
            return i
        i += 1
    return V[-1] + 1

def maxfreq(V):
    C = 1
    MAX = 0
    V.sort()
    pivot = V[0]
    for i in range(1, len(V)):
        if V[i] != pivot:
            pivot = V[i]
            C = 0
        C += 1
        MAX = max(MAX, C)
    return MAX

def main():
    N, M = map(int, input().split())
    A = []
    C = []
    for _ in range(N):
        A.append(input())
    C = A[:]

    for i in range(N):
        for j in range(M):
            is_duplicate = False
            for k in range(M):
                if C[i][k] == C[i][j] and j != k:
                    A[i] = A[i][:k] + '.' + A[i][k+1:]
                    is_duplicate = True
            for k in range(N):
                if C[k][j] == C[i][j] and i != k:
                    A[k] = A[k][:j] + '.' + A[k][j+1:]
                    is_duplicate = True
            if is_duplicate:
                A[i] = A[i][:j] + '.' + A[i][j+1:]

    for i in range(N):
        for j in range(M):
            if A[i][j] != '.':
                sys.stdout.write(A[i][j])
    sys.stdout.write('\n')

if __name__ == "__main__":
    main()
