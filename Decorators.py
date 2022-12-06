def adding(num):
    return num+1
adding_one = adding
print(adding_one(10))

def adding(num):
    def adding_one(num):
        return num + 1
    total = adding_one(num)
    return total

print(adding(12))
def calling(new_func):
    new_number = 12
    return new_func(new_number)

print(calling(adding))

def hello():
    def greeting():
        return "Hi there"
    return greeting
new_greet =hello()
print(new_greet())