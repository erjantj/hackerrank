from collections import deque
class Solution:
    def bfs(self, start, rooms, visited):
        openSet = deque([start])
        while openSet:
            node = openSet.popleft()

            if node in visited:
                continue
            visited.add(node)

            for nextNode in rooms[node]:
                openSet.append(nextNode)

    def canVisitAllRooms(self, rooms):
        visited = set()
        self.bfs(0, rooms, visited)
        return len(visited) == len(rooms)

rooms = [[1],[2],[3],[]]
# rooms = [[1,3],[3,0,1],[2],[0]]

print(Solution().canVisitAllRooms(rooms))
        