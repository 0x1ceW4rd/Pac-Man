from collections import deque


class PathFinder:
    
    def __init__(self, maze):
        self.maze = maze

    def bfs(self, start, destination):
        visited = {start}
        parent = {start: None}
        queue =deque([start])
        if not self.maze.cell_checker(start):
            return None

        if not self.maze.cell_checker(destination):
            return None
        while queue:
            current = queue.popleft()
            x, y = current
            neighbors = [
                (x + 1, y),  # RIGHT
                (x - 1, y),  # LEFT
                (x, y + 1),  # DOWN
                (x, y - 1)   # UP
            ]
            if current == destination:
                break
            for neighbor in neighbors:
                if (
                    neighbor not in visited
                    and self.maze.mv_checker(current, neighbor)
                ):
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

        if destination not in parent:
            return None
        path = []
        current = destination

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()
        return path