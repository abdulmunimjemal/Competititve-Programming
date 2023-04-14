class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals) == 0:
            return []
        elif len(intervals) == 1:
            return list(intervals)
        else:
            i = 0
            while len(intervals) - 1 > i:
                # imagine two consecutive intervals in sorted list [start_0, end_0] and [start_1, end_1]
                start_0, end_0 = intervals[i][0],  intervals[i][1]
                start_1, end_1 = intervals[i+1][0],  intervals[i+1][1]

                if ((end_0 >= end_1) and (start_1 >= start_0)): # case-i: middle
                    intervals.append([start_0, end_0]) # add the merged
                    intervals.remove(intervals[i]) 
                    intervals.remove(intervals[i]) # remove the two intials
                    intervals.sort()
            
                elif ((end_0 >= start_1) and (end_0 < end_1)): 
                    intervals.append([start_0, end_1])
                    intervals.remove(intervals[i]) 
                    intervals.remove(intervals[i])
                    intervals.sort()

                else:
                    i += 1
            return intervals
