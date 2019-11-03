# https://leetcode.com/problems/dota2-senate/
import collections


def predictPartyVictory(senate: str) -> str:
    voters = collections.deque()

    people = [0, 0]
    bans = [0, 0]

    for c in senate:
        team = c == 'R'  # R is 1, D is 0
        voters.append(team)
        people[team] += 1

    while all(people):
        voter = voters.popleft()

        # Use pending ban on voter if there is one, do not requeue
        if bans[voter] > 0:
            bans[voter] -= 1
            people[voter] -= 1
        # Otherwise, add a pending ban for the other team and requeue
        else:
            bans[voter ^ 1] += 1
            voters.append(voter)

    return 'Dire' if people[0] else 'Radiant'


senate = "RDDR"
print(predictPartyVictory(senate))