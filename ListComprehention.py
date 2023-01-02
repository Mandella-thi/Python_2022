fruits_list =["fig", "banana","kiwi", "cherry"]
my_list = []

for item in fruits_list:
    if "i" in item:
        my_list.append(item)

print(my_list)
mo_list= []
for item in fruits_list:
    if len(item) >3:
        mo_list.append(item)

print(mo_list)

