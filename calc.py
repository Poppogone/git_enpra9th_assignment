def calc_gcd(a, b):
    while b:
        a, b = b, a%b
    
    return a

def list_prime(a):
    if a < 2:
        return []
    
    is_prime = [True] * (a + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(a**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, a+1, i):
                is_prime[j] = False

    primes = [i for i, val in enumerate(is_prime) if val]

    return primes

print("input the number")
a=int(input())
print("a is " + str(a))
print("input the additional number")
b=int(input())
print("b is " + str(b))

print("Addition:a+b="+ str(a+b))
print("Substruction:a-b="+ str(a-b))
print("Multiplication:a*b="+str(a*b))
print("Division:a/b="+ str(a/b))

gcd = calc_gcd(a,b)
print("GCD(a,b) is "+ str(gcd))

prime_a = list_prime(a)
prime_b = list_prime(b)
print("prime number (<=a) is " + str(prime_a))
print("prime number (<=b) is " + str(prime_b))