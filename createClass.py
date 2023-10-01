#Create a class(design, blueprint, guideline)
#class/design object/result():
class TutoringCenter(): #(entire task.full product)
    def tutoring_students(self, x, y): #self == object/result/TtoringCenter
        return x + y
#Instantiate some objects of the class(some attributes/parts of the final product created by that guideline)
course = TutoringCenter() #one instance/part of the product, subtask)
course.date = '2015-01-01' #attribute
course.title = 'Python Basics' #attribute
course.description = 'Learn the basics of Python' #attribute
course.tutoring_students(course.date, course.title)
#each of these attributes are related to one instance/part/subtask of the class
print(course.tutoring_students(course.date, course.title))
"""
print(type(course)) # <class '__main__.TutoringCenter'> HERE I created my own data type
print(type(course.date))
print(type(course.title))
print(type(course.description))

class/design object/result(self/object, parameters)
            |
            |
instance/subpart of the result
            |
            |
attributes/properties of the instance
            |
            |
object/result.method(parameters)
"""

class ZinnahFamily():
    def zinnah_children(self, x, y):
        return x * y

daughter = ZinnahFamily()
daughter.NAME = 'Fariha'
daughter.age = 21
daughter.gender = 'Female'
daughter.salary = 20
daughter.hours_worked = 40
daughter.zinnah_children(daughter.salary, daughter.hours_worked)
print(daughter.zinnah_children(daughter.salary, daughter.hours_worked))
