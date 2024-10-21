class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age >= 0:
            self.__age = age

    def __str__(self):
        return f"Name is {self.name} and age is {self.age}"
