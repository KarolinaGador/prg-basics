# class definition
class Student():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

def main():
    # object creation based on the class
    student1 = Student("Dominic", 19, "Male")
    student2 = Student("Olivia", 21, "Female")
    student3 = Student("Alici", 23,"Female")
    


    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old')
    print(f'{student2.name}, {student2.age} years old')
    print(f'{student3.name}, {student3.age} years old')

if __name__ == "__main__":
    main()