from Person import Person
import util

class Student(Person):
    def __init__(self, id: int, name: str, age: int, field_of_study: str|None = None, year_of_study: int|None = None, grade_avg: int|None = None):
        super().__init__(id, name, age)
        if field_of_study == None:
            self._field_of_study = input("What is their field of study? ")
        else:
            self._field_of_study = field_of_study
        
        if year_of_study == None:
            self._year_of_study = util.numberInputValidator("year of study") 
        else:
            self._year_of_study = year_of_study

        if grade_avg == None:
            self._grade_avg = util.numberInputValidator("student average")
        else:
            self._grade_avg = grade_avg
    

    def getFieldOfStudy(self) -> str:
        return self._field_of_study
    

    def setFieldOfStudy(self, field: str) -> None:
        self._field_of_study = field
    
    
    def getYearOfStudy(self) -> str|int:
        return self._year_of_study
    

    def setYearOfStudy(self, year: str) -> None:
        self._year_of_study = year


    def getGradeAvg(self)-> str|None|int:
        return self._grade_avg
    

    def setGradeAvg(self, avg: int) -> None:
        self._grade_avg = avg


    def getPersonAsDict(self) -> dict:
        student_dict = super().getPersonAsDict()
        student_dict.update(
            {
                "Field Of Study": self.getFieldOfStudy(), 
                "Year Of Study": self.getYearOfStudy(), 
                "Grade Average": self.getGradeAvg()
                }
        )
        return student_dict 

    
    def getPersonString(self) -> str:
        return super().getPersonString() + ", their field of study is " + self.getFieldOfStudy() + ", they are in year " + str(self.getYearOfStudy()) + ", their avarage is " + str(self.getGradeAvg())


    def printMyself(self) -> None:
        print(self.getPersonString())
        

if __name__ == "__main__":
    test_id = 42
    test_name = "John"
    test_age = 35
    test_field_of_study = "Cosmology"
    test_year_of_study = 2
    test_grade_avg = 75
    student1 = Student(test_id, test_name, test_age, test_field_of_study, test_year_of_study, test_grade_avg)
    if student1.getId() != test_id:
        print("The ID should be " + str(test_id) + ", instead it's " + str(student1.getId()))
    if student1.getName() != test_name:
        print("The studnet's name should be " + test_name + ", instead it's " + str(student1.getName()))
    if student1.getAge() != test_age:
        print("The age should be " + str(test_age) + ", instead it's " + str(student1.getAge()))
    if student1.getFieldOfStudy() != test_field_of_study:
        print("The student's field of study should be " + test_field_of_study + ", instead it's " + student1.getFieldOfStudy())
    if student1.getYearOfStudy() != test_year_of_study:
        print("The year of study should be " + str(test_year_of_study) + ", instead it's " + str(student1.getYearOfStudy()))
    if student1.getGradeAvg() != test_grade_avg:
        print("The student's avarage should be " + str(test_grade_avg) + ", instead it's " +str(student1.getGradeAvg()))