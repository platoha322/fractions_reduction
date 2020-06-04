def greatest_common_divisor(a,b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    gcd = a + b
    return gcd

def greatest_common_divisor2(a,b):
    max_div = min(abs(a), abs(b))
    for i in range(max_div,0,-1):
          if a%i == 0 and b%i == 0:
              return i


def fract_red(a,b):
    gcd = greatest_common_divisor(a,b)
    return  a/gcd, b/gcd




a = input ("")
b = input("")
print (fract_red(a,b))
