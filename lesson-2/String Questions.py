# 1-masala
a = input("ISmingiz nima :")
b = int(input("Qachon tug'ilgansiz: "))
print(f"Yoshingiz {2025-b} da")

# 2-masala
text ='LMaasleitbtui'
print(text[1:3] + text[5:7] + text[-4]+ text[-2])
print(text[0]+text[3:5]+text[6]+text[-3]*2 + text[-1] )

# 3-masala
a = input()
print(len(a))
print(a.upper())
print(a.lower())

# 4- masala
a = input()
b = len(a)
n = 0
for i in range(1,b+1):
    if a[i-1]==a[-i]:
        n+=1
if n==b:
    print("True")
else:
    print("False")
    
# 5-masala
a = input()
x=a.lower()
b = len(a)
c = ["a","e","i","o","u"]
unli = 0
undosh = 0
for i in range(b):
    if x[i].isalpha() and x[i] in c:
        unli+=1
    elif x[i].isalpha():
        undosh +=1
print(f"Unlilar : {unli}, Undoshlar: {undosh}")

# 6-masala
a = input()
b = input()
if a in b:
    print("Ha")
elif b in a:
    print("Ha")
else:
    print("Yo'q")

# 7-masala
gap = input()
eski = input()
yangi = input()
print(gap.replace(eski, yangi))

# 8-masala
a = input()
if len(a)==0:
    print("Hech qanday belgi yo'q")
else:
    print(a[0],a[-1])

# 9-masala
a = input()
print(a[:: -1])

# 10-masala
a = input()
b = a.split()
print(len(b))

# 11-masala
a = input()
c = 0
for i in a:
    if i.isdigit():
        c+=1
if c==0:
    print("Yo'q")
else:
    print("Bor")
        
# 12-masala
a = input()
a = a.split()
b = ","
c = b.join(a)
print(c)

# 13-masala
a = input()
a = a.split()
b = ","
c = b.join(a)
print(c)
        
# 14-masala
a = input()
b = input()
x = len(a)
y = len(b)
j = 0
if x==y:
     for i in range(0,x):
        if a[i]==b[i]:
            j+=1
     if j==x:
         print("Teng")
     else:
         print("Teng emas")
else:
    print("Teng emas")

# 15-masala
a = input()
b = a.split()
c = ""
for d in b:
    c+=d[0].upper()
print(c)

# 16-masala
a = input()
b = input()
c = ""
a = a.replace(b, c)
print(a)

# 17-masala
a = input()
b = "aeiou"
c = "*"
for i in a:
    if i in b:
        a = a.replace(i, c)
print(a)

# 18-masala
a = input()
a = a.split()
b = input()
c = input()
if a[0]==b and a[len(a)-1]==c:
    print("Yes")
else:
    print("No")




















