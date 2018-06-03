class Stack():

    def __init__(self):
        self.values=[]

    def push(self,member):
        return self.values.append(member)

    def pop(self):
        return self.values.pop()

    def peak(self):
        for i in self.values:
            print i,
    
