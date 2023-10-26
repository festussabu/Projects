# class Animal:
#
#     def __init__(self, category, name, age, used_as):
#         (instance variables)
#         self.category = category
#         self.name = name
#         self.age = age
#         self.used_as = used_as
#
#
#     def main(self):
#         print("Category:", self.category, "Name:", self.name, "Age:", self.age)
#
#     def use(self):
#         print("He is my", self.used_as)
#
#
# run = Animal("Dog", "Lab", "8", "Pet")
#
# run.main()
# run.use()






# class Student:
#
#     #calss variable
#     school_name = "ST.Joseph"
#
#     def __init__(self, name, age):
#
#         #instance variable
#         self.name = name
#         self.age = age
#
# student = Student("Festus", 20)
#
# #accessinf instance avriable
# print("Student Name:", student.name, "\nStudent Age:", student.age)
#
# #access calss variable
# print("School name:", Student.school_name)
#
# #modify instance variable
# student.name = "Raima"
# student.age = "26"
# print("Student Name:", student.name, "\nStudent Age:", student.age)
#
# #modify class variable
# Student.school_name = "ST.Antony"
# print("School Name:", Student.school_name)






# class Fruits:
#
#     Healthy = "It is healthy"
#
#     def __init__(self, name, colour):
#         self.name = name
#         self.colour = colour
#
#     def main(self):
#         print("Fruit name:", self.name, "\nFruit colour:", self.colour)
#
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#     def change_colour(self, new_colour):
#         self.colour = new_colour
#
#     @classmethod
#     def change_health(cls, new_health):
#         cls.Healthy = new_health
#
# fruit = Fruits("Apple", "Red")
#
# fruit.main()
# print(Fruits.Healthy)
#
#
# fruit.change_name("Orange")
# fruit.change_colour("Orange")
# fruit.main()
#
# Fruits.change_health("Healthy")
# print(Fruits.Healthy)






# class Car:
#
#     def __init__(self, make, model, year ):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def main(self):
#         print("My_car: ")
#         print("make: ", self.make)
#         print("model: ", self.model)
#         print("year: ", self.year)
#
#     def other(self):
#         print("\nMy_friends_car: ")
#         print("make: ", self.make)
#         print("model: ", self.model)
#         print("year: ", self.year)
#
# a = Car("Nissan", "GTR", "2000")
# b = Car("Tokyo", "Acura RLX", "2010")
#
# a.main()
# b.other()





# Using deafult cosntructor

# class Employee:
#     def dsiplay(self):
#         print("i am on leave today")
#
#
# emp = Employee()
# emp.dsiplay()




# Using non-paramadarised cosntructor

# class Company:
#     def __init__(self):
#         self.name = "Festus"
#         self.address = "kerala"
#
#     def show(self):
#         print(self.name, self.address)
#
#
# com = Company()
# com.show()





#parametarised constructor

# class Student:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(self.name, self.age)
#
# info = Student("Festus", 20)
# info.show()
#
# more_info = Student("raima", 26)
# more_info.show()





# destroctor

# class Student:
#
#     #constructor
#     def __init__(self, name):
#         print("inside costructor")
#         self.name = name
#         print("object initialized")
#
#     def show(self):
#         print("my name is", self.name)
#
#     def __del__(self):
#         print("inside destructor")
#         print("object destroyed")
#
# student = Student("Festus")
# student.show()

# del student

# student.show()




# import time
# class Student:
#
#     #constructor
#     def __init__(self, name):
#         print("inside costructor")
#         self.name = name
#         print("object initialized")
#
#     def show(self):
#         print("my name is", self.name)
#
#
#     def __del__(self):
#         print("object destroyed")
#
#
# s1 = Student("Emma")
# s2 = s1
# s1.show()
#
# del s1
#
# time.sleep(2)
# print("after sleep")
# s2.show()





# private class

# using name mangling
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
# emp = Employee("Festus", 1000)
# print(emp._Employee__salary)

#using public method on private

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#
#     def show(self):
#         print(self.name)
#         print(self.__salary)
#
# e = Employee("festus", 3000)
# e.show()



#protected calss

# class Company:
#     def __init__(self):
#         self._project = "ANSCER"
#
# class Employee(Company):
#     def __init__(self, name):
#         self.name = name
#         Company.__init__(self)
#
#     def show(self):
#         print(self.name)
#         print(self._project)


# a = Employee("Festus")
# a.show()
#
# print(a._project)



#setter, getter

# class Employee:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#
#
#     def get_age(self):
#         return self.age
#
#     def get_name(self):
#         return self.name
#     def set_age(self ,age):
#         self.age = age
#
#     def set_name(self ,name):
#         self.name = name
#
#     def full_modify(self ,name, age):
#         self.age = age
#         self.name = name
#
#
# emp = Employee("Fetsus", 20)
# print(emp.name, emp.get_age())
#
# emp.set_age(19)
# print(emp.name, emp.get_age())
#
# emp.set_name("Ribin")
# emp.set_age(28)
# print(emp.name, emp.get_age())
#
#
# emp.full_modify("Raima", 26)
# print(emp.name, emp.age)





# overriding

