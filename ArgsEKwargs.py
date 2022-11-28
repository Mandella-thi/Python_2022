def addition(*args):
    result =0
    for x in args:
        result = result + x
    print(result)
addition(12,13)

def newOrder(**kwargs):
    for key, value in kwargs.items():
        print("{} is equal to {}".format(key, value))

newOrder(Tea ="Green", price =1.8, size ="medium")