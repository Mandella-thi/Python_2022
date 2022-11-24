names =["Ahmed","Ibra","Joe", "Marcelo"]
new_enum = enumerate(names)
print(type(new_enum))
print(list(new_enum))
for index, name in enumerate(names):
    print(index, name)
names=["Ahmed", "Ibra", "Joe", "Marcelo"]
new_enum= enumerate(names)
print(new_enum.__next__())
print(new_enum.__next__())