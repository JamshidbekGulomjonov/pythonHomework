# 1-masala
a = float(input())
print(format(a,".2f"))

# 2-masala
a,b,c= map(int,input().split())
print(min(a,b,c),max(a,b,c))

# 3-masala
a = int(input())
b = a*1000
c = a*100000
print(f"{b} metr, {c} cm")

# 4-masala
a,b = map(int, input().split())
x = max(a,b)//min(a,b)
y = max(a,b)%min(a,b)
print(f"bolinma: {x}, qoldiq: {y}")

# 5-masala
a = float(input("Selsiy: "))
b = 1.8*a + 32
print(f"Faradey : {a}")

# 6-masala
a = (input())
print(int(a[-1]))

# 7-masala
a = int(input())
if a%2==0:
    print("Juft")
else:
    print("Toq")