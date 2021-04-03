class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l
        
    def area(self):
        return self.width * self.len
    
    def change_size(self, w, l):
        self.width = w
        self.len = l
        