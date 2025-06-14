# inheritance

# class Animal:
#     def __init__(self,name):
#         self.name=name
#         self.is_alive=True
#
#     def eat(self):
#         print(f"{self.name} is eating.")
#
#     def sleep(self):
#         print(f"{self.name} is sleeping.")
#
# class dog(Animal):
#     def speak(self):
#         print("WOOF!")
#
# class cat(Animal):
#     def speak(self):
#         print("MEOW!")
#
# Dog = dog("Tommy")
# Cat = cat("Tom")
# Dog.eat()
# Dog.sleep()
# Cat.sleep()
# Cat.eat()
# Dog.speak()
# Cat.speak()

#MULTIPLE INHERITANCE
#MULTILEVEL INHERITANCE

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
# class prey(Animal):
#     def flee(self):
#         print(f'{self.name} is fleeing.')
#
# class predator(Animal):
#     def hunt(self):
#         print(f'{self.name} is hunting.')
#
# class rabbit(prey):
#     pass
#
# class hawk(predator):
#     pass
#
# class fish(predator,prey):
#     pass
#
# Fish = fish("Nemo")
# Rabbit = rabbit("Robin")
# Hawk = hawk("Temo")
#
# Fish.hunt()
# Rabbit.flee()
# Fish.flee()
# Hawk.hunt()

#
# #ABSTRACTION
#
# from abc import ABC ,abstractmethod
# class vehicle(ABC):
#      @abstractmethod
#      def go(self):
#          pass
#
#      @abstractmethod
#      def stop(self):
#          pass
#
# class car(vehicle):
#     def go(self):
#         print("You can drive")
#
#     def stop(self):
#         print("You can stop")
#
# class motorcycle(vehicle):
#     def go(self):
#         print("You can drive")
#
#     def stop(self):
#         print("You can stop")
#
# class truck(vehicle):
#     def go(self):
#         print("You can drive")
#
#     def stop(self):
#         print("You can stop")
#
# car = car()
# car.go()
# car.stop()
# truck = truck()
# truck.go()
# truck.stop()
# motorcycle = motorcycle()
# motorcycle.go()
# motorcycle.stop()
#



#SUPER FUNCTION
