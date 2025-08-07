class op:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
class no(op):
    def __init__(self,name,age,uin):
        super().__init__(name, age)
        self.__uin = uin
    def get_uin(self):
        return self.__uin
    def set_uin(self, uin):
        self.__uin = uin

n = no('affan',24,'201p062')
print(n.get_name())
print(n.get_age())
print(n.get_uin())

n.set_name('madam')
n.set_age(23)
n.set_uin('201p')

print(n.get_name())
print(n.get_age())
print(n.get_uin())



from abc import ABC, abstractmethod
class animal:
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        print("bow... bow...")
class cat(animal):
    def sound(self):
        print("meow meow")

d = dog()
c = cat()

c.sound()
d.sound()