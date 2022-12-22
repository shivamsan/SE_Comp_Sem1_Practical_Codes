def print_menu():
    print("-----------------------MENU--------------------")
    print("\t1. Display the addition of the matrix")
    print("\t2. Display the substraction of the matrix")
    print("\t3. Display the multiplication of matrices")
    print("\t4. Display the transpose of matrices")
    print("\t5. End")
    print("-----------------------------------------------")
 
n1 = int(input("Enter order of matrix 1 and 2:"))
matrix1 = []
matrix2 = []
print("Enter ", n1*n1," Numbers for matrix1")
for i in range (n1):
    a = []
    for j in range (n1):
        a.append(int(input()))
    matrix1.append(a)

print("Enter ", n1*n1, " Numbers for matrix2")
for i in range (n1):
    a = []
    for j in range (n1):
        a.append(int(input()))
    matrix2.append(a)
def display():
 print("Matrix1: ")
 for i in range(len(matrix1)):
    print(matrix1[i])
 print("Matrix2: ")
 for i in range(len(matrix2)):
    print(matrix2[i])
display()
print_menu()
choice = int(input("Enter your choice: "))
while(choice != 5):

    if(choice == 1):
        print("Addition of 2 matrices :")
        for i in range(n1):
            for j in range(n1):
                print(" ",matrix1[i][j]+matrix2[i][j], end = " ")
            print()

    if(choice == 2):
        print("Substraction of 2 matrices :")
        for i in range(n1):
            for j in range(n1):
                 print(" ",matrix1[i][j]-matrix2[i][j], end = " ")
            print()

    if(choice == 3):
        for i in range(n1):
            for j in range(n1):
                x = 0
                for k in range(n1):
                    x += matrix1[i][k] * matrix2[k][j]
                print(" ",x, end = " ")
            print()

    if(choice == 4):
        choice2 = int(input("Enter which matrix to transpose[1/2] :"))
        if(choice2 == 1):
            for i in range(n1):
                for j in range(n1):
                     print(" ",matrix1[j][i], end = " ")
                print()

        else:
            for i in range(n1):
                for j in range(n1):
                    print(" ",matrix2[j][i], end = " ")
                print()
    
    print_menu()
    choice = int(input("Enter your choice: "))