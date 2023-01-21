class A(object):
    def __init__(self):
        pass


a = A()
print(a)


class B(object):
    def __new__(cls, *args, **kwargs):
        print("new")
        return super(B, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print("init")
        super(B, self).__init__(*args, **kwargs)


b = B()
print(b)


class C(object):
    def __call__(self, *args, **kwargs):
        """ call new first then init before call"""
        super(C, self).__call__(*args, **kwargs)


c = C()
print(c)

'''
in python everything is object like type , int , etc
everything inherits from object on its type
base class for everything is type
'''


class DMeta(type):
    def __call__(cls, *args, **kwargs):
        print("call")
        return super(DMeta, cls).__call__(*args, **kwargs)

    def __init__(cls, name, bases, dct):
        print("init")
        super(DMeta, cls).__init__(name, bases, dct)


class D(metaclass=DMeta):
    pass


print(D())


E = type('E', (), {})
print(E())

F = type('Bar', (E,), dict(attr=100))
print(F())
print(F().attr)

'''
Since type is a metaclass, that makes Meta a metaclass as well.
In the same way that a class act as a template for the creation of objects, 
a metaclass act as a template for the creation of classes. 
Metaclasses are sometimes referred to as class factories.
'''
