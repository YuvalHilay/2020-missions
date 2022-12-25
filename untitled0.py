
def check_perfectrow(matrix,n): #fun check that the row is perfect
    for j in range(n): #check all the organs in matrix<n
        for k in range(n):
            if(matrix[j][k]>n):
                return False
    countlist=[] #define matrix count list
    for l in range(n):
            row_l=[]
            for m in range(n):
                row_l.append(0)
            countlist.append(row_l)
    for i in range(n):
        for t in range(n):
            countlist[i][matrix[i][t]-1]+=1
    for p in range(n):
        for a in range(n):
            if(countlist[p][a]!=1):
                return False
    return True
def check_perfectcol(matrix,n): #fun check that the col is perfect
    for j in range(n): #check all the organs in matrix<n
        for k in range(n):
            if(matrix[j][k]>n):
                return False
    countlist=[] #define matrix count list
    for l in range(n):
            row_l=[]
            for m in range(n):
                row_l.append(0)
            countlist.append(row_l)
    for i in range(n):
        for t in range(n):
            countlist[t][matrix[i][t]-1]+=1
    for p in range(n):
        for a in range(n):
            if(countlist[p][a]!=1):
                return False
    return True
def main():
    row=int(input("Enter the matrix dimension: "))
    while(row!=0): # run until row input is zero
        #matrix=[0]*row[0]*row
        matrix=[] #define matrix 
        for l in range(row):
            row_l=[]
            for m in range(row):
                row_l.append(0)
            matrix.append(row_l)
        print("enter the entries rowwise: ",end='')
        for i in range(row): #take input for the matrix
            for j in range(row):
                matrix[i][j]=int(input())
        for t in range(row): #print the matrix
            for k in range(row):
                print("%5d" %matrix[t][k])
            print()
        if(check_perfectrow(matrix, row)==False): #call for check if matrix is perfect
            print("The matrix is not perfect")
        elif(check_perfectcol(matrix, row)==False):
             print("The matrix is not perfect")
        else:
            print("The matrix is perfect")
        row=int(input("Enter the matrix dimension: "))
    print("Finish")
main()