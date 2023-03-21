# given function
def cons(a, b):
    def pair(f):
        return f(a, b)
    
    return pair


# Using Closures the same way as the given question
def car(pair):
    def first(a, b): return a
    
    return pair(first)


def cdr(pair):
    def last(a, b): return b
    
    return pair(last)


# testing
car(cons(3, 4))
cdr(cons(3, 4))