class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = slow_time = 0

        for p, s in sorted(zip(position, speed), reverse=True):
            eta = (target - p)/s
            if slow_time < eta:
                ans+=1
                slow_time = eta
        return ans