# class Student:
#     def __init__(self,name="Hello user"):
#         self.name = name
#
#     def display(self):
#         return f"Name is {self.name}"
#
# student1 = Student()
# student2 = Student("Ali")
# print(student1.display())
# print(student2.display())

# class Greets:
#     def __init__(self, name="Hello"):
#         self.name = name
#
#     def display(self):
#         return f"Hello {self.name}!"
#
#     def mul_msgs(self,*names):
#         for name in names:
#             print(f"Hello {name}")
#
# # greets1 = Greets()
# greets2 = Greets("Ali")
# greets3 = Greets()
# greets3.mul_msgs("Ali","Ahmad")
# # print(greets1.display())
# print(greets2.display())
# print(greets3.display())

#METHOD OVERLOADING

# class Multiply:
#     def multiply(self,*nums):
#         if len(nums) == 1:
#             print(nums[0])
#         elif len(nums) == 2:
#             print(nums[0] * nums[1])
#         else:
#             print("Too many arguments")
# m1 = Multiply()
# m1.multiply(2)
# m1.multiply(3,4)
# m1.multiply(4,6,3)
# m1.multiply(5,7)

class Divide:
    def divide(self,*nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] / nums[1]
        else:
            return "too many arguments"

d1 = Divide()
d2 = Divide()
d3 = Divide()
print(d1.divide(3))
print(d2.divide(9,3))
print(d3.divide(3,9,7))