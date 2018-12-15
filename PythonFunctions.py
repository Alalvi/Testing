"""
#functions:
def The_function(param,param1):
    print(param,param1)
    return 
def Many_parameters(*args):
    for param in args:
        print(param)
    #the return is not necesary if there is no information to returm
def dictionary_of_parameters(**kwargs):
    print("Name: ", kwargs.get("name"))
    print("Age: ", kwargs.get("age"))
    print("Career: ", kwargs.get("Career", "Not studying"))
dictionary_of_parameters(name="Peter", age=23, career= "professional goat thrower")
"""


"""
#Classes:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __info(self):
        print(self.name+str(self.age))
a = Person ("Peter",27)
a.infor()

#Inherance:
class Student(Person):
    def __init__(self, name, age, career):
        Person.__init__(self,name,age)
        self.career= career
    def complete__info(self):
        print(self.career)
a=Student("Peter", 27, "Professional goat thrower")
a.complete_info()
"""

"""
Modules:
    import module_name
    var= module_name.method()
"""

"""
#lists:
list1=[1,2,3,4,5,6,7,8]
list1= list("hello")
len(list1) #returns quantity of elements
list1[2]#returns the element of position 2
list1.append(10)#annex the 10 at the end
list1.pop()#erases the last element and prints it
list1.count(element)#counts how many times the elements is inside the list
del list1[position] #erases the element on the position designated
list1.remove(x)#Erase the first instance of x in the list
list1[1:4]#return the elements of list1 from position 1 to 3

if 5 in list1: #ask if there is a 5 in the list
    print("Bob, Do something!"
for element in list1:
          print (element) #prints every element in the list
"""

"""
#Dictionaries:

dictionary ={'name':'Peter', 'age':23,'career':'professional goat thrower'}
print(dictionar['name'])

dictionary['institution']='UCT'
del dictionary['name']
dictionary.clear)=
del dictionary

str(dictionary)#print-able version

for key, value in dictionary.items(): #loof through a dictionary
    print(key + ": " + str(value))
"""
