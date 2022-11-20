import matplotlib.pyplot as plt
x=[0,2,4,6]
y=[1,3,4,8]
plt.plot(x,y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Plotted x and y values")
plt.legend("Data 1")
#Saving the plot
plt.savefig("plot.png",dpi= 350,bbox_inches='tight')
plt.show()