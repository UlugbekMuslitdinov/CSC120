import sys


class GridPos:
    """
    This class represents a single position on the grid.
    It has a position, which is a tuple of (x, y) coordinates.

    Attributes:
        position (tuple): The (x, y) coordinates of the position.
        occupied (Ship): The ship occupying the position, if any.
        guessed (bool): Whether the position has been guessed.

    Methods:
        __str__: Returns a string representation of the position.
        __repr__: Returns a string representation of the position.
    """
    def __init__(self, x, y):
        self.position = (x, y)
        self.occupied = None
        self.guessed = False

    def __str__(self):
        if self.guessed:
            if self.occupied:
                return "X"
            else:
                return "O"
        else:
            return " "

    def __repr__(self):
        return self.__str__()


class Board:
    """
    This class represents a board of player 1.
    It has a grid, which is a list of GridPos objects.

    Attributes:
        grid (list): The grid of the board.
        ships (list): The ships on the board.

    Methods:
        __str__: Returns a string representation of the board.
        __repr__: Returns a string representation of the board.
    """
    def __init__(self):
        self.grid = []
        self.ships = []
        for i in range(10):
            for j in range(10):
                self.grid.append(GridPos(i, j))

    def get_coordinates(self, x, y):
        """
        Returns the GridPos object at the given coordinates.

        Args:
            x (int): The x coordinate.
            y (int): The y coordinate.

        Returns:
            GridPos: The GridPos object at the given coordinates.

        Pre-condition:
            x and y must be between 0 and 9.

        Post-condition:
            The GridPos object at the given coordinates is returned.
        """
        for pos in self.grid:
            if pos.position == (x, y):
                return pos

    def __str__(self):
        output = ""
        for i in range(10):
            for j in range(10):
                output += self.grid[i * 10 + j].__str__()
            output += ""
        return output

    def __repr__(self):
        return self.__str__()


class Ship:
    """
    This class represents a single ship on the board.
    It has a name, a size, a list of positions, a list of hit positions, and a sunk attribute.

    Attributes:
        name (str): The name of the ship.
        size (int): The size of the ship.
        positions (list): The positions of the ship.
        hit_positions (list): The positions of the ship that have been hit.
        sunk (bool): Whether the ship has been sunk.

    Methods:
        __str__: Returns a string representation of the ship.
        __repr__: Returns a string representation of the ship.
    """
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hit_positions = []
        self.sunk = False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


def main():
    """
    The main function of the program.

    Arguments:
        None

    Returns:
        None
    """
    # Create a board
    board = Board()

    # Get the file name of player 1's ships
    player1_file = str(input())
    f = open(player1_file, "r").read().splitlines()
    for line_str in f:
        line = line_str.split()
        ship_name = line[0]
        ship_size = 0
        if ship_name == "A":
            ship_size = 5
        elif ship_name == "B":
            ship_size = 4
        elif ship_name == "S":
            ship_size = 3
        elif ship_name == "D":
            ship_size = 3
        elif ship_name == "P":
            ship_size = 2
        # Create a ship
        ship = Ship(ship_name, ship_size)
        x1 = int(line[1])
        y1 = int(line[2])
        x2 = int(line[3])
        y2 = int(line[4])
        if x1 != x2 and y1 != y2:
            # Check if the ship is placed horizontally or vertically
            print("ERROR: ship not horizontal or vertical: " + line_str)
            sys.exit()
        if x1 < 0 or x1 > 9 or x2 < 0 or x2 > 9 or y1 < 0 or y1 > 9 or y2 < 0 or y2 > 9:
            # Check if the ship is placed within the grid
            print("ERROR: ship out-of-bounds: " + line_str)
            sys.exit(0)
        real_size = 0
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(y1, y2 + 1):
                position = board.get_coordinates(x1, i)
                if position.occupied:
                    # Check if the ship is placed on another ship
                    print("ERROR: overlapping ship: " + line_str)
                    sys.exit(0)
                real_size += 1
                position.occupied = ship
                ship.positions.append(position)
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for i in range(x1, x2 + 1):
                position = board.get_coordinates(i, y1)
                if position.occupied:
                    # Check if the ship is placed on another ship
                    print("ERROR: overlapping ship: " + line_str)
                    sys.exit(0)
                real_size += 1
                position.occupied = ship
                ship.positions.append(position)
        if real_size != ship_size:
            # Check if the ship is placed with the correct size
            print("ERROR: incorrect ship size: " + line_str)
            sys.exit(0)
        board.ships.append(ship)
    if len(board.ships) != 5:
        # Check if the board has 5 ships
        print("ERROR: fleet composition incorrect")
        sys.exit(0)
    # Get the file name of player 2's guesses
    player2_file = str(input())
    f = open(player2_file, "r").read().splitlines()
    for line in f:
        line = line.split()
        hit_x = int(line[0])
        hit_y = int(line[1])
        if hit_x > 9 or hit_y > 9:
            print("illegal guess")
        else:
            position = board.get_coordinates(hit_x, hit_y)
            if position.occupied:
                ship = position.occupied
                ship.hit_positions.append(position)
                if ship.size == len(ship.hit_positions):
                    print("{} sunk".format(ship))
                    ship.sunk = True
                elif ship.size > len(ship.hit_positions) and position.guessed is False:
                    print("hit")
                elif ship.size > len(ship.hit_positions) and position.guessed is True:
                    print("hit (again)")
            else:
                if position.guessed is False:
                    print("miss")
                elif position.guessed is True:
                    print("miss (again)")
            position.guessed = True
            for ship in board.ships:
                if ship.sunk is False:
                    break
            else:
                print("all ships sunk: game over")
                sys.exit(0)


main()
