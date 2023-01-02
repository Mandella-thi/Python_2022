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

newList = []
for new_char in "Power of comprehension!":
    newList.append(new_char)

print(newList)
newList2 =[new_char for new_char in "Power of comprehension!"]
print(newList2)

new_matrix =[]
for x in range(5):
    new_matrix.append([])
    for y in range(8):
        new_matrix[x].append(y)
print(new_matrix)

new_matrix2 =[ [y for y in range(8)] for x in range (5)]
print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
print(new_matrix2)