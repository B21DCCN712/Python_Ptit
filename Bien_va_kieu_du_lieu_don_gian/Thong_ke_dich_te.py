visited = [0][0] * 105
n,m=map(int,input().split())
a= [ [int(x) for x in input().split()] for i in range(m)]

dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

res=0

q=[]
for i in range(n):
    for j in range(m):
        if a[i][j]==-1:
            q.append([i,j])
for u in q:
    for i in range(0,8):
        x,y=u[0]+dx[i],u[1]+dy[i]
        if x>=0 and x<n and y>=0 and y<m:
            #print(a[x][y])
            res += a[x][y]
            a[x][y]=0
print(res)