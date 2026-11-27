from maze_adapter import Maze_Adapter
from pathfinder import PathFinder
print("LEVEL.PY IS RUNNING")

class Level():
    def __init__(self, width, height, seed):
        self.width = width
        self.height = height
        self.seed = seed
        self.maze_adapter = Maze_Adapter(self.width, self.height, self.seed)
        self.maze = self.maze_adapter.maze
        self.entry = self.maze_adapter.entry
        self.exit = self.maze_adapter.exit

lvl = Level(10, 10, 42)
print(lvl.maze)
print(lvl.entry)
print(lvl.exit)
bfs = PathFinder(lvl.maze)
print(bfs.bfs(lvl.entry, lvl.exit))
