class person:
    def __init__(s, name, age):
        s.__name = name
        s.__age = age
        
    def show(s):
        print(f'{s.__name}, {s.__age}')
    def set_age(s,new_age):
        if new_age > 0:
            s.__age = new_age
p = person('affan', 24)
p.show()
p.__name = "shaikh"
p.show()
