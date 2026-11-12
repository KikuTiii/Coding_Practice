# You are given a list of tasks. Each task contains a priority and a name.

# A smaller priority number means the task should be processed first.

# Return the task names in the order they should be processed.

# All priorities are unique.

import heapq

class Solution:
    def processTasks(
        self,
        tasks: list[tuple[int, str]]
    ) -> list[str]:

        heapq.heapify(tasks)
        result = []

        while tasks:
            Priority, task = heapq.heappop(tasks)
            result.append(task)
        return result


#Tests
solution = Solution()

assert solution.processTasks([
    (3, "email"),
    (1, "production bug"),
    (2, "tests")
]) == [
    "production bug",
    "tests",
    "email"
]

assert solution.processTasks([
    (10, "documentation"),
    (2, "deploy"),
    (5, "review"),
    (1, "fix bug")
]) == [
    "fix bug",
    "deploy",
    "review",
    "documentation"
]

assert solution.processTasks([
    (1, "only task")
]) == [
    "only task"
]

assert solution.processTasks([]) == []

print("Todos os testes passaram!")