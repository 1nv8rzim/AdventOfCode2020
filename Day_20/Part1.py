with open("Day_20/input.txt") as file:
    lines = file.read()

lines = lines.split('\n\n')

tiles = {}
for card in lines:
    tile = int(card.split(":")[0].split(" ")[1])
    value = [list(x) for x in card.split(":")[1].strip().split("\n")]
    tiles[tile] = value

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
p1 = 1
for c in cvals:
    p1 *= c
print(p1)
