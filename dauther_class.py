class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l
        
    def print_size(self):
        print("""{} on {}
              """.format(self.width,
                         self.len))
        
class Square(Shape):
    def area(self):
        return self.width * self.len

def print_size(self):
    print(""" {} on {}
          """.format(self.width,
                     self.len))
    
    