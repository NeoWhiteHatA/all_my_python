class PublicPrivateExample:
    def __init__(self):
        self.public = 'safe'
        self._unsafe = 'danger'
        
    def public_method(self):
        #clients may use this method
        pass
    def _unsafe_method(self):
        #clients do not use this method
        pass
    self.public = 'safe'
    self._unsafe = 'danger'