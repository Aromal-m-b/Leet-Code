class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[0] - x[1] )
        
        total = 0
        energy = 0

        for actual,mini in tasks:
            if energy < mini:
                total += mini-energy
                energy = mini
            energy -= actual
        return total
