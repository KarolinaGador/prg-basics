# class definition
class Student():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.gender = "Male"
    student2.name = "Olivia"
    student2.age = 21
    student2.gender = "Female"
    student3.name = "Alici"
    student3.age = 23
    student3.gender = "Female"


    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old')
    print(f'{student2.name}, {student2.age} years old')
    print(f'{student3.name}, {student3.age} years old')

if __name__ == "__main__":
    main()