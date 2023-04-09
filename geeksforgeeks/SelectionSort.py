#User function Template for python3

class Solution: 
    def select(self, arr, i):
        return selectionSort(arr,i)
    
    def selectionSort(self, arr,n):
        index = len(arr)
        for i in range(index):
            min = arr[i]
            for j in range(i, index):
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends