print("Hello, World!");

if 5 > 2:
    print("Five is greater than two!")

### COMMENTS ###

#This is a comment
"""
A
multi 
line
comment
"""

### VARIABLES ###

x = 5
y = "John"
print(x)
print(y)

x = 4
x = "Sally"
print(x)

x = str(3)      # x will be '3'
y = int(3)      # y will be 3
z = float(3)    # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite
print(a, type(a), A, type(A))

myvar="John"
my_var="John"
_my_var="John"
myVar="John"
MYVAR="John"
myvar2="John"
myVariableName="John"
MyVariableName="John"
my_variable_name="John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

a=b=c="Orange"
print(a)
print(b)
print(c)

fruits=["apple","banana","cherry"]
d,e,f=fruits
print(d)
print(e)
print(f)

g = "Python is awesome"
print(g)

h="Python"
i="is"
j="awesome"
print(h, i, j)

k="Python "
l="is "
m="awesome"
print(k+l+m)

n=5
o=10
print(n+o)

p=5
q="John"
print(p,q)

r="awesome"
def myfunc():
    print("Python is " + r)

myfunc()

s="awesome"
def myfunc1():
    s="fantastic"
    print("Python is " + s)

myfunc1()

print("Python is " + s)

def myfunc2():
    global t
    t = "fantastic"

myfunc2()

print("Python is " + t)

u="awesome"

def myfunc3():
    global u
    u = "fantastic"

myfunc3()

print("Python is " + u)

### DATA TYPES ###

v = 5
print(type(v))

v1 = "Hello World"                              #str - string
v2 = 20                                         #int - integer
v3 = 20.5                                       #float - floating point number
v4 = 1j                                         #complex - complex value
v5 = ["apple", "banana", "cherry"]              #list
v6 = ("apple", "banana", "cherry")              #tuple
v7 = range(6)                                   #range
v8 = {"name" : "John", "age" : 36}              #dict - dictionary = key:value pair
v9 = {"apple", "banana", "cherry"}              #set
v10 = frozenset({"apple", "banana", "cherry"})  #frozenset
v11 = True                                      #bool - boolean
v12 = b"Hello"                                  #bytes
v13 = bytearray(5)                              #bytearray
v14 = memoryview(bytes(5))                      #memoryview
v15 = None                                      #NoneType

print(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15)

## CONSTRUCTOR FUNCTIONS ##
v16 = str("Hello World")
v17 = int(20)
v18 = float(20.5)
v19 = complex(1j)
v20 = list(("apple", "banana", "cherry"))
v21 = tuple(("apple", "banana", "cherry"))
v22 = range(6)
v23 = dict(name="John", age=36)
v24 = set(("apple", "banana", "cherry"))
v25 = frozenset(("apple", "banana", "cherry"))
v26 = bool(5)
v27 = bytes(5)
v28 = bytearray(5)
v29 = memoryview(bytes(5))

print(v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29)

### PYTHON NUMBERS ###

v30 = 1         #int
v31 = 2.8       #float
v32 = 1j        #complex

print(v30, type(v30))
print(v31, type(v31))
print(v32, type(32))

## INTEGERS ##

v33 = 1
v34 = 3565622554887711
v35 = -3255522

print(v33, type(v33))
print(v34, type(v34))
print(v35, type(v35))

## FLOATS ##
v36 = 1.10
v37 = 1.0
v38 = -35.59

print(v36, type(v36))
print(v37, type(v37))
print(v38, type(v38))

v39 = 35e3
v40 = 12E4
v41 = -87.7e100

print(v39, type(v39))
print(v40, type(v40))
print(v41, type(v41))

## COMPLEX NUMBERS ##
v42 = 3+5j
v43 = 5j
v44 = -5j

print(v42, type(v42))
print(v43, type(v43))
print(v44, type(v44))

## TYPE CONVESRION ##

v45 = 1     #int
v46 = 2.8   #float
v47 = 1j    #complex

#convert from int to float:
v48 = float(v45)

#convert from float to int:
v49 = int(v46)

#convert from int to complex:
v50 = complex(v47)

print(v45, type(v45), v48, type(v48))
print(v46, type(v46), v49, type(v49))
print(v47, type(v47), v50, type(v50))

## RANDOM NUMBER ##
import random

print(random.randrange(1, 10))

### PYTHON CASTING ###
v51 = int(1)        #v51 will be 1
v52 = int(2.8)      #v52 will be 2
v53 = int("3")      #v53 will be 3

print(v51, type(v51), v52, type(v52), v53, type(v53))

