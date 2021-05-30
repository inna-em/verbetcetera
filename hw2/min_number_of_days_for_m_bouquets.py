class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) >= m * k:
            curr_min = max(bloomDay)
            r = curr_min
            l = 1
            while l < r:
                num_days = (l + r) // 2
                if self.hasMBouquets(bloomDay, num_days, k, m):
                    curr_min = min(curr_min, num_days)
                    r = num_days
                else:
                    l = num_days + 1
            if l == r:
                return curr_min
        return -1

    def hasMBouquets(self, bloomDay, num_days, k, m):
        flowers_in_row = 0
        num_bouquets = 0
        for num in bloomDay:
            if num <= num_days:
                flowers_in_row += 1
                if flowers_in_row == k:
                    flowers_in_row = 0
                    num_bouquets += 1
                    if num_bouquets == m:
                        return True
            else:
                flowers_in_row = 0
        return False
