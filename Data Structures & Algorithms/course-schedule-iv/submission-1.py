class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_map = defaultdict(set)

        for course in prerequisites:
            course, depend = course
            adj_map[course].add(depend)
        
        def dfs(course_num):
            if course_num in prereq_map:
                return prereq_map[course_num]
            
            prereqs = set()
            for depend in adj_map[course_num]:
                prereqs.add(depend)
                prereqs.update(dfs(depend))
            
            prereq_map[course_num] = prereqs

            return prereqs

        prereq_map = defaultdict(set)
        for course_num in range(numCourses):
            dfs(course_num)
        
        print(prereq_map)

        result = []
        for query in queries:
            course_num, prereq = query
            if prereq in prereq_map[course_num]:
                result.append(True)
            else: result.append(False)
        
        return result
