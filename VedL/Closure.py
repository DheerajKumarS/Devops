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
