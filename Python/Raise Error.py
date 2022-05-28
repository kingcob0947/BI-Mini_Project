### raised an error when user pass any other value instead of integer to the function:-
# def add_function(a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a+b
#     raise TypeError("Oops you are passing wrong data type.")
# print(add_function('3',6))

### Notimplemented Error:-
##for all the animal classes that have subclasses, it will be necessary to define a sound method for that
# class otherwise an error will come.
class animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("You have define this method in subclass")

class dog(animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "bhow bhow"

class cat(animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "meao meao"

doggy = dog("roxy", "pitbull")
catty = cat("caty", "billa")
print(catty.sound())

### we want that add only and only those object of mobile class. the same should be added to my sublass mobilestore
#and not added any string tonmobilestore:-(raise TypeError)
class mobile:
    def __init__(self, name):
        self.brand = name


class mobilestore:
    def __init__(self):
        self.name = []

    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, mobile):
            self.name.append(new_mobile)
        else:
            raise TypeError("New mobile should be object of mobile class")

oneplus = mobile("one plus 6")
samsung = "galaxy s8"
mobstore = mobilestore()
mobstore.add_mobile(oneplus)
print(mobstore.name)

