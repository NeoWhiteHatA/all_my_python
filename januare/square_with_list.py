class squre_list():
    #create empty list for
    #added parameters for squares
    sq_list = []
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.sq_list.append((self.width,
                             self.len))
        
    def print_size(self):
        print("""{} on {} on {} on {}""".format(self.width,
                                    self.len))
                    