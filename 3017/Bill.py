"""rov"""
a = int(input())
b = a*0.1
if a > 10000:
    b = 1000
    v = (a+b)*0.07
    print(f"{a+b+v:.2f}")
elif a < 500:
    b = 50
    v = (a+b)*0.07
    print(f"{a+b+v:.2f}")
elif 500 <= a <= 10000:
    v = (a+b)*0.07
    print(f"{a+b+v:.2f}")
