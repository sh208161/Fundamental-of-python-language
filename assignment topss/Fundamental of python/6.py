# without using temp 
a=7
b=6
print("Before swapping")
print(f"value of a: {a} and b: {b}")

a,b = b,a
 
print("After swapping")
print(f"value of a : {a} and b: {b}")

# with temp

p=7
q=10

temp=p
p=q
q=temp

print(f"swapped value of p= {p} and q={q}")