## How to create a class :-
# class Person:
#     pass

## how to create an object:-
 # object= Person()

## Create a class and object:-
# class person:
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def full_details(self):
#         return f" The person name is {self.name}, age of person is {self.age} and gender is {self.gender}"
#
# person1 = person("harshit", 25, "M")
# print(person1.full_details())

##Create a Laptop class with attributes like brand, model, and price and create two object of this class.
# class laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def full_details(self):
#         return f"the laptop brand is {self.brand}, model is {self.model} and price is {self.price}"
#
# laptop1 = laptop("hp", "ryzen5", 45000)
# laptop2 = laptop("dell", "lattitude", 40000)
# print(laptop1.full_details())
# print(laptop2.full_details())

## define a method function inside the body of class, they define the the behaviers of an object:-
# class laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def full_details(self): #this is method inside the body
#         return f"the laptop brand is {self.brand}, model is {self.model} and price is {self.price}."
#
#     def write_a_program(self): #this is method inside the body
#         print("create an application in python language.")
#
# laptop1 = laptop("hp", "ryzen5", 45000)
# print(laptop1.full_details())
# print(laptop1.write_a_program())

## define a function in a class, class name is laptop which is give 20% discount:-
# class laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def full_details(self):
#         return f"{self.brand} {self.model} and price is {self.price}"
#
#     def applying_discount(self, num):
#         off_price = (num/100)* self.price
#         return self.price-off_price
#
# laptop1 = laptop("hp", "ryzen5", 45000)
# print(laptop1.full_details())
# print(laptop1.applying_discount(20))

## CLASS VARIABLES:-
## Create a laptop class and that class have one object. in laptop class give 10% discount:-
# class laptop:
#     discount_percent = 20
#     def __init__(self, brand, model, price ):
#         self.brand = brand
#         self.model = model
#         self.price = price
#     @property
#     def apply_off(self):
#         off_price = (self.discount_percent/100)*self.price
#         return self.price-off_price
#
# lapy = laptop("hp", "ryzen", 45000)
# print(lapy.apply_off())

## if give discount any perticular object like you have two object laptop1 and laptop2 in laptop class.give 50% discount on laptop2.
# class laptop:
#     discount_percent = 10
#     def __init__(self, brand, model, price ):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def discount_price(self):
#         off_price = (self.discount_percent/100)*self.price
#         return self.price-off_price
#
# laptop1 = laptop("hp", "pavilion", 40000)
# laptop2 = laptop("hp", "ryzen5", 45000)
#
# laptop2.discount_percent = 50
# print(laptop1.discount_price())
# print(laptop2.__dict__)
# print(laptop2.discount_price())

## COUNT MEthod in class:-
## Create a class of person and create an object of person and findout how many object in their person:-
# class person:
#
#     count_object = 0
#     def __init__(self, name, age, gender ):
#         person.count_object += 1
#         self.name= name
#         self.age = age
#         self.gender = gender
#
# p1 = person("pravin", 26,"M")
# p2 = person("Meera", 27,"F")
# p1 = person("pravin", 26,"M")
# p2 = person("Meera", 27,"F")
# print(person.count_object)

## Class method:-
# class Person:
#     count_instances = 0
#     def __init__(self, name, age, gender):
#         Person.count_instances += 1
#         self.name= name
#         self.age = age
#         self.gender = gender
#
#     @classmethod
#     def count_instance(cls):
#         return f"you have created {cls.count_instances} instance of {cls.__name__} class."
#
#     def full_details(self):
#         return f"name is {self.name} age of person is {self.age} and the gender is {self.gender}"
#
#     def age_above_18(self):
#         return self.age>18
#
# p1 = Person("anand", 26, "M")
# p2 = Person("anand1", 27, "M")
# print(p1.count_instance())
# print(Person.count_instance())

## Constructors:-
# class Person:
#     count_instance = 0
#     def __init__(self, name, age, gender):
#         Person.count_instance += 1
#         self.name= name
#         self.age = age
#         self.gender = gender
#
#     @classmethod
#     def from_string(cls, string):
#         name, age, gender = string.split(",")
#         return cls (name, age, gender)
#
#     @classmethod
#     def count_instances(cls):
#         return f"you have created {Person.count_instance} instances of {cls.__name__} class."
#
#     def full_details(self):
#         return f"{self.name} {self.age} {self.gender}"
#
# p1 = Person("anand", 27, "M")
# print(p1.full_details())
# print(Person.count_instances())
# print(Person.from_string)

