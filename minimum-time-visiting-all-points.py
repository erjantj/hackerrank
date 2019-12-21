class Solution:
    def minTimeToVisitAllPoints(self, points):
        if not points or len(points) == 1:
            return 0
        time = 0
        steps = 0
        for i in range(1, len(points)):
            p1 = points[i-1]
            p2 = points[i]
            
            while p1[0] != p2[0] or p1[1] != p2[1]:
                dx = abs(p1[0]-p2[0])
                dy = abs(p1[1]-p2[1])
                
                if dx == 0:
                    steps = dy
                elif dy == 0:
                    steps = dx
                elif dx < dy:
                    steps = dx
                else:
                    steps = dy
                
                time += steps
                
                if p1[0] < p2[0]:
                    p1[0] += steps
                elif p1[0] > p2[0]:
                    p1[0] -= steps

                if p1[1] < p2[1]:
                    p1[1] += steps
                elif p1[1] > p2[1]:
                    p1[1] -= steps
        return time


points = [[1,1],[3,4],[-1,0]]
points = [[3,2],[-2,2]]
points = [[3,2]]
print(Solution().minTimeToVisitAllPoints(points))