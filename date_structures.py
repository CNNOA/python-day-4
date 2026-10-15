empty_list = []

grocery_list = ["apple","bread","ice cream","pizza"]
second_list = [[1,2],[3,4,5]]

students = ["Huch", "ishan","Pooja","Tyler","Sam"]
students.append("Jeff")
print(students)

students.remove("Sam")
print(students)


def main():
    grade = input("What grade did you get?")

    if grade >= 90:
        print("You got an A")

    if grade >= 80:
        print("You got a B")

    else:
        print("You got a C")


#For Loop
 students = [“Sam”, “Pooja”, “Alina”, “Susan”]

# for student in students:
#     print(student,"It's great!")