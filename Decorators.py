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