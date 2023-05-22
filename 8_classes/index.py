class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi my name is {self.name}")
        
person1 = Person("Marcy", 22)

person1.introduce()

# -- INHERITANCE --
class Student(Person): # Person is the parent class
    def __init__(self, name, age, program):
        super().__init__(name, age) # "super" copies the properties of the parent class
        self.program = program
        
student1 = Student("Watashi", 21, "BSIS")


