from mazegenerator import MazeGenerator
import sys, pygame, os

maze = MazeGenerator()

maze.generate()


print(maze.maze)
