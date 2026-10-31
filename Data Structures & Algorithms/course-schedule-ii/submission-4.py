from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 0 -> 1 -> 2 -> 0
        graph = defaultdict(list)
        indegree = [0] * numCourses
        queue = deque()
        result = []
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        print(graph, indegree)
        for idx, course in enumerate(indegree):
            if course == 0:
                queue.append(idx)
        print(queue)
        while queue:
            current = queue.popleft()
            result.append(current)

            for nxt in graph[current]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return result if len(result) == numCourses else []
