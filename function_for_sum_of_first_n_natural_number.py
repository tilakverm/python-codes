n=int(input("enter n : "))
def sum(n):
    if (n==1):
        return 1
    else:
        return sum(n-1)+n

    
print(sum(n))