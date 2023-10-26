# #KEYWORDimport keyword
# print(keyword.kwlist)
# help("keywords")
#
# print(help("if"))
# print (keyword.iskeyword("if"))
# print (keyword.iskeyword("ram"))
# print (keyword.iskeyword("ravi"))
#
# print (keyword.kwlist)
#
#
#
# VARIABLE
# variable_name="variable_value"
# name="ABC"
# age=24
# salary=24560.60
# print(name)
# print(age)
# print(salary)
#
#
# #many vales to multiple variable
# x,y,z="A","B","C"
# print(x)
# print(y)
# print(z)
#
# x,y,z="apple","banana","cherry"
# print(x)
# print(y)
# print(z)
#
# #one column to multiple variabe
# x=y=z="orange"
# print(x)
# print(y)
# print(z)
#
# #unpack a collection
# fruits=["apple","orange","banana"]
# x,y,z=fruits
# print(x)
# print(y)
# print(z)
#
# #output variable
# x="Python is simple"
# print(x)
#
# x="python"
# y="is"
# z="awesome"
# print(x,y,z)
# print(x+y+z)
#
# #valid variable names
# myvar="john"
# my_var="john"
# myVar="john"
# _my_var="john"
# MYVAR= "john"
# MyVar="john"
#
#
#
# DATABASE:
# #INTEGER
# #decimal formate (base 10)
# age=30
# print(age)
# print(type(age))
# print(id(age))
#
# #Binary formate(base 2)
# b=0B111
# print(b)
# print(type(b))
# print(id(b))
#
#
# #Octal form (base 8)
# b=0o1253
# print(b)
# print(type(b))
# print(id(b))
#
# #Hexa Decimal(base16)
# x=0xcab
# print(x)
# print(type(x))
# print(id(x))
#
# #Float:
# f=1.356
# print(f)
# print(type(f))
# print(id(f))
#
# #Complex
# com=5+8j
# print(com)
# print(type(com))
# print(id(com))
#
# #Boolien
# b=True
# print(b)
# print(type(b))
# print(id(b))
#
# #none type
# def m1():
#     a=10
# print(m1())
#
# #String Sequence:
# S1='Python'
# S2="Python"
# print(S1,S2)
#
# S3="""Python
#          IIHT"""
# print(S3)
# print(type(S3))
# S4="""Welcome to
#          Python Class"""
#
# print(type(S4))
#
#
# ### List type
#
# #display list
# my_list=["kavya","Lohit",25,38.45]
# print(my_list)
# print(type(my_list))
#
# #Accessing first element of list
# print(my_list[0])
#
# #slicing of list
# print(my_list[1:4])
#
# # Modify 2nd element of list
# my_list[1]="Ram"
# print(my_list[1])
# print(type(my_list))
#
# #create list using a list class
# my_list2=list(["mohit","Ramya",20,35.14])
# print (my_list2)
#
# #Create a tuple:
# my_tuple= (12, 25, 45, 33,70)
# print (my_tuple)
# print(type(my_tuple))
#
# #Accessing 3rd element of tuple:
# print(my_tuple[2])
#
# #Create a tuple using tuple class
# my_tuple2= tuple((15, 20, 55, 20, 36))
# print(my_tuple2)
#
# #slice a tuple:
# print(my_tuple2[3:6])
# print(my_tuple[2:7])
#
# #'tuple' objects does not support item assignment
#
# #Create a Dictionary:
# my_dict={1:"Ramya", 2:"Isha", 3:"Arya"}
#
# #Display Dictionary:
# print(my_dict)
# print(type(my_dict))
#
# #Create a Dictionary using Dict class:
# my_dict2=dict({1:"Hari", 2:"Varsha", 3:"Janu"})
# print(my_dict2)
#
# #Acess the value with a key:
# print(my_dict[2])
#
# #Change the value of the key
# my_dict2[1]="Suraj"
# print (my_dict2)
#
# #Create a set by using curly brackets:
# my_set={125,65,42,31,"Mohit"}
# print(my_set)
# print(type(my_set))
#
# #Create a Set by using Set class:
# my_set2= set({100,25.75,"jessa"})
# print(my_set2)
# print(type(my_set2))
#
# #Add elementto set:
# my_set.add(350)
# print(my_set)
#
# #Remove Element fom set
# my_set.remove(31)
# print (my_set)
#
# my_set={12,43,28,52,36}
# print(my_set)
# print(type(my_set))
#
# # CREATING FROZENSET:
# f_set = frozenset(my_set)
# print(type(f_set))
#
# ### BYTES
# a=[8,57,32,19,66]
# b=bytes(a)
# print(type(b))
# print(b[1])
# print(b[-2])
#
# ##Create Bytearray:
# list1=[20,6,36,57,88]
# b_array=bytearray(list1)
# print(b_array)
# print(type(b_array))
#
# # Modifying Bytearray:
# b_array[1]=76
# print(b_array[1])
#
# # Iterate bytearray:
# for i in b_array:
#     print(i, end="  ")
#
# ##Range:
# numbers=range(15,9,3)
# print(numbers)
# print(type(numbers))
#
# #Iterate range using for loop:
# for i in range(10,30,25):
#     print(i,end="  ")
#
# ###TYPE CONVERTION:
#
# ##float to integer
# pi=7.56
# print(type(pi))
#
# #converting float integer
# num=int(pi)
# print("integer number:", num)
# print (type(num))
#
# ##boolean to integer:
# flag_true=True
# flag_false=False
# print(type(flag_true))
# print(type(flag_false))
#
# #converting boolean to integer
# num1=int(flag_true)
# num2=int(flag_false)
# print("integer number:", num1)
# print(type(num1))
# print("integer number:",num2)
# print(type(num2))
#
# ##String to integer:
# S1="123"
# S2="890"
# print(type(S1))
# print(type(S2))
#
# #converting string to integer
# num1=int(S1)
# num2=int(S2)
# print("integer number:",num1)
# print (type(num1))
# print("integer number:",num2)
# print(type(num2))
#
#
# ###CONVERTING TO FLOAT
#
# ##Integer to Float
# a=258
# print(type(a))
#
# #convertion
# num=float(a)
# print("float integer:",num)
#
# ##String to float:
# S1="6573"
# S2="3456"
# print(type(S1))
# print(type(S2))
#
# #Convertion
# num1=float(S1)
# num2=float(S2)
# print("float integer:",num1)
# print(type(num1))
# print("float integer:",num2)
# print(type(num2))
#
# ##Boolean to Float:
# b=True
# print(type(b))
#
# #Convertion
# num=float(b)
# print("float integer:",num)
# print(type(num))
#
# ##CONVERTING TO STRING:
#
# #Integer to String:
# a=685
# print(type(a))
#
# #Convertion
# num=str(a)
# print("string number:",num)
# print(type(num))
#
# ##Float to String:
# b=12.53
# print(type(b))
#
# #Convertion
# num=str(b)
# print("string number:",num)
# print(type(num))
#
# ##Boolean to string:
# b=False
# print(type(b))
#
# #Convertion
# num=str(b)
# print("string number:",num)
# print(type(num))
#
# ##Complex to String:
# com=5+6j
# print(type(com))
#
# #Convertion
# num=str(com)
# print("string number:",num)
# print(type(num))
#
# ##CONVERTING TO BOOLEAN:
#
# #INTEGER TO BOOLEAN
# n=20
# print(type(n))
#
# #Convertion
# num=bool(n)
# print("boolean number:",num)
# print(type(num))
#
# n=0
# print(type(n))
#
# num=bool(n)
# print("boolean number:",num)
# print(type(num))
#
# ##STRING TO BOOLEAN:
# S1="python"
# print(type(S1))
#
# #Convertion:
# num=bool(S1)
# print("boolean number:",num)
#
# #COMPLEX TO BOOLEAN:
# com=20+5j
# print(type(com))
#
# Convertion:
# num=bool(com)
# print("boolean number:",num)
# print(type(num))
#
# ##CONVERTING TO COMPLEX:
#
# #Integer to Complex:
# a=20
# print(type(a))
#
# Convertion
# num=complex(a)
# print("complex number:",num)
# print(type(num))
#
# #FLOAT TO
#
#
# a=5.142
# print(type(a))
#
# Covertion
# num1=complex(a)
# print("complex number:",num1)
# print(type(num1))
#
# #STRING TO COMPLEX:
# S2="Pyhon"
# print(type(S2))
#
# Convertion
# num1=complex(S2)
# print("complex number:",num1)
# complex() arg is a malformed string
#
# #BOOLEAN TO COMPLEX:
# b=True
# print(type(b))
#
# Convertion:
# num=complex(b)
# print("complex number:",num)
# print(type(num))
#
#
#
# OPERATOR:
# ##AIRTHMATIC OPERATOR
#
# ##ADDITION:
# num1=int(input("enter 1st number"))
# num2=int(input("enter 2nd number"))
# res=num1+num2
# print("Addition of 2 numbers:",res)
#
# name=input("enter name")
# print(name)
#
# #SUBTRACTION:
# num1=int(input("enter 1st number"))
# num2=int(input("enter 2nd number"))
# sub=num1-num2
# print("substraction of 2 number:",sub)
#
# #MULTIPLICATION:
#
# num1=int(input("enter 1st number"))
# num2=int(input("enter 2nd number"))
# multi=num1*num2
# print("multiplication of 2 number:",multi)
#
# #DIVISION:
# num1=int(input("enter 1st number"))
# num2=int(input("enter 2nd number"))
# division=num1/num2
# print("division of 2 number:",division)
#
# FLOOR DIVISION:
# num1=int(input("enter 1st number"))
# num2=int(input("enter 2nd number"))
# floor=num1//num2
# print("floor division of 2 number:",floor)
#
# #MODULUS:
# num1=int(input("enter 1st num"))
# num2=int(input("enter 2nd number"))
# mod=num1%num2
# print("modulus of 2 number:",mod)
#
# #EXPONENTS:
# num1=int(input("enter 1st number"))
# num2=int(input("enter 2nd number"))
# expo=num1**num2
# print("exponents of 2 number:",expo)
#
# ##RELATIONAL OPERATOR:
#
# a=15
# b=6
# c=10
#
# print(a>b)
# print(a>b>c)
# print(a<=c)
# print(a>=b)
# print(c<b)
#
# #ASSIGNMENT OPERATOR:
# x=7
# y=5
#
# x+=y
# print(x)
#
# x-=y
# print(x)
#
# x*=y
# print(x)
#
# x/=y
# print(x)
#
# x//=y
# print(x)
#
# x%=y
# print(x)
#
# x**=y
# print(x)
#
# #LOGICAL OPERATOR:
#
# print(True and True)
# print(True and False)
#
#
# ##LOGICAL OPERATOR:
# #LOGICAL AND
# a=5
# b=6
#
# if a>2 and b<10:
#     both the condition is true
#      print(a*b)
#
# if a<2 and b>10:
#     print(a+b)
#
# #LOGICAL OR:
# if a>6 or b<10:
#     one condition is true
#     print(a+b)
#
# if a<6 or b>5:
#     print(a-b)
#
# #LOGICAL NOT
# actual use in code
# a=True
#
# if not a:
#     print(a)
#
# print(not 10)      #false
# print(not 0)       #true
#
# #IN OPERATOR:
# my_list=[54,56,15,25,3]
#
# number=56
# if number in my_list:
#     print("number is present")
#
# print(15 in my_list)
# print(28 in my_list)
#
# #NOT IN OPERATOR:
# print(37 not in my_list)
# print(3 not in my_list)
#
# #IDENTITY OPERATOR
# ##IS OPERATOR:
# a=25
# b=26
# c=25
#
# print(a is b)
# print(a is c)
# print(id(a))
# print(id(c))
# print(id(b))
#
# #IS NOT OPERATOR:
# print(a is not b)
# print(a is not c)
#
# ##BITWISE
# # & Bitwise and
# a=7
# b=4
# c=5
# print(a & b)   #4
# print(a &c)    #5
# print(b&c)     #4
#
# # | Bitwise or
# print(a|b)     #7
# print(a|c)     #7
# print(b |c)    #5
#
# # ^ Bitwise XOR
# print(a ^ b)   #3
# print(a ^ c)   #2
# print(b ^ c)   #1
#
# example
# a=8
# b=5
# c=7
#
# print(a&b)  #0
# print(a&c)  #0
# print(b&c)  #5
#
# print(a|b)  #13
# print( b|c)  #7
# print(c|a)   #15
#
# print(a^b)   #13
# print(a^c)   #15
# print(b^c)   #2
#
# #  Bitwise left Shift
#
#
# #>> Bitwise right shift
# print(5>>2)
#
# print(4>>2)
#
#
#
# ##AIRTHMETIC OPERATORS:
#
# #ADDITION(+):
#
# num1=int(input("enter the 1st number"))     #58
# num2=int(input("enter the 2nd number"))     #97
# add=num1+num2
# print("Addition of 2 numbers:",add)         #155
#
# #SUBTRACTION(-):
# num1=int(input("enter the 1st number"))    #98
# num2=int(input("enter the 2nd number"))    #55
# sub=num1-num2
# print("subtraction of 2 numbers:",sub)     #43
#
# #MULTIPLICATION(*):
# num1=int(input("enter 1st number"))         #57
# num2=int(input("enter 2nd number"))         #98
# multi=num1*num2
# print("multiplication of 2 number:",multi)     #350
#
# #DIVISION(*):
# num1=int(input("enter 1st number"))       #128
# num2=int(input("enter 2nd number"))       #24
# div=num1/num2
# print("division of 2 number:",div)         #5.3333
#
# #FLOOR DIVISION(//):
# num1=int(input("enter 1st number"))       #124
# num2=int(input("enter 2nd number"))       #12
# floor=num1//num2
# print("floor division of 2 number:",floor)   #10
#
# #MODULUS(%):
# num1=int(input("enter 1st number"))   #265
# num2=int(input("enter 2nd number"))   #12
# mod=num1%num2
# print("modulus of 2 number:",mod)      #1
#
# #EXPONENTS(**):
# num1=int(input("enter 1st number"))     #15
# num2=int(input("enter 2nd number"))     #3
# expo=num1**num2
# print("exponets of 2 number :",expo)    #3375
#
# ##RELATIONAL / COMPARISION OPERATOR:
# x=36
# y=12
# z=12
# print(x>y)          #true
# print(x<z)          #false
# print(x<z>y)        #false
# a=50
# b=26
# c=50
# print(a>=b)         #true
# print(c<=b>=a)      #false
#
# ##ASSIGNMENT OPERATOR:
# a=12
# a=a+10
# print(a)          #22
#
# b=56
# a+=b
# print(a)           #78
#
# b-=a
# print(b)           #-22
#
# c=5
# b*=c
# print(b)        #-110
#
# b/=a
# print(b)       #-1.410
#
# b//=c
# print(c)       #5
#
# c%=a
# print(a)      #78
#
# b**=a
# print(b)      #1.0
#
#
# ##LOGICAL OPERATOR:
#
# # AND OPERATOR:
# a=125
# b=42
# if a>100 and b<50:
#     both condition is true
#     print(a*b)          #5250
#
# print(354 and 126)       #126
#
# # OR OPERATOR:
# c=75
# if a<100 or c>50:
#     either one operator is true
#     print(a/b)           #2.976
#
# print(125 or 320)        #120
#
# # NOT OPERATOR:
#
# if not a:
#     print(a)
#
# print(not 100)     #false
# print(not 20)      #false
#
# ##MEMBERSHIP OPERATOR:
#
# #IN OPERATOR:
# my_list=["apple","banana","grapes","orange"]
# fruits=input("enter name")
#
# if fruits in my_list:
#     print("mango" in my_list)
#
# print(my_list)
#
# #NOT IN OPERATOR:
# my_list=[25,65,120,78]
# print(58 not in my_list)    #true
# print(78 not in my_list)     #false
#
# ##IDENTITY OPERATOR:
#
# #IS OPERATOR:
# a=56
# b=39
# c=56
# print(a is b)          #false
# print(a is c)          #true
# print(id(a))           #140729843710472
# print(id(c))           #140729843710472
# print(id(b))           #140729843709928
#
# #IS NOT OPERATOR:
# x=24
# y=24
# z=56
# print(x is not y)      #false
# print(z is not y)      #true
#
# ##BITWISE OPERATOR:
#
# & Bitwise AND:
# a=24
# b=56
# c=20
#
# print(a&b)    #24
# print(a&c)    #16
# print(b&c)    #16
#
# | Bitwise OR:
# x=78
# y=40
# z=32
# print(a|b)    #56
# print(a|c)    #28
# print(b|c)    #60
#
# ^ Bitwise XOR:
# m=24
# n=16
# o=64
# print(m^n)    #8
# print(m^o)    #88
# print(n^o)    #80
#
# # ~ Bitwise 1's Compliment:
# a=-17
# print(~a)     #16
#
# b=28
# print(~b)      #-29
#
# #<< Bitwise left shift:
# a=8
# b=2
# print(a<<b)   #32
# print(5<<3)   #40
# print(4<<2)   #16
#
# #>> Bitwise right shift
# print(7>>2)    #1
# print(8>>1)    #4
#
#
#
# CONTROL FLOW STATEMENT:
# #IF CONDITION:
#
# num=7
# if num<10:
#     print(num*num)
# print("next line of code")
#
# #IF-ELSE CONDITION:
# password=input("enter password")
# if password=="mycomputer":
#     print("correct password")
# else:
#     print("incorrect passward")
#
# #IF-ELIF-ELSE CONDITION:
# desg=int(input("enter number"))
# if desg==1:
#     print("admin")
# elif desg==2:
#     print("executive")
# elif desg==3:
#     print("manager")
# elif desg==4:
#     print("hr")
# else:
#     print("give valid number")
#
# #NESTED-IF-ELSE:
# num1 = int(input("enter first number"))
# num2 = int(input("enter second number"))
# if num1 >= num2:
#     if num1==num2:
#         print(num1,'is equal',num2)
#     else:
#         print(num1,'is greater than',num2)
# else:
#     print(num1,'is smaller than',num2)
#
# ##PROGRAMMS:
#
# 1.
# num1=int(input("enter 1st number"))         #68
# num2=int(input("enter 2nd number"))         #55
# if num1>=num2:
#     print(num1,"is biggest of given 2 number",num2)
# else:
#     print("false")
#
# 3. POSITIVE OR NEGATIVE
# number=input("enter numbers")       #-75
# if number>="0":
#     print("possitive")
# else:
#     print("negative")             #negative
#
# 2. ODD or EVEN:
# numbers=int(input("enter numbers"))
# if (num %  2)==0:
#     print(" it is even number")
# else:
#     print("it is odd number")
#
# 4.
# num=int(input("enter number"))
# if num==1:
#     print("one")
# elif num==2:
#     print("two")
# elif num==3:
#     print("three")
# else:
#     print("give correct number")
#
# 5.
# age=int(input("enter number"))
# if age>=18:
#     print("eligible for voting")
# else:
#     print("not eligible")
#
#
# ##ITERATIVE STATEMENT:
#
# # FOR LOOP:
# 1.
#
# for i in range(10):
#     print(i)
#
# 2.
# for num in range(1,10):
#     print(num)
#
# 3.for loop in string :
# str="welcome to python"
# for i in str:
#     print(i)
#
# 4.for loop in list :
# list=[24,36,54,69,"Hi"]
# for i in list:
#     print(i)
#
# 5.Index number of each character:
# s=input("enter some string")
# i=0
# for x in s:
#     print("The character is present at",i,"index number is:",x)
#     i=i+1
#
# 6.repeat the world 10 times:
# for i in range(10):
#     print("hello")
#
# 7.for reversing the list:
# list=[10,20,30,40]
# for i in reversed(list):
#     print(i)
#
# 8.To find even number:
# for i in range(10):
#     if i%2==0:
#         print(i)       #0 2 4 6 8
#
# 9.To find odd numbers:
# for i in range(11):
#     if i%2!=0:
#         print(i)     #1 3 5 7 9
#
# 10.To find reverse number between 0 to 10:
# for i in range(10,0,-1):
#     print(i)                       #10 9 8 7 6 5 4 3 2 1
#
# 11.To find the sum from 0 to 22:
# sum=0
# for i in range(0,22,2):
#     sum=sum+i
#     print(sum)                    #110
#
# 12.To calculate square of each element:
# num=[1,2,3,4,5,6]
# for i in num:
#     square=i**2
#     print("Square of the number",i,"is:",square)      #square of the number 6 is:36
#
# 13.calculate the average number of list of the number:
# numbers=[10,20,30,40,50,60]
# sum=0
# for i in numbers:
#     sum=sum+i
# list_size=len(numbers)
# print(list_size)
# avg=sum/list_size
# print("average number of list is:",avg)         #35.0
#
# list=eval(input("enter list"))
# for i in list:
#     print(i)
#
# #FOR LOOP USING IF-ELSE CONDITION:
# 1. To find even & odd numbers:
# for i in range(1,11):
#     if i%2==0:
#         print("Even number is",i)            #Even number is 2
#     else:
#         print("Odd number is",i)             #Odd number is 3
#
# 2.use else block to display "Done" after execution of number:
# for i in range(1,6):
#     print(i)
# else:
#     print("Done")                         #1 2 3 4 5 DOne
#
# 3.Reverse the given number list:
# list=[10,20,30,40,50,60]
# for i in reversed(list):
#     print(i)              #60 50 40 30 20 10
#
# Print reversed number using for loop:
# num=5
# start=5
# stop=-1
# step=-1
# for num in range(num,-1,-1):
#     print(num)             #5 4 3 2 1
#
# #ENUMERATE FUNCTION:
# num=[4,5,8,9,7,3]
# for i,v in enumerate(num):
#     print("numbers[",i,']=',v)       #number [0]=4
#     print(i,v)           #0 4
#
# 2
# numbers=[1,2,3,4,5]
# size=len(numbers)
# for i in range(size):
#     print("Index:",i," ","value",numbers[i])             #Index: 0   value 1::Index: 1   value 2::Index: 2   value 3::Index: 3   value4 ::Index: 4   value 5
#
#
# ##WHILE LOOP:
# #Examples:
# 1
# n=input("enter number")
# while n:
#     print("hello")
#
# 2
# x=1
# while x<=10:
#     print(x)
#     x=x1
#
# 3
# number=[1,2,3,4]
# size=len(number)
# for i in range(size):
#     print("Index:",i," ","value:",number[i])
#
# 4
# n=int(input("enter numbers"))                  # 25
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("The sum of 1st",n,"number is:",sum)       #325
#
# 5
# name=""
# while name !="Python":
#     name=input("enter name")
# print("thanks for confirmation")
#
# 6 To print hello 10 times:
# n=0
# while n<10:
#     print("Hello")
#     n=n+1
#
#
# ##ASSIGNMENTS ON LOOP:
#
# 1.Print first 10 natural number by using while loop:
# i=1
# while i<11:
#     print(i)
#     i=i+1                     #1 2 3 4 5 6 7 8 9 10
#
# 2.Print following pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#        print(j,end=" ")
#     print(" ")
#
# 3.Calculate th sum of all the numbers from 1 to given number:
# sum=0
# num=int(input("enter number"))          #22
# for i in range(num):
#     sum=sum+i
#     print("The Sum is:",sum)            #231
#
# 4.Print multiplication of given number:
# number=int(input("enter number"))          #12
# print("multiplication of given number")
# for i in range(1,11):
#     count=number*i
#     print(number,'*',i,'=' ,count)         #12 * 1 = 12 ;12 * 2 = 24 ;12 * 3 = 36 ;12 * 4 = 48 ;12 * 5 = 60.........
#
# 5. display the list using loop
# list1=[12,75,150,180,145,525,50]
# for i in list1:
#     if i>500:
#         break;
#     if i>150:
#         continue;
#     if i%5==0:
#         print(i)                  #75 150 145
#
#
#
# 6.count total number of digit in a number:
# number=int(input("Enter number"))
# count=0
# while number>0:
#     count=count+1
#     number=number//10
#     print("the total number of digit is:",count)
#
# 7.print the following pattern:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# rows =5
# for i in reversed(range(1,rows+1)):
#     for j in reversed(range(1,i+1)):
#         print(j, end=" ")
#     print(" ")
#
# 8.print the list in reverse order by using loop:
# list=[10,20,30,40,50]
# for num in reversed(list):
#     print(num)                                 #50 40 30 20 10
#
# 9.display number from -10 to -1 using for loop:
# for i in range(-10,-0,1):
#     print(i)                                  #-10 -9 -8 - 7 -6 -5 -4 -3 -2 -1
#
# 10.Use else block to display a message "Done" after successful execution of for loop:
# for i in range(1,10):
#     print(i)
# else:
#     print("Done")                                 #1 2 3 4 5 6 7 8 9 Done
#
# 11. Write a program to display all prime numbers within a range:
# start=10
# end=50
# print("Prime number b/n",start ,"and", end ,"are")
#
# for num in range (start,end+1):
#     all prime number are greater than 1
#     if number is less than or equal to 1,it is not prime
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 break
#         else:
#             print(num)                             #11 13 17 19 23 29 31 33 37 39 41 43 47
#
# 12.Display Fibonacci series upto nth term:
# num,num1=0,1
# print("Fibonacci sequence")
# for i in range(10):
#     print(num,end=" ")
#     res=num+num1
#     num=num1
#     num1=res                                    #0 1 1 2 3 5 8 13 21 34
#
# 13.Find the factorial of given number
# num=int(input("Enter the number"))
# factorial=1
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)
#
# 14.Reverse the given integer:
# num = 75642
# reversed_num = 0
#
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
#
# print("Reversed Number: " + str(reversed_num))              #24657
#
# 15. Use the loop to display elements from a given list present at odd index position:
# my_list=[10, 20,30,40,50,60,70,80,90,100]
#
# for i in my_list[0::2]:
#     print(i,end=" ")                    #10 30 50 70 90
#
# 16.Calculate the cube of all number from 1 to a given number:
# i=1
# num=int(input("Enter number"))
# for i in range(1,num+1):
#     cube=i**3
#     print("Cube of ",i,"is:",cube)
#
# 17.Find the sum of the series upto n terms
# sum=0
# n=int(input("enter number"))
# for i in range(n):
#     sum=sum+n
#     print("Sum of",i ,"is:",sum)
#
# 18.Print the following pattern:
# write a program to print the following start pattern using the for loop:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print(" ")
# for i in reversed(range(1,rows+1)):
#     for j in reversed(range(1,i+1)):
#         print("*",end=" ")
#     print(" ")
#
#
#
#
# STRING FUNCTION:
# ## STRING FUNCTION:
# # Using single quotes:
# str='Hello Word'
# print(str)                                 # Hello Word
#
# #Using double quotes:
# str1="Welcome to IIHT"
# print(str1)                                 #Welcome to IIHT
#
# #Using triple quotes:
# str2='''Triple quotes are generally used for
#        represent the multiline or
#         doosting'''
# print(str2)
#
# ##STRING INDEX:
# str="Function"
# print(str[0])        #F
# print(str[1])        #u
# print(str[2])        #n
# print(str[3])        #c
# print(str[4])        #t
# print(str[5])        #i
# print(str[6])        #o
# print(str[7])        #n
#
# # STRING OPERATOR:
# S1="Python"
# S2="class"
# print(type(S1))                             #class str
# print(type(S2))
# print(S1+S2)                                #Pythonclass
# print(S1*3)                                 #PythonPythonPython
# print(S1[2])                                #t
# print(S1[:])                                #Python
# print("o" in S1)                            #True
# print('t' not in S1)                        #False
# print(S1[3])                                #h
# print(S1[2:4])                              #th
# print(r'c://python37')                      #c://python
# print("the string str:%s"%(S1))             #the string str:Python
#
# ##==SLICE OPERATOR:
# str="Welcome to python class"
#
# #positive slice:
# start 0th index to end:
# print(str[0:])                              #Welcome to python class
# start 1st index to 5th index:
# print(str[1:5])                              #elco
# starts 2nd index to 3rd index:
# print(str[2:4])                              #lc
# starts 0th to 2nd index:
# print(str[:3])                                #Wel
# start 4th to 6th index:
# print(str[4:7])                               #ome
#
# #negative sclice:
# str="Welcome to python class"
# print(str[-1])                              #s
# print(str[-3])                              #a
# print(str[-2])                              #s
# print(str[-4:-1])                           #las
# print(str[-7:-2])                           #n cla
#
# Reversing the given string:
# print(str[::-1])                            #ssalc nohtyp ot emocleW
# print(str[-15])                              #t
#
# ##==FORMATING STRING:
# #Using curly braces:
# print("{} and {} both are the best friend ".format("Davan","Abhilash"))         #Davan and Abhilash both are the best friend
#
# Positional arguments:
# print("{1} and {0} best players".format("Virat","Rohit"))           # Rohit and Virat best players
#
# Keyword arguments:
# print("{a},{b},{c}".format(a="Abhay",b="Geeta",c="Ricky"))           #Abhay,Geeta,Ricky
#
# 1.
# Integer=10
# float=12.253
# string="Devid"
# print("Hi I am Integer...My value is %d\nHi I am Float..."                 #Hi I am Integer...My value is 10
#       "My value is %f\nHi Iam string...."                                  #Hi I am Float...My value is 12.253000
#       "My value is %s"%(Integer,float,string))                             #Hi Iam string....My value is Devid
#
# #Integer
# print("*** Integer **")         #** Integer ***
# a=15
# b=25
# print(f"{a}")                           #15
# print(f"{a} {b}")                       #15 25
# print(f"{b} {a}")                       #25 15
#
# #Float
# print("*** Float ***")            #*** Float ***
# c=10.26
# d=9.68
# print(f"{c}")                                 #10.26
# print(f"{c} {d}")                             #10.26 9.68
# print(f"{d} NBSP {c}")                        # 9.68 NBSP 10.26
#
# #STRING
# print("*** String **")              #** String ***
# f_name = "Chota"
# l_name = "Bheem"
# print(f"{f_name}")                           #Chota
# print(f"{f_name}  {l_name}")                 #Chota Bheem
# print(f"{l_name} {f_name}")                  #Bheem Chota
#
# #INTEGER TO STRING
# name="Vardhan"
# age =18
# print(f"Hello my name is {name}")            #Hello my name is Vardhan
# print(f"{name} {age}")                        #Vardhan 18
# print(f"{age}  {name} ")                       #18 Vardhan
#
# #INTEGER
# print("** Integer **")
# num=15
# print(f"{num}")                      #15
# print(f"{num:d}")                    #15
# print(f"{num:+5d}")                  #  +15
# print(f"{num:<5d}")                  #15
# print(f"{num:<5d}")                 #15**
# print(f"{num:>5d}")                 #**15
# print(f"{num:^5d}")                  # 15
# print(f"{num:^5d}")                 #*15*
# print(f"{num:>5d}")                  #   15
#
# #FLOAT:
# print("*** Flaot **")         #** Flaot ***
# num=15.25
# print(f"{num}")                     #15.25
# print(f"{num:f}")                   #15.250000
# print(f"{num:6f}")                  #15.250000
# print(f"{num:15f}")                 #      15.250000
# print(f"{num:8.5f}")                #15.25000
# print(f"{num:>8.2f}")               #   15.25
# print(f"{num:<8.2f}")               #15.25
# print(f"{num:<8.2f}")              #15.25**
# print(f"{num:>8.2f}")              #**15.25
# print(f"{num:^8.2f}")               # 15.25
# print(f"{num:^8.2f}")              #*15.25*
#
# #STRING:
# print("***String**")              #**String***
# name ="Hulk"
# print(f"{name}")                         #Hulk
# print(f"{name:s}")                       #Hulk
# print(f"{name:8s}")                      #Hulk
# print(f"{name:<8}")                      #Hulk
# print(f"{name:<8}")                     #Hulk*
# print(f"{name:>8}")                      #    Hulk
# print(f"{name:>8}")                     #***Hulk
# print(f"{name:^8s}")                     #  Hulk
# print(f"{name:^8}")                     #Hulk*
#
# #THOUSAND SEPARATOR:
# price=1526823425
# print(f"{price:,}")                                     #1,526,823,425
# print(f"{price:,}")                                     #1,526,823,425
#
# #EXPRESSION
# print(f"{10*8}")                                          #80
#
# #EXPRESSING PERCENTAGE
# a=50
# b=3
# print(f"{a/b:.2%}")                                       #1666.67
#
# #ACCESSING ARGUMENTS? ITEMS
# value=(10,20)
# print(f"{value[0]} {value[1]}")                         #10  20
#
# #FORMAT WITH DICT:
# data={'rahul':2030, 'sonam':1500, 'dhanush':3000}
# print(f"{data['rahul']:d}  {data['sonam']:d}")               #2030  1500
#
# #CALLING FUCTION
# name="htttpshow"
# print(f"{name}")                                 #htttpshow
# print(f"{name.upper()}")                         #HTTTPSHOW
#
# #CURLY BRACES
# print(f"{10}")                                  #10
# print(f"{{10}}")                                #{10}
#
# #DATE AND TIME
# from datetime import datetime
# today=datetime(2019,10,5)
# print(f"{today}")                                #2019-10-05 00:00:00
# print(f"{today:%d-%b-%Y}")                       #05-Oct-2019
# print(f"{today:%d/%b/%Y}")                       #05/Oct/2019
# print(f"{today:%b/%d/%Y}")                       #Oct/05/2019
#
#
#
# write a programm to accept string from the key board & display its character by index wise both positive & negative:
# str="Java Point"
# print(str)                      #Java Point
#
# print(str[0:])                              #J a v a P o i n t
#                                             0 1 2 3 4 5 6 7 8
#
# print(str[::-1])                            #t   n  i  o  P   a  v  a  J
#                                             -9 -8 -7 -6 -5  -4 -3 -2 -1
#
#
# write a program to acess each char string forward and back word direction by while loop:
# def reverse_while(string):
#     Declare a string variable
#     rstring = ''
#
#     We will calculate string length
#     And subtract 1 because string index start with 0
#     length = len(string) - 1
#     We will run the loop with last string index
#     while length >= 0:
#         print('String Index: ',string[length],' - ', length)           #String index:s-7 String Index: e-6  String Index:i-5
#                                                                        String Index:h-4 String Index:c-3  String Index:e-2
#         Appending chars in reverse order                              #String Index:t-1  String Index:S-2
#         rstring = rstring + string[length]
#
#         Decrements string index by 1
#         length = length - 1
#     return rstring
#
# string = 'Stechies'
# Print Original and Reverse string
# print('Original String: ', string)                                #Stechies
# print('Reverse String: ', reverse_while(string))                  #seihietS
#
# #STRING WITH COMPARISION OPRATOR:
# str=input("enter main string")                          #our national animal is tiger
# sub=input("enter sub string")                           #national
# if sub in str:
#     print(f"{sub} is found in main string")
# else:
#     print(f"{sub} is not found in main string")                   #national is found in main string
#
# s1=input("enter main string")                                 #python
# s2=input("enter sub string")                                  #java
# if s1==s2:
#     print("both strings are equal")
# elif s1>=s2:
#     print("first string is less than second string")         # first string is less than second string
# else:
#     print("first string is greater than second string")
#
# ## Removing the space from the string:
# rstrip()=to remove the space from right hand side
#  lstrip()=to remove the space from left hand side
# strip()=to remove the space from both side
#
# city=input("enter your name of city")
# scity=city.strip()
# if scity=="Hydrabad":
#     print("Welcome to Hydrabad")
# elif scity=="Bangalore":
#     print("Hello Karnataka")
# elif scity=="Chennai":
#     print("Hi Chennai")
# else:                                                   #kerala
#     print("you enter invalid city")                     #you enter invalid city
#
# ##FIND():
#
# ##finding string there are 4 types
# find for forward direction
# rfind for backword direction
#
#
# s.find(substrig)
# Return index of first occurrence of the given number
# If it is not available then we will get -1
#
# s="Learning Python is very difficult "
# print(s.find("Python"))                            # 9
# print(s.find ("java"))                             #-1
# print(s.find("r"))                                 #3
# print(s.rfind("r"))                                #21
#
# #DISPLAY ALL POSITION OF SUBSTRING IN A GIVEN MAIN STRING
# s=input("enter main string")                       #Learning python is very difficult
# sub=input("enter sub string")                       #i
# flag=False
# pos=-1
# n=len(s)
# while True:
#     pos=s.find(sub,pos+1,n)
#     if pos==-1:
#         break
#     print("Found at position :",pos)                            #Found at position : 5
#     flag=True                                                   #Found at position : 16
# if flag==False:                                                #Found at position : 25
#     print("not found")                                          #Found at position : 28
#
# #TO COUNT THE NUMBER IN STRING:
# s="abhnabfdababnaajikab"
# print(s.count("a"))                      #7
# print(s.count("ab"))                     #5
# print(s.count("a",3,9))                  #2
#
# ##RELPACING THE WORD FROM GIVEN STMT:
# s="Learning python is very difficult"
# s1=s.replace("python","java")
# print(s1)                                   #Learning java is very difficult
# print(id(s1))                               #2078854704752
# print(id(s))                                #2078852411824
#
# #SPLIT
# we can split the given string acc to specified saparetor by using split method
# SYNTAX ; l.split(separator)
# s="learning python is very easy"                       #learning
# l=s.split(" ")                                         #python
# for i in l:                                            #very
#     print(i)                                           #easy
#
# l=s.split("-")
# for i in l:
#     print(i)                                          #learning python is very easy
#
# s="22-02-2023"
# l=s.split("-")                                 #22
# for i in l:                                    #02
#     print(i)                                   #2023
#
# JOINING
# we can join  group of  the string (list or tuple) write a given separator.
# separator
# s=separator.join(group of string)
#
# t=('mango','apple','orange')
# l=" :: ".join(t)
# print(l)                                     #mango :: apple :: orange
#
# CHANGING CASE:
# s="Dehli is the capital of India"
# print(s.upper())                                 #DEHLI IS THE CAPITAL OF INDIA
# print(s.lower())                                 #dehli is the capital of india
# print(s.title())                                 #Dehli Is The Capital Of India
# print(s.swapcase())                              #dEHLI IS THE CAPITAL OF iNDIA
# print(s.capitalize())                            #Dehli is the capital of india
#
# CHECKING STARTING AND ENDING PART OF STRING:
#
#
# Python content  the following methods for this purpose
# 1.s.startwith(substring)
# 2.endswith(substring)
#
# s="learning python is very easy"
# print(s.startswith("learning"))                       #True
# print(s.startswith("very"))                           #False
# print(s.endswith("easy"))                             #True
# print(s.endswith("is"))                               #False
#
# # TO CHECK TYPES OF CHARATOR PRESENT IN A STRING
# print("jaVa1256".isalnum())                    #True
# print("national Bird".isalpha())               #False
# print("125600".isdigit())                      #True
# print("124li".islower())                       #True
# print("Flag".istitle())                        #True
# print("MS SQL".isupper())                      #True
# print(" like".isspace())                       #False
# print(" ".isspace())                           #True
#
# #BY USING USER INPUT
# s=input("enter any character")
# if s.isalnum():
#     print("alpha numeric char")
#     if s.isalpha():
#         print("Alphabet character")
#         if s.islower():
#             print("Lower case Alphabet Character")
#         else:
#             print("Upper case Alphabet Character")
#     else:
#         print("It is digit" )
# elif s.isspace():
#     print("it is space char")
# else:
#     print("no space special char")
#
# #1.WRITE A PROGRAM TO REVERSE A GIVEN STRING
# str=input("enter the string")
# for i in reversed (str):
#     print(i)
# print(str[::-1])                  #emoclew
#
# #2.PROGRAM TO REVERSE  THE ORDER OF SENTENCE:
#
# s=input("enter the sentence")
# l=s.split()
# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i])
#     i=i-1
# res=" ".join(l1)                                 #tiger is a national animal
# print(res)                                       #animal national a is tiger
#
#
# #3. PROGRAM TO REVERSE INTERNAL CONTENT OF EACH WORD
# str=input("enter the sentence")
# print("original string is :",str)                        #original string is : python is very easy
# l=" ".join(reversed(str))
# print("the reversed string of string is :",l)            #the reversed string of string is : y s a e   y r e v   s i   n o h t y p
#
#
# #4.WRITE A PROGRAM TO PRINT CHAR AT ODD POSITION & GIVEN POSITION IN STRING:
# str=input("enter the string")                                # p y t h o n
# even_char=[]                                                 # 0 1 2 3 4 5
# odd_char=[]
# for i in range(len(str)):
#     if i%2==0:
#         even_char.append(str[i])
#     else:
#         odd_char.append(str[i])
# print("Odd character:",odd_char)                           #Odd character: ['y', 'h', 'n']
# print("Even character:",even_char)                         #Even character: ['p', 't', 'o']
#
#
# #5. PROGRAM TO MERGE CHAR 2 STRING INTO A SINGLE STRING BY TAKING CHAR ALTERNATIVELY
# s1=input("enter main string")             #python
# s2=input("enter sun string")              #class
# i,j=0,0
# res=" "
# while i<len(s1) or j<len(s2):
#     if i<len(s1):
#         res=res+s1[i]
#         i+=1
#     if j<len(s2):
#         res=res+s2[j]
#         j+=1
# print(res)                             # pcyltahsosn
#
#
# #6. WRITE A PROGRAM TO SORT THE CHARACTER OF THE STRING AND FIRST ALPHABET SYMBOLS:
# s=input("enter some string")                      #B4A1D36
# s1=s2=res=""
# for i in s:
#     if i.isalpha():
#         s1=s1+i
#     else:
#         s2=s2+i
# for i in sorted(s1):
#     res=res+i
# for i in sorted(s2):
#     res=res+i
# print(res)                                        #ABD13346
#
# #7.WRITE A PROGRAM FOR THE FOLLOWING REQUIREMENT:
# S=input("enter some string")                              #a4b3c2
# res=" "
# for i in S:
#     if i.isalpha():
#         res=res+i
#         p=i
#     else:
#         res=res+p*(int(i)-1)
# print(res)                                               #aaaabbbcc
#
#
# ##ASSIGNMENT:
# ##1.WRITE A PROGRAM TO CREATE A NEW STRING MADE OF AN INPUT STRING FIRST,MIDDLE & LAST CHAR:
# str1="James"
# res=str1[0]
# #to get string size
# i=len(str1)
# # to get middle index
# mi=int(i/2)
# # to get middle char and add it to result
# res=res+str1[mi]
# to get last char and add it to results
# res=res+str1[i-1]
#
# print("New string ",res)                    #Jms
#
# ##2.WRITE A PROGRAM TO CREATE A MEW STRING MADE OF THE MIDDLE THREE CHAR OF AN INPUT:
# str1="JohnDipPeta"
# str2="JaSonAy"
# def get_middle_three_chars(str1):
#     print("Original string is",str1)
#     #first get middle index number
#     mi=int(len(str1)/2)
#
#     use string slicing to get result char
#     res=str1[mi-1:mi+2]
#     print("Middle Three char are:",res)
# get_middle_three_chars("JohnDipPeta")                                    #Middle Three char are: Dip
# get_middle_three_chars("JaSonAy")                                        #Middle Three char are: Son
#
#
# ##3.GIVE 2 STRING S1&S2 WRITE A PROGRAM TO CREATE A NEW STRING S3BY APPENDING S2 INTHE MIDDLE OF S1:
# s1="Ault"
# s2="Kelly"
# def append_middle(s1,s2):
#     print("Original string are:",s1,s2)                             #Original string are: Ault Kelly
#     #middle index numberof s1
#     mi=int(len(s1)/2)
#
#     #get char from 0to the middle index number from s1
#     x=s1[:mi:]
#     #concatenate s2 to it
#     x=x+s2
#     #append remaining char from s1
#     x=x+s1[mi:]
#     print("After appending new string in middle:",x)                #After appending new string in middle: AuKellylt
# append_middle("Ault","Kelly")
#
# ##4.WRITE A PROGRAM TO ARRANGE THE CHAR OF A STRING SO THAT ALL LOWERCASE LETTER SHOULD COME FIRST:
# str="PYnAtivE"
# print("Original string",str)                                   #Original string PYnAtivE
# lower=[]
# upper=[]
# for char in str:
#     if char.islower():
#         #add lowercase char to lower list
#         lower.append(char)
#     else:
#         #add uppercase char to upper list
#         upper.append(char)
# #Join both string
# sorted_str=" ".join(lower+upper)
# print("Result :",sorted_str)                                 #Result : n t i v P Y A E
#
# ###5.COUNT ALL LETTERS, DIGITS AND SPECIAL SYMBOLS FROM A GIVEN STRING:
# str="P@#yn26at^&i5ve"
# def fin_digits_chars_symbols(str):
#     char_count=0
#     digit_count=0
#     symbol_count=0
#     for char in str:
#         if char.isalpha():
#             char_count+=1
#         elif char.isdigit():
#             digit_count+=1
#         #if it is not letter / digit then it is a special symbol
#         else:
#             symbol_count+=1
#     print("Chars=",char_count,"Digits=",digit_count,"symbols=",symbol_count)
# print("Total counts of Chars,Digits and Symbols \n")                             # Total counts of Chars,Digits and Symbols
# fin_digits_chars_symbols(str)                                                    #Chars= 8 Digits= 3 symbols= 4
#
#
# ##6.CREATE A MIXED STRING USING THE FOLLOWING RULES:
# S1="Abc"
# S2="Xyz"
# #get string length
# S1_length=len(S1)
# S2_length=len(S2)
#
# #get length of a bigger string
# length=S1_length if S1_length>S2_length else S2_length
# res=" "
#
# #reverse S2
# S2=S2[::-1]
# #iterate string
# #S1 assending and S2 decending
#
# for i in range(length):
#     if i<S1_length:
#        res=res+S1[i]
#     if i<S2_length:
#         res=res+S2[i]
# print(res)                               #AzbycX
#
# ##7.WRITE A PROGRAM TO FIND ALL OCCURANCE OF "USA" IN A GIVENSTRING IGNORING THE CASE:
# str="Welcome to USA.usa awesome,isn't it?"
# sub_str="USA"
#
# #convert string into lowercase:
# temp_str=str.lower()
#
# #use count functon
# count=temp_str.count(sub_str.lower())
# print("The USA count is",count)                         #The USA count is 2
#
# ##8.CALCULATE THE SUM AND AVERAGE OF THE DIGITS PRESENT IN A STRING:
# str="PYnative29@#8496"
# total=0
# i=0
# for char in str:
#     if char.isdigit():
#         total+=int(char)
#         i+=1
# #aveage =sum /count of digits
# avg=total/i
# print("Sum is:",total,"Average is:",avg)                    #Sum is: 38 Average is: 6.333333333333333
#
# ##9.WRITE A PROGRAM TO COUNT OCCURANCE OF ALL CHARACTER WITHIN A STRING:
# str1="Apple"
# #create a result dictionary
# char_dict=dict()
#
# for char in str1:
#     count=str1.count(char)
#     #add/update the count  of character
#     char_dict[char]=count
# print("Results:",char_dict)                                #Results: {'A': 1, 'p': 2, 'l': 1, 'e': 1}
#
#
#
# LIST
# a=[25,12,63,12.25]
# print(a)
#
# a=list((10,36,"python",36.42,'apple'))
# print(a)
# print(type(a))
#
# l=len(list)
# print(l)
# print(a[1])
# print(a[-2])
#
# print(a[2:7])
# print(a[::-1])
#
# ADDING ELEMENT TO THE LIST:
# 1.APPEND: It will accept only one parameter and add it at the end of the list.
# my_list=[9,24,12,"Ram",6.8]
# my_list.append("Python")
# print(my_list)                    #[9, 24, 12, 'Ram', 6.8, 'Python']
#
# my_list.append([25,12,3])
# print(my_list)                    #[9, 24, 12, 'Ram', 6.8, 'Python', [25, 12, 3]]
#
# list=[]
# list.append("Python")
# list.append("is")
# list.append("simple")
# print(list)                               #['Python', 'is', 'simple']
#
#
# 2.INSERT:It is used to add the object(element) at the specified position in the list.It accept 2 parameter position and object.
# Syntax: insert=(index,object):
#
# my_list=[9,24,12,"Ram",6.8]
# my_list.insert(2,"Sham")
# print(my_list)                           #[9, 24, 'Sham', 12, 'Ram', 6.8]
#
# my_list.insert(3,[87,10.32,12])
# print(my_list)                           #[9, 24, 'Sham', [87, 10.32, 12], 12, 'Ram', 6.8]
#
# 3.EXTEND:it will accept the list of elements and add them at the end of the list.
# my_list=[9,24,12,"Ram",6.8]
# my_list.extend([24,80,"Janvi"])
# print(my_list)                                     #[9, 24, 12, 'Ram', 6.8, 24, 80, 'Janvi']
#
# # to add all elements to list upto 100 which are divisible by 10
# list=[]
# for i in range(0,101):
#     if i%10==0:
#         print(i)
#         list.append(i)
# print(list)                     #[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# TO FIND THE SQUARE TOOT OF GIVEN LIST:
# my_list=[2,3,4,5,6,7]
# for i in range(len(my_list)):
#     square=my_list[i]**2
#     my_list[i]=square
# print( "Square of given list:",my_list)                   #Square of given list: [4, 9, 16, 25, 36, 49]
#
# CREATE LIST ADDING ELEMENT TO THE LIST:
#
# s_id=[101,"hari","BE"]
# s_id.append("java")
# print(s_id)                                 #[101, 'hari', 'BE', 'java']
#
# s_id.insert(2,"A division")                 #[101, 'hari', 'A division', 'BE', 'java']
# print(s_id)
#
# s_id.extend(["lab",1,"sql",3])
# print(s_id)                                 #[101, 'hari', 'A division', 'BE', 'java', 'lab', 1, 'sql', 3]l=
#
# SPLITING THE LIST OF STRING:
# s=("Tiger is a national animal")
# l=s.split()
# print(l)                                     #['Tiger', 'is', 'a', 'national', 'animal']
#
# #FIND POSITIVE AND NEGATIVE INDEX IN THE GIVEN LIST:
# a=[10,"apple",3.15]                                                                 #10 is available at positive index: 0 and at negative index: -3
# x=len(a)                                                                            #apple is available at positive index: 1 and at negative index: -2
# for i in range(x):                                                                  #3.15 is available at positive index: 2 and at negative index: -1
#     print(a[i],"is available at positive index:",i,"and at negative index:",i-x)
#
#
# MODIFY THE ITEM OF A LIST:
# my_list=list([2,4,6,8,9,10])
#
# Modify single items
# my_list[0]=20
# print(my_list)                              #[20, 4, 6, 8, 9, 10]
#
# Modify range of items
# modify from 1st index to 4th index:
# my_list[1:4]=[40,60,80]
# print(my_list)                              #[20, 40, 60, 80, 9, 10]
#
# # Modify from 3rd index to end
# my_list[3:]=[80,90,100]
# print(my_list)                              #[20, 40, 60, 80, 90, 100]
#
# Square of the list:
# my_list=[2,4,6,8,9,10]
# for i in range(len(my_list)):
#     square=my_list[i]**2
#     my_list[i]=square
# print(my_list)
#
#
#
#
# my_list = [21, 30, 40, 50]
# my_list.pop(1)
# print(my_list)
#
#
# my_list = [21, 30, 40, 50]
# my_list.clear()
# print(my_list)
#
#
# my_list = [21, 30, 40, 50]
# del my_list
#
#
# my_list = [21, 30, 40, 50]
# del my_list[1:3]
# print(my_list)
#
# my_list = [21,4.3, 4]
# my_list.append(3)
# print(my_list)
#
# my_list = [21,4.3, 4]
# my_list.insert(1, 2)
# print(my_list)
#
# my_list = [21,4.3, 4]
# my_list.extend([25])
# print(my_list)
#
#
# my_list = [21, 30, 40, 30, 50, 30]
# for i in my_list:
#     my_list.remove(30)
# print(my_list)
#
#
#
# list comprehention
#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)
#
#
#
#
# l = [2, 3, 5, 6, 7]
# square  = [i**2 for i in l if i % 2==0]
# print(square)
#
#
#
#
#
# l = [43,34,34,65, 56],[4,66,565,75,908]
# print(l[1][2])
# for i in l:
#     print(i)
#     for j in i:
#         print(j)
#
#
#
#
#
# Reverse a list in Python
# Given:
# list1 = [100, 200, 300, 400, 500]
# for i in list1[::-1]:
#     print(i)
#
#
#
#
#
# Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list,
# then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
#
# Given:
#
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# l= [i + j for i, j in zip(list1, list2)]
# print(l)
#
#
#
#
#
# Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
# l= [i**2 for i in numbers ]
# print(l)
#
#
#
#
#
# Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# l = [i+ j for i in list1 for j in list2]
# print(l)
#
#
#
#
#
# Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
#
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for (i, j) in zip(list1,list2[::-1]):
#  print(i,j)
#
#
#
#  Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# res = list(filter(None, list1))
# print(res)
#
#
#
#
# Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List
#
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
#
#
#
#
#
#
#
# Extend nested list by adding the sublist
# You have given a nested list.
# Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
#
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# a = "h", "i", "j"
# list1[2][1][2].extend(a)
# print(list1)
#
#
#
#
# Replace list’s item with new value if found
# You have given a Python list.
# Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
#
# list1 = [5, 10, 15, 20, 25, 50, 20]
# index = list1.index(20)
# list1[index] = 200
# print(list1)
#
#
#
# Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20. Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.
#
# my_list = [5, 20, 15, 20, 25, 50, 20]
# for i in my_list:
#     try:
#         my_list.remove(20)
#     except ValueError:
#         print()
# print(my_list)
#
#
#
# s = (10,)
# print(type(s))
#
# s = ("helo",)
# print(type(s))
#
# t1 = 2, 4, 3, 53, 64, 6
# print(type(t1))
#
# t = t1[::-2]
# print(t)
#
# t1 = 2, 4, 3, 53, 64, 6, 2
# t = t1.count(2)
# a = t1.index(2)
# print(t)
# print(a)
#
#
#
# t1 = 2, 4, 3, 53, 64, 6, 43, 7, 6
# print(t1 * 3)
#
# t2 = (2, 4, 34, [3, 34, 546],(12, 345))
# print(type(t2))
#
#
#
# print(list(t1))
# print(tuple([1, 2, 3, 4]))
#
#
#
#  ##########################################  SET  *****************************************************
#
#
# set1 = {}
# print(type(set1))
# set1 = set()
# print(type(set1))
#
#
# set2 = {21, 23 , 32, 42}
# if 20  in set2:
#         print("True")
# else:
#     print("False")
#
# s3 = set((1, 2, 3, 4))
# print(len(s3))
#
#
#
# set2 = {21, 23 , 32, 42}    #add a new item
# set2.add(2)
# print(set2)
#
#
# #Create a set from list:
# list=[65, 64, 3, 4, 43, 564, 64]
# print(set(list))
#
#
# # Using empty set
# s1={}
# print(type(s1))   #empty set = dict
#
#
#
# #Creating set with initial item
# # Syntax:
# s={"item1","item2","item3"}
#
#
# # to check item in set we are using membership operator
# fruits={"banana","mango","orange","apple"}
# print( "banana" in fruits)                #True
#
# # Accessing the element in set
# fruits={"banana","mango","orange","apple"}
# for i in fruits:
#     print(i)       #apple   #banana   #mango     #orange
#
# # Adding element to set:
# fruits={"banana","mango","orange","apple"}
# fruits.add("cherry")
# print(fruits)                             #{'mango', 'apple', 'banana', 'orange', 'cherry'}
#
# Add multiple item using  Update()
#    the Update() allow us to add multiple item to the set
# fruits={"banana","mango","orange","apple"}
# grossary=("Rice","Wheat","Corn","Maida")
# fruits.update(grossary)
# print(fruits)                           #{'apple', 'Corn', 'banana', 'Rice', 'orange', 'mango', 'Maida', 'Wheat'}
# #
# fruits={"banana","mango","orange","apple"}
# fruits.update(["tomato","watermelon","Kiwi"])
# print(fruits)
#
# #Removing the item from a set
# # We can remove item from a set using remove() method.
#
# fruits={'mango', 'apple', 'banana', 'orange', 'cherry'}
# fruits.remove("apple")
# print(fruits)                   #{'orange', 'banana', 'cherry', 'mango'}
#
# # # The discard() method will not throw any error if the items you want to delete is not present in a list.
# fruits={"banana","mango","orange","apple"}
# fruits.discard("pappaya")
# print(fruits)                          #{'banana', 'orange', 'apple', 'mango'}
#
# #The pop() method remove a random item from a list and it will return the removed item.
# chocolates={"munch","park","kitkat","dairy milk"}
# chocolates.pop()
# print(chocolates)                       #{'kitkat', 'munch', 'park'}
#
# # If we are inserted in the removed item.
# fruits={"banana","mango","orange","apple"}
# removed_item=fruits.pop()
# print(removed_item)                       #mango
#
# # Clearing item in a set
# #   If we want to clear or empty the set, we use clear() method
# name={"Abhay","Nitya","Pooja","Tanu","Satya"}
# name.clear()
# print(name)                       #set()
#
# # Deleting a set
# # If we want to delete the set itself we use del() method
#
# st={"Item1","Item2","Item3","Item4","Item5","Item6"}
# del st
#
# grossary = ("Rice", "Wheat", "Corn", "Maida")
# del grossary
#
# # Converting list to set
# grossary = ("Rice", "Wheat", "Corn", "Maida")
# set=set(grossary)
# print(set)                      #{'Rice', 'Wheat', 'Corn', 'Maida'}
# print(type(set))                #<class 'set'>
#
#
# ## JOINING SET:
#  we can jion two set using 'union()' or 'update()' method
# #
# # """
# # ---UNION =this method return a new set.won't contain dupliate elements
# # """
# # Syntax
# st1={"Item1","Item2","Item3","Item4","Item5"}
# st2={"Item2","Item3","Item6","Item7"}
# st3=st1.union(st2)
# print(st3)                            #{'Item1', 'Item2', 'Item6', 'Item4', 'Item3', 'Item7', 'Item5'}
#
# veg={"Patato","Onion","Tamato","Carrot","Beans"}
# fruits={"Grapes","Longane","Guva","Pineapple","Cherry"}
# veg=veg.union(fruits)
# print(veg)
#
# # """
# #    INTERSECTION returns a set of items which are in both the set.
# # """
#
# # Syntax:
# st1={"Item1","Item2","Item3","Item4","Item5"}
# st={"Item4","Item3","Item1"}
# st3=st1.intersection(st)
# print(st3)
#
# python={'p','y','t','h','o','n'}
# dragon={'d','r','a','g','o','n'}
# set=python.intersection(dragon)
# print(set)                        #{'o', 'n'}
#
# whole_number={0,1,2,3,4,5,6,7,8,9}
# even_numbers={0,2,4,6,8}
# inter=whole_number.intersection(even_numbers)
# print(inter)              #{0, 2, 4, 6, 8}
#
# ## Checking the diff b/w two set: It returns the diff between two set
# # Syntax:
# st1={"Item1","Item2","Item3","Item4","Item5"}
# st2={"Item2","Item4","Item6"}
# st3=st2.difference(st1)            #{'Item6'}
# st4=st1.difference(st2)            #{'Item5', 'Item1', 'Item3'}
# print(st3, st4)
#
# whole_number={0,1,2,3,4,5,6,7,8,9}
# even_numbers={0,2,4,6,8}
# number=whole_number.difference(even_numbers)
# print(number)                     #{1, 3, 5, 7, 9}
# .
#
# python={'p','y','t','h','o','n'}
# dragon={'d','r','a','g','o','n'}
# diff=python.difference(dragon)
# diff1=dragon.difference(python)
# print(diff1)                      #{'g', 'a', 'r', 'd'}
# print(diff)                       #{'p', 'y', 'h', 't'}
#
# ## Finding synmetric difference between 2 set:
# # It returns the synmetric diff b/w 2 sets .It means that it return a set contain all elements.
#
# # Syntax:
# st1={"Item1","Item2","Item3","Item4","Item5"}
# st2={"Item2","Item4","Item6"}
# # it means (A\B)and(B\A)
# st=st2.symmetric_difference(st1)
# print(st)                     #{'Item3', 'Item1', 'Item6', 'Item5'}
#
# whole_number={0,1,2,3,4,5,6,7,8,9}
# some_number={1,3,5,7,0,23,3}
# st=some_number.symmetric_difference(whole_number)
# print(st)                                #{2, 4, 6, 8, 9}
# #
# python={'p','y','t','h','o','n'}
# dragon={'d','r','a','g','o','n'}
# diff=python.symmetric_difference(dragon)
# print(diff)                                #{'r', 'g', 't', 'p', 'y', 'd', 'h', 'a'}
#
#
#
#
# ## Checking subset and super set:
# # """
# # A set can be a subset or superset of other set:
# #   Subset:_issubset()- it is used to find weather a set is a subset of another set
# #   superset:_issuperset()-
# # """
#
#
#
# # # Syntax:
# st1={"Item1","Item2","Item3","Item4","Item5"}
# st2={"Item2","Item4"}
# s3=st2.issubset(st1)
# s4=st1.issuperset(st2)
# print(s3, s4)
#
#
# python={'p','y','t','h','o','n'}
# dragon={'d','r','a','g','o','n'}
# set=python.issuperset(dragon)
# set2=dragon.issubset(python)
# print(set)                     #False
# print(set2)                    #False
#
#
#
#
# ##Joining Sets
# # """* If 2 sets do not have a common item
# #    *or items call them disjoint set
# #    *we can check if 2 sets are joint or disjoint using _isdisjoint() method
# # """
#
#
#
# # # Syntax:
# st1={"Item1","Item2","Item3","Item4","Item5"}
# st2={"Item2","Item4"}
# s1=st1.isdisjoint(st2)
# print(s1)              #False
#
# ####even_num={0, 2, 4, 6, 8}
# #### odd_num={1, 3, 5, 7, 9}
# num=even_num.isdisjoint(odd_num)
# print(num)                  #True
#
# ##Sorting the set
# set1={20, 4, 6, 9, 15}
# sorted_list=sorted(set1)
# print(sorted_list)           #[4, 6, 9, 15, 20]
#                              #{4, 6, 9, 15, 20}
#
#
#
# # write a program to eliminate duplicate elements present in the list
# number=[2,5,8,17,36,5,2,9,17,11]
# def Remove(number):
#     list=[]
#     for i in number:
#         if i not in list:
#             list.append(i)
#     return(list)
# print(Remove(number))                    #[2, 5, 8, 17, 36, 9, 11]
#
#
# # write a program to print diff vowels present in a given word
# stmt= input("Enter any statement : ")           #Welcome to python class
# vowels =['a','e','i','o','u']
# list1=[]
# for x in stmt:
#     if (x in vowels and x not in list1):
#         list1.append(x)
# print("Vowels present in given statement : ",list1)
#
#
#
# a = 10
# b = 3
# print(a & b) (*)
# print(a | b)   (+)
# print(a^b)     (+)
# print(~20)
# print(10<<2)
# print(5>>3)
#
#
#
#
# a = [1, 2, 3, 5, 7, 8, 4, 5 , 3]
# a.sort()
# print(a)
#
# a = sorted([1, 2, 3, 5, 7, 8, 4, 5, 3])
# print(a)
#
#
# a = sorted("This is a test string from Andrew".split())
# print(a)
#
#
# PATTERN
# length = 3
#
# for i in range(length):
#     for j in range(length):
#          if(i == 0 or i == length - 1 or j == 0 or j == length - 1):
#             print('*', end = ' ')
#          else:
#             print(' ', end = ' ')
#     print()
#
#
#
#
# for i in range(3):
#     for j in range(3):
#         if (j == 0 or j == 2):
#           print("*", end=" ")
#         else:
#             print("           ", end=" ")
#     print()
#
#
#
# check weather person is eligible to vote or not
#
# n = 18
# # a = int(input("enter age:"))
# # if (a>=n):
# #     print("eligible to vote")
# # else:
# #     print("not eligible to vote")
#
#
# 1.Write a program to find biggest of two given number
#
# a = int(input("enter 1st numebr: "))
# b = int(input("enter 2nd numebr: "))
# if a>b:
#     print(a, " is bigger than ", b)
# else:
#     print(b, "is bigger than", a)
#
#
# 3.Check whether given number is positive or negative
#
# a = int(input("enter a number: "))
# if a>0:
#     print("it is positive")
# elif a== 0:
#      print("it is zero")
# else:
#     print("it is negative")
#
#
# avarage of numbers
# numbers = [10, 20, 30, 40, 50]
# for i in numbers:
#     avarage = sum(numbers)/len(numbers)
# print(avarage)
#
#
#
# Write a program to take single digit number from keyboard and print it's value in a English word.
# n = int(input("enter a number: "))
# if n==0:
#     print("Zero")
#
# elif n==1:
#     print("One")
# elif n==2:
#     print("Two")
# elif n==3:
#     print("Three")
# elif n==4:
#     print("Four")
# elif n==5:
#     print("Five")
# elif n==6:
#     print("Six")
# elif n==7:
#     print("Seven")
# elif n==8:
#     print("Eight")
# elif n==9:
#     print("Nine")
# else:
#     print("not a digit")
#
#
#
# name = input("enter a name: ")
# while name== "erik":
#     print('correct name ')
#     break
# else:
#     print("incorrect name")
#
#
# mulltiplication table
# a = int(input("enter a number: "))
# for i in range(1, 11):
#     print(i,"x", a,":",i*a)
#
#
# Print First 10 natural numbers using while loop
#
# a = 1
# while(a<=10):
#     print(a)
#     a+=1
#
#
#
# Print the following pattern
# Write a program to print the following number pattern using a loop
#
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()
#
#
#
# Calculate the sum of all numbers from 1 to a given number
#
# s = [1, 24, 4 ,4,6]
# for i in s:
#     a = sum(s)
#     print(a)
#     break
#
#
#
# Write a program to print multiplication table of a given number
#
# a = int(input("enter a number: "))
# for i in range(1, 11):
#     b = (i*a)
#     print(a, "x", i, "=" ,b)
#
#
#
#
# Display numbers from a list using loop
#
# num = [12, 75, 150, 180, 145, 525, 50]
# b = []
#
# for i in num:
#     if i>150:
#       if i>500:
#           break
#       continue
#     if i % 5 ==0:
#       b.append(i)
# print(b)
#
#
# Count the total number of digits in a number
#
#
# d = 123
# print(len(str(d)))
#
#
#
# Print the following pattern
# Write a program to use for loop to print the following reverse number pattern
#
# for i in range(0, 6):
#     for j in range(5-i, 0, -1):
#         print(j, end=" ")
#     print()
#
#
# Print list in reverse order using a loop
# Given:
#
# list1 = [10, 20, 30, 40, 50]
# print(list1[::-1])
#
#
#
#  Reverse a given integer number
# Given:
#
# a = 76542
# print(str(a)[::-1])
#
#
# Display numbers from -10 to -1 using for loop
#
# for i in range(-10, 0):
#     print(i)
#
#
# Use else block to display a message “Done” after successful execution of for loop
#
# for i in range (1, 10):
#     if 1==0:
#         print("nah")
#     else:
#         print("DONE")
#         break
#
#
# Write a program to display all prime numbers within a range
#
# for i in range(1, 10):
#     if i>1:
#         for j in range(2, i):
#             if (i%j) == 0:
#                 break
#             else:
#              print(i)
#              break
#
#
#
#
# Display Fibonacci series up to 10 terms
#
# num = 10
# n1, n2 = 0, 1
# sum = 0
# if num<=0:
#  print("enter a number greater than 0")
# else:
#   for i in range(0, num):
#      n1 = n2
#      n2 = sum
#      sum = n1 + n2
#      print(sum)
#
#
#
# Find the factorial of a given number
#
# a = int(input("enter a number: "))
# factorial = 1
# if a<0:
#     print("please enter digit greater than 0")
# else:
#     for i in range (1, a+1):
#         factorial*=i
#     print(factorial)
#
#
#
#
# Reverse a given integer number
#
# Use a loop to display elements from a given list present at odd index positions
#
# Given:
#
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(1, len(my_list), 2):
#  print(i)
#
#
#
#
#
# Calculate the cube of all numbers from 1 to a given number
#
# a = int(input("enter a number: "))
# b = a**3
# print(b)
#
#
#
#
#
# Find the sum of the series upto n terms
#
#
#
#
#
#
#
#
#
#
# rint the following pattern
# Write a program to print the following start pattern using the for loop
#
# for i in range (1, 6):
#     for j in range (1, i+1):
#         print("*", end=" ")
#     print()
# for i in range (1, 6):
#     for j in range(5-i, 0, -1):
#         print("*", end=" ")
#     print()
#
#
#
#
# def add_number (num1, num2):
#     return num1 + num2
# def multiply_number (num1, num2):
#     return num1 * num2
# number1 = int(input("enter 1st number: "))
# number2 = int(input("enter 2nd number: "))
# sum_result = add_number(number1, number2)
# print("sum =", sum_result)
# product_result = multiply_number(number1, number2)
# print("product =", product_result)
#
#
#
#
#
# names  = ["raima", "festus", "ribin", "festus"]
# names.remove("raima")
# print(names)
#
# names.pop(0)
# print(names)
#
# del names[2]
# print(names)
#
#
# names.reverse()
# print(names)
#
#
# names.sort()
# print(names)
#
# count = names.count("festus")
# print(count)
#
#
#
#  ###############################LIST##########################################
#
#
#
#
# l1 = [10, 20, 30, 40, 30]
# l2 = [60, 70, 80, 60]
# if 20 in l1:
#  print("available!")
# else:
#     print("noo")
# if 20 not in l2:
#     print("available here too!")
# else:
#     print("noo")
#
# print(l1  + l2)
# print(l1 * 5)
# print(l1[1])
# print(l1[1:6:2])
# print(len(l1))
# print(l2.count(60))
# print(l1.index(30))
# print(l1.index(30,3, 6)) #giving poditions
# print(min(l1))
# print(max(l1))
# print(l1.remove(20))
# print(l1)
# print(l1.pop(2))
# print(l1)
# print(l2.clear())
# print(l2)
# print(l2.copy())
# print(l2)
# l1.append(2)
# print(l1)
# l1.append([1, 2, 3])
# print(l1)
# l1[2]= 10
# print(l1)
#
#
#
#
#
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)
#
#
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
#
# k = [i + j for i,j in zip(list1,list2)]
# print(k)
#
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
# square = [i**3 for i in numbers]
# print(square)
#
#
#
#
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# a = [i + j for i in list1 for j in list2]
# print(a)
#
#
#
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for i, j in zip(list1, list2[::-1]):
#     print(i, j)
#
#
#
#
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# a = list(filter(None, list1))
# print(a)
#
#
#
#
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
#
#
#
#
#
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# list1[2][1][2].extend(["h", "i", "j"])
# print(list1)
#
#
# list1 = [5, 10, 15, 20, 25, 50, 20]
# a = list1.index(20)
# list1[a]= 200
# print(list1)
#
#
#
# list1 = [5, 20, 15, 20, 25, 50, 20]
# a= [*set(list1)]
# print(sorted(a))
#
#
# n = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# for i in n:
#     print(i)
# to present elemnet in matrix wise
#
# for i in range(len(n)):
#     for j in range(len(n[1])):
#         print(n[i][j], end="  ")
#     print()
#
#
# l = [2, 33, 654, 657, 4, 654, 23, 65]
# print(sorted(l))
# l.sort(reverse=True)
# print(l)
#
#
# ############################TUPLE#################################################
#
#
# tuple1 = (10, 20, 30, 40, 50)
# a = tuple1[::-1]
# print(a)
#
# t1 = ("Orange", [10, 20, 30], (5, 15, 25))
# p = t1[1][1]
# print(p)
#
# tuple1 = (50,)
# print(tuple1)
# print(type(tuple1))
#
# tuple1 = (10, 20, 30, 40)
# a = tuple1[0]
# b = tuple1[1]
# c = tuple1[2]
# d = tuple1[3]
# print(b)
#
# tuple1 = (11, 22)
# tuple2 = (99, 88)
# tuple1, tuple2 = tuple2, tuple1
# print(tuple2)
# print(tuple1)
#
#
#
# tuple1 = (11, 22, 33, 44, 55, 66)
# a = tuple1[3:5]
# print(a)
#
#
# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0] = 222
# print(tuple1)
#
#
#
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# a= tuple(sorted(list(tuple1), key=lambda x:x[1]))
# print(a)
#
#
# tuple1 = (50, 10, 60, 70, 50)
# a = tuple1.count(50)
# print(a)
#
#
#
# listChar = [45, 45, 45, 45]
#
# nTemp = listChar[0]
# bEqual = True
#
# for item in listChar:
#     if nTemp != item:`
#         bEqual = False
#         break;
#
# if bEqual:
#     print("True")
# else:
#     print("False")
#
#     #or#
#
# if(len(set(listChar))==1):
#     print("True")
# else:
#     print("False")
#
#
#
# ##########################SET#######################################################3
#
#
#
#
# write  a program to eliminate duplicate elements present in the list
#
# num = [1, 2, 2, 2, 3, 4, 5, 5, 4, 7]
# num1 = [*set(num)]
# print(num1)
#
# write a program to check vovels
#
# a = input("enter a letter: ")
# vovels = "a", "e", "i", "o", "u"
# for i in a:
#     if i in vovels:
#         print("it is a vovel")
#     else:
#         print("not a vovel")
#
#
#
#
#
#
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
#
# b= sample_set.union(sample_list)
# print(b)
#
#
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# a = set1.intersection(set2)
# print(a)
#
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.union(set2))
#
#
#
#
# set1 = {10, 20, 30, 40, 32}
# set2 = {20, 40, 50, 40, 55}
# print(set1.difference(set2))
# #
# #
#
#
# set1 = {10, 20, 30, 40, 50}
# removea_set = {10, 20, 30}
# a= set1.symmetric_difference(removea_set)
# print(a)
#
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.symmetric_difference(set2))
#
#
#
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# print(list(set1.intersection(set2)))
#
#
#
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.symmetric_difference(set2))
#
#
#
#

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.intersection(set2))
# print(set1)
# set1.intersection_update(set2)
# print(set1)
#
# print(set1)

