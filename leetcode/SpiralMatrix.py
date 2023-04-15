class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ordered = []
        while len(matrix) != 0:
            # case 1: remove first line
            ordered += matrix.pop(0)  # pops the first and adds the popped to the list
            
            # case 2, last digit of every line
            
            if matrix and matrix[0] != []: # make sure the last popping won't make it empty
                for line in matrix:
                    ordered.append(line.pop()) # pop the last
            
            if matrix: # three go back on the last one
                ordered += matrix.pop()[::-1]  # from last to first
            
            if matrix and matrix[0] != []: # first value of every line from bottom up
                for line in matrix[::-1]:
                    ordered.append(line.pop(0))
        return ordered