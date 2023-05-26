import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        d = {}
        pre_heap = []

        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1
        for key, value in d.items():
            heapq.heappush(pre_heap, (value, key))
            if len(pre_heap) > k:
                heapq.heappop(pre_heap)

        ans = []
        for _ in range(k):
            _, value = heapq.heappop(pre_heap)
            ans.append(value)
        return ans