#WAP to add two matrices
a=[[2,5,4],[1,3,9],[7,6,2]]
b=[[1,8,5],[7,3,6],[4,0,9]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]+b[i][j]
print(c)