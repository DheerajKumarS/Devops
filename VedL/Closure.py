# basically concept in context of nested function

def outer_fun():
    name = "ved"

    def print_name():
        print(name)

    return print_name()


f = outer_fun()
# del outer_fun
del f


# f()
# outer_fun()

# closure condition :
# must be a nested function... inner func must use the enclosing variable and outer func must return the inner func..

def outer_func():
    leader = "laaduaa"  # enclosing variable

    def inner_func():
        print(leader)

    # name = 'aaaa'
    #  return inner_func()

    return inner_func()


outer_func()
# print(type(outer_func()))

# suppose assign
x = outer_func()
print(type(x))


# x is nonetype as its didn't recived the value... for inner_func()

def outer_func1():
    name = 'Ved'

    def inner_func1():
        # name = "sonu"
        print(name)

    return inner_func1


y = outer_func1()
print(outer_func.__closure__)

print(y.__closure__)
# print(y.__closure__[1].cell_contents) #tuple index out of range
print(y.__closure__)


#


# save some function in list and print them one by one

def func_generator():
    funcs = []  # empty list
    for i in range(3):
        def f():
            return i * 2

        funcs.append(f)
    return funcs


f1, f2, f3 = func_generator()
print(f1(), f2(), f3())

# here we can the code is not returning the correct functional value instead its
# keep on printing 444

print(f1.__closure__[0].cell_contents)
print(f2.__closure__[0].cell_contents)
print(f3.__closure__[0].cell_contents)


# code to print three different values by three different function

def funcs_generator():
    funcs = []
    for i in range(3):
        def f(j=i):
            return j * 2

        funcs.append(f)
    return funcs


f1, f2, f3 = funcs_generator()
print(f1(), f2(), f3())

print(f1.__closure__)
print(f2.__closure__)
# none
# Above function returning means these are not closure as they don't require anything to remember
# As in above case we have i enclosing variable is just being passed to inner function as a parameter
# its not being used as a variable in local inner f()


