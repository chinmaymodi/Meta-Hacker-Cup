import time
start = time.time()

from enum import Enum

class ChessPiece(Enum):
    king = 'K' # done
    queen = 'Q' # done
    rook = 'R' # done
    bishop = 'B' # done
    knight = 'N' # done
    nightrider = 'S'
    archbishop = 'A' # done
    kraken = 'E' # done

    def getThreatenedPositions(self, pos, board):
        #print('Checking threatened positions for Piece', self, 'at position', pos)
        x, y = pos
        ret = set()
        def move(dx, dy):
            if x == dx and y == dy:
                # somehow got our own pos back
                # dont update ret but keep going
                return True
            if 1 <= dx <= 16 and 1 <= dy <= 16:
                # these are valid values
                if (dx, dy) in board:
                    ret.add((dx, dy))
                    # once added, have to stop
                    return False
                else:
                    # not a piece we can threaten, BUT it is fine to continue
                    return True
            else:
                # reached edge of board, stop
                return False
        if self == ChessPiece.kraken:
            ret |= board.keys() - {pos}
        if self == ChessPiece.king:
            ret |= set((x+dx, y+dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0)) & board.keys()
        if self in (ChessPiece.knight, ChessPiece.archbishop):
            ret |= set((x+dx, y+dy) for dx in (-2, -1, 1, 2) for dy in (-2, -1, 1, 2) if abs(dx) != abs(dy)) & board.keys()
        if self in (ChessPiece.bishop, ChessPiece.archbishop, ChessPiece.queen):
            # i need to move them in each of the 4 directions until i reach a piece or the end of the board
            for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                i = 1
                while True:
                    nx, ny = x + i*dx, y + i*dy
                    if not move(nx, ny):
                        break
                    i += 1
        if self in (ChessPiece.rook, ChessPiece.queen):
            for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                i = 1
                while True:
                    nx, ny = x + i*dx, y + i*dy
                    if not move(nx, ny):
                        break
                    i += 1
        if self == ChessPiece.nightrider:
            for dx, dy in ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)):
                i = 1
                while True:
                    nx, ny = x + i*dx, y + i*dy
                    if not move(nx, ny):
                        break
                    i += 1
        #print('Returning', ret)
        return ret

file = "chess_2_input.txt"
ans = []
with open(file, 'r') as f:
    n = int(f.readline())
    for i in range(n):
        positions = int(f.readline())
        pieces = {}
        for _ in range(positions):
            line = f.readline()
            pieceName, *coordinates = line.split(' ')
            coordinates = tuple(int(c) for c in coordinates)
            pieces[coordinates] = ChessPiece(pieceName)
        f.readline()
        #print(i, pieces)
        threatened = set()
        for coordinates, piece in pieces.items():
            for neighbor in piece.getThreatenedPositions(coordinates, pieces):
                threatened.add(neighbor)
        #print(threatened)
        ans.append(str(len(threatened)))
outputfile = "chess_2_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')