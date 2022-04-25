

class Person:

    def __init__(self, name: str, last_name: str, age: int):
        self.name = name
        self.last_name = last_name
        self.age = age

    def get_name(self) -> str:
        return self.name

    def get_last_name(self) -> str:
        return self.last_name

    def get_age(self) -> int:
        return self.age


class Student(Person):

    def __init__(self, name: str, last_name: str, age: int, student_code: str):
        super().__init__(name, last_name, age)
        self.student_code = student_code

    def get_student_code(self) -> str:
        return self.student_code


juan = Student("juan", "perez", 25, "201510090010")
print('age: ', juan.get_age())
print('code: ', juan.get_student_code())


