class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        total_students = len(students)
        students_liking_squares = sum(students)
        students_liking_circles = total_students - students_liking_squares

        i = 0
        while students_liking_squares and students_liking_circles:
            if sandwiches[i] == 0:
                students_liking_circles -= 1
            else:
                students_liking_squares -= 1
            i += 1
        
        while students_liking_squares and sandwiches[i] == 1:
            students_liking_squares -= 1
            i += 1
        
        while students_liking_circles and sandwiches[i] == 0:
            students_liking_circles -= 1
            i += 1
        
        return students_liking_squares or students_liking_circles