class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

   
    def get_name(self):
        return self.__name

 
    def set_age(self, age):
        if age < 0:
            raise ValueError("Tuổi không hợp lệ")
        self.__age = age

    def __str__(self):
        return f"{self.__name} - {self.__age}"

    def speak(self):
        print("Hello!")

    @classmethod
    def say_hi(cls):
        print("Hi from class")

    @staticmethod
    def info():
        print("Static method")

    def __eq__(self, other):
        return self.__age == other.__age


class Student(Person):  
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return f"{super().__str__()} - {self.grade}"


p1 = Person("Phong", 19)
p2 = Person("hieu", 18)

print(p1)
p1.speak()
Person.say_hi()
Person.info()
print(p1 == p2)

s = Student("Linh", 19, "Phong")
print(s)