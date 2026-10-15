student_grade={
   "  Onn": "A",
   "Bnn": "B",
   "Qnn":"C",
   "Gnn": "D",
   "Ann": "G"
   "user not found"
}

student = input("What is the student's name?")

if student_grade.get(student):
    print(student,"got a", student_grade.get(student))

else:
    print("Student not found.")