# 
class Person:

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastame = lname

    def __str__(self):
        return (f'My name is {self.firstname} {self.lastame}')
    
class Student(Person):
    def __init__(self, fname, lname, std):
        self.standard = std
        super().__init__(fname,lname)

    def __str__(self):
        return f'{super().__str__()} and I am in {self.standard} standard'



person1 = Person('Harsh', 'Mehra')
print(person1)

student1 = Student('Harsh', 'Mehra', 10)
print(student1)