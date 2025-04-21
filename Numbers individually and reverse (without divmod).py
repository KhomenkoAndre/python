cod= int(input())

a=(cod//1000)
print(a)

w=(cod%1000)
b=(w//100)
print(b)

c=(cod%100)
d=(c//10)
print(d)

g=(cod%10)
print(g)

print(a,b,d,g)
print(g,d,b,a)
