from mazegenerator import MazeGenerator
from maze import Maze
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
        self.entry = self.generator.maze_entry
        self.exit = self.generator.maze_exit
        self.maze = Maze(self.width, self.height, self.generator.maze)
 
    
    