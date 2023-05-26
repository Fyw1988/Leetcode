def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    hash = [0] * 26
    for i in s:
        hash[ord(i) - ord('a')] += 1
    for i in t:
        hash[ord(i) - ord('a')] -= 1
    for i in range(len(hash)):
        if hash[i] != 0:
            return False
    return True
