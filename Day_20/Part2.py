with open("Day_20/input.txt") as file:
    lines = file.read()

lines = lines.split('\n\n')

tiles = {}
for tile in lines:
    i = int(tile.split(":")[0].split(" ")[1])
    val = [list(x) for x in tile.split(":")[1].strip().split("\n")]
    tiles[i] = val


board = []
for i in range(12):
    board.append([-1]*12)
bids = []
for i in range(12):
    bids.append([-1]*12)


def allflips(tile):
    ret = []
    ret += allrotations(tile)
    ret += allrotations(fliplr(tile))
    ret += allrotations(fliptd(tile))
    ret += allrotations(fliptd(fliplr(tile)))
    return ret


def fliplr(tile):
    ret = []
    for i in range(len(tile)):
        ret .append(tile[len(tile)-1-i])
    return ret


def fliptd(tile):
    ret = []
    for i in range(len(tile)):
        ret .append(tile[i][::-1])
    return ret


def rotate(tile):
    ret = []
    for i in range(len(tile)):
        ret.append([-1]*len(tile))
    for i in range(len(tile)):
        for j in range(len(tile)):
            ret[j][len(tile)-1-i] = tile[i][j]
    return ret


def allrotations(tile):
    return [tile, rotate(tile), rotate(rotate(tile)), rotate(rotate(rotate(tile)))]


def top(tile):
    return "".join(tile[0])


def bottom(tile):
    return "".join(tile[9])


def left(tile):
    return "".join([x[0] for x in tile])


def right(tile):
    return "".join([x[9] for x in tile])


roted = {}
for tid in tiles:
    roted[tid] = allflips(tiles[tid])


def norm(s):
    r = s[::-1]
    if hash(r) < hash(s):
        return r
    else:
        return s


def edges(t):
    return [norm(left(t)), norm(right(t)), norm(bottom(t)), norm(top(t))]


edgeToTid = {}
tidToEdges = {}
for tid in tiles:
    for edge in edges(tiles[tid]):
        if edge not in edgeToTid:
            edgeToTid[edge] = set([])
        edgeToTid[edge].add(tid)
        if tid not in tidToEdges:
            tidToEdges[tid] = set([])
        tidToEdges[tid].add(edge)
tidToEdgeCount = {}
for tid in tiles:
    c = 0
    for edge in tidToEdges[tid]:
        if len(edgeToTid[edge]) == 1:
            c += 1
    tidToEdgeCount[tid] = c

cvals = [x for x in tidToEdgeCount if tidToEdgeCount[x] == 2]
evals = [x for x in tidToEdgeCount if tidToEdgeCount[x] == 1]
corners = {(0, 0), (11, 0), (0, 11), (11, 11)}


def solve(i, j, t):
    if i == 12:
        return True
    ni = i
    nj = j+1
    if nj == 12:
        nj = 0
        ni = i+1
    candidates = t
    if (i, j) in corners:
        candidates = t & set(cvals)
    elif i == 0 or j == 0 or i == 11 or j == 11:
        candidates = t & set(evals)
    for tid in candidates:
        for tile in roted[tid]:
            if i != 0 and top(tile) != bottom(board[i-1][j]):
                continue
            if j != 0 and left(tile) != right(board[i][j-1]):
                continue
            board[i][j] = tile
            bids[i][j] = tid
            if solve(ni, nj, t - set([tid])):
                return True
    return False


solve(0, 0, set(tiles.keys()))

final = []
for y in range(12):
    for yy in range(10):
        s = ""
        r = ""
        for x in range(12):
            s += "".join(board[y][x][yy])
            r += "".join(board[y][x][yy][1:-1])
        if yy != 0 and yy != 9:
            final.append(r)

monster = ['                  # ',
           '#    ##    ##    ###',
           ' #  #  #  #  #  #   ']


def ismonster(entry, xx, yy):
    for x in range(len(monster)):
        for y in range(len(monster[0])):
            if monster[x][y] == '#' and entry[xx+x][yy+y] != '#':
                return False
    for x in range(len(monster)):
        for y in range(len(monster[0])):
            if monster[x][y] == '#':
                entry[xx+x][yy+y] = 'O'
    return True


for entry in allflips(final):
    entry = [list(x) for x in entry]
    m = 0
    for xx in range(96):
        for yy in range(96):
            try:
                if ismonster(entry, xx, yy):
                    m += 1
            except IndexError:
                aosenuthtsauneo = 5021
    if m != 0:
        c = 0
        for x in range(96):
            for y in range(96):
                if entry[x][y] == '#':
                    c += 1
        print(c)
        break
