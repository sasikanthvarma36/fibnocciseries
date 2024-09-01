n=int(input("Enter the number ="))
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

f= fibonacci()
fl=[
    next(f)
    for _ in range (n+1)
]
print(fl)
