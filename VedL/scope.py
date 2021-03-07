name = "ved"


def print_name():
    name = "python_geek"
    #   print(name)
    return name


f = print_name()
print(f)
print(name)

# change in global variable using Global keyword

name = "ladu"


def print_name1():
    global name
    name = "python-boss"
    return name


y = print_name1()
print(y)
print(name)

# enclosing variables and its concepts
name = 'Laduaaa'


def printname_outer():
    name = 'ved'

    def printname_inner():
        name = "Ladu"
        print(name)

    printname_inner()
    print(name)
    return

# @printname_outer
# def print_outer():
#    name = 'sonu'
#   return name


printname_outer()
print(name)
