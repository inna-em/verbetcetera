class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[position[i], speed[i]] for i in range(len(speed))]
        cars.sort(key=lambda x: -x[0])
        fleets = 0
        curr_max_time = -1
        for pos, spd in cars:
            dst = target - pos
            time = dst / spd
            if time > curr_max_time:
                curr_max_time = time
                fleets += 1
        return fleets 
