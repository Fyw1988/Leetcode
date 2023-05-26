from collections import *


class Solution:
    def findItinerary(self, tickets):
        # defaultdic(list) 是为了方便直接append
        tickets_dict = defaultdict(list)
        for item in tickets:
            tickets_dict[item[0]].append(item[1])
        # 给每一个机场的到达机场排序，小的在前面，在回溯里首先被pop(0）出去
        # 这样最先找的的path就是排序最小的答案，直接返回
        for airport in tickets_dict:
            tickets_dict[airport].sort()
        '''
        tickets_dict里面的内容是这样的
        {'JFK': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        '''
        path = ["JFK"]

        def backtracking(start_point):
            # 终止条件 tickets的长度代表车票数，车站数=车票数+1
            if len(path) == len(tickets) + 1:
                return True
            for _ in tickets_dict[start_point]:
                # 必须及时删除，避免出现死循环
                end_point = tickets_dict[start_point].pop(0)
                path.append(end_point)
                # 只要找到一个就可以返回了
                if backtracking(end_point):
                    return True
                path.pop()
                tickets_dict[start_point].append(end_point)

        backtracking("JFK")
        return path


class Solution:
    def __init__(self):
        self.path = ["JFK"]

    def findItinerary(self, tickets):
        tickets_dict = defaultdict(list)
        for ticket in tickets:
            tickets_dict[ticket[0]].append(ticket[1])
        for airport in tickets_dict:
            tickets_dict[airport].sort()
        self.backTracking(tickets_dict, len(tickets), "JFK")

        return self.path

    def backTracking(self, tickets_dict, length, start):
        if len(self.path) == length + 1:
            return True

        for _ in tickets_dict[start]:
            airport = tickets_dict[start].pop(0)
            self.path.append(airport)
            if self.backTracking(tickets_dict, length, airport): return True
            self.path.pop()
            tickets_dict[start].append(airport)