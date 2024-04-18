class Arith:
    def sum(self, *args):
      return sum(args)
        
a1 = Arith()
print(a1.sum(10,10,10, 20))
print(a1.sum(20,10,30, 40, 50))