v54 = float(1)      #v54 will be 1.0
v55 = float(2.8)    #v55 will be 2.8
v56 = float("3")    #v56 will be 3.0
v57 = float("4.2")  #v57 will be 4.2

print(v54, type(v54), v55, type(v55), v56, type(v56), v57, type(v57))

v58 = str("s1")     #v58 will be 's1'
v59 = str(2)        #v59 will be '2'
v60 = str(3.0)      #v60 will be '3.0'

print(v58, type(v58), v59, type(v59), v60, type(v60))

### STRINGS ###
print("Hello")
print('Hello')

v61 = "Hello"
print(v61)

## MULTI LINE STRINGS ##
v62 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(v62)

v63 = '''Lorem ipsom dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod empor incididunt
ut labore et dolore magna aliqua'''

print(v63)

v64 = "Hello, World!"

print(v64[1])

for x in "banana":
    print(x)

## STRING LENGTH ##
v65 = "Hello, World!"
print(len(v65))

## CHECK STRING ##
txt = "The best things in life are free!"
print("free" in txt)

txt1 = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present in variable txt1.")

txt2 = "The best things in life are free!"
print("expensive" not in txt2)

txt3 = "The best things in life are free!"
if "expensive" not in txt3:
    print("No, 'expensive' is NOT presentin variable txt3.")

### STRING SLICING ###
txt4 = "Hello, World!"
print(txt4[2:5])

txt5 = "Hello, World!"
print(txt5[:5])

txt6 = "Hello, World!"
print(txt6[2:])

txt7 = "Hello, World!"
print(txt7[-5:-2])

### MODIFY STRINGS ###
txt8 = "Hello, World!"
print(txt8.upper())

txt9 = "Hello, World!"
print(txt9.lower())

txt10 = " Hello, World! "
print(txt10.strip()) #returns "Hello, World!"

txt11 = "Hello, World!"
print(txt11.replace("H", "J"))

txt12 = "Hello, World!"
print(txt12.split(",")) #returns ['Hello', 'World!']

txt13 = "Hello,"
txt14 = "World!"
txt15 = txt13 + txt14
print(txt15)

txt16 = "Hello,"
txt17 = "World!"
txt18 = "Hello, World!"
print(txt18)

### FORMAT STRINGS ###
age = 36
txt19 = "My name is John, and I am {}"
print(txt19.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity1 = 3
itemno1 = 567
price1 = 49.95
myorder1 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder1.format(quantity1, itemno1, price1))

### ESCAPE CHARACTERS ###
txt20 = "We are to so called \"Vikings\" from the north."
print(txt20)

txt21 = "this is a string..."
print(txt21.capitalize())

txt22 = "THIS IS ANOTHER STRING!"
print(txt22.casefold())

print("Centered text:", txt21.center(50))
print("\"a\" appears", txt21.count("a"), "time in string txt21")

print("UTF-8 encoded string: ", txt21.encode())

print("txt21 ends with '.': ", txt21.endswith('.'))

txt23 = "H\te\tl\tl\to"
print(txt23.expandtabs(2))

txt24 = "Hello, welcome to my world."
print("'welcome' is found at position", txt24.find("welcome"), "in txt24.")

txt25 = "For only {price:.2f} dollars!"
print("txt25 formated:", txt25.format(price = 49))

print("'welcome' found at index", txt24.index("welcome"), "in string txt24.")

txt26 = "Company12"
print("txt26('",txt26, "') is alphanumeric:", txt26.isalnum())

txt27 = "Company123"
print("txt27('", txt27, "') is ascii:", txt27.isascii())

txt28 = "1234"
print("txt28('", txt28 , "') is decimal: ", txt28.isdecimal())

txt29 = "50800"
print("txt29('",txt29,"') is made of digits:", txt29.isdigit())

txt30 = "Demo"
print("txt30('",txt30,"') is a valid identifier(made of:[a-z] | [0-9] | [_]):", txt30.isidentifier())

print(txt21, "is lowercase:", txt21.islower())

txt31 = "565543"
print(txt31, "is numeric:" , txt31.isnumeric())

txt32 = "Hello! Are you #1?"
print(txt32, "is printable:", txt32.isprintable())

txt33 = "     "
print(txt33, "is whitespaces:", txt33.isspace())

txt34 = "Hello, And Welcome To My World!"
print(txt34, "is a title(each word is capitalized):", txt34.istitle())

print(txt22, "is uppercase:", txt22.isupper())

myTuple = ("John", "Peter", "Vicky")
print("#".join(myTuple))

