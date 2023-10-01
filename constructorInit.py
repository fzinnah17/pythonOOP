class CcnyDegree(): #curriculum/design to geth the degree from this instituition
    
    credits_completed = 45
    #assign all the attributes we want to assign to the object/result/product in the parameters of the constructor
    def __init__(self, name, credits = None, courses = None, department = None): #constructor

        #Run validations
        assert credits > 0, f"Credits {credits} should be greater than zero"
        assert courses > 0, f"Courses {courses} should be more than zero" 

        # Assign attributes to self object
        print(f'The instances are: {name}')
        #dynamic attribute assignment
        self.name = name
        self.credits = credits
        self.courses = courses
        self.department = department
        #(self, name, credits = None, courses = None, department = None)
        #assigning to None means we don't have to pass in anything to the parameters

    def engineering_degree(self): #we don't have to pass in separate parameters anymore
        return self.credits * self.courses
    
    def student_finished(self):
        return self.courses * self.credits_completed #using self helps to use any class/instance level attribute

#instance/subpart of the class/design
computer_engineering = CcnyDegree('Computer Engineering', 120, 26)
#having constructor also allows us to have separate attribute outside
computer_engineering.students = True
print(computer_engineering.student_finished())




#instance/subpart.method/function 
#               |
#               |
# returns the result from the method call
print(computer_engineering.engineering_degree())

print(CcnyDegree.__dict__) #class attribute
print(computer_engineering.__dict__) #instance attribute

#attributes/properties of the instance
# computer_engineering.credits = '120'
# computer_engineering.courses = ['Calculus', 'Physics', 'Programming', 'Electronics']
# computer_engineering.department = 'Grove School of Engineering'
#instance/subpart.method/functions/ability to give me the degree(objext/result/product, parameters)
# computer_engineering.engineering_degree(computer_engineering.department, computer_engineering.credits)

# print(computer_engineering.engineering_degree(computer_engineering.department, computer_engineering.credits)
# )
"""print(computer_engineering.name)
print(computer_engineering.credits)
print(computer_engineering.courses)
print(computer_engineering.department)
Computer Engineering
120
['Calculus', 'Physics', 'Programming', 'Electronics']
Grove School of Engineering"""