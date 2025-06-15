from Person import Person
import util

class Employee(Person):
    def __init__(self, id: int, name: str, age: int, field_of_work: str|None = None, salary: int|None = None):
        super().__init__(id, name, age)
        if field_of_work == None:
            self._field_of_work = input("What is their field of work? ")
        else:
            self._field_of_work = field_of_work

        if field_of_work == None:
            self._salary = util.numberInputValidator("salary")
        else:
            self._salary = salary


    def getFieldOfWork(self) -> str:
        return self._field_of_work
    

    def setFieldOfWork(self, field_of_work: str) -> None:
        self._field_of_work = field_of_work


    def getSalary(self) -> int|None:
        return self._salary
    

    def setSalary(self, new_salary: int) -> None:
        self._salary = new_salary

    
    def getPersonAsDict(self) -> dict:
        employee_dict = super().getPersonAsDict()
        employee_dict.update(
            {
                "Field Of Work": self.getFieldOfWork(), 
                "Salary": self.getSalary()
                }
        )
        return employee_dict


    def getPersonString(self) -> str:
        return super().getPersonString() + ", their field of work is " + self.getFieldOfWork() + ", and their salary is " + str(self.getSalary())


    def printMyself(self) -> None:
        print(self.getPersonString())

if __name__ == "__main__":
    test_id = 280
    test_name = "Alex"
    test_age = 47
    test_salary = 100000
    test_field_of_work = "Content Creator"
    employee1 = Employee(test_id, test_name, test_age, test_field_of_work, test_salary)
    if employee1.getId() != test_id:
        print("The ID should be " + str(test_id) + ", instead it's " + str(employee1.getId()))
    if employee1.getName() != test_name:
        print("The employee's name should be " + test_name + ", instead it's " + str(employee1.getName()))
    if employee1.getAge() != test_age:
        print("The age should be " + str(test_age) + ", instead it's " + str(employee1.getAge()))
    if employee1.getFieldOfWork() != test_field_of_work:
        print("The employee's field of work should be " + test_field_of_work + ", instead it's " + employee1.getFieldOfWork())
    if employee1.getSalary() != test_salary:
        print("The employee's salary should be " + str(test_salary) + ", instead it's " +str(employee1.getSalary()))