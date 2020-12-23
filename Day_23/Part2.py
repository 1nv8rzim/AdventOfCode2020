input = '368195742'

cups = list(map(int,input))

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"({self.val})"

lookup = {}

nodes = [Node(int(c)) for c in input]

cur = 10
while len(nodes) < 1000000:
    nodes.append(Node(cur))
    cur += 1

for a,b in zip(nodes,nodes[1:]):
    a.next = b

nodes[-1].next = nodes[0]

lookup = {}
for node in nodes:
    lookup[node.val] = node

cur = nodes[0]

for _ in range(10000000):
    a = cur.next
    b = a.next
    c = b.next
    cur.next = c.next
    used = {cur.val,a.val,b.val,c.val}
    cval = cur.val
    while cval in used:
        cval -= 1
        if cval == 0:
            cval = 1000000
    new_ins = lookup[cval]
    ins_nxt = new_ins.next

    new_ins.next = a
    c.next = ins_nxt

    cur = cur.next

cup1 = lookup[1]
a = cup1.next
b = a.next

print(a.val * b.val)