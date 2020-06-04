a = c = int(input("numerator "))
b = d = int(input("denominator "))

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a

gcd = a + b
