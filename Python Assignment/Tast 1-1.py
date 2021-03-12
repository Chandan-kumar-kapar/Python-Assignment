n = int(input("Enter number of Rows: "))
sym = input("Enter symbol: ")
for i in range(1, n+1):
    print((" "*((2*n)-(2*i)))+f"{sym} "*i)
