size = int(input("Enter the size of the pattern: "))

row = 1  

while row <= size:
    for column in range(size):
        print("*", end=" ")
    
    print()  
    row += 1

