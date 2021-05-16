# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# %% classes

employee1_name = "messi"
employee1_age= 33
employee1_address = "sadasdas"

class Employee(object):
    # attribute = age,address,name
    # behaviour = pass
    pass

employee1 = Employee()

# %%

class Footballer:
    football_club = "barcelona"
    age = 30

f1 = Footballer()
print(f1)
print(f1.age)
print(f1.football_club)

f1.football_club = "real madrid"

print(f1.football_club)

# %% methods

class Square(object):
    edge = 5
    area = 0
    
    def area(self):
        self.area = self.edge*self.edge # 5*5
        print("Area : ",self.area)
        
s1 = Square()
print(s1)
print(s1.edge)

s1.edge = 7
s1.area()

# %% methods vs functions

class Emp(object):
    age = 25
    salary = 1000
    
    def ageSalaryRatio(self): # method
        a = self.age / self.salary
        print("Method : ",a)

# function
def ageSalaryRatio(age,salary):
    a = age/salary
    print("Func : ",age/salary)

e1 = Emp()
e1.ageSalaryRatio()

ageSalaryRatio(30, 3000)

# %% return
def findArea(a,b): # a = pi, b = r
    area = a*b**2
    return area
result1 = findArea(3,5)
print(result1)

# %% yapıcı - constructor - initializer
class Animal(object):
    def __init__(self,a,b): # (name, age) = ("dog", 2) = (a, b)
        self.name = a
        self.age = b
        
    def getAge(self):
        print(self.age)
        return self.age
    
    def getName(self):
        print(self.name)

a1 = Animal("dog", 2)
a2 = Animal("cat", 3)
a3 = Animal("bird", 4)

# %% calculator project
# class -> init -> method/attribute -> func vs methods

class Calc(object):
    "calculator"
    # init metodu
    def __init__(self,a,b):
        "initialize values"
        # attribute
        self.value1 = a
        self.value2 = b
    
    def add(self):
        "addition a+b = result -> return result"
        return self.value1 + self.value2
    
    def multiply(self):
        "multiplication a*b = result -> return result"
        return self.value1 * self.value2
    
    def division(self):
        "division a/b = result -> return result"
        return self.value1 / self.value2
    
print("Choose add(1), multiply(2), division(3)")
selection = input("select 1 or 2 or 3 : ")
v1 = int(input("first value : "))
v2 = int(input("second value : "))

c1 = Calc(v1,v2)
if selection == "1":
    add_result = c1.add()
    print("Add : {}".format(add_result))
elif selection == "2":
    multiply_result = c1.multiply()
    print("Multiply {}".format(multiply_result))
elif selection == "3":
    division_result = c1.division()
    print("Division {}".format(division_result))
else:
    print("Error : There is no proper selection3")

# %% encapsulation

class BankAccount(object):
    def __init__(self,name,money,address):
        self.name = name
        self.__money = money
        self.address = address
    
    # get and set
    def getMoney(self):
        return self.__money
    
    def setMoney(self,amount):
        self.__money = amount
        
    # private
    def __increase(self):
        self. __money = self.__money + 500
        
p1 = BankAccount("messi", 1000, "barcelona")
p2 = BankAccount("neymar", 2000, "paris")

print(p1.getMoney())
p1.setMoney(5000)
print("after set method : ",p1.getMoney())
# p1.increase()
# print("after raise : ",p1.getMoney())

# %% miras - inheritance

class Animal:
    # parent
    def __init__(self):
        print("animal is created")
    
    def walk(self):
        print("animal walk")
    
    def toString(self):
        print("Animal toString")
        
class Monkey(Animal):
    # child
    def __init__(self):
        super().__init__() # use init of parent class
        print("Monkey is created")
    
    def climb(self):
        print("Monkey is climbing")

    def toString(self):
        print("Monkey toString")

class Bird(Animal):
    # child
    def __init__(self):
        super().__init__()
        print("Bird is created")
        
    def fly(self):
        print("bird is flying")
        
    def toString(self):
        print("monkey toString")

x = Animal()
y = Monkey()
z = Bird()