#
#
#
#
# frozen set are immuttable version of set
#
#
#
#
#
# #####################dictionary#######################################
#
#
# write a program to enter name and persentage of marks kn a dict and display information on the screen
# dict1 = {}
# dict1["marks: 10%"] = "erik"
# dict1["marks: 50%"] = "rahul"
# dict1["marks: 40%"] = "raima"
# dict1["marks: 30%"] = "ribin"
# dict1["marks: 20%"] = "ebin"
# print(dict1)
#
# d = {"name": int(input("enter name:")), "mark": 21}
# d1 = {"name": "rahul", "mark": "30%"}
# d2 = {"name": "ribin", "mark": "30%"}
# d3 = {"name": "raima", "mark": "40%"}
# d4 = {"name": "ebin", "mark": "50%"}
#
# print(d)
# print(d1)
# print(d2)
# print(d3)
# print(d4)
#
#
#
# rec = {}
# num_student = int(input("enter number of students: "))
# i = 1
# while i<=num_student:
#      name = input("enter a name: ")
#      mark = (input("enter marks: "))
#      rec[name]= mark
#      i+=1
# print("name of students","\t", "% of marks" )
# for x in rec:
#     print("\t",x,"\t\t\t",rec[x])
#
#
#
#
#
# dict with one entry
# a = {"erik":19,"place": ['bnglr']}
# print(a)
#
#
# #dict with one entry
# d = {"name":"festus", "age": 19}
# print(d)
# print(d["name"])     #accesing data
#
#
# print(d.get("age"))     #using get
#
# d["email"] = "Festus.Hoopa@gmail.com"      #adding new entry to dict
# print(d)
#
#
# a = {"erik":19,"place": ['bnglr'], 10:"character"}        #creating dict with value as a dict, stringa n integer
# print(a)
#
#
# b = dict({("name", "festus"), ("age", 19), ("sex", "M")})       #create a dict from sequence havin each item as pair
# print(b)
#
#
#
#
# add items to the dict, #2 ways
#
# a = {"erik":19,"place": 'bnglr'}
# a.update({"ribin":"anscer", "raima":"sister"})
# print(a)
#
# a["rahul"]="robotics"
# print(a)
#
# #modyfying
# a["erik"] = "is my name"
# print(a["erik"])
#
#
# numbers = {2, 4, 5, 1}
# sq = {x :x**2 for x in numbers if x%2==0}
# print(sq)
#
#
# dict1 = {"c" : 2, "a": 1, "b":3}
# dict2 = {"kelly":4, "emma": "23 years old",}
# print(sorted(dict1))
# print(sorted(dict1.values()))
# print(sorted(dict1.keys()))
# print(sorted(dict1.items()))
#
# #copy
# l =dict1.copy()
# print(l)
# dict2 = dict1
# print(dict2)
#
# joining two dicts(using update)
# dict1.update(dict2)
# print(dict1)
# print(dict1["emma"])
#
# # (using **kwargs)- we can join more than 2 dicts
# a = {**dict1, **dict2}
# print(a)
#
#
# cheking a key pressent or not
# name = "emma"
# if name in dict2:
#     print(dict2[name])
# else:
#     print("key name not found")
#
#
#
#
# modifying
# dict2["emma"] = "22 years old"
# print(dict2)
#
#
# dict2.update({"emma": "21 yrears old"})
# print(dict2)
#
#
#
# each dict will store value of single student
# jessa = {"name":"jessa", "age":19,"country":"India" }
# kelly = {"name":"jessa", "age":20,"country":"Canada" }
# martha = {"name":"jessa", "age":21,"country":"Australia" }
#
# #nested dict
# class1 = {"student1": jessa, "student2":kelly, "student3":martha}
#
# #get students name and age
# print(class1["student1"]["name"])
# print(class1["student1"]["age"])
#
#
# #display each students deatails
# for key, values in class1.items():
#     print(key)
#     for i, j in values.items():
#         print(i, ":", j)
#     print()
#
#
# #adress of person
# address = {"state":"kerala", "city":"ekm"}
#
# #storing person d3etails with adress as a nested dict
# person = {"name": "festus", "class": 12, "address":address}
#
# # print(person)
# # #print city
# # print("city :", person["address"]["city"])
#
# #get all details in the dict
# for key, value in person.items():
#     if key == "address":
#         print("\n")
#         print("person address")
#         for i, j in value.items():
#             print(i, ":", j)
#     else:
#         print(key, ":", value)
#
#
#
#
# write a progrm to take dictionary from the keyword and print the sum of values
# d = eval(input("enter dictionary: "))
# a = sum(d.values())
# print(a)
#
#
#
# # write a program to find number of occurence of each letter presesntin the given string
# # #
# a = "pythonissimple"
# out = {x : a.count(x) for x in set(a)}
# print(out)
#
# write a program to find the no: of occurrence of each vowel present in the given string
#
# input1 = input("enter a string: ")
# input1 =  input1.casefold()
# vowels = "aeiou"
# a= {}.fromkeys(vowels, 0)
# for ch in input1:
#     if ch in vowels:
#         a[ch] +=1
# for vowels in a:
#     print(vowels, "=", a[vowels])
#
#
#
# Project
#
# print("\t")
# print("festus",",", "raima",",", "ribin", "-","select a name from it to know the mark")
# print("\t")
# a = input("enter a name : ")
# print("\t")
# u=0
# names = {"festus":2, "raima":4, "ribin":5}
# for i in names:
#     if (i==a):
#         print("name:",i,"\t\t\t","mark =", names[i])
#     while (u==0):
#       print("\t")
#       z = input("do you want to know any others peoples mark?\t\t enter yes or no: ")
#       print("\t")
#       if z=="yes":
#           a = input("enter a name : ")
#           print("\t")
#           for i in names:
#               if (i == a):
#                   print("name:", i, "\t\t\t", "mark =", names[i])
#       else:
#           print("thankyou")
#           u=1
#           break
#
#
#
#
#
#
# Project for Student Name and Marks:
#
# n=int(input("Enter no of students:"))
# d={}
# for i in range(n):
#    Student_Name=input("Enter Student Name:")
#    Student_Marks=input("Enter Student Marks:")
#    d[Student_Name]=Student_Marks
# while True:
#     Student_Name=input("Enter Student_Name to get Student_Marks?")
#     Student_Marks=d.get(Student_Name,-1)
#     if Student_Marks==-1:
#         print("Student_Name not found")
#     else:
#         print("The Student_Marks of",Student_Name,"are",Student_Marks)
#     option=input("Do you want to find another Student_Marks[yes][No]")
#     if option=='No'or "no":
#         break
#
#
#
#
#
#
# project for Employee Name and Salary:
#
# n=int(input("Enter no of Employees:"))
# d={}
# for i in range(n):
#     Employee_Name=input("Enter Employee Name:")
#     Employee_Salary=input("Enter Employee Salary:")
#     d[Employee_Name]=Employee_Salary
# while True:
#     Employee_Name=input("Enter Employee_Name to get Employee_Salary?")
#     Employee_Salary=d.get(Employee_Name,-1)
#     if Employee_Salary==-1:
#         print("Employee_Name not found")
#     else:
#         print("The Employee_Salary of",Employee_Name,"are",Employee_Salary)
#     option=input("Do you want to find another Employee_Salary[yes][No]")
#     if option=='No':
#         break
# print("Thanks for using our applications")
#
#
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# a = {keys[i]: values[i] for i in range(len(keys))}
# print(a)
#
#
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)
#
#
#
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# keys = ["name", "salary"]
# new = {i: sample_dict[i] for i in keys}
# print(new)
#
#
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# keys = ["name", "salary"]
# for i in keys:
#     sample_dict.pop(i)
# print(sample_dict)
#
#
#
#
#
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict["class"]["student"]["marks"]["history"])


