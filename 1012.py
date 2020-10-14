#1012 유기농 배추

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x,y):
    if x<=-1 or x>=m or y<=-1 or y>=n:
        return False

    if maps[y][x] ==1:
        maps[y][x]=0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

# main
test_case = int(input())
answer=[]
for i in range(test_case):
    m, n, k = map(int,input().split())
    maps = [[0]*m for _ in range(n)]

    for i in range(k):
        x, y = map(int,input().split())
        maps[y][x] = 1

    result = 0
    for i in range(m):
        for j in range(n):
            if maps[j][i]==1:
                if dfs(i,j)==True:
                    result+=1

    answer.append(result)

# output result
for i in range(test_case):
    print(answer[i])
