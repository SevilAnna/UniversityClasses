def isitprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = 1
while num <=50:
    if isitprime(num):
        digits = num%10 + (num%100)//10 + (num%1000)//100 + (num%10000)//1000 + (num%100000)//10000 + (num%1000000)//100000 + (num%10000000)//1000000
        if digits == 5:
            print(num, digits, "--> prime")
        print(num,digits)
    num+=2