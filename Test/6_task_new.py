a = [[1,2], [3,4]]
b = [[1,2], [3,4]]


def matrixmult(a,b):
    if len(a[0]) != len(b):
        print('!!')
    sum_ = 0     
    new_matr=[]  
    final=[] 
    try:
        for k in range(len(a)):
            for j in range(len(b[0])):
                for i in range(len(a[0])):
                    sum_ = sum_ + a[k][i] * b[i][j]
                new_matr.append(sum_)
                sum_ = 0
            final.append(new_matr)
            new_matr= []  
    except IndexError:
        print("Матрицы нельзя перемножить")         
    return final

print(matrixmult(a, b))

