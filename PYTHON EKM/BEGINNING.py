# n = int(input("Enter a num: "))
# if n%2 == 0:
#     k("even number")
# else:
#     k("odd number")

#HW
#1
# n = int(input("enter an integer: "))
# x = n + n * n + n * n * n
# k(x)

#2
# n = int(input("enter a number: "))
# num = 17
# if n > num:
#     k(abs(2*(num - n)))
# else:
#     k(num - n)

#3
# num_1 = int(input("enter 1st number: "))
# num_2 = int(input("enter 2nd number: "))
# num_3 = int(input("enter 3rd number: "))
# if num_1 == num_2 == num_3:
#     k(3*(num_1 + num_2 + num_3))
# else:
#     k(num_1 + num_2 + num_3)

#4
# letter = input("Enter a letter: ")
# vowels = ["a", "e", "i", "o", "u"]
# if letter in vowels:
#     k(letter, "Is a vowel")
# else:
#     k(letter, "Is not a vowel")


'''swap 2 numvers'''
# a = 20
# b = 10
# c = a
# a = b
# b = c
# k(f"a: {a}, b: {b}")


'''swap 2 numvers without using third vatiable'''
# a = 10
# b = 5
# a, b = b, a
# k(f"a: {a}, b: {b}")

'''find area and parameter of:
rectangle
square
triangle
'''
#rec
# rec_length = int(input("enter length: "))
# rec_width = int(input("enter width: "))
# a_rec = rec_length * rec_width
# p_rec = 2*(rec_length+rec_width)
# k(f"area of rectangle is {a_rec}")
# k(f"perimeter of rectangle is {p_rec}")

#square
# sq_side = int(input("enter one side: "))
# a_sq = sq_side**2
# p_sq = 4*sq_side
# k(f"area of square is {a_sq}")
# k(f"perimeter of square is {p_sq}")

#triangle
# tri_base = int(input("enter length: "))
# tri_height = int(input("enter height: "))
# a_tri =(1/2) * tri_base * tri_height
# tri_s1 = int(input("Enter length of side 1: "))
# tri_s2 = int(input("Enter length of side 2: "))
# tri_s3 = int(input("Enter length of side 3: "))
# p_tri = tri_s1 + tri_s2 + tri_s3
# k(f"area of triangle is {int(a_tri)}")
# k(f"perimeter of triangle is {p_tri}")

'''find sum and average of 5 number'''
# l = [2, 3, 4, 5, 6]
# sum_num = sum(l)
# avg_nun = sum_num/len(l)
# k(f"sum of 5 numbers is {sum_num}")
# k((f"average of 5 numbers is {int(avg_nun)}"))

'''find circumference and area of a circle'''
# pi = 3.14
# r_cir = int(input("Enter radius of circle: "))
# c_cir = 2*pi*r_cir
# a_cir = pi * (r_cir**2)
# k(f"circumference of circle is {c_cir}")
# k(f"area of circle is {a_cir}")

'''find volume of a sphere'''
# pi = 3.14
# r_sp = int(input("Enter radius of sphere: "))
# vol_sp = (4/3)*pi*(r_sp**3)
# k(f"volume of sphere is {round(vol_sp)}")

'''convert degree to fahrenheit'''
# degree = int(input("Enter degree: "))
# F = (degree * 9/5) + 32
# k(f"fahrenheit is {F}")

'''swap a and b in other languages'''
# a = 10
# b = 5
# a = a+b
# b = a-b
# a = a-b
# k(a)
# k(b)


'''k hello n times'''
# n = int(input("Enter a num: "))
# k("hello\n"*n)


# present_days = int(input("enter present days: ")) 
# absent_days = int(input("enter absent days: "))
# total_days = present_days + absent_days
# per_attended_class = round((present_days/total_days)*100)
# k(per_attended_class,"%")
# if per_attended_class > 75:
#     k("student is able to write exam")
# else:
#     k("student is not able to write exam")


# for i in range(1500, 2701):
#     if i%7 == 0 and i%5 == 0:
#         k(i)


# user = int(input("Enter a number: "))
# '''
# if 0-100 == 1%
# if 101-200==5%
# if 200+ == 10%
# '''
# if user <= 100:
#     k("1%")
# elif user <=200 and user > 100:
#     k("5%")
# else:
#     k("10%")


# c_f = input("Enter 'celsius' or 'fahrenheit': ")
# user_tem = int(input("Enter a tem: "))
# '''
# ask user for a tem value 
# if it's celsius then convert it into celsius 
# else into farengeit
# '''
# if c_f == 'fagranheit':
#     k(f"celsius to fagrenheit: {(user_tem * 9/5) + 32}") 
# else:
#     k(f"fagrenheit to celsius: {(user_tem - 32) * 5/9}")

# var = int(input("Enter a number: "))
# for num in range(1, 11):
#     k(f"{var} x {num} = {num*var}")


