class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        res = [i - j for i, j in zip(gas, cost)]
        start = 0
        curSum = 0
        l = len(gas)   # 需要走过的总路程
        for i in range(l):
            curSum += res[i]
            if curSum < 0:
                curSum = 0
                start = i + 1
        if sum(res) < 0:
            return -1
        else:
            return start


class Solution2:
    def canCompleteCircuit(self, gas, cost):
        start = 0
        curSum = 0
        totalSum = 0
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if curSum < 0:
                curSum = 0
                start = i + 1
        if totalSum < 0: return -1
        return start
