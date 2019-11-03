def minimumSwap(s1: str, s2: str) -> int:
    if (s1 + s2).count('x') % 2 != 0 or (s1 + s2).count('y') % 2 != 0:
        return -1

    s1 = [c for c in s1]
    s2 = [c for c in s2]

    moves = 0
    action_taken = True
    while s1 != s2:

        if not action_taken:
            return -1
        action_taken = False

        for i in range(len(s1)):

            if s1[i] != s2[i]:
                for j in range(i + 1, len(s1)):
                    if s1[i] == s1[j] and s1[j] != s2[j]:
                        s1[i] = s2[i]
                        s2[j] = s1[j]
                        action_taken = True
                        moves += 1
                        break

                if not action_taken:
                    for j in range(i, len(s1)):
                        if s1[j] != s1[i] and s1[j] != s2[j]:
                            s1[j] = s1[i]
                            s2[j] = s2[i]
                            action_taken = True
                            moves += 1
                            break
    return moves


s1 = "xx"
s2 = "yy"

print(minimumSwap(s1, s2))
