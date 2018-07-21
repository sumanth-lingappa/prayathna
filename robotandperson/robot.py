class Robot:
    name = ''
    color = ''
    weight = ''
    following = None

    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w

    def introduceSelf(self):
        print "My name is {} and I am following {}".format(self.name, self.following.name)
