class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # 1. Map: Course -> list of its prerequisites
        # Note: Usually, the graph is built as Prereq -> Course for easier flow,
        # but we can stick to your Course -> Prereq logic.
        adj = defaultdict(list)
        for course, depend in prerequisites:
            adj[course].append(depend)
            
        visited = set()      # Currently in recursion stack (Cycle detection)
        completed = set()    # Already added to course_order (Memoization)
        course_order = []

        def dfs(course):
            if course in visited:
                return False # Cycle detected
            if course in completed:
                return True  # Already processed
            
            visited.add(course)
            
            # Visit all prerequisites first
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            
            # After all prerequisites are done, finish this course
            visited.remove(course)
            completed.add(course)
            course_order.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return [] # Return empty list if a cycle is found
                
        return course_order