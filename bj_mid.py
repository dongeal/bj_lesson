import sys
sys.stdin = open("input.txt", "r")
from collections import deque

def bfs(color,si,sj):
    global cnt, blind
    RG = 0
    if blind  and (color == 'R' or color == 'G'):
        RG = 1
    q = deque()
    v[si][sj] = cnt 
    q.append((si,sj))
    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci + di, cj +dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] ==0 :
                if  blind and RG and  (arr[ni][nj] == 'R' or arr[ni][nj] == 'G') :
                    v[ni][nj] = cnt
                    q.append((ni,nj))
                if blind and not RG and arr[ni][nj] == color :
                    v[ni][nj] = cnt
                    q.append((ni,nj))
                if not blind and arr[ni][nj] == color:
                    v[ni][nj] = cnt
                    q.append((ni,nj))
    return 

N = int(input())
arr= [list(input()) for _ in range(N)]
blind = False
cnt = 0
v=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if v[i][j] == 0:
            cnt +=1
            bfs(arr[i][j],i,j)
ans1 = cnt
blind = True
cnt = 0
v=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if v[i][j] == 0:
            cnt +=1
            bfs(arr[i][j],i,j)
print(v)
ans2 = cnt
print(ans1, ans2)    




# def bfs(a,b):
#     na='    '
#     v = [0]*10000
#     q = deque()
#     q.append((a,0))
#     v[int(a)] = 1
#     while q:
#         ca , cnt = q.popleft()
#         if ca == b :
#             return cnt
#         for i in range(4):
#             for j in range(10):
#                 if i ==0:
#                     na = str(j)+ca[1]+ca[2]+ca[3]
#                 if i ==1:
#                     na = ca[0]+str(j)+ca[2]+ca[3]
#                 if i ==2:
#                     na = ca[0]+ca[1]+str(j)+ca[3]  
#                 if i ==3:
#                     na = ca[0]+ca[1]+ca[2]+str(j) 
#                 if v[int(na)] == 0 and int(na) in p:
#                     q.append((na,cnt+1))
#                     v[int(na)] = 1 
#     return 'impossible'

# p=set()
# n=9999
# sieve = [True] * n #전부 소수라고 초기 설정
# m = int(n ** 0.5)
# for i in range(2, m + 1):
#     if sieve[i] == True:
#         for j in range(i+i, n, i):
#             sieve[j] = False
# for i in range(1000,9999):
#     if sieve[i] == True:
#         p.add(i)

# T = int(input())
# for i in range(T):
#     a,b = map(str,input().split())
#     print(bfs(a,b))





# def is_prime_list(n):
#     sieve = [True] * n #전부 소수라고 초기 설정
#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:
#             for j in range(i+i, n, i):
#                 sieve[j] = False
# # 소수 목록 산출
#     return [i for i in range(2, n) if sieve[i] == True]

#i이후 i의 배수들을 False 판정

# def bfs():
#     v=[[0]* W for _ in range(H)]
#     q= deque()
#     q.append((si,sj, -1))
#     v[si][sj] = 1
#     while q:
#         ci, cj,cnt = q.popleft()
#         if (ci,cj) == (ei,ej):
#             return cnt
#         for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
#             # 한줄 반복.... 
#             ni, nj = ci, cj
#             while True:
#                 ni, nj = ni+di, nj+dj 
#                 if 0<=ni<H and 0<=nj<W :
#                     if arr[ni][nj] =='*':
#                         break
#                     if v[ni][nj] == 0:
#                         q.append((ni,nj, cnt+1))
#                         v[ni][nj] = 1

#                 else:
#                     break

# W, H = map(int, input().split())
# arr= [list(input()) for _ in range(H)]
# flag = 0
# for i in range(H):
#     for j in range(W):
#         if arr[i][j] == 'C':
#             if flag == 0:
#                 si, sj = i, j
#                 flag = 1
#             else:
#                 ei, ej = i, j

# print(bfs())



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






# def water_line():
#     global v_w
#     v_w =[[2500]*C for _ in range(R)]

#     q=deque()
#     for i in water:
#         si,sj = i
#         q.append(i)
#         v_w[si][sj] = 0
#     while q:
#         ci,cj = q.popleft()
#         for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
#             ni, nj = ci+di, cj+dj
#             if 0<= ni <R and 0<=nj <C and v_w[ci][cj] +1 < v_w[ni][nj] \
#                 and arr[ni][nj] != 'D' and arr[ni][nj] !='X':
#                 v_w[ni][nj] = v_w[ci][cj] +1
#                 q.append((ni,nj))

