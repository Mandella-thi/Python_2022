x =b'Python programing'
print(type(x))
new= memoryview(x)
print(type(new))
print(new)
print(new.obj)
print(new.tolist())
x=bytearray("Python is so powerful","utf-8")
print(type(x))

