# https://leetcode.com/problems/implement-strstr/
def strStr(haystack: str, needle: str) -> int:
    if (len(needle) == 0):
        return 0

    if len(haystack) == len(needle):
        if haystack == needle:
            return 0

    for i in range(len(haystack) - len(needle) +1):
        match = True
        for j in range(len(needle)):
            hs_num = haystack[i+j]
            nd_num = needle[j]
            if hs_num != nd_num:
                match = False
                break
        if match:
            return i
    return -1


hs = "mississippi"
nd = "pi"

print(strStr(hs, nd))
