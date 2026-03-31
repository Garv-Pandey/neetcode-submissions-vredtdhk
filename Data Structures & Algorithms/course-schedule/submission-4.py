class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = defaultdict(list)
        for prereq in prerequisites:
            course, depends = prereq
            course_map[course].append(depends)
        

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if not course_map[course]:
                return True
            
            visited.add(course)
            result = True
            for req_course in course_map[course]:
                if not dfs(req_course):
                    return False
            
            visited.remove(course)
            course_map[course] = []
            return result
        
        for course in prerequisites:
            if not dfs(course[0]):
                return False
        
        return True