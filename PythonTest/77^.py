import copy
class KV:
    pass
k=KV()
k.a=10
k.b=20
v=copy.copy(k)
print k==v
