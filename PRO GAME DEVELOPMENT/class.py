
#class and objects
#class or "blueprint"
class Student():
    name=""
    age=13
    form="A"
    teacher="Mrs smith"
    year_group=8
#constructor-gets called when object is created
    def __init__(self):
        print(" new object made!")
#changing details
    def details(self):
        self.name= input("enter your name!")
        self.age= input("input your age-")
#showing details
    def show(self):
        print("the detail of the student are-")
        print(self.name)
        print(self.age)
        print(self.form)
        print(self.teacher)
        print(self.year_group)
#objects
john = Student()    
sarah = Student()
sarah.details()
sarah.show()
