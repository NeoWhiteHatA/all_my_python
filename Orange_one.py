class OrangeOne():
    def __init__(self, w, c, p):
        """weight in gramm"""
        self.weight = w
        self.color = c
        self.price = p
        self.mold = 0
        print('Create')
    def rot(self, days, temp):
        self.mold = days * temp