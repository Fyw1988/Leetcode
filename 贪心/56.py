class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        res = []
        area = [-2, -1]
        for i in range(len(intervals)):
            if intervals[i][0] > area[1]:
                res.append(area)
                area = intervals[i]
            else:
                area[1] = max(area[1], intervals[i][1])
        res.append(area)
        return res[1:]