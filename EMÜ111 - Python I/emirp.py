def isitprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def isitemirp(n):
    n = int(n)
    if isitprime(n) == False:
        return False

    reverse = 0
    while n != 0:
        x = n % 10
        reverse *= 10
        reverse += x
        n = int(n / 10)
    return isitprime(reverse)


for num in range(1024681, 2000000, 2):
    if isitemirp(num):
        dig2 = (num % 100 - num % 10)/10
        dig3 = (num % 1000 - num % 100)/100
        dig4 = (num % 10000 - num % 1000)/1000
        dig5 = (num % 100000 - num % 10000)/10000
        dig6 = (num % 1000000 - num % 100000)/100000
        if dig2!=dig3 and dig2!=dig4 and dig2!=dig5 and dig2!=dig6 and dig3!=dig4 and dig3!=dig5 and dig3!=dig6 and dig4!=dig5 and dig4!=dig6 and dig5!=dig6:
            if dig2==0 or dig2==2 or dig2==4 or dig2==6 or dig2==8:
                if dig3==0 or dig3==2 or dig3==4 or dig3==6 or dig3==8:
                    if dig4==0 or dig4==2 or dig4==4 or dig4==6 or dig4==8:
                        if dig5==0 or dig5==2 or dig5==4 or dig5==6 or dig5==8:
                            if dig6==0 or dig6==2 or dig6==4 or dig6==6 or dig6==8:
                                print(num)