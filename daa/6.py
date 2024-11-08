#tc o(n^2) and sc O(n^3)
def obst(p,q,n):
    c = [[0 for _ in range(n+1)] for _ in range(n+1)]
    w = [[0 for _ in range(n+1)] for _ in range(n+1)]
    root = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n+1):
        c[i][i] =0
        w[i][i] = q[i]
        root[i][i] =0

    for length in range(1,n+1):
        for i in range(n-length+1):
            j = i+length
            w[i][j] = w[i][j-1] + p[j-1]+q[j]
            c[i][j] = float('inf')
            for k in range(i+1,j+1):
                cost = c[i][k-1] + c[k][j] + w[i][j]
                if cost <c[i][j]:
                    c[i][j] = cost
                    root[i][j] = k
    return c[0][n]

n = 4
p = [3,3,1,1]
q = [2,3,1,1,1]
print("cost:",obst(p,q,n))