def start():
    #GLOBAL_CONSTANT_NAME =  a value that should never change within the program's execution
    # Personal Details
    NAME = 'Farnaz'
    # print(NAME)
    # print(type(NAME))

    #Birthday Details
    BIRTHDAY = '08/17/1997'
    # print(BIRTHDAY)
    # print(type(BIRTHDAY))

    age = 26
    # print(age)
    # print(type(age))

    #Wage Calculation

    hourly_wage = 29.5 #will change in the future
    hours_worked = 31 #changes every week
    weekly_wage = hourly_wage * hours_worked
    # print(weekly_wage)
    # print(type(weekly_wage))

if __name__ == '__main__': #name of the current module
    start()