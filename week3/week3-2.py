class A:
    def hello(self):
        print("Hello from A")





class B(A):
    def hello(self):
        print("Hello from B")
        super().hello()




class C(A):
    def hello(self):
        print("Hello from C")
        super().hello()



class D(B, C):
    def hello(self):
        print("Hello from D")
        super().hello()


class E(C):
    def hello(self):
        print("Hello from E")
        super().hello()


class F(B,E):
    def hello(self):
        print("Hello from F")
        super().hello()


class G(B, D):
    def hello(self):
        print("Hello from G")
        super().hello()




print(G.mro())

# F first, and B and E from  F(B,E), and for  B and E
# and, E inherits C, which inherits from A, so B E and C A Object.


