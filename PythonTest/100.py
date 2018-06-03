class A:
    def x(self):
        return 2+2*2
class B:
    def x(self):
        return 5-4*8/4+10
class C(B,A):
    pass
c=C()
print c.x()
