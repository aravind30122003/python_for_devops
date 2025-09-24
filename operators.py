
# Arithmetic operator

a = 5
b = 2

print(a + b)  # 7
print(a - b)  # 3
print(a * b)  # 10
print(a / b)  # 2.5
print(a // b) # 2
print(a % b)  # 1
print(a ** b) # 25

# comparison operators

a = 5
b = 2

print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= 5)  # True
print(b <= 2)  # True

# logical operator

a = 5
b = 2

print(a > 2 and b < 5)  # True
print(a > 2 or b > 5)   # True
print(not(a > b))       # False

# assignment operator

a = 5
a += 3
print(a)  # 8

a *= 2
print(a)  # 16

# bitwise operator 
a = 5  # 0101 in binary
b = 3  # 0011 in binary

print(a & b)  # 1  (0001)
print(a | b)  # 7  (0111)
print(a ^ b)  # 6  (0110)
print(~a)     # -6 (invert bits)
print(a << 1) # 10 (1010)
print(a >> 1) # 2  (0010)
