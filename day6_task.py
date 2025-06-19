# #POLYMORPHISM
# import math
# from abc import ABC,abstractmethod
#
# class Shape:
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius * self.radius
#
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# class Square(Shape):
#     def __init__(self,width):
#         self.width = width
#
#     def area(self):
#         return self.width * self.width
#
# class Pizza(Circle):
#     def __init__(self,topping,radius):
#         super().__init__(radius)
#         self.topping = topping
#
# Shapes = [Circle(2),Rectangle(2,5),Square(4),Pizza("Cheese",9)]
#
# for shape in Shapes:
#     print(f"{shape.area()}m\u00b2")
#
# #DUCK TYPING
#
# class Animal:
#     alive = True
#
# class Dog(Animal):
#     def speak(self):
#         print("Woof!")
#
# class Cat(Animal):
#     def speak(self):
#         print("Meow!")
#
# class Car:
#
#     alive = False
#
#     def speak(self):
#         print("Honk!")
#
# Animal = [Dog(),Cat(),Car()]
#
# for animal in Animal:
#     animal.speak()
#     print(animal.alive)
#
# #AGGREGATION
#
# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def list_books(self):
#             return(f"{book.title} by {book.author} of {book.pages} pages" for book in self.books)
#
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
# # Create library and books
# library = Library("Sky Line Library")
#
# book1 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 200)
# book2 = Book("Fluent Python", "Luciano Ramalho", 250)
# book3 = Book("Python for Data Analysis", "Wes McKinney", 300)
#
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
#
# # Print library name
# print(library.name)
#
# for book in library.list_books():
#     print(book)
#
#EXAMPLE
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def add_address(self,address):
#         self.address = address
#
#     def show_info(self):
#         return(f"{self.name} is {self.age} years old lives in street no.{address.street} of {address.city} of {address.state} state and its zip code is {address.zip}")
#
# class Address:
#     def __init__(self, street, city, state, zip):
#         self.street = street
#         self.city = city
#         self.state = state
#         self.zip = zip
#
# student = Student("Johny",19)
#
# address = Address(1,"Los Angeles","California",90002)
#
# print(student.show_info())

#COMPOSITION

# class Engine:
#     def __init__(self, horse_power):
#         self.horse_power = horse_power
#
# class Wheel:
#     def __init__(self, size):
#         self.size = size
#
# class Car:
#     def __init__(self,make, model, horse_power,wheel_size):
#         self.make = make
#         self.model = model
#         self.engine = Engine(horse_power)
#         self.wheels = [Wheel (wheel_size) for wheel in range(4)]
#
#     def display(self):
#         return (f"{self.make} {self.model} {self.engine.horse_power}hp {self.wheels[0].size}in")
#
# car1 = Car('Toyota', 'Ford', 120, 18)
# car2 = Car('Audi', 'Ford', 120, 50)
# car3 = Car('Audi', 'Ford', 120, 50)
#
# print(car1.display())
# print(car2.display())
# print(car3.display())

#EXAMPLE

# class Chapter:
#     def __init__(self, title, chapter_number):
#         self.title = title
#         self.chapter_number = chapter_number
#
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.chapters = []
#
#     def add_chapter(self, chapter):
#         self.chapters.append(chapter)
#
#     def show_book(self):
#         return(f"Chapter no.{chapter.chapter_number} {chapter.title}" for chapter in self.chapters)
#
# book = Book("Rich Dad, Poor Dad","Robert T.Kiyosaki")
#
# chapter1 = Chapter("Rich Dad, Poor Dad", 1)
# chapter2 = Chapter("The Rich Don’t Work for Money", 2)
# chapter3 = Chapter("Why Teach Financial Literacy?", 3)
#
# book.add_chapter(chapter1)
# book.add_chapter(chapter2)
# book.add_chapter(chapter3)
#
# for chapter in book.show_book():
#     print(chapter)



