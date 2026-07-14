##List##
##a = "anahita"
#print(a[3:6:1])
#print(a[::-1])
#my_val=['ana','hita']
#print(type(my_val))
###############################
##Tuple##
#T1=(1,4,6,9)
#print(type(T1))
#T2= ('apple','orange',(1,3,5))
#print(type(T2))
########################################
#Set# #HashTable
#set_t={1,2,4,4,9,8}
#list_t=[1,2,4,4,9,8]
#print(set_t,list_t)
############################################
##Dictionary##
#D1= {"name":"anahita","city":"nashta","age":19}
#print(D1)
#print(type(D1))
#############################
#def my_function(parameters):
#function
#def print_hello():
  #  for i in range(3):
 #       print('hello')

#print_hello()
######################################
################################تمرین اول
#تولید یک عدد رندوم
#اگر n % 2 == 0 :
#چاپ کن زوج
#وگرنه چاپ کن فرد
#def check_odd_even (num):
 #   if num % 2 == 0 :
   # else:
    #    print ("odd")
#num =int(input("Enter a num :"))
#check_odd_even(num)


##############################تمرین دوم
#گرفتن ورودی از کاربر
#دنباله بساز از 0 تا آن عدد
#همه ی اعداد را جمع کن
#برگردان نتیجه  را
#def sum_nums (num):
#    total = 0
#    for i in range (num+1):
#        total = total + i

#    return total
#i = int(input('Enter a num:'))
#print (sum_nums(i))       


############################تمرین3
#def count_characters(text):
#     numbers = 0
#     letters = 0
      
#     for ch in text:
     
#      if ch.isalpha():
#        letters += 1
     
#      elif ch.isdigit():
##       numbers+= 1
 #    return {
 #   "characters": letters ,
 #   "numbers": numbers 
 #   }  
#result = count_characters(input("Enter your text: "))
#print(result)
###############################################################################
#Exception 
#try :
#    print(7/0)
#except :
#    print("Didnt excute")


#try:
##     print(7/0)
#     print("after")
#except ZeroDivisionError :
#     print ("didnt excute")
#finally:
#     print("end of the program")
#########################################


############تمرین های بخش دوم 
###############################################تمرین 1
# دریافت ورودی از کاربر
#username = input("enter your username: ")
#password = input("enter your password: ")

# بررسی با شرط ها
#if username == "admin":                # نام کاربری درست ، بررسی پسوورد
#    if password == "admin":             # هم نام کاربری وهم پسوورد درست
#        print("successful login")          #  نام کاربری درست ولی پسورد اشتباه است
#    else:
#         print("incorrect password")
#else:
     #نام کاربری اشتباه 
#    print("user not found")
###############################################################################
######################################تمرین2

#for num in range (1,11):
    
#    if num==5 :
#        continue
    
#    elif num==8:
#       break
#else :
#    print(num)
#print("The game is over")
#####################################################

################################################تمرین 3

# تعریف لیست‌ها
# List_1 = [1, 2, 3, 4, 5]
# List_2 = [4, 5, 6, 7, 8]
# print  (List_1)
# print(List_2)

                                             # مرحله 1: ادغام دو لیست با عملگر 
# Edgham_list = List_1 + List_2
# print(" Edgham List: ", Edgham_list)

# # مرحله 2: حذف مقادیر تکراری با   set
# unique_list = list(set(Edgham_list))
# print("Unique list: ", unique_list)

# #  3 عضو اول
# first_three = unique_list[:3]
# print("first_three: ", first_three)
#############################################################

############################Object-Oriented Programming(OOP)####################
# class Student:
#     def __init__(self,name):
#         self.name = name
   
#     def introduce(self):
#         print ("My name is",self.name)

# s1 =Student("Ali")

# s1.introduce() 

# s2 =Student('sara')
# s2.introduce()

# s3= Student('Anahita')
# s3.introduce()
########################################################Ex1
# class Student:

#     def __init__(self, age, lastname):
#         self.age = age
#         self.lastname = lastname

#     def introduce(self):
#         print("my lastname is", self.lastname)


# s1 = Student(20, "rezaie")
# s1.introduce()

# s2 = Student(19, "sefidi")
# s2.introduce()     
#################################################################Ex2(برند ماشین)
# class Car:
#     def __init__(self,brand):
#         self.brand=brand

#     def show (self):
#         print("brand: ",self.brand)
# c1 = car("BMW")
# c1.show()

# c2= car("Benz")
# c2.show()

# c3 =car("Audi")
# c3.show()
####################################################Ex3(مساحت مستظیل)
# class Rectangle :
#     def __init__(self,length,width):
#         self.length=length 
#         self.width=width 
#     def area(self):
#         return self.length*self.width
# r1 = Rectangle(5,3)
# print(r1.area())

# r2 = Rectangle(5,6)
# print(r2.area())

# r3= Rectangle(10002,234)
# print(r3.area())
########################################################################################
#####################MagicMethod#########################
# num=10
# res = num.__add__(5) 
# print(res)
####################################تابع str
# class Student:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#      return f"Stusent :{self.name}"
# s1=Student("ALi")
# print(s1) 
###########################################تابعlen
# name="Anahita"
# print(len(name))
#########################
# class Team :
#    def __init__(self,members):
#       self.members = members
#    def __len__(self): 
#       return len(self.members)
# t1 =Team(["ALi","Sara","Reza"])
# print(len(t1))
######################Inheritance##################
# class Animal :                           #،کلاس والد،بجای تکراراز ازث بری استفاده میکنیم 
#     def eat(self):
#         print("Eating...")
# class Dog(Animal):                           #سگ از حیوان به ارث میبره
#     pass
# d = Dog()
# d.eat()
#####################################################
# class Animal:
#     def eat(self):
#         print("Eating..")
#     def sleep(self):
#         print("Sleeping..")
# class Dog(Animal):
#     def bark(self):
#         print("woof")  #چرا چیزی پرینت نمیشه؟تا الان کلاس مشخص کردیم ،بدون هیچ متدی
# d= Dog()
# d.eat()
# d.sleep()
# d.bark()
##########################################
#########################################
# class Human:
#     def __init__(self,name,lastname):
#         self.name=name
#         self.lastname=lastname
#     def fullname(self):
#         return self.name+ "  "+self.lastname
#     def __str__(self):
#         return self.name+ "object"

# class Employee(Human):
#     manager= "hasan"
#     def programmer(self):
#         print("maybe im a programmer")
# p1=Employee("ali","bigdeli")
# print(p1)
# print(p1.programmer())
###############################################
