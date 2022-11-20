import collections
#usar biblioteca colections
player = collections.namedtuple("player",["name","age", "country"])
p1= player("Fred", 28, "Brazil")
p2= player("Marcelo", 31,"Brazil")
print(p1.age)
print(p1)
firstD =collections.OrderedDict()
firstD["x"]=70
firstD["y"]=75
firstD["E"]=77
firstD["M"]=79
print(firstD)
for a,b in firstD.items():
    print(a,b)
q= collections.deque([5,10,15,20,25])
print(q)