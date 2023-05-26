class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[0])
        remv = 0
        area = [-10e6, -10e5]
        for i in range(0, len(intervals)):
            if intervals[i][0] >= area[1]:
                area = intervals[i]
                continue
            else:
                remv += 1
                area = intervals[i] if intervals[i][1] < area[1] else area
        return remv


s = Solution()
print(s.eraseOverlapIntervals([ [1,2], [1,2], [1,2] ]))