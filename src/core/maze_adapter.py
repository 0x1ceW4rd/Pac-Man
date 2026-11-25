from mazegenerator import MazeGenerator
from src.core.maze import Maze
class Maze_Adapter():
    

    def __init__(self, width, height, seed):
        self.width = width
        self.height = height
        self.seed = seed
        self.generator =  MazeGenerator(
                size=(self.width, self.height),
                perfect=False,
                seed=self.seed
                )
    def maze(self):
        maze = Maze(self.width, self.height, self.generator.maze)
        return maze
    
    