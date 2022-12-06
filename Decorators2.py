def new_message(text):
    "Outer message"
    def another_message():
        "Our nested mensage"
        print(text)
    another_message()

print(new_message("hello, this is a randon text message"))
print(new_message)
def new_capital(new_func):
    def new_inner():
        the_func = new_func()
        upper_case = the_func.upper()
        return upper_case
    return new_inner

def greeting():
    return "hi, python programing"
new_decorating = new_capital(greeting)
print(new_decorating())

@new_capital
def greeting2():
    return "hi, python programing2"

print(greeting2())