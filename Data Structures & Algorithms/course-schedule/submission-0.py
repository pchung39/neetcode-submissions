from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # first build graph and indegrees
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        queue = deque()
        for course, prereq in prerequisites:
            print(course, prereq)
            graph[prereq].append(course)     # finishing prereq unlocks course
            indegrees[course] += 1
        
        for course in range(numCourses):
            if indegrees[course] == 0:      # defaultdict gives 0 courses never seen
                queue.append(course)

        while queue:
            current = queue.popleft()
            for nxt in graph[current]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    queue.append(nxt)

        for key, value in indegrees.items():
            if value > 0:
                return False
        return True
        
        