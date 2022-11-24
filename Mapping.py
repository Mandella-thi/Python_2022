new_list =[10,20,30,40,50]
def addition(n):
    return n+5
my_list = map(addition, new_list)
print(my_list)
for item in my_list:
    print(item)
def adding(x,y):
    return x+y
my_list= map(adding,('apple ','watermelon '),('banana','fig'))
print(tuple(my_list))
print(type(my_list))

new_list =[5,12,20,25,30]
cube_n =map(lambda n: n*n*n, new_list)
print(cube_n)
print(tuple(cube_n))
number1 =[10,20,30]
number2 =[40,50,60]
new_result = map(lambda a,b: a*b, number1, number2)
print(new_result)
print(list(new_result))