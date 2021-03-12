c = 65
n = int(input("Enter row Size: "))
for i in range(n):
    for j in range(i):
        print(chr(c), end=" ")
        c += 1
    print()
