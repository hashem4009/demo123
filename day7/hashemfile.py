class Student:
  def __init__(self,name='hashem', age = 30):
    self.name = name
    self.age = 30

newStudent = Student('hashem', 8)
oldStudent = Student('smith', 12)
print("Old attributes:", newStudent.name, newStudent.age)
print("Older Student attributes:", oldStudent.name, oldStudent.age)