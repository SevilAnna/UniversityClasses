def isitprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def isitpalprime(n):
    n = int(n)
    if isitprime(n) == False:
        return False

    reverse = 0
    new_n = n
    while new_n != 0:
        x = new_n % 10
        reverse *= 10
        reverse += x
        new_n = int(new_n / 10)
    if reverse == n:
        return isitprime(reverse)


for num in range(1000001, 9999999, 2):
    if isitpalprime(num):
        print(num)