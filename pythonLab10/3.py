import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

def f(a, b):
    t = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    x = np.sin(a * t)
    y = np.sin(b * t)
    return x, y

line = ax.plot([],[])[0]
ax.set(xlim=[-1, 1], ylim=[-1, 1])
b = 3
def update(frame):
    freq = (b*frame/100, b)
    x, y = f(freq[0], freq[1])
    line.set_xdata(x)
    line.set_ydata(y)
    return line


anim = animation.FuncAnimation(fig=fig, func=update, frames=101, interval=100)
plt.show()
