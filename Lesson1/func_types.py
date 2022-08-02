
def say_hello(name):
    return f'Hello, {name}'

#say_hello('Roselle')
#print(say_hello('Roselle'))

#example of first class citizenship
def by_first_val(seq):
    #Assumes seq is a iterable with at least 1 element
    return seq[0] #returns first elem of the seq

def by_second_val(seq):
    #Assumes seq is a iterable with at least 1 element
    return seq[1] #returns second elem of the seq

#vvvvvvv another func that accepts 2 param, req a seq
def mirror(seq, filter_=None):
    #Assumes seq is a iterable with at least 1 element
    if filter_: #if filter_ is given
        #assume filter_ is a function with 1 req arg / param
        #feed in the val of seq into filter and return
        return filter_(seq)
    return seq

seq = list(range(3))
out1 = mirror(seq) #no filter func
out2 = mirror(seq, filter_=by_first_val) #not calling bfv func yet
#referencing by_first_val into the filter_ variable^^^^
out3 = mirror(seq, filter_=by_second_val)

print('out1 ->', out1)
print('out2 ->', out2)
print('out3 ->', out3)