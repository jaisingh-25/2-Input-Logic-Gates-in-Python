# The in-built gates in python are - AND, OR, NOT
X=bool(input("Enter X - "))
Y=bool(input("Enter Y - "))

print(X,Y)

# This is the AND gate
O=X and Y
print("AND : ", O)

# This is the OR gate
O=X or Y
print("OR : ", O)

# This is the NOT gate
O1= not X
O2= not Y
print("NOT : ", O1)
print("NOT : ", O2)

# This is the NAND gate
A=X and Y
O= not A
print("NAND : ", O)

# This is the NOR gate
A=X or Y
O= not A
print("NOR : ", O)

# This is the XOR gate
A= not X
B= not Y
C= A and Y
D= B and X
O=C or D
print("XOR : ", O)

# This is the XNOR gate
A= not X
B= not Y
C= A and Y
D= B and X
E=C or D
O= not E
print("XNOR : ", O)