#
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# a = dict.fromkeys(employees, defaults)
# print(a)
# #
#
#
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# for i in sample_dict.values():
#     if 200 in sample_dict.values():
#         print("it is present")
#         break
#     else:
#         print("not found")
#         break
#
#
#
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sample_dict["my_name"] = sample_dict.pop("name")
# print(sample_dict)

#
#
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# a = min(sample_dict.keys())
# print(a)

#
#
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict['emp3']["salary"] = 8500
# print(sample_dict)
# #
#
#
#
# ####################FUNTIONS#########################################
# def funtion-name(parameter1, parameter2)
#             """doc string"""
#             funtion body
#            write some action
# return value
#
#
#
#
# write a funtion to take no: as input and print itzm square value
# def square(no1):
#    a = no1**no1
#    print(a)
# square(2)
#
#
# write funtion to cehck weather the given no is odd or even
# def odd_even(num):
#     if num%2==0:
#         print("it is even")
#     else:
#         print("it is odd")
# odd_even(5)
#
# write a funtion to find the factorial of a given number
#
#
#
# def factorial(num):
#     factorial = 1
#     if num < 0:
#         print("Sorry, factorial does not exist for negative numbers")
#     elif num == 0:
#         print("The factorial of 0 is 1")
#     else:
#         for i in range(1, num + 1):
#             factorial = factorial * i
#         print("The factorial of", num, "is", factorial)
# factorial(int(input("enter a number: ")))
#
#
#
#
# write a program for arthemetic operations:
#
# def arthemetic_operation(a, b):
#     print(a, " + ", b, "=", a+b)
#     print(a, " * ", b, "=", a*b)
#     print(a, " / ", b, "=", a/b)
#     print(a, " - ", b, "=", a-b)
#     print(a, " % ", b, "=", a%b)
#     print(a, " // ", b, "=", a // b)
#     print(a, " ** ", b, "=", a ** b)
#
#
# arthemetic_operation(2, 2)
#
#
#
# dog string
# def factorail(x):
#     """this is called doc string"""
#     return x
# print(factorail.__doc__)
#
# def factorail(x):
#  """
#     this is called doc string
#
#     we can use double string too
#
#  """
# print(factorail.__doc__)
#
#
#
#
# def is_even(list1):
#     even_num  = []
#     for i in list1:
#         if i%2 ==0:
#             even_num.append(i)
#     return even_num
# even_num = is_even([2, 32, 34, 65, 7, 8, 10])
# print("Even number are: ", even_num)
#
#
#
#
#
# global
# global_lang = "DataScience"
# def test():
#     local_lang = "python"
#     print(local_lang)
# test()
# print(global_lang)
#
#
# def funtion():
#     local_variable = 22
#     print(local_variable)
# def funtion2():
#      # print(local_variable)
# funtion()
# funtion2()
#
#
#
# global_variable = 99
# def funtion():
#      print(global_variable)
# def funtion2():
#      print(global_variable)
# funtion()
# funtion2()
#
#
#
#
#
# def arthemetic(a,b):
#     add = a+b
#     sub = a - b
#     div = a / b
#     multi = a * b
#     modu = a % b
#     fdiv = a // b
#     doub = a ** b
#     return add, sub, div,multi, modu, fdiv, doub
# a, b, c, d, e, f, g = arthemetic(2, 3)
# print(a)
#
#
#
# x = 4
# def funtion2():
#     print(x)
# def funtion():
#     global x
#     x = 5
#     print(x)
# funtion2()
# funtion()
#
#
# defult value argument
# def message(name = "festus"):
#     print("Hello",name)
# message()
# message("luffy")
#
#
#
#
# def add(*numbers):
#     total = 0
#     for i in numbers:
#         total +=i
#     print(total)
# add(2, 3, 3, 3)
#
#
#
#
# def names(name1, nmae2):
#     print(name1, nmae2)
#
# names("festus", "raima")
# names("festus",nmae2= "raima")
# names(name1="festus", nmae2="raima")
# names(name1="festus", "erik")
#
#
#
#
#
# def find_average_marks(marks):
#     sum_of_marks = sum(marks)
#     number_of_subjects = len(marks)
#     average_marks = sum_of_marks / number_of_subjects
#
#     return average_marks
#
#
# def compute_grade(average_marks):
#     if average_marks >= 80.0:
#         grade = 'A'
#     elif average_marks >= 60:
#         grade = 'B'
#     elif average_marks >= 50:
#         grade = 'C'
#     else:
#         grade = 'F'
#
#     return grade
#
#
# marks = [55, 64, 20, 65]
# average_marks = find_average_marks(marks)
# grade = compute_grade(average_marks)
#
# print("Your average marks is", average_marks)
# print("Your grade is", grade)
#
#
#
#
#
#
# def even(list):
#     even_num  = []
#     for i in list:
#         if i%2 ==0:
#             even_num.append(i)
#     return even_num
# even_num = even([10, 5, 12, 78, 6, 1, 7, 9])
# print(even_num)
#
#
#
#
#
# def factorial(num):
#     if num==0:
#         return 1
#     else:
#         return num*factorial(num-1)
# print(factorial(5))
#
#
#
#
#
# using lambda#
# l = [2, 3, 4, 5]
#
#
# find_even = list(filter(lambda x:x%2==0, l))
# print(find_even)
#
#
# cube = list(map(lambda x:x**3, l))
# print(cube)
#
#
#
# from  functools import reduce
# add = reduce(lambda x,y:x+y, l)
# print(add)
#
#
#
# Create a function in Python
# Write a program to create a function that takes two arguments, name and age, and print their value.
#
#
# def name_age(a,b):
#     print("my name is", a)
#     print("my age is", b)
# name_age("festus", 19)
#
#
#
# def func1(*numbers):
#     for i in numbers:
#         print(numbers)
#         break
# func1(20, 40, 60)
# func1(80, 100)
#
#
#
#
#
#
# def calculation(a, b):
#      res = a+b, a-b
#      return res
#
# res = calculation(40, 10)
# print(res)
#
#
#
# def show_employee(a, b = 9000):
#     print("employee name:", a)
#     print("employee salary:", b)
# show_employee("festus")
#
#
#
# def outer_fun(a, b):
#
#     def inner(a, b):
#         return a + b
#
#     add = inner(a, b)
#     return add + 5
#
# result = outer_fun(5, 10)
# print(result)
#
#
#
# def add(numbers):
#     total = 0
#     for i in numbers:
#         total = total+i
#     print(total)
# add(range(0, 11))
#
#
#
#
#
#
# def display_student(name, age):
#     print(name, age)
# display_student("Emma", 26)
# new_name = display_student
# new_name("emma", 19)
#
#
#
#
# print(list(range(4, 30, 2)))
#
#
#
#
# x = [4, 6, 8, 24, 12, 2]
# a = max(x)
# print(a)
#
#
#
# def per_hundred(x):
#     return x / 100
#
#
# my_answer = per_hundred(5000)
# print(my_answer)
#
#
#
# def plus(x):
#     return x+2
# a = plus(6)
# print(a)
#
#
#
# def plus_two(x):
#     print (x+2)
#     return (x+2)
#
# func = plus_two(2)
# print(func)
#
#
#
#
# def meggage(name, salary= 2000):
#     print(name, salary)
# meggage("arjun")
#
#
# # Function life expectancy calculation
# def new_life(name, age):
#     if smoker(name) == True:
#         life_exp = 60
#     else:
#         life_exp = 80
#
#     life_remaining = life_exp - age
#
#     msg = "Hi " + name + "! Your new expected remaining life is: " + str(life_remaining) + " years."
#     return msg
#
#
# def smoker(name='', smoke=False):
#     if name.capitalize() in ["Jane", "Zack", "Melissa"]:
#         smoke = True
#     return smoke
#
#
# print(new_life("jane", 30))
# print(new_life("erik", 30))
#
#
#
#
# def wish(name):
#     print("good morning", name)
# greetings = wish
# greetings("festus")
# wish("erik")
# del wish
# wish("zebra")                       #if we del one name we can always access that funtion by using alias name
# greetings("zorojuro")
#
#
#
#
# def detail(roll):
#     x = [23,43,22,56]
#     if roll in x:
#         print(f"Roll number {roll} is present")
#     else:
#         print(f"Roll number {roll} is absent")
# detail(int(input("Enter roll no. ")))
#
#
#
#
#
#
#
# using decorators
#
# def samrt_division(func):
#     def inner(a, b):
#         if b==0:
#             print("can't divide")
#         else:
#             return func(a, b)
#     return inner
# @samrt_division
# def div(a,b):
#     return a/b
#
#
# print(div(20, 2))
# print(div(20, 0))
#
#
#
#
# chaning
# def outer(func):
#     def inner(name):
#         print("first")
#         func(name)
#     return inner
# def outer2(func):
#     def inner(name):
#         print("second")
#         func(name)
#     return inner
# @outer
# @outer2
# def wish(name):
#     print(name)
# wish("Festus")
#
#
#
#
#
#
#
# def outer():
#     print("It is outer")
#     def inner():
#         print("itz inner")
#     print("its outer 2")
#     return inner
# f1 = outer()
# f1()
# f1()
# f1()
#
#
#
#
# def name():
#     yield "Erik"
#     yield "Festus"
#     yield "Strawhat"
# a= name()
# print(next(a))
# print(next(a))
# print(next(a))
#
#
#
#
# write a program to generate first n numbers
#
# def numbers(n):
#     a = 1
#     while a<=n:
#         yield a
#         a= a+1
# values = numbers(10)
# # for i in values:
# #     print(i)
#
# l1 = list(values)
# print(l1)
#
#
# ##
#
#
#
# #fibanocci series
# def fib():
#     a, b = 0, 1
#
#     while True:
#         yield b
#         b = a + b
#         a = b - a
#
# for num in fib():
#     if num > 10:
#         break
#     print(num)
#
#
#
#
# reverse coutdown
# def reverse_countdodwn(num):
#     while num>0:
#         yield num
#         num = num-1
# res = reverse_countdodwn(10)
# for i in res:
#     print(i)
#
#
#
#
#
#
#
#
#
#
#
#
# ############################## MODULE #############################
#
# import math
# print(math.factorial(5))
#
#
# from math import pi
# print(pi)
#
# # we can import 2 or more funtions at a time
#
# import random, math
# print(random.randint(10, 20))
#
#
# # we can cahnge the name of a funtion as we wish
#
# from math import sqrt as square_root
# print(square_root(9))
#
#
# # for getting all the funtions inside a funtion
#
# from math import *
# print(pow(3, 2))
# print(fabs(-4235))  #fabs always gives the positive value + it shows the exact no: before and after a floating number
#
#
#
#
# import test
# test.add(10, 20)
#
# import test
# a = test.a
# b = test.b
# print(a)
# print(b)
#
#
#
# import string
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
#
#
# import os  #creating a dict
# os.mkdir("")  #cahnging current dict
# os.chdir("")   #getting current making dict
# os.getcwd()   #removing dict
# os.rmdir()
#
#
# import math
# print(dir(math))
# help(math)
#
#
#
# import sys
# print(sys.path)
#
#
# import test
# print(test.city[1])
# print(test.city)
#
#
#
#
# from random import randint
# print(randint(5, 10))
#
#
#
#
#
#
# number = 400
# def a():
#     global number
#     number= number+200
# print(number)
# a()
# a()
# print(number)
#
#
#
#
# import random
#
# greeting = ["hello", "hi", "hey", "howdy"]
# colors  = ["red", "green", "blue"]
# deck =  list(range(1, 53))
#
# value = random.uniform(1, 3)
# print(value)
#
#
# value = random.randint(1, 3)
# print(value)
#
#
# value = random.choice(greeting)
# print(value+ ", Festus")
#
#
# value = random.choices(colors, k = 5)
# print(value)
#
#
# value = random.choices(colors, weights=[20, 20, 90], k  = 5)
# print(value)
#
# random.shuffle(deck)
# print(deck)
#
#
# hand = random.sample(deck, k = 5)
# print(hand)
#
#
# value = random.choices(deck, k = 5)
# print(value)
#
#
#
#
# ''' Super simple module to create basic random data for tutorials'''
# import random
#
# first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']
#
# last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']
#
# street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']
#
# fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']
#
# states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
#
# for num in range(1):
#     first = random.choice(first_names)
#     last = random.choice(last_names)
#
#     phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'
#
#     street_num = random.randint(100, 999)
#     street = random.choice(street_names)
#     city = random.choice(fake_cities)
#     state = random.choice(states)
#     zip_code = random.randint(10000, 99999)
#     address = f'{street_num} {street} St., {city} {state} {zip_code}'
#
#     email = first.lower() + last.lower() + '@gmail.com'
#
#     print(f'{first} {last}\n{phone}\n{address}\n{email}\n')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# ############################TRY EXCEPTION ERROR###############################
#
# a = 10
# b = 20
# try:
#  print(a+c)
#
# except NameError as name :
#     print("NameError", name)
# except SyntaxError:
#     print("SyntaxError")
# except(ValueError, TypeError, NameError):
#     print("not a valid value")
#
# print(a+b)

