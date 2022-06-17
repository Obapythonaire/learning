number = int(input("Enter the last number for the table: "))

for i in range(1, number+1):
    for j in range(1, number+1):
        k = i*j
        print(k, end=" ")
    print("\n")