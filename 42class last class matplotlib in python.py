from matplotlib import pyplot as plt

# x-axis values

x = [5, 2, 1, 4, 7]
# Y-axis values

y = [10, 5, 8, 4, 2]
# Function to plot

plt.plot(x,y)
# function to show the plot
plt.show()

from matplotlib import pyplot as plt
plt.plot([1,2,3],[4,5,1])
plt.show()

from matplotlib import pyplot as plt
x=[5,8,10]
y=[12,16,6]
plt.plot(x,y)
plt.title("Durga")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.show()

from matplotlib import pyplot as plt

x=[5,8,10]
y=[12,16,6]
x2=[6,9,11]
y2=[6,15,7]
plt.plot(x,y,'g',label="line one",linewidth=3)
plt.plot(x2,y2,'r',label="line two",linewidth=5)
plt.title("Durga")
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.legend()
plt.grid(True,color='k')
plt.show()

from matplotlib import pyplot as plt

plt.bar([1,3,5,7,9],[5,2,7,8,2],label="Example one")
plt.bar([2,4,6,8,10],[8,6,2,5,6],label="Example two",color='g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title("Bar Graph")
plt.show()

from matplotlib import pyplot as plt
ages=[22,56,78,23,54,67,98,12,34,57,89,34,67,83,49,23,75,39,23,56,78,90]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(ages,bins,histtype='bar',rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Histogram")
plt.show()

from matplotlib import pyplot as plt
x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]
plt.scatter(x,y,label='skitscat',color='k',s=40,marker="*")
plt.xlabel('x')
plt.ylabel('y')
plt.title("ScatterPlot")
plt.show()

from matplotlib import pyplot as plt

days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]

plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=5)
plt.plot([],[],color='r',label='working',linewidth=5)
plt.plot([],[],color='k',label='playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])
plt.xlabel('x')
plt.ylabel('y')
plt.title("Stack plot")
plt.legend()
plt.show()

from matplotlib import pyplot as plt

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0, 0, 0),
        autopct='%1.1f%%'
        )

plt.title("PiePlot")
plt.show()