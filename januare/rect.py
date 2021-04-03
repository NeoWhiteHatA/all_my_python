class Rect():
    def __init__(self, l, w, a):
        self.len = l
        self.width = w
        self.altid = a
    def perimeter(self):
        return self.len + self.width + self.altid