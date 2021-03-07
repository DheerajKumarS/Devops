def add_author(func):  # simple decorator func
    print('ved')
    return func


@add_author
def get_title(func1):
    print('planet songs')
    return func1


# print(get_title())
# is not required for when we are passing func to get_publications


# @get_title
def get_publication():
    return 'laadu'


get_publication = get_title(get_publication)

print(get_publication())


# wrap a function Decortaor behaviour

def add_things(func):
    def wrapper():
        title = func()
        new_title = title + ' !!!'
        return new_title

    return wrapper


# @add_things
def get_title():
    return 'laduaaaaaaaa'


get_title = add_things(get_title)
print(get_title())


