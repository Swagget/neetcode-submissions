class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        self.students = students
        self.sandwiches = sandwiches
        while not self.deadlock_check():
            if self.students[0] == self.sandwiches[0]:
                self.student_accept()
            else:
                self.student_refuse()
            if len(self.sandwiches) == 0:
                return 0
        return len(self.sandwiches)

    def student_refuse(self):
        self.students = [*self.students[1:], self.students[0]]
    
    def student_accept(self):
        self.students = self.students[1:]
        self.sandwiches = self.sandwiches[1:]

    def deadlock_check(self):
        if self.sandwiches[0] not in self.students:
            return True
        return False