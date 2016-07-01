def myfunc(a, b):
    print(a, b)


# using myfunc:

a = 1

myfunc(a,b=3)
#In the original text, there was no value for b, meaning the function will print an error. Thus, you would need to add a value to
#b in order for "myfunc" to print. It will print 1,3.
