import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Set the size of the grid
GRID_SIZE = 50

# Set the probability of a cell being alive at the start
INITIAL_PROBABILITY = 0.5

# Set the number of generations to simulate
NUM_GENERATIONS = 10

# Set up the grid
grid = np.random.choice([0, 1], size=(GRID_SIZE, GRID_SIZE), p=[1-INITIAL_PROBABILITY, INITIAL_PROBABILITY])

def count_neighbors(x, y):
  """Count the number of live neighbors for a cell at (x, y)"""
  num_neighbors = 0
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      if (i != x or j != y) and i >= 0 and i < GRID_SIZE and j >= 0 and j < GRID_SIZE:
        num_neighbors += grid[i][j]
  return num_neighbors

def update_grid():
  """Update the state of the grid based on the rules of the Game of Life"""
  global grid
  new_grid = np.zeros((GRID_SIZE, GRID_SIZE))
  for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
      num_neighbors = count_neighbors(i, j)
      if grid[i][j] == 1:
        if num_neighbors == 2 or num_neighbors == 3:
          new_grid[i][j] = 1
      else:
        if num_neighbors == 3:
          new_grid[i][j] = 1
  grid = new_grid

# Set up the plot
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='gray')

# Define the animation function
def animate(i):
  """Update the plot for the ith generation"""
  update_grid()
  im.set_data(grid)
  return im,

# Run the animation
anim = animation.FuncAnimation(fig, animate, frames=NUM_GENERATIONS, repeat=True, interval=100)
plt.show()