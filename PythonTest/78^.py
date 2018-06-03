import copy
class KV:
    pass
k=KV()
k.a=19
k.b=22
v=copy.copy(k)
print k is v
