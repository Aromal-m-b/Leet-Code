class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[0] - x[1] )
        
        total = 0
        energy = 0

        for i in range(0,len(tasks)):
            if energy < tasks[i][1]:
                total += tasks[i][1]-energy
                energy = tasks[i][1]
            energy -= tasks[i][0]
        return total
