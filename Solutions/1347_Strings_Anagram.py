class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)

        diff = s_counter - t_counter

        return sum(diff.values())
