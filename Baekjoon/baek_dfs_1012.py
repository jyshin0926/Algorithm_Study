import sys
sys.setrecursionlimit(100000)       # dfs로 풀이
# dfs는 stack 대신 재귀함수로도 구현 가능
# 반복적 재귀 실행 위해 recursionlimit 범위 설정

def dfs(x,y):
    visited = list()
    array = list()
    visited[x][y] = True
    directions = [(-1,0),(1,0),(0,-1),(0,1)]    # 상하좌우 이동
    for dx, dy in directions:
        nx, ny = x + dx, y + dy     # next_x, next_y
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if array[nx][ny] and not visited[nx][ny]:   # nx, ny가 2차원 배열에 포함되어 있으면 해당 원소를 방문하지 않은 경우 방문하도록 처리
            # 배추가 심어져있는 곳만 방문
            dfs(nx,ny)

for _ in range(int(input())):
    m,n,k = map(int,input().split())
    array = [[0]*m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        y,x = map(int, input().split())
        array[x][y] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] and not visited[i][j]:
                dfs(i,j)    # dfs(i,j)로 dfs가 수행된 횟수 계산
                result += 1 # dfs 수행될 때마다 result += 1
    print(result)   # 최종 result