## Property & Setter Decorator:-
## CHange the price of the phone class:-
# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self._price = price
#
#     def full_details_phone(self):
#          return f"{self.brand} {self.model} and price is {self._price}"
#
#     def make_a_call(self, phone_number):
#         print(f"calling {phone_number}...")
#
#     def full_name(self):
#         return f"{self.brand} {self.model}"
#
# phone1 = Phone("sony", "xperia", 18000)
# phone1._price = 20000
# print(phone1._price)
# print(phone1.full_details_phone())

## print function as a attrubute with the help of @property decorator:-
# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self._price = price
#     @property
#     def full_specification(self):
#         return f"{self.brand} {self.model} and price is {self._price}"
#
#     def make_a_call(self, phone_number):
#         print(f"calling {phone_number}...")
#
#     def clik_image(self):
#         print("Show the image")
#
# phone1 = Phone("nokia", "6.1plus", 15000)
# phone1._price = 20000
# print(phone1._price)
# print(phone1.make_a_call(9759254341))
# print(phone1.full_specification)

## WAP, create a class and in class no set negative price:-
# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self._price = price
#
#     @property
#     def price(self):
#         return self._price
#     @price.setter
#     def price(self, new_price):
#         self._price = max(new_price, 0)
# phone1 = Phone("nokia", "6.1plus", 15000)
# phone1.price = -15000
# print(phone1.price)

## Inheritance:-
# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def full_details(self):
#         return f'{self.brand} {self.model} {self.price}'
#
#     def make_a_call(self, phone_number):
#         print(f"calling {phone_number}...")

# class smartphone(phone):
#     def __init__(self, brand, model, price, RAM):
#         super().__init__(brand, model, price)
#         self.RAM = RAM
#
# phone1 = phone('sony', 'xperia', 18000)
# print(phone1.make_a_call(9759254341))
# smart = smartphone('nokia', '6.1plus', 12000, '4gb')
# print(smart.make_a_call(8294728874))
# print(smart.full_details())

### Can derive more then one class from base class:-
# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def full_details(self):
#         return f'{self.brand} {self.model} {self.price}'
#
#     def make_a_call(self, phone_number):
#         print(f"calling {phone_number}...")
#
# class smartphone(phone):
#     def __init__(self, brand, model, price, ram):
#         super().__init__(brand, model, price)
#         self.ram = ram
#
# class smartphone1(phone):
#     def __init__(self, brand, model, price, ram, camera):
#         super().__init__(brand, model, price)
#         self.ram = ram
#         self.camera = camera
#
# phone1 = phone('sony', 'xperia', 21000)
# phone2 = smartphone('nokia', '6.1plus', 16000, '4gb')
# phone3 = smartphone1('apple', 'iphone6s', 33000, '4gb', '32mp')
# print(phone1.full_details())
# print(phone2.make_a_call(1234567898))
# print(phone3.camera)

### Multilevel inheritance:-
# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def full_details(self):
#         return f'{self.brand} {self.model} {self.price}'
#
#     def make_a_call(self, phone_number):
#         print(f"calling {phone_number}...")
#
# class smartphone(phone):
#     def __init__(self, brand, model, price, ram):
#         super().__init__(brand, model, price)
#         self.ram = ram
#
# class smartphone1(smartphone):
#     def __init__(self, brand, model, price, ram, camera):
#         super().__init__(brand, model, price, ram)
#         self.camera = camera
#
# phone1 = phone('sony', 'xperia', 21000)
# phone2 = smartphone('nokia', '6.1plus', 16000, '4gb')
# phone3 = smartphone1('apple', 'iphone6s', 33000, '4gb', '32mp')
# print(phone1.full_details())
# print(phone2.make_a_call(1234567898))
# print(phone3.camera)

### Method overrriding:-
# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def full_details(self):
#         return f'{self.brand} {self.model} {self.price}'
#
#     def make_a_call(self, phone_number):
#         print(f"calling {phone_number}...")
#
# class smartphone(phone):
#     def __init__(self, brand, model, price, ram):
#         super().__init__(brand, model, price)
#         self.ram = ram
#
#     def full_details(self):
#         return f'{self.brand}, {self.model}, {self.price}, {self.ram}'
#
# class smartphone1(smartphone):
#     def __init__(self, brand, model, price, ram, camera):
#         super().__init__(brand, model, price, ram)
#         self.camera = camera
#
#     def full_details(self):
#          return f'{self.brand} {self.model} {self.price} {self.ram} {self.camera}'
#
# phone1 = phone('sony', 'xperia', 21000)
# phone2 = smartphone('nokia', '6.1plus', 16000, '4gb')
# phone3 = smartphone1('apple', 'iphone6s', 33000, '4gb', '32mp')
# print(phone1.full_details())
# print(phone2.full_details())
# print(phone3.camera)
# print(isinstance(phone3, smartphone))

