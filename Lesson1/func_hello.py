"""
def func_name1():
    return

def func_name2(val):
    return

def func_name3(x, y, z):
    return

def func_name4(val=None):
    return

def func_name5(x=1, y=1, z=1):
    return


def func_name6(x, y=1, z=1):
    return

"""

val = "Hello"
x, y, z = (7, 8, 9)  # multiple assignment


def func_name1():
    return


def func_name2(val):
    return val


def func_name3(x, y, z):

    # Returning multiple values turns them into a tuple
    # i.e. This will return a tuple with 3 elements
    return x, y, z


def func_name4(val=None):
    return val


def func_name5(x=1, y=1, z=1):
    return x, y, z


def func_name6(x, y=1, z=1):
    return x, y, z


print('val ->', val)
print('x, y, z ->', x, y, z)
print('func_name1 ->', func_name1())
print('func_name2 ->', func_name2(6))
print('func_name3 ->', func_name3(6, 7, 8))
print('func_name4 ->', func_name4())
print('func_name5 ->', func_name5())
print('func_name6 ->', func_name6(6, z=8))
