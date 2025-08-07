from abc import ABC, abstractmethod
class vehile(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class car(vehile):
    def start_engine(self):
        print("car engine started")
    def stop_engine(self):
        print("car engine stop")

class bike(vehile):
    def start_engine(self):
        print("bike engine started")
    def stop_engine(self):
        print("bike engine stop")


car = car()
car.start_engine()
car.stop_engine()

bike = bike()
bike.start_engine()
bike.stop_engine()