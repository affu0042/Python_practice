class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def brands(self):
        print("the brand name is",self.brand)
    def models(self):
        print(" the model name is  ", self.model)
c1 = car("BMW", "X7")
c1.brands()
c1.models()
