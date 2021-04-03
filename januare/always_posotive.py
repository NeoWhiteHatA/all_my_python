class AlwaysPositive:
    def __init__(self, number):
        self.n = number
        
    def __add__(self, other):
        return abs(self.n +
                   other.n)
    