class company_employee:
    com = []
    def __init__(self, name, city):
        self.name = name
        self.city = city
    def add(cls,name,city):
        new_emp = cls(name,city)
        cls.com.append(new_emp)
n = int(input('enter a number'))
for i in range(n):    
    name = input("Enter a name")
    city = input("enter a city name")

ce = company_employee(name,city)
for i in ce.com:
    print(f'{ce.name} {ce.city}')