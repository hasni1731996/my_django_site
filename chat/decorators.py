def Params(oldFunc):
    def inside(*args,**kwargs):
        print('in Decorator function')
        print('Entered arrguments..',args,kwargs)
        return oldFunc(*args,**kwargs)
    return inside

@Params
def Multi(x,y=10):
    print('in actual function')
    print('SUMM of arguments...from Multi func',x+y)

Multi(2,5)
#Multi(2,5,name='hassan',age=22) #####If we want to pass dict to function ##########

##############Implimenting Python's Class Method & Static Method Decorators #############
# class Person(object):

#     def __init__(self, first_name, last_name):
#         print('in Constructor')
#         self.first_name = first_name
#         self.last_name = last_name
#         print(first_name,last_name)
        
#     @classmethod
#     def get_person(cls, first_name):
#         print('in class method decorator')
#         return cls(first_name, "") ###here it only gets the first_name from class instance & then return it to constructor

#     @staticmethod  
#     def validate_name(name):
#         print (len(name))
#         if len(name) > 5:
#             print('grater than length 5')

#         else:
#             print('equal or less than length 5')

# # Person('hassan','khan') ### it gives consturctor call & print both first_name & last_name 
# # Person.get_person('hasni') ### it gives @classmethod call & only prints first_name
# Person.validate_name('hahahahah8e8e8e8e8e8e8e8e')

###########ENDS##############################
