def calc_gcd(a, b):
    while b:
        a, b = b, a%b
    
    return a

def calc_lcm(a,b,gcd_ab):
    gcd_ab = calc_gcd(a,b)

    return a*b/gcd_ab


def list_prime(a):
    if a < 2:
        return []
    
    is_prime = [True] * (a + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(a**0.5) + 1): #Sieve of Eratosthenes
        if is_prime[i]:
            for j in range(i*i, a+1, i):
                is_prime[j] = False

    primes = [i for i, val in enumerate(is_prime) if val]

    return primes

a=int(input("input the number : "))
print("a is " + str(a))
b=int(input("input the additional number : "))
print("b is " + str(b))

print("Addition:a+b="+ str(a+b))
print("Substruction:a-b="+ str(a-b))
print("Multiplication:a*b="+str(a*b))
print("Division:a/b="+ str(a/b))

gcd = calc_gcd(a,b)
print("GCD(a,b) is "+ str(gcd))

lcm = calc_lcm(a,b,gcd)
print("LCM(a,b) is " + str(lcm))

primes_a = list_prime(a)
primes_b = list_prime(b)
print("prime number (<=a) is " + str(primes_a))
print("prime number (<=b) is " + str(primes_b))