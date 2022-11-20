def new_pretty(func):
    def new_inner():
        print("Hi, i got decorated")
        func()
    return new_inner()
@new_pretty #aplica essa função na outra
def theNormal():
    print("Hi, I'm the normal")

