# myfloat = 7.0
# print (myfloat)
# myfloat = float (5)
# print myfloat)

# mystring = "hello world"
# print (mystring)
# mystring = 'hello'
# print(mystring)
# mystring = "what a wonderful world"
# print (mystring)


# one = 1
# two = 2
# three = one + two
# print (three)

# hello = ' hello'
# world = ' world'
# helloworld = hello + '' + world
# print (helloworld)

# a, b  = 3 , 4
# print (a,b)
# print ( a + b)


# cannot mix number with strings. It will give error message.
# one = 1
# two = 2
# hello = "hello"
# print (one + two + hello)

mystring  = 'hello world'
myfloat = 10.0
myint = 20

if mystring == "hello world":
    print ("string: %s" %mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print ("Float: %f" %myfloat)
if isinstance(myint, int) and myint == 20:
    print ("Integer: %d" %myint)

