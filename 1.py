num = 5

for i in range(num):
    for j in range(0, i+1):
        print("*", end="")
    print("")
for i in reversed(range(num)):
    for j in reversed(range(0, i)):
        print("*", end="")
    print("")