# def bfs():
#     v=[[2500]*C for _ in range(R)]
#     q=deque()
#     q.append((Si,Sj))
#     v[Si][Sj] = 0
#     while q:
#         ci,cj = q.popleft()
#         if (ci,cj) == (Di,Dj):
#             return v[ci][cj]
#         for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
#             ni, nj = ci+di, cj+dj
#             if 0<= ni <R and 0<=nj <C and v[ci][cj] +1 < v[ni][nj] \
#                 and v[ci][cj]+1 < v_w[ni][nj] and arr[ni][nj] !='X':
#                 v[ni][nj] = v[ci][cj] +1
#                 q.append((ni,nj))
                  
#     return 'KAKTUS'

# R,C = map(int,input().split())
# arr = [list(input()) for _ in range(R)]
# water = []
# for i in range(R):
#     for j in range(C):
#         if arr[i][j]== 'D':
#             Di,Dj = i,j
#         if arr[i][j] =='S':
#             Si,Sj = i,j
#         if arr[i][j] =='*':
#             water.append((i,j))

# water_line()

# print(bfs())






# def bfs():
#     si, sj = 0, 0
#     k = K      # 벽 부순 횟수
#     v = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]

#     q = deque()
#     q.append((si,sj,k))
#     v[si][sj][K] = 1  # 벽 안 부순 탐색수
#     while q:
#         ci,cj,k = q.popleft()

#         if ci == N-1 and cj == M-1:
#             return  v[ci][cj][k]
        
#         for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
#             ni, nj = ci + di , cj +dj
#             if 0 <= ni < N and 0 <= nj < M :
#                 if arr[ni][nj] == 0 and v[ni][nj][k] ==0:
#                     v[ni][nj][k] = v[ci][cj][k]+1 
#                     q.append((ni,nj,k))              
#                 if arr[ni][nj]== 1 and k >0 and v[ni][nj][k] == 0: 
#                     v[ni][nj][k-1] = v[ci][cj][k] +1
#                     q.append((ni,nj,k-1))      
                    
#     return -1 

# N, M ,K= map(int, input().split())
# arr = [list(map(int,input())) for _ in range(N)]

# print(bfs())







# 16946 벽부수고 이동 4
# from collections import deque

# def grouping(si,sj):
#     global gr_no
#     cnt = 1
#     gr_numbers = set()
#     q = deque()
#     gr_numbers.add((si,sj))
#     v[si][sj] = 1
#     q.append((si,sj))
#     while q:
#         ci,cj = q.popleft()
#         for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
#             ni, nj = ci + di , cj +dj
#             if 0<= ni <N and 0<= nj < M and arr[ni][nj] == 0 and v[ni][nj] ==0:
#                 cnt += 1
#                 v[ni][nj] =1
#                 gr_numbers.add((ni,nj))
#                 q.append((ni,nj))
#     gr_no +=1            # 1번그룹부터.......
#     for y,x in gr_numbers:  
#         gr_board[gr_no] = cnt  # 그룹 넘버에 0의 갯수 저장
#         gr_names[y][x] = gr_no # 그룹 넘버를 보드좌표에 저장
#     return         

# N, M = map(int, input().split())
# arr = [list(map(int,input())) for _ in range(N)]
# v =[[0] * M for _ in range(N)]  # 방문 배열
# gr_board = {0:0}                # 0 그룹 이름: 0 갯수 
# gr_names = [[0] * M for _ in range(N)] # 좌표에 그룹 넘버 메모
# gr_no = 0                              #그룸 넘버 초기값
# near_4 = set()                         # 나중에 1 주변 4방향 그룹넘버 저장
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0 and v[i][j] == 0:
#             grouping(i,j)           # 그룹 만들기 (이름, 0의 갯수)

# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1:
#             for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
#                 ni, nj = i + di , j +dj
#                 if 0<= ni <N and 0<= nj < M :      # 1인경우 인접한 4곳 그룹이름 세트로저장
#                     near_4.add(gr_names[ni][nj])    # 중복방지를 위해
#             for c in near_4:                        # 이름에 따른 그룹cnt 합산   
#                 arr[i][j] += gr_board[c]           
#             arr[i][j] = arr[i][j]%10         # 10으로 나눈 나머지
#             near_4.clear()                   # 다음번 1을 위하여 세트 클리어    
            
# for lst in arr:
#     print(*lst, sep = '')



# input =sys.stdin.readline
#2206 벽부수고 이동하기
# from collections import deque
# def bfs():
#     si, sj = 0, 0
#     wall = 0      # 벽 부순 횟수
#     v = deque([[[0,0]for _ in range(M)] for _ in range(N)])
#     q = deque()
#     q.append((si,sj,wall))
#     v[si][sj][0] = 1  # 벽 안 부순 탐색수
#     while q:
#         ci,cj,wall = q.popleft()

#         if ci == N-1 and cj == M-1:
#             return  v[ci][cj][wall]
        
