

from re import L


class LocalVar():
    
    lcount=0
    def __init__(self):
        self
    
    def lcount_inc(self):
        self.lcount=self.lcount+1
        return self.lcount

LocalV=LocalVar()