'''string funtions'''
# text = "hello howdy dodo"
# printext_2 = " python" 
# print(text.strip())
# print(text.index("h"))
# print(text[1])
# print(text.split())
# print(text.upper())
# print(text.lower())
# print(text.replace("hello", "HI"))
# print(text.replace(" ", ""))
# print(text+text_2)
# print(text.startswith("he"))
# print(text.endswith("o"))
# print(text.isalpha)
# print(text.isnumeric)
# print(text.isdigit)
# print(text.isalnum)

# n = int(input("enter a number: "))
# string = "hello world"
# for i in range(n):
#     k(string)


# string = input("Enter a string: ")
# if string.startswith("Hi"):
#     k(string)
# else:
#     k("Hi " + string)


# string = "malayalam"
# if string[0:] == string[::-1]:
#     k("it is plaindrome")
# else:
#     k("it is not plaindrome")


# string = "hello"
# vovel = ['a', 'e', 'i', 'o', 'u']
# if any(i in string for i in vovel ):
#     k("it contains vovels")
# else:
#     k("it does not contains vovels")


# entered_string = "festuss"
# first_letter = entered_string[0]
# second_letter = entered_string[-1]
# mid = len(entered_string)
# middle_letter = mid // 2
# new_string = first_letter+ second_letter+ str(entered_string[middle_letter])
# k(new_string)


# letters = []
# digits = []
# special_symbols = []
# user = input("enter: ")
# for i in user:
#     if i.isalpha():
#        letters.append(i)
#     elif i.isnumeric():
#         digits.append(i)
#     else:
#         special_symbols.append(i)
# k(f"letters {letters}")
# k(f"digits {digits}")
# k(f"special symbols {special_symbols}")


'''list'''
'''mutable'''
# lst = [2, 3 ,3, 4 ,4, 2,2]
# lst_2 = ["Mango", "Apple", "Banana"]
# k(lst.count(3))
# k(len(lst))
# lst[3]=3
# k(lst)
# lst.append(67)
# k(lst)
# lst.insert(2, 6)
# k(lst)
# lst_2.sort()
# k(lst_2)
# lst_2.reverse()
# k(lst_2)
# lst.extend(lst_2)
# k(lst)
# lst.remove(2)
# lst.pop(5)
# k(lst)
# print(min(lst))
# print(max(lst))

# list = [2, 3, 10]
# k(sum(list))

# list = [2, 10]
# mul = 1
# for num in list:
#     mul*=num
# k(mul)

# list = [1, 3, 4, 4, 5]
# k(list.count(4))


'''tuple'''
'''immutable'''
# mytuple = (2, 4, 3, 4)
# print(mytuple[1])
# print(len(mytuple))
# print(mytuple.count(4))
# print(sum(mytuple))
# print(min(mytuple))
# print(max(mytuple))
# print(mytuple.index(4))
# list = [1, 2]
# print(tuple(list))


'''set'''
'''unordered, unchangable, unindexed, mutable, no duplicate elements'''
# my_set = {2, 4, 5 ,5 ,6, 7}
# my_set.add(1)
# print(my_set)
# my_set.clear()
# print(my_set)
# set = {2, 3,4 ,5,6}
# discard, union, intersection, difference, isdisjoin, issubset, issuperset

# lst =  ["raima", "festus", "ribin"]
# dic = {num: lst.index(num) for num in lst}
# print(dic)


'''dict'''
# dic = {"Day_1":"Sunday", "Day_2": "Monday", "Day_3": "Tuesday"}
# print(dic)


'''fintions'''
# code reusability
# Avoid repetation
# 2 types - in-built funtions and user-defined funtions
# with arguments and without arguments
# def add():
#   x = int(input("enter a num:"))
#   y = int(input("enter a num:"))
#   print(x+y)
# add()

# x = int(input("enter a num:"))
# y = int(input("enter a num:"))
# def add(x,y):
#   print(x+y)
# add(x, y)

# def add(x,y):
#   print(x+y)
# x = int(input("enter a num:"))
# y = int(input("enter a num:"))
# add(x, y)

# def add(x,y):
#   print(x+y)
# add(3, 5)


# def check_number(n):
#   if n in range(0,10):
#     print("n is inside range")
#   else:
#     print("n is outside range")
# check_number(3)
  
# def reverse():
#   user_input = input("Enter a string: ")
#   reversed_string = ""
#   for letter in user_input:
#     reversed_string = letter + reversed_string
#   print("Reversed string:", int(reversed_string))
# reverse()

# def vovels():
#   v = 0
#   c= 0
#   str = input("enter a string: ")
#   lst = ["a", "e", "i", "o", "u"]
#   for char in str:
#     if char in lst:
#       v+=1 
#     else:
#       c+=1
#   print(f"consonant: {c}")
#   print(f"vovel: {v}")     
# vovels()


'''Lambda'''
# div = lambda a, b: a-b
# a = int(input(""))
# b = int(input(""))
# print(div(a, b))


# Prgrm = lambda x: x+15
# mul = lambda z, y: z*y
# print(Prgrm(10))
# print(mul(5, 5))


