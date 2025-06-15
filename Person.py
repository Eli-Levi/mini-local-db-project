class Person:
    def __init__(self, id: int, name: str, age: int):
        self._id = id
        self._name = name
        self._age = age
    

    def getName(self) -> str:
        return self._name
    

    def setName(self, name: str) -> None:
        self._name = name
    

    def getAge(self) -> int:
        return self._age
    

    def setAge(self, age: int) -> None:
        self._age = age


    def getId(self) -> int:
        return self._id
    

    def setId(self, id: int) -> None:
        self._id = id


    def getPersonAsDict(self) -> dict:
        return {"id": self.getId(), 
                "name": self.getName(), 
                "age": self.getAge()}


    def getPersonString(self) -> str:
        return str(self.getName()) + "'s id is " + str(self.getId()) + " and they are " + str(self.getAge()) +" years old"


    def printMyself(self) -> None:
        print(self.getPersonString())

if __name__ == "__main__":
    test_id = 101
    test_name = "Sam"
    test_age = 35
    person_1 = Person(test_id, test_name, test_age)
    if person_1.getId() != test_id:
        print("The ID should be " + str(test_id) + ", instead it's " + str(person_1.getId()))
    if person_1.getName() != test_name:
        print("The person's name should be " + test_name + ", instead it's " + str(person_1.getName()))
    if person_1.getAge() != test_age:
        print("The age should be " + str(test_age) + ", instead it's " + str(person_1.getAge()))