# class Vehicle:
#     def __init__(self, name, colour, price):
#         self.name = name
#         self.colour = colour
#         self.price = price
#
#     def show(self):
#         print(self.name, self.colour, self.price)
#
#     def speed(self):
#         print("speed is 120 km/h")
#
#     def gear(self):
#         print("there are 5 gears")
#
# class Car(Vehicle):
#
#     def speed(self):
#         print("speed is 180 km/h")
#
#     def gear(self):
#         print("there are 7 gears")
#
#
#
# car = Car("DETAILS: BUGATI", "BLACK", 1000000)
# car.show()
# car.speed()
# car.gear()
#
# print("\n")
#
# truck = Vehicle("DETAILS: TRUCK X2", "WHITE", 999999)
# truck.show()
# truck.speed()
# truck.gear()




# polymorphism

# class Circle:
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         print("area of circle is", self.pi*self.radius*self.radius)
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         print("area of rectangle is", self.length*self.width)
#
#
# def Area(self):
#     self.area()
#
#
# circle = Circle(10)
# rectangle = Rectangle(10, 5)
#
# Area(circle)
# Area(rectangle)






# method overloading

# def addition(a, b):
#     c = a+b
#     print(c)
#
# def addition(a, b, c):
#     d = a+b+c
#     print(d)
#
# addition(2, 3)    #we will get type error, cuz def always take laetst one.
#
# addition(2, 2, 3)
#


# add

# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __add__(self, other):
#        return  self.pages+other.pages
#
# b1 = Book(10)
# b2 = Book(20)
# print("addition:", b1+b2)



# multiply

# class Employee:
#     def __init__(self, days):
#         self.days = days
#
#     def __mul__(self, other):
#        return  self.days * other.salary
#
# days = 50
# salary = 800
#
# print("monthly income:",days*salary)







# inheritance:-

# single inheritance

# class Manager:
#     def Manager_info(self):
#         print("inside Manager class")
# class Employee(Manager):
#     def Employee_info(self):
#         print("inside Employee class")
#
# a = Employee()
# a.Manager_info()
# a.Employee_info()




# mukltiple inheritance

# class Father:
#     def dad_name(self, name):
#         print(name)
#
# class Mother:
#     def mom_anme(self, name):
#         print(name)
#
# class Son(Father, Mother):
#     def son_name(self, name):
#         print(name)
#
# a = Son()
# a.dad_name("Father")
# a.mom_anme("motehr")
# a.son_name("son")





# multilevel inheritance

# class Fruit:
#     def main_fruit(self, number):
#         print(number)
#
# class Apple(Fruit):
#     def apple(self, colour):
#         print(colour)
#
# class Rotten_apple(Apple):
#     def orange(self, how_much):
#         print(how_much)
#
# a = Rotten_apple()
# a.main_fruit("how many fruits: 5")
# a.apple("colour of apple is  red",)
# a.orange("How many rotten apple: 3")



# hierarchial inheritance

# class Flower:
#     def main(self):
#         print("Dis is the main FLOWER!")
#
# class Rose(Flower):
#     def rose(self, colour):
#         print(colour)
#
# class Sunflower(Flower):
#     def sunflower(self, color):
#         print(color)
#
# a = Rose()
# a.main()
# a.rose("COLOUR OF ROSE: PINK")
#
# b = Sunflower()
# b.main()
# b.sunflower("COLOUR OF SUNFLOWER: YELLOW")




#hybrid inheritance

# class Animal:
#     def __init__(self):
#         print("ANIMAL CLASS")
#
#
# class Mammal(Animal):
#     def mammal(self, category):
#         print("catagory is", category)
#
# class Birds(Animal):
#     def birds(self, number):
#         print("number of birds are,", number)
#
# class Bat(Mammal, Birds):
#     def bat(self, time):
#         print(time, "they will wander around")
#
# b = Mammal()
# b.mammal("mammals")
#
# c = Birds()
# c.birds(6)
#
# d = Bat()
# d.bat("8:00 PM")




# superclass

# class Company:
#     def company_name(self):
#         return "ANSCER"
#
# class Employee(Company):
#     def info(self):
#         a = super().company_name()
#         print(a)
#
# e = Employee()
# e.info()





# Exercise 1: Create a Class with instance attributes Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def Car(self):
#         print(f"car max speed is {self.max_speed} and mileage is {self.mileage}")
#
# c = Vehicle(250, 10)
# c.Car()


# Exercise 2: Create a Vehicle class without any variables and methods

# class Vehicle:
#     pass


# Exercise 3: Create a child class Bus that will inherit all the variables and methods of the Vehicle class Given:
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     def bus(self):
#         print("This is inside Vehicle class")
#
# a = Bus("ar", 120, 15)
# a.bus()


# Exercise 4: Class Inheritance Given:
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
# Use the following code for your parent Vehicle class.

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity=50):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# class Bus(Vehicle):
#     pass
#
# bus = Bus("NSMR", 120, 15)
# capacity = bus.seating_capacity()
# print(capacity)


# Exercise 5: Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
# Use the following code for this exercise.
class Vehicle:
    colour = "WHITE"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

car = Car("jaguar",250, 8)
print("car colour is", car.colour)

bus = Bus("jaguar",250, 8)
print("bus colour is", bus.colour)

vehicle = Vehicle("jaguar",250, 8)
print("vehicle colour is", vehicle.colour)









