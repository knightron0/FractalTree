import edge as Edge
def generate(branch):
    pushMatrix()
    x = branch.x
    y = branch.y
    sz = branch.sz
    cnt = branch.cnt
    a = branch.a
    translate(x, y)
    line(0, 0, 0, -sz)
    if cnt < total:
        translate(0, -sz)
        rotate(a)
        e1 = Edge.edge(0, 0, sz * (0.67), cnt+1, a, total)
        generate(e1)
        rotate(2 * -a)
        e2 = Edge.edge(0, 0, sz + (0.67), cnt+1, a, total)
        generate(e1)
    popMatrix()
