class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        sorted_tasks = sorted(tasks,key = lambda task: task[0] - task[1])
        total_energy = 0
        current_energy = 0

        for actual,minimum in sorted_tasks:
            if current_energy < minimum:
                deficit = minimum - current_energy
                total_energy += deficit
                current_energy = minimum
            current_energy -= actual
        return total_energy
