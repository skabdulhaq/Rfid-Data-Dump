import numpy
x = "31 32 35 30"
val = [ int(str("0x"+data),16)for data in x.split(" ")]
def xor():
    q = hex(numpy.bitwise_xor.reduce(val)).upper()
    test = q[2:].rjust(2,"0")
    print(test)
def complem():
    for d in val:
        print(hex(~d), end=" ")
complem()