

# Euclid's algorithum for fining the greatest common divisor of two number
def gcd(a,b):
    while b :
        a ,b = b, a % b
    return a

a , b = 200, 150 

print(gcd(a,b))

# Euler's totient function for counting the number of positive integers less
# than or equalt to n that are relatively prime to n 
def EulerTotient(n):
    amount = 0
    for i in range(1,n+1):
        if gcd(n,i) ==1 :
            amount += 1
    return amount

total = 0
for i in range(1,10):
    total = EulerTotient(i)

print(total)
    