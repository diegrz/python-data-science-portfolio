import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
from random_walk import RandomWalk 

rw = RandomWalk(500)
rw.fill_walk()

fig, ax = plt.subplots()

def update(frame):
	"""Esta funcion ejecuta cada frame"""
	ax.clear()

	ax.scatter(rw.x_values[:frame], rw.y_values[:frame], s=10)
	
	#ax.plot(rw.x_values[:frame], rw.y_values[:frame], linewidth=1)
	ax.set_title(f"Paso: {frame}")


# Animación

ani = FuncAnimation(fig, update, frames=len(rw.x_values), interval=0.1, repeat=False)

plt.show()