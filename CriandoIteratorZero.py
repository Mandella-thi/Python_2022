class Incrementing:
    def __iter__(self):
        self.count =0
        return self
    def __next__(self):
        if self.count <=15:

            x =self.count
            self.count = self.count +1
            return x
        else: raise StopIteration
new_obj = Incrementing()
new_iter = iter(new_obj)
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
for i in new_iter:
    print(i)