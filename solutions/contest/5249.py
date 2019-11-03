import collections


def minRemoveToMakeValid(s: str) -> str:
    lefts = collections.deque()
    rights = collections.deque()


    for i in range(len(s)):
        if s[i] == '(':
            lefts.append(i)
        elif s[i] == ')':
            if len(lefts) == 0:
                rights.append(i)
            else:
                lefts.pop()

    sol = ""

    for i in range(len(s)):
        if not (i in lefts or i in rights):
            sol += s[i]

    return sol


foo = "())()((("
print(minRemoveToMakeValid(foo))