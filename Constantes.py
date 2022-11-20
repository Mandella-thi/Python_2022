PI =3.14
print(PI)
PI=2.10
print(PI)
drink = "avalible"
food = None
#função
def new_menu(a):
    if a ==drink:
        print(drink)
    else:
        print(food)

new_menu(drink)
new_menu(food)
#tipos de listas em pyton
fruits =["fig", "lemon", "Banana"]#lIST
numbers=(1,2,3,4)#tuple, são imutáveis
words= {"First word": 'Banana', "Second word": "Hi"}#dicttionary
chars={"A","B","C"}#set

#tipos de numeros em python
x=5
y= 3.5
z = 2 +3j
print(x, "is of type", type(x))
print(y, "is of type", type(y))
print(z, "is of type", type(z))

mix =[2,3.7, 'hi']
print(type(mix))
print("Separador no print")
print(1,3,5,7,8, sep= "*")
print(1,3,5,7,8, sep= "*", end="&")
print("Formatar saída do print")
print("The value of x is {} and the value of y is {}".format(x, y))
print(3/2)
myList =["Arroz", "feijao", "bolo"]
for i in myList:
    print(i)
    for j in i:
        print(j)
fruits =["fig", "apple", "watermelon"]
fruits.append("Orange")
print(fruits)
fruits2 =["lemon","cherry"]
fruits.extend(fruits2)
print(fruits)
fruits.remove("watermelon")
print(fruits)
fruits.pop(1)
print(fruits)
del fruits[0]
print(fruits)
newfruits= ("fig", "banana", "lemon")
print(newfruits)
print(len(newfruits))
print(type(newfruits))
fruits_set={"apple","Oranje", "lemon"}
print(fruits_set)

xi= "Paralelepipedo de crack"
xi= xi[1:22]
print(xi)


def new_function():
    print("Hi, from the new_function")

new_function()
def soma(a,b):
    return a+b
print(soma(1,2))
def hi_function(name = "Marcelo"):
    print("Hi "+ name)

hi_function("Thiago")
def new_names(name1, name2, name3):
    print("The first name is: "+name1)
    print("The second name is: " + name2)
    print("The last name is: " + name3)

new_names("Q","Marcel","John")
def numbers(n):
    if(n>0):
        result = n + numbers(n-1)
        print(result)
    else:
        result =0
    return result
print(numbers(4))
p= lambda i: i+10
print(p(5))
calculate= lambda x, y: x*y
print(calculate(5,7))
math_op = lambda x, y, z: x*y +z
print(math_op(2,3,4))
#Lambda with user function
def multiply(n):
    return lambda x:x*n
double = multiply(2)
triple = multiply(3)
print(double(10))
print(triple(10))
class NewClass:
    num =10
print(NewClass)
p1= NewClass()
print(p1.num)
#using init
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
ob1 = Person("Dony", 40)
print(ob1.name)
print(ob1.age)
f = open("Hi.txt","r") #r de ler o arquivo
#print(f.read())
#print(f.readline())
#print(f.readline())
for x in f:
    print(x)
f.close()
#f = open("main.txt", "a")
#f.write("another one bites the dust")
#f.close()
f=open("main.txt","r")
print(f.read())
f.close()
import platform
a = platform.system()
print(a)
