class dog:
    def speak(self):
        print ("Bow bow")
class cat:
    def speak(self):
        print("Meow")
class goat:
    def speak(self):
        print("may may")

def animal_sound(animal):
    animal.speak()


d = dog()
c = cat()
g = goat()

animal_sound(d)
animal_sound(c)
animal_sound(g)
