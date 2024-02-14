class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        skipped = 0
        while len(students) != skipped:
            if not (students and sandwiches): break
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                skipped = 0
            else:
                students.append(students.pop(0))
                skipped += 1
        return len(students)
        