class jug(object):
    def __init__(self, cap):
        self.val = 0
        self.cap = cap
        self.name = str(self.cap)
    def getValue(self):
        return self.val
    def setValue(self, val):
        self.val = val
    def getCap(self):
        return self.cap
    def getName(self):
        return self.name
    def __str__(self):
        return f'Cap ={self.cap}, CurrentVal ={self.val}'

class PlayGround(object):
    def __init__(self):
        self.jugs = {}
    
    def addJug(self, jug):
        self.jugs[jug.getName()] = jug.getValue()

    def fill(self, jug):
        if not jug.getCap() == jug.getValue():
            jug.setValue(jug.getCap()- jug.getValue())
            self.jugs[jug.getName()] = jug.getValue()
        else:
            print('already filled')
            pass 
    def Empty(self, jug):
        jug.setValue(0)
        self.jugs[jug.getName()] = jug.getValue()
    
    
    def PourAllToOther(self, jug, other):
        #(x,y) --> (0, x + y)     if x + y <= b
        if jug.getValue() + other.getValue() <= other.getCap():
            other.setValue(other.getValue() + jug.getValue())
            jug.setValue(0)
            self.jugs[jug.getName()] = jug.getValue()
            self.jugs[other.getName()] = other.getValue() 
    
    
    def PourToOther(self, jug, other):
        if jug.getValue() + other.getValue() <= other.getCap():
            #(x,y) --> (0 , x + y)          if x + y < b
            other.setValue(jug.getValue() + other.getValue())
            jug.setValue(0)
            self.jugs[jug.getName()] = jug.getValue()
            self.jugs[other.getName()] = other.getValue()

        if jug.getValue() + other.getValue() > other.getCap():
            #(x,y) --> (x - (b - y), b)     if x + y > b
            jug.setValue(jug.getValue() - (other.getCap() - other.getValue()))
            other.setValue(other.getCap())
            self.jugs[jug.getName()] = jug.getValue()
            self.jugs[other.getName()] = other.getValue()

    def __str__(self):
        return str(self.jugs)


def testJugs(jugs):
    Threejug,FiveJug = jugs
    p = PlayGround()
    for jug in jugs:
        p.addJug(jug)
    p.fill(Threejug)
    print(p)
    p.PourToOther(Threejug, FiveJug)
    print(p)
    p.fill(Threejug)
    print(p)
    p.PourToOther(Threejug, FiveJug)
    print(p)
    p.Empty((Threejug))
    print(p)

def JugAlgorithm(target, jugs):
    Smalljug,BigJug = jugs
    assert target <= BigJug.getCap() , 'target is bigger than big Jug capacity'
    p = PlayGround()
    p.addJug(Smalljug)
    p.addJug(BigJug)
    init = 0
    for s in range(10):
        for t in range(-10, 10):
            if s * jugs[0].getCap() + t * jugs[1].getCap() == target:
                init = s      # x = s*a + t*b --> x - s*a = t*b
    print(init)

    for _ in range(init):
        p.fill(Smalljug)
        p.PourToOther(Smalljug, BigJug)
        if BigJug.getValue() == BigJug.getCap():
            p.Empty(BigJug)
            p.PourToOther(Smalljug, BigJug)
        if Smalljug.getValue() == target or BigJug.getValue() == target:
            return p
    return init
print(JugAlgorithm(7, [jug(3), jug(10)]))
