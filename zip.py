h ={}
#for i in zip([1,2,3],['x','y','z']):
    #global h


 #   print(i)
#print(x)

#unzipping
unzipping = zip([10,20,30],['x','y','z'],['$','@','*'])
x,y,z = zip(*unzipping)
print(x,y,z)