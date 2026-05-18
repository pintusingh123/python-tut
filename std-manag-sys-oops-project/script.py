class Student:
  all_std = []
  def __init__(self, name, roll_num, marks):
    self.name = name
    self.roll = roll_num
    self.marks = marks

  def update_new_marks(self, new_marks):
    self.marks = new_marks

  @classmethod
  def find_student_by_roll(cls, roll_num):
    for std in cls.all_std:
      if std.roll == roll_num:
        return std
    return None






  @classmethod
  def add_student(cls):
    name = input("Enter student name: ")
    roll_num = int(input("Enter student roll number: "))
    marks = input("Enter student marks: ")
    std = Student(name, roll_num, marks)
    cls.all_std.append(std)
    print(f"Student {name} added successfully.")

  @classmethod
  def update_marks(cls):
     roll_num = int(input("Enter student roll number to update marks: "))
     student = cls.find_student_by_roll(roll_num)
     if student:
      new_marks = int(input("Enter new marks: "))
      student.update_new_marks(new_marks)
      print(f"Marks updated for {student.name}.")
     else:
      print("Student not found.")


  @classmethod
  def show_all_students(cls):
    if not cls.all_std:
      print("No students found.")
    else:
      for std in cls.all_std:
        print(f"Name: {std.name}, Roll Number: {std.roll}, Marks: {std.marks}")

  @classmethod
  def delete_student(cls):
    roll_num = int(input("Enter student roll number to delete: "))
    for std in cls.all_std:
      if std.roll == roll_num:
        cls.all_std.remove(std)
        print(f"Student {std.name} deleted.")
        break
    else:
      print("Student not found.")

