class Maze():
    direction_value ={"RIGHT":2, "LEFT":8, "UP":1, "DOWN":4}
    opposite_direction = {
        "RIGHT": "LEFT",
        "LEFT": "RIGHT",
        "UP": "DOWN",
        "DOWN": "UP"
    }

    def __init__(self, width, height, cells):
        
        self.width = width
        self.height = height
        self.cells = cells
    def cell_checker(self, cell):
        x ,y = cell
        if  y < self.height and x < self.width and y >= 0 and x >= 0:
            return True
        return False
    
    def mv_checker(self, current, destination):
        if self.cell_checker(current) and self.cell_checker(destination):
            if self.direction(current,destination) != "invalid":
                x, y = current
                dx, dy = destination
                dirv = self.direction(current, destination)
                if not (self.cells[y][x] & self.direction_value[dirv]):
                    if not (self.cells[dy][dx] & self.direction_value[self.opposite_direction[dirv]]):
                        return True

        return False              
    def direction(self, current, destination):
        x, y = current
        dx, dy = destination
        dfx = dx - x
        dfy = dy - y
        if (dfx, dfy) == (1, 0):
            return "RIGHT"
        elif (dfx, dfy) == (-1, 0):
            return "LEFT"
        elif (dfx, dfy) == (0, 1):
            return "DOWN"
        elif (dfx, dfy) == (0, -1):
            return "UP"
        else:
            return "invalid"
        