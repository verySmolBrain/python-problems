class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sortedOrder = []

        inDegree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}

        for edge in prerequisites:
            child, parent = edge[0], edge[1] 
            graph[parent].append(child)
            inDegree[child] += 1
        
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        while sources:
            vertex = sources.pop()
            sortedOrder.append(vertex)

            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        if len(sortedOrder) != numCourses:
            return False
        return True