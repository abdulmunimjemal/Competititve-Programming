class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        skipped = 0
        sandwiches = deque(sandwiches)
        students = deque(students)
        while students and len(students) != skipped:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                skipped = 0
            else:
                students.append(students.popleft())
                skipped += 1
        return skipped