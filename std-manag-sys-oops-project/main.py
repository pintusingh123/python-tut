from script import Student

def menu():
  while True:
    print("\n==============Student Management System==============")
    print("1. add student")
    print("2.Update Marks")
    print("3. Show all students")
    print("4. Delete Student")
    print("5. exit")

    choice = int(input("Enter your choice: "))

    match choice:
      case 1:
        Student.add_student()
      case 2:
        Student.update_marks()
      case 3:
        Student.show_all_students()
      case 4:
        Student.delete_student()
      case 5:
        print("Exiting the system. Goodbye!")
        exit()
      case _:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
     menu()