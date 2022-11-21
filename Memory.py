x =b'Python programing'
print(type(x))
new= memoryview(x)
print(type(new))
print(new)
print(new.obj)
print(new.tolist()) #Asc values-valores ASCII
x=bytearray("Python is so powerful","utf-8")
print(type(x))

y = memoryview(x)
print(y)
print(y[4])
print(chr(y[4]))
new =y.tobytes()
print(type(new))
print(new)
x= memoryview(b'45, 77, 88')
y=x[4]
print(y)
print(type(y))