n=int(input("enter the number"))
if n>1:
    for i in range(1,n+1):
        if n % i ==0:
            print("not a prime number")
            break
        else:
            print("prime number")
    print()        