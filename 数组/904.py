# 这题的思路其实和209是完全一样的滑动窗口，只不过这题需要用到哈希表来记录窗口左端需要跳到的位置，哈希表暂时还未涉及
def totalFruit(fruits):
    """
    :type fruits: List[int]
    :rtype: int
    """
    cnt = Counter()

    left = ans = 0
    for right, x in enumerate(fruits):
        cnt[x] += 1
        while len(cnt) > 2:
            cnt[fruits[left]] -= 1
            if cnt[fruits[left]] == 0:
                cnt.pop(fruits[left])
            left += 1
        ans = max(ans, right - left + 1)

    return ans