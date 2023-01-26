def dec(f):
    def new(V0, V1, t):
        res = f(V0, V1, t)
        res=str(res)+"\n"+str(V0*t + res*t**2/2)
        return res
    return new

@dec
def calc(V0, V1, t):
    return (V1-V0)/t

try:
    print(calc(int(input("V0")), int(input("V")), int(input("t"))))
except ValueError:
    print("введены не числа")
except ZeroDivisionError:
    print("t = 0, так быть не должно")