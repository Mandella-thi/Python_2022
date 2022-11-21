new_list =[10,20,30,40,50]
def addition(n):
    return n+5
my_list = map(addition, new_list)
print(my_list)
for item in my_list:
    print(item)