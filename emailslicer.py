a = input("Enter email:")

def s(a):
    for i in range(len(a)):
        if a[i] == "@":
            print("Email username:", a[:i])
            print("Email Domain name:", a[i + 1 :]) 
            

x = s(a)
print(x)