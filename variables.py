#casting of variables
a= int(3.4)
print(type(a))

#variable name can not start with a number

_a=0
print(_a)

#camel case
myVarName =90
print(myVarName)

#pascalcase
MyVarName = 78
print(MyVarName)

#Snakecase
myvarname =98
print(myvarname)

#assigning multiple variables
a,b,c = "hi","hey","hello"
print(a)
print(b,c)

list1 = ["aple",1,2]
x,y,z = list1


#global variables
x="ji"
def myfun():
    global x 
    x = "fan"
    print(x)
    
myfun()
print(x)