#         for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
#             ni, nj = ci + di , cj +dj
#             if 0 <= ni < N and 0 <= nj < M :
#                 if arr[ni][nj] == '0' and v[ni][nj][wall] ==0:
#                     v[ni][nj][wall] = v[ci][cj][wall]+1 # 1번도 안부수면 
#                     q.append((ni,nj,wall))              # wall 이 0인채 돌다가
#                 if arr[ni][nj]== '1' and wall == 0: # 1번 부수면 wall 이
#                     v[ni][nj][1] = v[ci][cj][0] +1  # 1로바뀌고 계속 돌아감      
#                     q.append((ni,nj,1))             # 이때 wall 0 값을 넘겨받음
                    
#     return -1 # 도달 못하면

# N, M = map(int, input().split())
# arr = [input() for _ in range(N)]

# print(bfs())





# a,b,c = map(int, input().split())

# def bfs(x,y,z):
#     tot = x+y+z
#     q=[]
#     v=[[0]*tot for _ in range(tot)]
#     v[x][y] = 1
#     q.append((x,y))
    
#     while q:
#         cx,cy= q.pop(0)
#         cz= tot -(cx+cy)
#         if cx==cy==cz:
#             return 1
#         for nx,ny in ((cx,cy),(cx,cz),(cy,cz)):
#             if nx==ny: continue
#             if nx>ny :
#                 nx,ny=ny,nx
#             nx, ny = nx + nx, ny - nx
#             mi = min(nx,ny, tot-(nx+ny))
#             ma = max(nx,ny, tot-(nx+ny))
#             if v[mi][ma]==0:	
#                 v[mi][ma] = 1
#                 q.append((mi,ma))
#     return 0	

# print(bfs(a,b,c))	


# # 14502 연구소
# from collections import deque
# from itertools import combinations

# def bfs(wall):                  # 바이러스 퍼트리는 함수
#     global cnt
#     cnt = CNT - 3         # 총 0의개수에서 벽 3개 뺀것 (정답의 초기값)
    
#     visit =[[0] * M for _ in range(N)] # 방문리스트
#     q = deque()
#     for ti,tj in virus:     # 바이러스 위치를  q에 삽입
#         visit[ti][tj] = 1   # 그곳 방문처리
#         q.append((ti,tj))
#     while q :
#         ci, cj = q.popleft()    # 큐 있는동안 4방향, 범위내, 미방문, 0 인곳
#         for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
#             ni , nj = ci + di, cj + dj
#             if 0<= ni < N and 0<= nj <M and arr[ni][nj] == 0 and visit[ni][nj] == 0:
#                 visit[ni][nj] = 1
#                 q.append((ni,nj))
#                 cnt -= 1        # 바이러스 번졌슴으로 -1 하기
    
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# lst = []                        # 0 인 좌표들의 리스트
# virus = []                      # 2 인 좌표리스트
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             lst.append((i,j))
#         if arr[i][j] ==2 :
#             virus.append((i,j))
# CNT = len(lst)                  # 시작전 0의 개수
# ans = 0

# for wall in combinations(lst,3): # 0인곳 3개씩 조합한 경우수(벽 세울곳)
#     for i,j in wall :            # 넘겨 받은 벽 세우기 (1로 표시)
#         arr[i][j] = 1   
#     bfs(wall)                   # 그 벽을 쌓고 바이러스 퍼트리기
#     ans = max(ans, cnt)
#     for i, j in wall :          
#         arr[i][j] = 0           # 벽 세운것 원위치

# print(ans)


# for i in range(CNT-2):      # 0인곳 3개씩 조합한 경우수(벽 세울곳)
#     for j in range(i+1, CNT-1):
#         for k in range(j+1, CNT):
#             bfs((lst[i],lst[j],lst[k]))  # 그 벽을 쌓고 바이러스 퍼트리기
#             ans = max(ans, cnt)
# print(ans)







# def bfs(k,cnt):
#     q=[]
#     v = [0] * 101
#     q.append((k,cnt))
#     while q:
#         k , cnt = q.pop(0)
#         if k == 100:        # 100 이면 완료
#             return cnt

#         for i in range(1,7):  # 주사위 1--6
#             nk = k+i
#             if 1<= nk <= 100 and v[nk] == 0: #범위내 미방문
#                 v[nk] = 1
#                 for j in range(N):           # 새위치가 뱀, 사다리
#                     if nk ==X[j] :nk = Y[j]
#                 for j in range(M):
#                     if nk == U[j] : nk =U[j]
#                 v[nk] = 1                   # 방문처리
#                 q.append((nk, cnt+1))
                
# N, M = map(int, input().split())
# X = []
# Y = []
# U = []
# V = []
# for i in range(N):  # 사다리 좌표
#     x, y = map(int, input().split())
#     X.append(x)
#     Y.append(y)
# for i in range(M):  # 뱀 좌표
#     u, v = map(int, input().split())
#     U.append(u)
#     V.append(v)

