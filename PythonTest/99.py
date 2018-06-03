class A:
    def x(self):
        return 'Hello world'
class B:
    def x(self):
        return 'Hello python'
class C(A,B):
    pass
c=C()
print c.x()
