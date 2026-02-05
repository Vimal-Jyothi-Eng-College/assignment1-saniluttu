r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))
r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    A = []
    B = []
    C = []

    print("Enter elements of first matrix:")
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input()))
        A.append(row)

    print("Enter elements of second matrix:")
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input()))
        B.append(row)

    # Initialize result matrix with zeros
    for i in range(r1):
        row = []
        for j in range(c2):
            row.append(0)
        C.append(row)


    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

    print("Resultant Matrix:")
    for i in range(r1):
        for j in range(c2):
            print(C[i][j], end=" ")
        print()