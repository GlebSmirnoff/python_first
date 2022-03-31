print('Hello World')
x = 5
print(x)

f = open("1.txt", "r")

print(f.read())
f.close()


with open("1.txt", "a") as f:
    f.write("Goodbuy File")

