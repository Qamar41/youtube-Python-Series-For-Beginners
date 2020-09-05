                                                  # Scope 


# LEGB
# Local , Enclosing , Global , BuiltIn



# x='Glbal x'

# def testing(new):

    
#     x= f'local x {new}'

#     print(x)


# testing('hello')


# print(new)
# # print(x)





def min():
    pass


# min()





# min([2,3,5,6,1,8])

# # print(m)

# import builtins


# print(dir(builtins))

x = 5

def outer():
    # x='outer x'

    # print(x)

    def inner():

        # x='inner x'
        print(x)

    inner()


outer()