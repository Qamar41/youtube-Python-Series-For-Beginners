                                        # Functions
# def functionname():
#     body



# def greetings(name,age):
#     print('Good Morning {} , and age is {}'.format(name,age))


# greetings(age=23,name='Qamar')



# *args , **kwargs



def Student (*pos,**nam):

    print(pos)
    print(nam)



subjects=['Math','Chemistry','Biology']

info={ 'name' : 'Ahamd' , 'roll' :'bsf1234'}

Student(*subjects, **info)
Student('Math','Chemistry','Biology' , name = 'Ahamd' , roll ='bsf1234')


