class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 先根据身高降序排列
        people.sort(key=lambda x: (-x[0], x[1]))

        # 根据每个元素的第二个维度k，贪心算法，进行插入
        que = []
        for p in people:
            que.insert(p[1], p)
        return que
