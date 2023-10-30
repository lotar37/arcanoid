from random import randint
class Point:
    # global link, number
    link = None
    number = 0

    def __init__(self,num):
        self.number = num

    def setLink(self, obj):
        self.link = obj

class Node:
    node = []
    first = None
    def __init__(self):
        prev = None
        for i in range(10):
            p = Point(i)
            if prev:
                prev.setLink(p)
            prev = p
            self.node.append(p)
        print([p.number for p in self.node])
        self.first = self.node[0]

    def reverse(self):
        obj = self.first
        prev = None
        while obj:
            next = obj.link
            if prev:
                obj.link = prev
                prev = obj
            else:
                prev = Point(obj.number)
                prev.link = None

            obj = next
        self.first = prev

    def reverse2(self, obj=None, prev = None):

        if not obj:
            obj = self.first
            prev = Point(obj.number)
            prev.link  = None
            self.reverse2(obj.link, prev)
        else:
            if obj.link:
                next = obj.link
                obj.link = prev
                self.reverse2(next, obj)
            else:
                obj.link = prev
                self.first = obj



    def view(self):
        obj = self.first
        while obj:
            print("object",obj.number, end=" ")
            if obj.link:
                print("ссылается на {0} ".format(str(obj.link.number)))
                obj = obj.link
            else:
                print("ни на что не ссылается")
                obj = None

n = Node()

n.reverse2()
n.view()
n.reverse()
n.view()

