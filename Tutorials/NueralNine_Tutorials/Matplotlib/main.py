import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

x_data = np.random.random(1000) * 100
y_data = np.random.random(1000) * 100

plt.scatter(x_data, y_data, c='red', marker='*',s=150,alpha=0.3)
plt.show()

years = [2006 + x for x in range(16)]
weights = np.random.randint(low=80,high=90,size=(16,))

plt.plot(years, weights, c='b', lw=3,linestyle="--")
plt.show()

plt.plot(years, weights, "bo--" ,lw=3)
plt.show()

x = ["C++", "C#", "Python", "Java", "Go"]
y = [20,50,140,1,45]

plt.bar(x,y, color='r')
plt.show()

plt.bar(x,y, color='b',align="edge",width=0.5,edgecolor="g",lw=6)
plt.show()

ages = np.random.normal(20,1.5,1000)
plt.hist(ages, bins=20)
plt.show()

plt.hist(ages, bins=[ages.min(), 18, 21, ages.max()])
plt.show()

plt.hist(ages, bins=20, cumulative=True)
plt.show()

langs = ["C++", "C#", "Python", "Java", "Go"]
votes = [20,50,140,1,45]
explodes = [0,0,0.3,0,0]

plt.pie(votes,labels=langs,explode=explodes,autopct="%.2f%%",startangle=90)
plt.show()

heights = np.random.normal(172,8,300)

plt.boxplot(heights,vert=False)
plt.show()


years = [2014 + x for x in range(10)]
income = np.linspace(start=50, stop=80,endpoint=True,num=10)

income_ticks = list(range(45,82,2))

plt.plot(years,income)
plt.title("Income of John (in USD)",fontsize=20, fontname='Times New Roman')
plt.xlabel("Years")
plt.ylabel("Yearly Income in USD")
plt.yticks(income_ticks, [f"{x}k USD" for x in income_ticks])
plt.show()


stock_a = np.linspace(start=50, stop=80,endpoint=True,num=10)
stock_b = np.linspace(start=10, stop=30,endpoint=True,num=10)
stock_c = np.linspace(start=100, stop=130,endpoint=True,num=10)

plt.plot(stock_a,label="Apple")
plt.plot(stock_b,label="Microsoft")
plt.plot(stock_c,label="Meta")
plt.grid(True)

plt.legend(loc="lower center")
plt.show()

langs = ["C++", "C#", "Python", "Java", "Go"]
votes = [20,50,140,1,45]


plt.pie(votes,autopct="%.2f%%",startangle=90,pctdistance=1)
plt.legend(labels=langs)
plt.show()

x = np.arange(100)

fig, ax = plt.subplots(nrows=2,ncols=2)

ax[0,0].plot(x, np.sin(x))
ax[0,0].set_title("Sine Wave")

ax[0,1].plot(x, np.cos(x))
ax[0,1].set_title("Cosine Wave")

ax[1,0].plot(x, np.random.random(100))
ax[1,0].set_title("Random Function")

ax[1,1].plot(x, np.log(x),label="Test")
ax[1,1].set_title("Log Function")
ax[1,1].legend(loc="lower center")

fig.suptitle("Four Plots")

plt.tight_layout()

plt.savefig("Test.png", dpi=300, transparent=False,bbox_inches='tight')

plt.show()

ax = plt.axes(projection="3d")

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

ax.scatter(x,y,z)
ax.set_title("3D Plot")
ax.set_xlabel("Test")
ax.set_zlabel("Bryh")
plt.show()


ax = plt.axes(projection='3d')

x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)

X,Y = np.meshgrid(x,y)

Z = np.sin(X) * np.cos(Y)

ax.plot_surface(X,Y,Z,cmap="Spectral")
ax.set_title("3D Plot")
ax.set_xlabel("Test")
ax.set_zlabel("Bryh")
plt.show()


import random

head_tails = [0,1]

for _ in range(100000):
    head_tails[random.randint(0,1)]+=1
    plt.bar( ["Heads","Tails"],head_tails,color=['red','blue'])
    plt.pause(0.001)
plt.show()