class Some:
    def __init__(self,x,y):
        self.x= x
        self.y= y
    def __lt__(self,nd_one):
        if self.x == nd_one.x:
            return self.y < nd_one.y
        else:
            return self.x < nd_one.x



lis = [Some(34,29), Some(27,33),Some(27,5)]
lis.sort()
for i in lis:
    print(i.x, i.y)
        