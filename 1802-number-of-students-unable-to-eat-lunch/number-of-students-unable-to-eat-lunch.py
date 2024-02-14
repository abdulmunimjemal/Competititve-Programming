class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches = deque(sandwiches)
        students = deque(students)
        counter = 0
        while students:
            if len(students) == counter: return counter

            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                counter = 0
            else:
                students.append(students.popleft())
                counter += 1

        return 0
        