class employee:
    def get_salary(self):
        print("Regular employee salary is 50K")
class designer(employee):
    def get_salary(self):
        print("salary of designer is 70K")
class developer(employee):
    def get_salary(self):
        print("salary of developer is 80K")
class manager(employee):
    def get_salary(self):
        print("salary of manager is 80K")

a=designer()
a.get_salary()
