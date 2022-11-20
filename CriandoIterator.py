class NewNumbers:
    def __iter__(self):
        self.a =1
        return self
    def __next__(self):
        if self.a <=17:
            x= self.a
            self.a+=1
            return x
        else:
            raise StopIteration
newclass = NewNumbers()
newiter= iter(newclass)
print((next(newiter)))
print((next(newiter)))
print((next(newiter)))
print((next(newiter)))
print((next(newiter)))
for x in newiter:
    print(x)
degree = 25
newtext ="The degree is {} celsius."
print(newtext.format(degree))