
def math(func):

    def pi(num=3.1437):
        func()
 
    return  pi()


def sum(a, b):

    return a + b

value = math(sum(1,4))