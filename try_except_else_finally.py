#The finally block gets executed no matter if the try block raises any errors or not:

#x = 1

try:
    print(x)
except:
    print("Something went wrong")
else:
    print("Else block got executed, x is defined")
finally:
    print("The 'try except' is finished")