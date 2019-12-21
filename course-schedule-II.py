class Solution:
    def exploreCoursePrerequisites(self, course, courses_graph, visited, exploring, result):
        if course in visited:
            return True

        if course in exploring:
            return False
        
        exploring.add(course)
        for dependentCourse in courses_graph[course]:
            hasCycle = not self.exploreCoursePrerequisites(dependentCourse, courses_graph, visited, exploring, result)
            if hasCycle:
                return False
        exploring.remove(course)
        visited.add(course)
        result.append(course)

        return True

    def findOrder(self, numCourses, prerequisites):
        exploring = set()
        visited = set()
        courses_graph = {}
        result = []

        for course in range(numCourses):
            courses_graph[course] = []
        
        for course, prerequisit in prerequisites:
            courses_graph[prerequisit].append(course)

        for course in range(numCourses):
            hasCycle = not self.exploreCoursePrerequisites(course, courses_graph, visited, exploring, result)
            if hasCycle:
                return []

        return list(reversed(result))

numCourses = 5
prerequisites = [[1,0],[2,0],[3,1],[3,2],[4,2],[0,4]]

# numCourses = 2
# prerequisites = [[1,0]] 
print(Solution().findOrder(numCourses, prerequisites))