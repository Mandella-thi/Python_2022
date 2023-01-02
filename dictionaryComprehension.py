numbers =[100, 200, 300, 400, 500]
students =["Joe", "Ronald", "Ahmed", "Marcelo", "Alves"]
new_dict = {x: y for (x,y) in zip(numbers,students)}
print(new_dict)
