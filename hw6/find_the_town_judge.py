class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        if len(trust) >= n - 1:
            tc = {} # trust counter, values = [k, m], where k is number of trusted people, m - number of peopl who trust this person
            for t in trust:
                if t[0] not in tc:
                    tc[t[0]] = [0, 0]
                tc[t[0]][0] += 1
                if t[1] not in tc:
                    tc[t[1]] = [0, 0]
                tc[t[1]][1] += 1
            for p in tc:
                if tc[p][0] == 0 and tc[p][1] == n-1:
                    return p
        return -1
