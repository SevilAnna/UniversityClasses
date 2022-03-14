#test version

n = int(input("enter number to find reverse: "))
reverse = 0
while n != 0:
        x = n % 10        #x is the last digit
        reverse *= 10
        reverse += x
        print("   n= ", n, "   x= ", x, "   reverse= ", reverse, end="  ")
        n = int(n / 10)
        print("  new n= ", n)
