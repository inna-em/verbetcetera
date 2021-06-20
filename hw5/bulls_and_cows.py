class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        s_counter = [0]*10
        g_counter = [0]*10
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
            else:
                s_counter[int(secret[i])] += 1
                g_counter[int(guess[i])] += 1
        cows = 0
        for idx in range(len(g_counter)):
            cows += min(g_counter[idx], s_counter[idx])
        return "{}A{}B".format(bulls, cows)
