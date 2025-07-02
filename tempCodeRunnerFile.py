def prime_factorization(a):
    prime_list = []
    i = 2 #minimum prime number
    for i in range (2,a-1):
        if a%i == 0:
            prime_list.append(i)
            a //= i
        else:
            i += 1