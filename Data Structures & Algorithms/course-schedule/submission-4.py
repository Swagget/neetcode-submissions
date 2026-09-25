class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_taken = set()
        num_prerequisites = [0 for _ in range(numCourses)]
        preq_satisfying = {}
        for requirement in prerequisites:
            num_prerequisites[requirement[0]] += 1 # This says that there is another prerequisite that needs to be satisfied.
            if requirement[1] in preq_satisfying:
                preq_satisfying[requirement[1]].append(requirement[0])
            else:
                preq_satisfying[requirement[1]] = [requirement[0]]
        
        available_courses = deque()
        for index, element in enumerate(num_prerequisites):
            if element == 0:
                available_courses.append(index)
        
        while len(courses_taken) < numCourses and len(available_courses) > 0:
            taking = available_courses.popleft()
            courses_taken.add(taking)
            if taking in preq_satisfying:
                for satisfied_prereq in preq_satisfying[taking]:
                    num_prerequisites[satisfied_prereq] -= 1
                    if num_prerequisites[satisfied_prereq] == 0:
                        available_courses.append(satisfied_prereq)

        if len(courses_taken) == numCourses:
            return True
        return False