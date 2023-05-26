class Solution(object):
    def dailyTemperatures(self, temperatures):
        s = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if s and temperatures[i] > temperatures[s[-1]]:
                while s and temperatures[i] > temperatures[s[-1]]:
                    ans[s[-1]] = i - s[-1]
                    s.pop()
            s.append(i)
        return ans


s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))