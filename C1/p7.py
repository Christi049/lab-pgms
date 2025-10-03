"""Create a Python dictionary representing a student's grades in different subjects (e.g., Math, Science, History). Write a function to calculate the average grade of the student across all subjects."""

student_grade = {
  'Math' : 99,
  'Science' : 100,
  'English' : 80
}

def average_grade(grade):
  total = sum(grade.values())
  count = len(grade)
  avg = total/count
  return avg

print(f"Average grade of student is {average_grade(student_grade)}")