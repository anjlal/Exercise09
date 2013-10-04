
def print_towers(t1,t2,t3):
    print "\tsrc tower:\t",t1
    print "\ttmp tower:\t",t2
    print "\tdest tower:\t",t3


# move_rings(rings,src_tower,dest_tower,tmp_tower)
def move_rings(n, t1, t2, t3):
# move rings among three different towers, start out with rings on tower1
# end with rings on tower2 
    if n > 1:
        move_rings(n-1, t1, t3, t2)
        move_rings(1, t1, t2, t3)
        move_rings(n-1, t3, t2, t1)
    elif n == 1:
        t2.append(t1.pop())


def main():
    tower1 = range(5,0,-1)
    tower2 = []
    tower3 = []
    rings = len(tower1)

    print "BEFORE: "
    print_towers(tower1,tower2,tower3)

    move_rings(rings,tower1,tower3,tower2)

    print "AFTER: "
    print_towers(tower1,tower2,tower3)

main()

