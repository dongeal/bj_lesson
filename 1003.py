# import sys  
# sys.stdin = open("bjtest.txt", "r")

# from collections import deque

# def bfs(si,sj):
#     q = deque()  #초기값 들
#     v =[[0]*N for _ in range(N)]
#     tlst = []

#     q.append((si,sj))   # 초기 데이타 삽입
#     v[si][sj] = 1
#     eat = 0

#     while q:
#         ci,cj = q.popleft()
#         if eat == v[ci][cj]:
#             return tlst, eat-1

#         #4방향, 범위내,미방문,나보다 작거나 같은물고기
#         for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
#             ni,nj = ci+di, cj+dj
#             if 0<=ni<N and 0<=nj<N and v[ni][nj] ==0 and arr[ni][nj] <= shark:
#                 q.append((ni,nj))
#                 v[ni][nj] = v[ci][cj] + 1
#                 if shark > arr[ni][nj] >0 :
#                     tlst.append((ni,nj))
#                     eat = v[ni][nj]

#     return tlst, eat-1

# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 9:
#             ci, cj = i,j
#             arr[i][j] = 0

# shark  = 2
# cnt = ans = 0
# while True:
#     tlst, dist = bfs(ci,cj)
#     if len(tlst) == 0:
#         break
#     tlst.sort(key = lambda x :(x[0],x[1]))
#     ci,cj = tlst[0]
#     arr[ci][cj] = 0 # 물고기 먹기
#     cnt += 1
#     ans += dist
#     if shark == cnt:
#         shark += 1
#         cnt = 0
# print(ans)        
lst =[(3,4),(2,2),(3,5),(4,1)]
lst.sort(key = lambda x:(x[0], x[1]))
print(lst)