# def palindrome(n):
#   if n[0:] == n[::-1]:
#     print(f"{n} is a palindrome")
#   else:
#     print(f"{n} not a palindrome")
# palindrome("1001")


# def add():
#   num = []
#   for i in range(0, 10+1):
#     num.append(i)
#   print(sum(num))
# add()


# x = int(input("Enter RollNo: "))
# def rollNum ():
#   present = "present"
#   absent = "absent"
#   presents_students = [3, 6, 4, 1, 7, 8, 34, 64, 12]
#   if x in presents_students:
#     print(present)
#   else:
#     print(absent)
# rollNum()

'''filter - for getting results according to the condition'''
# lst = [2, 3,4 ,5]
# x = list(filter(lambda n : n%2==0, lst))
# print(x)

'''map - for doing operation'''
# lst = [2, 3,4 ,5]
# x = list(map(lambda n : n**2, lst))
# print(x)


# lst = [1, 2, 3, 4, 5]
# x = len(list(filter(lambda x: x%2==0, lst)))
# y = len(list(filter(lambda x: x%2!=0, lst)))
# print(x, "even")
# print(y, "odd")


# def iterate():
#   for num in range(51):
#     if num%3==0:
#       print(f"{num} = Fizz")
#     elif num%5==0:
#       print(f"{num} = Buzz")
#     elif num%3==0 and num%5==0:
#       print(f"{num} = FizzBuzz")
# iterate()


# def0 dog():
#   user_input= int(input("Enter a age: "))
#   human_age = 10.5
#   if user_input <=2:
#     print(f"{user_input} dog years is equal to {human_age} human years ")
#   else:
#     for i in range (user_input - 2):
#       human_age+=4
#     print(f"{user_input} dog years is equal to {human_age} human years ")
# dog()  


# user_input = input("Enter a month: ")
# dic = {"January":31,"February":29, "March":31, "April":30, "May":31, "June":30, "July":31, "August":30, "September":31, "October":30, "November":31, "December":31}
# print(dic[user_input], "Days")
# 

# import math
# a = math.pi
# print(a)
# x = math.sqrt(100)
# print(x)
# x = math.gcd(12,36)
# print(x)
# x = math.pow(5, 3)
# print(x)

# 
# def add():
  # x = int(input(""))
  # y = int(input(""))
  # print(x+y) 

# def msg():
  # print("Hi I am Festus!")

'''HW'''
# def num():
#   for i in range(16):
#     if i==3 or i ==5:
#       continue
#     else:
#       print(i)
# num()


# import string
# def validity():
#     letters = set(string.ascii_letters)
#     symbols = set(["$", "*", "@"])
#     nums = set(string.digits)

#     user_input = input("Enter password: ")
#     if 6 <= len(user_input) <= 16:  # Check the length of the password
#         has_letter = any(char in letters for char in user_input)
#         has_symbol = any(char in symbols for char in user_input)
#         has_num = any(char in nums for char in user_input)

#         if has_letter and has_symbol and has_num:
#             print("Valid")
#         else:
#             print("Invalid")
#     else:
#         print("Password length must be between 6 and 16 characters.")
# validity()


# even_num = []
# for i in range(100, 401):
#   s = str(i)
#   if (int(s[0])%2 ==0) and (int(s[1])%2 ==0) and (int(s[2])%2 ==0):
#     even_num.append(s)
# print(",".join(even_num))


# def triangel():
#   side_1 = int(input("enter first side: "))
#   side_2 = int(input("enter second side: "))
#   side_3 = int(input("enter third side: "))
#   if side_1 == side_2 == side_3:
#     print("it's a equilateral triangle")
#   elif side_1 != side_2 != side_3 and side_1!= side_3!=side_2:
#     print("it's a scalene triangle")
#   elif side_1 == side_2 != side_3 or side_1 == side_3 != side_2 or side_1 != side_2 == side_3:
#     print("it's a isosceles triangle")
# triangel()



'''class'''
#class- group of similar objects
#object- instance of class
#Types of Inheritance- #single 
                       #multilevel 
                       #multiple
                       #hierarchial
                       #hybrid
#Polymorphism
#Encapsulation
#Abstraction

# class A:
#   def display(self):
#     print("parent calss")
# class B(A):
#   def show(self):
#     print("child calss")
# obj = B()
# obj.display()
# obj.show()


# class circle:
#   def radius(self):
#     self.r= int(input("Enter Radius: "))
# class Operation(circle):
#   def operation(self):
#     a = 3.14 * self.r ** 2
#     p = 2*3.14*self.r
#     print(f"Area of circle {a}")
#     print(f"Perimeter of circle {p}")
# main = Operation()
# main.radius()
# main.operation()


#multilevel inheritance
class A:
  def display(self):
    self.h = int(input("height: "))
class B(A):
  def show(self):
    self.b = int(input("width"))
class C(B):
  def show1(self):
    area = 1/2*self.b*self.h
    print(area)
main=C()
main.display()
main.show()
main.show1()