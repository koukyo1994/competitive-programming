num = input()
A, B = [int(x) for x in num.split()]

a, b = bin(A).replace("0b", ""), bin(B).replace("0b", "")
a = a.rjust(len(b), "0")
b = b.rjust(len(a), "0")
