# 这题由于字母的种类有限，因此也可以用数组来作为哈希表
def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    strmap = dict()
    for s in magazine:
        strmap[s] = strmap.get(s, 0) + 1
    for s in ransomNote:
        if s in strmap and strmap[s] != 0:
            strmap[s] -= 1
        else:
            return False
    return True
