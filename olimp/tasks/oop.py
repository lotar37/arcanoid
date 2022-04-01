class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

p1 = point(1,1)
p2 = point(1,1)
if p1 == p2:
    print("Equal True")
else:
    print("Equal False")