# print(bfs(1,0))




# def move(arr):   # 행단위로 이동 같은값 합치기
#     for i in range(len(arr)):  # 행 개수 만큼 처리
#         num = 0
#         tlst = []
#         for n in arr[i] : # 해당 행에서
#             if n == 0 : continue  
#             if n == num:  # 기준숫자와 같음, 합침
#                 tlst.append(num*2)
#                 num = 0
#             else:
#                 if num == 0 : # 처음 숫자를 만나면
#                     num = n
#                 else:
#                     tlst.append(num)
#                     num = n
#     # 종류후 기준숫자 있으면 tlst 추가 , 남은자리 0으로 채움
#         if num >0:
#             tlst.append(num)
#         arr[i] = tlst +[0] *(N - len(tlst)) # arr[i] 바꾸기
        



# def dfs(n,arr):
#     global ans
#     if n == 5 :
#         ans = max(ans, max(map(max,arr)))
#         return
    
#     # 좌측이동
#     narr = [lst[::] for lst in arr]  # 딥카피 $$$$$
#     move(narr)
#     dfs(n+1, narr)

#     narr = [lst[::-1] for lst in arr]  # 우측방향
#     move(narr)
#     dfs(n+1, narr)

#     arr_t = list(map(list, zip(*arr)))  # 전치행렬 열을 행으로사용
#     narr = [lst[::] for lst in arr_t]  # 상방향 딥카피 $$$$$
#     move(narr)
#     dfs(n+1, narr)

#     narr = [lst[::-1] for lst in arr_t]  # 하방향
#     move(narr)
#     dfs(n+1, narr)

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# dfs(0, arr)
# print(ans)


# # 1062 단어교육
# from itertools import combinations
# N, K = map(int, input().split())
# word_list = []
# for _ in range(N):
#     word_list.append(input().rstrip()[4:-4]) 

# def solve(t):
#     ct = 0
#     for word in word_list:
#         flag = 1
#         for alphabet in word:
#             if learnt[ord(alphabet)] == 0 :
#                 flag = 0
#                 break
#         if flag == 1:
#             ct += 1   
#     return ct

# if K >= 5:
#     learnt = [0] * 123
#     for x in {'a','c','i','n','t'} :
#         learnt[ord(x)] = 1
#     alphbets = set(chr(i) for i in range(97,123)) - {'a','c','i','n','t'} 
#     ans = 0
#     for teach in combinations(alphbets, K-5):
#         for t in teach:
#             learnt[ord(t)] = 1
#         cnt = solve(teach)
#         if cnt > ans :
#             ans = cnt
#         for t in teach:
#             learnt[ord(t)] = 0
#     print(ans) 
# else:
#     print(0)



# for i in range(123) :



# def dfs(n,sm):  # 백트랙킹  (모든경우 탐색  2^50 정도까지 가능)
#     global ans
#     if n >= N :
#         ans= max(ans, sm)
#         return

#     if n + arr[n][0]<= N:
#         dfs(n+arr[n][0], sm+arr[n][1]) 
#     dfs(n+1, sm)

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# ans = 0
# dfs(0,0)
# print(ans)

# Dp
# N = int(input())
# T = [0] * N
# P = [0] * N
# for i in range(N):
#     T[i], P[i] = map(int, input().split()) 

# dp = [0] * (N+1)
# for n in range(N-1, -1, -1): # 뒤 부터
#     if n + T[n] <= N:
#         dp[n] = max(dp[n+T[n]] + P[n], dp[n+1])
#     else:
#         dp[n] = dp[n+1]
# ans = dp[0]    
# print(ans)


# # 2580 스도쿠

# arr = [list(map(int, input().split())) for _ in range(9)]

# def valid(ci,cj,cv):
#     if cv in lst[ci]:
#         return False
#     for i in range(9):
#         if cv == lst[i][cj]:
#             return False
#     boxi = ci//3 * 3
#     boxj = cj//3 * 3
#     for i in range(3):
#         for j in range(3):
#             if cv == arr[boxi+i][boxj+j]:
#                 return False
#     return True    

# def sudoku(n):
#     if n== len(blank):
#         for line in arr: 
#             print(*line)
#         exit()
#     for i in range(1,10):
#         y = blank[n][0]
#         x = blank[n][1]
#         if valid(y,x,i):
#             arr[y][x] = i
#             sudoku(n+1)
#             arr[y][x] = 0

# lst = []
# blank = []
# for i in range(9):
#     lst.append(arr[i])
#     for j in range(9):
#         if arr[i][j] == 0 :
#             blank.append((i,j))
# sudoku(0)

