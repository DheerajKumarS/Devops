def func(*argv):
    for arg in argv:
        print(arg)


func("hi", "how", "are", "you")


# *args is defined to take more arguments than the number of arguments defined earlier
# it helps to pass a non-keyword, variable length argument lists

def func1(arg1, *args):
    print("first argument:", arg1)
    for arg in args:
        print("argument in *args", arg)


func1("hello", "Duggiee", "what", "are", "you", "doing")


# **kwargs is used to pass keyworded parameter, argument lists... double star helps us to pass keyword arguments.
# One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it.
# That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out

def myfunc(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myfunc(first='Ved', mid='Ved', last='Ved')
# here we have multiple arguments which is similar as key value and is listed as dict

