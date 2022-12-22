def printmenu (str):
 print("----------------------------MENU---------------------------")
 print(" \t1. Enter a new string: ")
 print(" \t2. Find the longest word in the string: ")
 print(" \t3. To check if the word is palindrome: ")
 print(" \t4. To find the index of first appearence of the sub string: ")
 print(" \t5. find frequency of appearence of a word or char: ")
 print(" \t6. Exit the program: ")
 print("-----------------------------------------------------------")
 print("Your string is: ", str)

def findIndex(string, substring):
 for i in range(0, (len(string)-len(substring)+1)):
    flag = 1
    for j in range(0, len(substring)):
        if string[i+j] != substring[j]: 
            flag = 0
            break
    if flag == 1: 
        return i
    return -1

def findCount(string, substring):
 count = 0
 for i in range(0, (len(string)-len(substring)+1)):
    flag = 1
    for j in range(0, len(substring)):
         if string[i+j] != substring[j]: 
            flag = 0
            break
    if flag == 1: 
         count = count+1
 return count

printmenu("NOT yet given")
choice = 1
while(choice != 6):
 if choice == 1 :
    string = input("Enter the new string: ")
    split = string.split()
 elif choice == 2:
    split = sorted(split, key = len)
    print("The longest word of the string is :", split[-1])
 elif choice == 3:
    s= string.lower()
    a = s[::-1]
    if(s == a):
        print("It is a palindrome")
    else:
        print("Not a palindrome")
 elif choice == 4 :
    es = input("Enter the substring to find: ")
    if findIndex(string, es) >= 0:
        print("The first appearence of the substring is :", findIndex(string, es))
    else:
        print("substring absent in the string")
 elif choice == 5:
    word = input("Enter word or char to find it occurence: ")
    print("Number of time your word or char has occured is: ", findCount(string, word))
 elif choice == 6:
    break
 else:
    print("wrong choice")
 printmenu(string)
 choice = int(input("Enter your choice(press 6 if u want to exit): "))