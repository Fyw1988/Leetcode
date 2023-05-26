class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: x[0])   # 按照左边界排序
        arrows = 0
        area = [-2e33, -2e32]
        for i in range(len(points)):
            if points[i][0] > area[1]:
                arrows += 1
                area = points[i]
            else:
                area[0] = max(points[i][0], area[0])
                area[1] = min(points[i][1], area[1])
        return arrows


s = Solution()
print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))