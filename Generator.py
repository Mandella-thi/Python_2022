def new_generator():
    x= 0
    print("Our first point here")
    yield x
    x+=1
    print("Our second point here")
    yield x
    x+=1
    print("Our third poin here")
    yield x
new_ob = new_generator()
#print(list(new_ob))

#print(f"The value of x is {next(new_ob)}")
#print(f"The value of x is {next(new_ob)}")
#print(f"The value of x is {next(new_ob)}")

for i in new_ob:
    print(f'The value of x is {i}')

new_list =[i*i for i in range(0,12)] #using List comprehension
new_generator2 =(i*i for i in range(0,12))

print(new_list)
print(new_generator2)
for num in new_generator2:
    print(num)