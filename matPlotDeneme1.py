#import matplotlib.pyplot as plt
#year = [1950, 1970, 190, 2010]
#pop = [2.519, 3.692, 5.263, 6.972]
#plt.plot(year,pop)
#plt.show()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
	graph_data = open('example.txt','r').read()
	lines = graph_data.split('\n')
	xs = []
	ys = []
	for line in lines:
		if len(line) > 1:
			x, y = line.split(',')
			xs.append(x)
			ys.append(y)
		ax1.clear()
		ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
