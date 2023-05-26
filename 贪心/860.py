#
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        res = {5:0, 10:0, 20:0}
        for i in range(len(bills)):
            res[bills[i]] += 1
            if bills[i] == 5:
                continue
            elif bills[i] == 10:
                if res[5] > 0:
                    res[5] -= 1
                    continue
                else:
                    return False
            else:
                if res[5] > 0 and res[10] > 0:
                    res[5] -= 1
                    res[10] -= 1
                    continue
                elif res[5] > 2:
                    res[5] -= 3
                    continue
                else:
                    return False
        return True
