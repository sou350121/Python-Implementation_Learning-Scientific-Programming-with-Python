
# Euclid's algorithum for fining the greatest common divisor of two number
def gcd(a,b):
    while b :
        a ,b = b, a % b
    return a

a , b = 200, 150 

print(gcd(a,b))