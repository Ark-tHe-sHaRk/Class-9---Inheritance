#Parent class
class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    
#Creating child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)

    def display(self):
        print('Name: ', self.name)
        print('Idnumber: ', self.idnumber)
        print('Salary: ', self.salary)
        print('post: ', self.post)



#Creation of an object 

The_Employee = Employee('ARk_tHe_$#@Rk', 48208, 9000000, 'CEO')
The_Employee.display()