x.toString()
y.toString()
z.toString()

print("------")

x.walk()
y.walk()
z.walk()
y.climb()
z.fly()


# %%

class Website:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    
    def loginInfo(self):
        print(self.name + " " + self.surname)

class Website1(Website):
    
    def __init__(self,name,surname,ids):
        Website.__init__(self,name,surname)
        self.ids = ids
        
    def login(self):
        print(self.name + " " + self.surname + " " + self.ids)
        
class Website2(Website):
    
    def __init__(self,name,surname,email):
        Website.__init__(self,name,surname)
        self.email = email
        
    def login(self):
        print(self.name + " " + self.surname + " " + self.email)


p1 = Website("selçuk", "akarın")
p2 = Website1("alican", "akarın", "123")
p3 = Website2("mustafa", "akarın", "mustafaakarin@gmail.com")

# %% soyut sınıflar - abstract classes

# abstract class'lar kendisinden türeyecek subclass'lar için bir şablon görevi görür.
# abstract class hiçbir şekilde instantiate edilemez. Hiçbir şekilde obje üretilemez. 
# Python'da bu kısıt direkt gelmez. Ama extend ediyoruz.
# abstract class'ta kullanılan herhangi bir abstract metot subclass'ta mutlaka tanımlanmalıdır.
# bir tane bir abstract metot varsa class abstract class'tır.

from abc import ABC, abstractmethod
class Animal(ABC):
  @abstractmethod
  def walk(self): pass
  def run(self): pass
class Bird(Animal):
  def __init__(self):
    print("bird")
  def walk(self):
    print("walk")
b = Bird()

# %% overriding

class Animal: # parent
    def toString(self):
        print("animal")
        
class Monkey(Animal):
    def toString(self):
        print("Monkey")

a1 = Animal()
a1.toString()

m1 = Monkey()
m1.toString() # monkey calls overriding method

# %% 
# polymorphism
class Employee:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary
  def raiseSal(self):
    raise_rate = 0.1
    self.salary += self.salary * raise_rate
    print("Employee : ",self.salary)
class CompEng(Employee):
  def __init__(self,name,salary):
    super().__init__(name,salary)
  def raiseSal(self):
    raise_rate = 0.2
    self.salary += self.salary * raise_rate
    print("Comp eng : ",self.salary)
class EEE(Employee):
  def __init__(self,name,salary):
    super().__init__(name,salary)
  def raiseSal(self):
    raise_rate = 0.3
    self.salary += self.salary * raise_rate
    print("EE eng : ",self.salary)
e1 = Employee("selçuk",1000)
ce = CompEng("bill gates",2000)
eee = EEE("tesla",3000)

# %%
"""
    OOP
      - class/object
      - attributes/methods
      - encapsulation/abstraction
      - inheritance
      - overriding/polymorphism
"""
from abc import ABC, abstractmethod
class Shape:
  """
      Shape = super class / abstract class
  """
  
  # abstract method
  @abstractmethod
  def area(self): pass

  @abstractmethod
  def perimeter(self): pass

  # overriding and polymorphism
  def toString(self): pass

#child
class Square(Shape):
  "sub class"

  def __init__(self,edge):
    self.__edge = edge # encapsulation private attribute

  def area(self):
    result = self.__edge**2
    print("Square area: ",result)

  def perimeter(self):
    result = self.__edge*4
    print("Square perimeter: ",result)
    
  # overrride and polymorphism
  def toString(self):
    print("Square edge: ",self.__edge)

# childe
class Circle(Shape):
  "circle class"
  # constant variable
  PI = 3.14

  def __init__(self,radius):
    self.__radius = radius

  def area(self):
    result = self.PI*self.__radius**2
    print("Circle area: ",result)

  def perimeter(self):
    result = 2*self.PI*self.__radius
    print("Circle perimeter: ",result)
    
  # override and polymorphism
  def toString(self):
    print("Circle radius: ", self.__radius)
    
c = Circle(5)
c.area()
c.perimeter()
c.toString()

print("****")

s = Square(5)
s.area()
s.perimeter()
s.toString()