#
#
#
# try:
#     a = 10
#     b = 0
#     c = a/b
#     print(c)
# except:
#     print("can't divide a number with zero")
#
#
#
#
#
#
# using finally
#
# a = 10
# b = 20
# try:
#   print(a+c)
# except NameError as name:
#      print("NameError", name)
# except SyntaxError:
#      print("SyntaxError")
# except(ValueError, TypeError, NameError):
#      print("not a valid value")
#
#
# finally:
#    print("hi")
#
#
#
#
#
#
# only situatiom when finnally can't be excecuted
#
# import os
#
# try:
#     print("try")
#     os._exit(0)
# except NameError:
#     print("nameerror")
# finally:
#     print("finally")
#
#
#
#
#
# using try and else
#
# try:
#     num1 = 10
#     num2 = 0
#     print(num1/num2)
#
# except ZeroDivisionError:
#     print("Zero Division Error")
#
# else:
#     print("Execution was succesful")
#
#
#
#
#
# class Error(Exception):
#     pass
# class if_value_small(Error):
#     pass
# class if_value_big(Error):
#     pass
#
#
# while True:
#     num = int(input("enetr a value from 10 to 50:"))
#     try:
#         if num<10:
#             raise if_value_small
#         elif num>50:
#             raise if_value_big
#     except if_value_small:
#         print("value is too small")
#         break
#     except if_value_big:
#         print("value is big small")
#         break
#     print("excecution was succesfull")
#     break
#
#
#
#

# try:
#     a = int(input("Enter a value: "))
#     b = int(input("Enter a value: "))
#     c = a/b
#     print(c)
# except ZeroDivisionError as e:
#     raise ValueError ("Division Error")
#
#
#
#
# it will throw error if value is greater than 100
# def interest(amount, year, rate):
#     try:
#         if rate >100:
#             raise ValueError(rate)
#         intrst = (amount*year*rate)/100
#         print("interest is", intrst)
#         return intrst
#     except ValueError:
#         print("ValueError - Out of rate", rate)
# print("case 1")
# interest(800, 6, 95)
#
# print("case 2")
# interest(800, 6, 1500)












































































