def calc_gcd(a, b):
    while b:
        a, b = b, a%b
    
    return a

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



