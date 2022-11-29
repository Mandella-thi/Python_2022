numbers= [10,20,30,40,50,60,70]
new_iterator = iter(numbers)
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
seq ="Iterator tutorial in python"
new_iterator = iter(seq)
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
def new_iterator1(n):
    my_iterable = iter(n)
    while True:
        try:
            print(next(my_iterable))
        except StopIteration:
            break
new_iterator1(seq)



