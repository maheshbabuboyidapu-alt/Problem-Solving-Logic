rate=30
n=20
m=10
h=int(input("Enter h:"))
if h<=2:
    print("Fee is 30")
elif h>2 and h<=5:
    h-=2
    rate+=n*h
    print(rate)
elif h>5:
    h-=5
    o=m*h
    rate+=o+60
    if rate >200:
        p=rate/100*10
        rate-=p
    print(f"Fee is {rate}")