### IsInstance:-
# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def full_details(self):
#         return f'{self.brand} {self.model} {self.price}'
#
#     def make_a_call(self, phone_number):
#         print(f"calling {phone_number}...")
#
# class smartphone(phone):
#     def __init__(self, brand, model, price, ram):
#         super().__init__(brand, model, price)
#         self.ram = ram
#
#     def full_details(self):
#         return f'{self.brand}, {self.model}, {self.price}, {self.ram}'
#
# class smartphone1(smartphone):
#     def __init__(self, brand, model, price, ram, camera):
#         super().__init__(brand, model, price, ram)
#         self.camera = camera
#
#     def full_details(self):
#          return f'{self.brand} {self.model} {self.price} {self.ram} {self.camera}'
#
# phone1 = phone('sony', 'xperia', 21000)
# phone2 = smartphone('nokia', '6.1plus', 16000, '4gb')
# phone3 = smartphone1('apple', 'iphone6s', 33000, '4gb', '32mp')
# print(phone1.full_details())
# print(phone2.full_details())
# print(phone3.camera)
# print(isinstance(phone3, smartphone))

### ISSUBCLASS:-
# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def full_details(self):
#         return f'{self.brand} {self.model} {self.price}'
#
#     def make_a_call(self, phone_number):
#         print(f"calling {phone_number}...")
#
# class smartphone(phone):
#     def __init__(self, brand, model, price, ram):
#         super().__init__(brand, model, price)
#         self.ram = ram
#
#     def full_details(self):
#         return f'{self.brand}, {self.model}, {self.price}, {self.ram}'
#
# class smartphone1(smartphone):
#     def __init__(self, brand, model, price, ram, camera):
#         super().__init__(brand, model, price, ram)
#         self.camera = camera
#
#     def full_details(self):
#          return f'{self.brand} {self.model} {self.price} {self.ram} {self.camera}'
#
# phone1 = phone('sony', 'xperia', 21000)
# phone2 = smartphone('nokia', '6.1plus', 16000, '4gb')
# phone3 = smartphone1('apple', 'iphone6s', 33000, '4gb', '32mp')
# print(phone1.full_details())
# print(phone2.full_details())
# print(phone3.camera)
# print(issubclass(smartphone, smartphone1))

### Multiple Inheritance:-
# class A:
#     def __init__(self):
#         return "I am just a class A"
#
#     def hello(self):
#         return "hello from class A"
#
# class B:
#     def __init__(self):
#         return "I am just a class B"
#
#     def hello(self):
#         return "hello from class B"
#
# class C(A,B):
#     pass
#
# instance_c = C()
# print(instance_c.hello())

### Magic method:-
# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def phone_name(self):
#         return f"{self.brand} {self.model}"
#
#     def __str__(self):
#         return f"{self.brand}, {self.model}, {self.price}"
#
#     def __repr__(self):
#         return f"phone (\'{self.brand}\', \'{self.model}\' {self.price})"
#
# phone1 = phone("nokia", "6.1plus", 12000)
# print(phone1.__str__())
# print(phone1.__repr__())
# print(str(phone1))
# print(repr(phone1))

### Operator Overloading:-
# class phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def __add__(self, other):
#         return self.price + other.price
#
# phone1 = phone("samsubg", "galaxy", 30000)
# phone2 = phone("nokia", "6.1plus", 45000)
# phone3 = phone1+phone2
# print(phone3)

# class computer:
#
#     def __init__(self):
#         print("i5 processor, 1TB HDD, 11 gen")
#
# comp1 = computer()
# computer.__init__(comp1)

# class car:
#
#     def __init__(self):
#         self.brand = "TATA"
#         self.model = "Jaguaar"
#
# c1 = car()
# c2 = car()
#
# c1.model = "range Rower"
# print(c1.model)
# print(c2.model)

class student:

    College = "DBIT"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def info(cls):
        return cls.College

s1 = student(43, 56, 87)
s2 = student(76, 98, 45)

print(s1.avg())
print(student.info())





