import sys  
sys.stdin = open("input.txt", "r")
from collections import deque
# input = sys.stdin.readline

def byunwhan(si,sj):
    for i in range(si,si+3):
        for j in range(sj, sj+3):
            A[i][j] = 1 - A[i][j]
    return

N, M = map(int, input().split())
A=[]
B=[]
for _ in range(N):
    A.append(list(map(int, input())))
for _ in range(N):
    B.append(list(map(int, input())))

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            byunwhan(i,j)
            cnt += 1
flag = 0
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            flag = 1
            break
if flag == 1:
    print(-1)
else:
    print(cnt)

# p =[0]*N
# p= list(map(int,input().split()))
# p.sort()
# np = 0   
# ans = 0
# for i in range(N):
#     np += p[i]      # 사람별 실제 대기시간
#     ans += np       # 누적 대기시간 
# print(ans)


# N = int(input())
# c = [[0] *2 for _ in range(N)] 
# for i in range(N):
#     c[i] = list(map(int, input().split()))
   
# c.sort(key = lambda x: (x[1],x[0]))
# cnt = 1
# et = c[0][1]
# for i in range(1,N):
#     if c[i][0] >= et:
#         et = c[i][1]
#         cnt += 1
    
# print(cnt)

# N, K = map(int, input().split())
# c=[]
# for i in range(N):
#     c.append(int(input()))
# c.sort(reverse= True)
# cnt = 0
# while True:
#     if K == 0:
#         break
#     for i in c:
#         if i > K : continue
#         while True:
#             K= K - i
#             cnt += 1
#             if i > K:
#                 break
# print(cnt)

# def bfs(s,t):
#     tlst =[]
#     q = deque()
#     v = set()
#     q.append((s,''))
#     while q:
#         c, tlst = q.popleft()
#         if c == t:
#             return tlst
#         for i in range(4):
#             if i == 0 and c*c <=1000000000  : # 곱셈
#                 n = c * c
#                 if n not in v:
#                     q.append((n,tlst + '*'))
#                     v.add(n)
#             elif i == 1 and c+c <= 1000000000 :
#                 n = c + c
#                 if n not in v:
#                     q.append((n,tlst + '+'))
#                     v.add(n)
#             elif i == 2:
#                 n = 0
#                 if n not in v:
#                     q.append((n,tlst +'-'))
#                     v.add(n)
#             elif i == 3 and c != 0:
#                 n = 1
#                 if n not in v:
#                     q.append((n,tlst +'/'))
#                     v.add(n)
#     return -1

# s,t = map(int, input().split())
# if s == t :
#     ans = 0
# else:
#     ans = bfs(s,t)
# print(ans)


# def bfs():
#     v=[[0] * W for _ in range(H)]
#     c=[[10000] * W for _ in range(H)]
#     q=deque()
#     q.append((si,sj,0,0))
#     v[si][sj] = 1
#     while q:  
#         ci, cj , dr, cnt= q.popleft()

#         if (ci,cj) == (ei,ej):
#             print(c)
            
#             return 

       
#         for di,dj,nr in ((-1,0,1),(1,0,2),(0,-1,3),(0,1,4)) :
#             ni, nj = ci + di, cj + dj
#             if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] != '*' and v[ni][nj]==0:
#                 if dr!=0 and dr != nr:
#                     q.append((ni,nj,nr,cnt+1))
#                     c[ni][nj] = min(c[ci][cj]+1,cnt+1)
#                 else:                
#                     q.append((ni,nj,nr,cnt))
#                     c[ni][nj] = min(c[ci][cj],cnt)
#                 v[ni][nj] = v[ci][cj]+1
              
        
# W, H = map(int, input().split())
# arr = [list(input()) for _ in range(H)]
# flag = 0
# for i in range(H):
#     for j in range(W):
#         if arr[i][j] == 'C':
#             if flag == 0:
#                 si, sj = i, j
#                 flag = 1
#             else:
#                 ei, ej = i, j

# # print(si,sj,ei,ej)

# print(bfs())





# from collections import deque
# input = __import__('sys').stdin.readline
# n = 8
# graph = [list(input().strip()) for _ in range(n)]
# visited = [[False] * n for _ in range(n)]
# dx = [0, 0, 1, -1, 1, -1, 1, -1, 0]
# dy = [1, -1, 0, 0, 1, 1, -1, -1, 0]

# q = deque()
# q.append((7, 0))
# visited[7][0] = True
# ans = 0
# while q:
#     i, j = q.popleft()
#     if graph[i][j] == '#':
#         continue
#     for idx in range(n + 1):
#         ni = i + dy[idx]
#         nj = j + dx[idx]
#         if ni < 0 or ni >= n or nj < 0 or nj >= n or graph[ni][nj] == '#':
#             continue
#         if ni == 0:
#             ans = 1
#         if not visited[ni - 1][nj]:
#             visited[ni - 1][nj] = True
#             q.append((ni - 1, nj))
# print(ans)

# input = sys.stdin.readline
# N, M, K = map(int, input().split())
# MAX = 500000

# arr = [list(map(int, input().strip())) for _ in range(N)]
# v = [[[MAX]*(K+1) for _ in range(M)] for _ in range(N)]
# v[0][0][K] = 0
# q = deque([(0, 0, 1, K)])
# ans = MAX

# while q :
#   ci, cj, cnt, brk = q.popleft()
#   if (ci, cj) == (N-1, M-1) :
#     print(cnt)
#     ans = min(ans, cnt)
    
#     continue

#   daytime = cnt % 2
#   for di,dj in ((-1,0),(1,0),(0,-1),(0,1)) :
#     ni, nj = ci + di, cj + dj
#     if 0 <= ni < N and 0 <= nj < M :
#       if arr[ni][nj] == 0 and v[ni][nj][brk] > cnt:
#         v[ni][nj][brk] = cnt
#         q.append((ni, nj, cnt+1, brk))
#       if arr[ni][nj] == 1 and brk and v[ni][nj][brk-1] > cnt :
#         if daytime : 
#           v[ni][nj][brk-1] = cnt
#           q.append((ni, nj, cnt+1, brk-1))
#         else :
#           q.append((ci, cj, cnt+1, brk))

# print(ans if ans < MAX else -1)

# # 9019 DSLR

# def bfs(a, b, ans):
#     q =[(a,ans)]
#     v =[0] * 10000
#     while q:
#         ca, ans = q.pop(0)
    
#         if ca == b :
#             return ans
#         for character in 'DSLR':
            
#             if character == 'D' :
#                 if 2 * ca > 9999:
#                     new_a = (2* ca ) % 10000
#                     if v[new_a] == 0:
#                         v[new_a] = 1
#                         q.append((new_a, ans + 'D'))
#                 else :
#                     new_a = 2 * ca
#                     if v[new_a] == 0:
#                         v[new_a] = 1
#                         q.append((new_a, ans + 'D'))
              
#             if character == 'S' :
#                 if ca == 0 :
#                     new_a = 9999
#                 else:
#                     new_a = ca -1
          
#                 if v[new_a] == 0:
#                     v[new_a] = 1
#                     q.append((new_a, ans +'S'))
#             if character == 'L' :
#                 tmp_ca = '0000' + str(ca)
#                 str_ca = tmp_ca[-4:]
#                 new_ca = str_ca[1:] + str_ca[:1]
#                 if new_ca =='0000':
#                     new_a = 0
#                     if v[new_a] == 0:
#                         v[new_a] = 1
#                         q.append((new_a, ans +'L'))
#                 else:
#                     slicing = 0
#                     for i in new_ca:
                    
#                         if i=='0':
#                             slicing += 1
#                         else:
#                             break
#                     new_ca = new_ca[slicing:]
                
#                     new_a = int(new_ca)
#                     if v[new_a] == 0:
#                         v[new_a] = 1
#                         q.append((new_a, ans +'L'))
#             if character == 'R' :
#                 tmp_ca = '0000' + str(ca)
#                 str_ca = tmp_ca[-4:]
#                 new_ca = str_ca[-1:] + str_ca[:3]
#                 if new_ca =='0000':
#                     new_a = 0
#                     if v[new_a] == 0:
#                         v[new_a] = 1
#                         q.append((new_a, ans +'R'))
#                 else:
#                     slicing = 0
#                     for i in new_ca:
                
#                         if i=='0':
#                             slicing += 1
#                         else:
#                             break
#                     new_ca = new_ca[slicing:]
            
#                     new_a = int(new_ca)
#                     if v[new_a] == 0:
#                         v[new_a] = 1
#                         q.append((new_a, ans +'R'))

# T = int(input())
# for _ in range(T):
#     A , B = map(int, input().split())
#     print(bfs(A, B, ''))







# 16948 death knight

# def bfs(r,c,end_r,end_c,cnt):
#     visit = [[0] * (N) for _ in range(N)] # 방문기록
#     visit[r][c] = 1                        
#     q = [(r,c,cnt)]
#     d =[(-2, -1),(-2, 1),(0, -2),(0, 2),(2, -1),(2, 1)]
#     while q:
#         cur_r ,cur_c, cnt = q.pop(0)
#         if cur_r == end_r and cur_c == end_c:
#             return cnt
#         for i in range(6) :
#             new_r, new_c = cur_r + d[i][0] , cur_c +d[i][1]
#             if 0 <= new_r < N and 0 <= new_c < N and visit[new_r][new_c] ==0:
#                 visit[new_r][new_c] = 1
#                 q.append((new_r,new_c,cnt + 1))

#     return -1

# N = int(input())
# r, c, end_r, end_c = map(int, input().split())

# print(bfs(r,c, end_r, end_c, 0)) # 시작, 끝, 카운트

# def bfs(n, cnt):
#     visit = [0]*101
#     visit[1] = 1
#     q = []

#     q.append((n,cnt))
#     while q :
#         current_pos, cnt = q.pop(0)
#         if current_pos == 100 :
#             return cnt

#         for i in range(1,7):
#             new_pos = current_pos + i
#             if 1 <= new_pos <= 100 and visit[new_pos] == 0:
#                 visit[new_pos] = 1
#                 if new_pos in ladder:
#                     new_pos = ladder[new_pos]
#                 if new_pos in snake:
#                     new_pos = snake[new_pos]
#                 visit[new_pos] = 1
#                 q.append((new_pos,cnt +1))
    
# ladder = {}
# snake = {}
# N ,M = map(int, input().split())
# for i in range(N):
#     key, value = map(int, input().split()) 
#     ladder[key] = value
# for i in range(M):
#     key, value = map(int, input().split()) 
#     snake[key] = value   

# print(bfs(1,0))





# # 12100 2048game
# def move(t_arr):
#     for i in range(N):
#         t_lst = []
#         num = 0
#         for n in t_arr[i] : # 해당 행에서
#             if n == 0 : continue  
#             if n == num:  # 기준숫자와 같음, 합침
#                 t_lst.append(num*2)
#                 num = 0
#             else:
#                 if num == 0 : # 처음 숫자를 만나면
#                     num = n
#                 else:
#                     t_lst.append(num)
#                     num = n
#     # 종류후 기준숫자 있으면 tlst 추가 , 남은자리 0으로 채움
#         if num >0:
#             t_lst.append(num)
#         t_arr[i] = t_lst +[0] *(N - len(t_lst)) # arr[i] 바꾸기
        
   
# def dfs(n, arr):
#     global ans
#     if n == 5:
#         ans = max(ans, max(map(max, arr)))
#         return
    
#     t_arr = [lst[::] for lst in arr]
#     move(t_arr)
#     dfs(n+1, t_arr)

#     t_arr = [lst[::-1] for lst in arr]
#     move(t_arr)
#     dfs(n+1, t_arr)

#     arr_temp = list(map(list, zip(*arr)))
#     t_arr = [lst[::] for lst in arr_temp]
#     move(t_arr)
#     dfs(n+1, t_arr)

#     t_arr = [lst[::-1] for lst in arr_temp] 
#     move(t_arr)
#     dfs(n+1, t_arr)

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# ans = 0
# dfs(0, arr)
# print(ans)


# 13460 구슬 탈출 2
# def move(i, j, dr):
#     back  = -1
#     for c in range(1,10):                   # 이동칸수 최대 9
#         ni, nj = i + di[dr]*c, j +dj[dr] * c  # 1칸 부터....
#         if arr[ni][nj] == '#' : return c + back # 벽만나면 뒤로 1칸
#         if arr[ni][nj] == 'O' : return c        # O 만나면 그만큼
#         if arr[ni][nj] == 'R' or arr[ni][nj] == 'B': back -=1 #겹쳐지나면 -1 빼기

# def dfs(n,ri,rj,bi,bj):
#     global ans
#     if (n,ri,rj,bi,bj) in v_set: # 이미 간 경우면 그만 
#         return
#     v_set.add((n,ri,rj,bi,bj))   # 갈 때 마다 표시
#     if n >= ans:                # 이미 n 이 이전ans 보다 크면 그만
#         return
#     if n > 10 :                 # 종료 조건
#         return 
#     for dr in range(4):         # 4방향
#         r_cnt = move(ri,rj,dr)  # 방향 별 이동 칸수만큼 
#         b_cnt = move(bi,bj,dr)
#         if r_cnt ==0 and b_cnt ==0: # 못움직이는 경우 다음 탐색
#             continue
#         nri, nrj = ri + di[dr] * r_cnt, rj +dj[dr] * r_cnt # 새 좌표
#         nbi, nbj = bi + di[dr] * b_cnt, bj +dj[dr] * b_cnt
#         if arr[nbi][nbj] =='O':         # 새 파란공 좌표가 O 면 그만
#             continue
#         else:
#             if arr[nri][nrj] == 'O':    # 새 빨간공 좌표가 O 면 n, ans 비교
#                 ans = min(ans, n)
#                 return 
            
#         arr[ri][rj], arr[bi][bj] = '.', '.'   # 공있던 자리 . 으로표시
#         arr[nri][nrj], arr[nbi][nbj] = 'R', 'B'   # 새 자리 공으로 표시     
#         dfs(n+1,nri,nrj,nbi,nbj)                # 그다음 탐색
#         arr[nri][nrj], arr[nbi][nbj] = '.', '.' # 새자리 다시 . 으로 표시
#         arr[ri][rj], arr[bi][bj] = 'R', 'B'     # 공있던 자리 공으로 원위치
 
# N, M = map(int, input().split())
# arr = [list(input()) for _ in range(N)]

# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 'R' : ri, rj = i, j
#         if arr[i][j] == 'B' : bi, bj = i, j

# v_set = set()           # visited
# di = [-1,1,0,0]
# dj = [0,0,-1,1]
# ans = 11
# dfs(1,ri,rj,bi,bj)
# if ans == 11:
#     ans = -1
# print(ans)

# from itertools import combinations
# N, K = map(int, input().split())
# lst = []

# def solve(lst, lnd):
#     cnt = 0
#     for word in lst:
#         canread = 1
#         for w in word:
#             if lnd[ord(w)] ==0:
#                 canread = 0
#                 break
#         if canread:
#             cnt += 1
#     return cnt

# if K < 5 :
#     print(0)
# else:
#     for i in range(N):
#         lst.append(input().rstrip()[4:-4])
        
#     ans = 0
#     ab = set(chr(i) for i in range(97,123)) -{'a','c','i','n','t'}
#     lnd = [0]* 123
#     for x in {'a','c','n','i','t'} :
#         lnd[ord(x)] = 1
#     for teach in combinations(ab,K-5):
#         for t in teach:
#             lnd[ord(t)] =1
#         cnt = solve(lst, lnd)
#         if cnt > ans:
#             ans = cnt
#         for t in teach:
#             lnd[ord(t)] = 0
       
#     print(ans)




# from collections import deque
# def bfs():
    
#     v = [[set() for _ in range(C)] for _ in range(R)]
#     q=deque()
#     ans = 1
    
#     q.append((0,0,arr[0][0]))
#     while q:
#         ci,cj, cv = q.popleft()
#         ans = max(ans, len(cv))

#         for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
#             ni,nj = ci + di, cj +dj
#             if 0<= ni < R and 0<= nj <C and arr[ni][nj] not in cv :
#                 if cv +arr[ni][nj] not in v[ni][nj]:
#                     q.append((ni,nj,cv+arr[ni][nj]))
#                     v[ni][nj].add((cv+arr[ni][nj]))
            
#     return ans

# R, C = map(int, input().split())
# arr = list(input().rstrip() for _ in range(R))
# ans = bfs()
# print(ans)


# def dfs(ci,cj,cnt):
#     global ans
#     ans = max(ans, cnt)   
#     if ans == 26 :
#         return
#     for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        
#         ni,nj = ci + di, cj +dj
        
#         if 0<= ni < R and 0<= nj <C and v[ord(arr[ni][nj])] == 0 :

#             v[ord(arr[ni][nj])] = 1
#             cnt += 1
#             dfs(ni,nj,cnt)   
#             v[ord(arr[ni][nj])] = 0
#             cnt -= 1         
          
#     return

# R, C = map(int, input().split())

# arr = list(input().rstrip() for _ in range(R))

# v = list([0] * 128)
# v[ord(arr[0][0])] = 1
# ans = 1
# dfs(0,0,1)
# print(ans)





# 4574 스도미노쿠 
# def backtracking(pos):
#     global flag
#     if flag:
#         return
#     if pos == 81:
#         for i in range(9):
#             print(''.join(map(str, sudoku_map[i])))
#         flag = True
#         return

#     y = pos // 9
#     x = pos % 9

#     if sudoku_map[y][x] == 0:
#         for dir in range(2):
#             ny = y + dy[dir]
#             nx = x + dx[dir]
#             if ny >= 9 or nx >= 9:
#                 continue
#             if sudoku_map[ny][nx] != 0:
#                 continue
#             for i in range(1, 9):
#                 for j in range(i + 1, 10):
#                     if not check[i][j]:
#                         check[i][j] = True
#                         if not row[y][i] and not col[x][i] and not matrix[(y // 3) * 3 + x // 3][i] and \
#                            not row[ny][j] and not col[nx][j] and not matrix[(ny // 3) * 3 + nx // 3][j]:
#                             sudoku_map[y][x] = i
#                             sudoku_map[ny][nx] = j
#                             row[y][i] = col[x][i] = matrix[(y // 3) * 3 + x // 3][i] = True
#                             row[ny][j] = col[nx][j] = matrix[(ny // 3) * 3 + nx // 3][j] = True
#                             backtracking(pos + 1)
#                             sudoku_map[y][x] = 0
#                             sudoku_map[ny][nx] = 0
#                             row[y][i] = col[x][i] = matrix[(y // 3) * 3 + x // 3][i] = False
#                             row[ny][j] = col[nx][j] = matrix[(ny // 3) * 3 + nx // 3][j] = False
#                         if not row[y][j] and not col[x][j] and not matrix[(y // 3) * 3 + x // 3][j] and \
#                            not row[ny][i] and not col[nx][i] and not matrix[(ny // 3) * 3 + nx // 3][i]:
#                             sudoku_map[y][x] = j
#                             sudoku_map[ny][nx] = i
#                             row[y][j] = col[x][j] = matrix[(y // 3) * 3 + x // 3][j] = True
#                             row[ny][i] = col[nx][i] = matrix[(ny // 3) * 3 + nx // 3][i] = True
#                             backtracking(pos + 1)
#                             sudoku_map[y][x] = 0
#                             sudoku_map[ny][nx] = 0
#                             row[y][j] = col[x][j] = matrix[(y // 3) * 3 + x // 3][j] = False
#                             row[ny][i] = col[nx][i] = matrix[(ny // 3) * 3 + nx // 3][i] = False
#                         check[i][j] = False
#     else:
#         backtracking(pos + 1)


# def main():
#     global flag
#     T = 0
#     while True:
#         sudoku_map.clear()
#         row.clear()
#         col.clear()
#         matrix.clear()
#         check.clear()
#         flag = False

#         n = int(input())
#         if n == 0:
#             break
#         T += 1
#         for _ in range(9):
#             sudoku_map.append([0] * 9)
#             row.append([False] * 10)
#             col.append([False] * 10)
#             matrix.append([False] * 10)
#             check.append([False] * 10)
      
#         for _ in range(n):
#             a1, b1, a2, b2 = input().split()
#             a1 = int(a1)
#             a2 = int(a2)
#             y = ord(b1[0]) - ord('A')
#             x = int(b1[1]) - 1
#             sudoku_map[y][x] = a1
#             row[y][a1] = col[x][a1] = matrix[(y // 3) * 3 + x // 3][a1] = True
#             y = ord(b2[0]) - ord('A')
#             x = int(b2[1]) - 1
#             sudoku_map[y][x] = a2
#             row[y][a2] = col[x][a2] = matrix[(y // 3) * 3 + x // 3][a2] = True
#             if a1 < a2:
#                 check[a1][a2] = True
#             else:
#                 check[a2][a1] = True
#         bb = list(map(str, input().split()))
#         for i in range(1, 10):
#             b1 = bb[i-1]
#             y = ord(b1[0]) - ord('A')
#             x = int(b1[1]) - 1
#             sudoku_map[y][x] = i
#             row[y][i] = col[x][i] = matrix[(y // 3) * 3 + x // 3][i] = True

#         print("Puzzle", T)
#         backtracking(0)


# if __name__ == "__main__":
#     dy = [0, 1]
#     dx = [1, 0]
#     sudoku_map = []
#     row = []
#     col = []
#     matrix = []
     
#     check = []
#     flag = False
#     main()

# arr=[list(map(int, input().split())) for _ in range(9)]
# def valid(ci,cj,cv):   
#     for j in range(9):   # 가로 점검
#         if cv == arr[ci][j] :
#             return False

#     for i in range(9):     # 세로 점검
#         if cv == arr[i][cj]:
#             return False

#     for i in range(3):
#         for j in range(3):
#             if cv == arr[ci//3 * 3 + i][cj//3 * 3 + j]: # 칸내에 이미 있으면
#                 return False

#     return True

# def sudoku(n):
#     if n==len(blank): # 종료조건
#         for lst in arr:
#             print(*lst)
#         exit()

#     for i in range(1,10):
#         y = blank[n][0]
#         x = blank[n][1]
#         if valid(y,x,i):
#             arr[y][x] = i
#             sudoku(n+1)
#             arr[y][x] = 0

# blank =[]
# for i in range(9):
#     for j in range(9):
#         if arr[i][j] == 0:
#             blank.append([i,j])

# sudoku(0)



# if valid(1,4,3) :
#     print("가능")
# else:
#     print("안돼요")



# 
# # 16198 구슬

# def dfs(e,energy):
#     for i in range(2 , len(e)-1):
#         v[i]= 1
#         energy += energy +e[i-1]*e[i+1]
#         tmp = e.pop(i)
#         dfs(e,energy)
#         e.insert(i,tmp)
#         v[i]=0






# N = int(input())
# W = [0]+list(map(int, input().split()))
# v=  [0] *(N+1)
# energy = 0

# dfs(W,energy)
# print(energy)






# # 16197 두동전


# def bfs(s):
#     q=deque()
#     di = [-1,0,1,0]
#     dj = [0,-1,0,1]
#     q.append(s)
#     while q:
#         cai,caj,cbi,cbj,cnt = q.popleft()
      
#         # 정답처리
#         if cnt >= 10:
#             return -1
#         for i in range(4):
#             nai = cai + di[i]
#             naj = caj + dj[i]
#             nbi = cbi + di[i]
#             nbj = cbj + dj[i]
#             # 일단 visited는 생략          # 범위내 이면
#             if 0<= nai <N and 0<= naj <M and 0<= nbi <N and 0<= nbj <M: 
#                 # 벽 이면
#                 if arr[nai][naj] =="#":
#                     nai, naj = cai, caj
#                 if arr[nbi][nbj] =="#":
#                     nbi, nbj = cbi, cbj
#                 q.append([nai,naj,nbi,nbj,cnt+1])
#             elif 0<= nai <N and 0<= naj <M: # 동전 B가 떨어진경우
#                 return cnt + 1
#             elif 0<= nbi <N and 0<= nbj <M: # 동전 A가 떨어진경우
#                 return cnt + 1
#             else: # 둘다 빠진경우
#                 continue
#     return -1 

# N, M = map(int, input().split())
# arr = [list(input().rstrip()) for _ in range(N)]
# st_pos =[]
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 'o' :
#             st_pos.append(i)
#             st_pos.append(j)

# print(bfs([*st_pos,0]))




# from collections import deque




# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# def bfs():
#     while coin:
#         x1, y1, x2, y2, cnt = coin.popleft()

#         if cnt >= 10:
#             return -1

#         for i in range(4):
#             nx1 = x1 + dx[i]
#             ny1 = y1 + dy[i]
#             nx2 = x2 + dx[i]
#             ny2 = y2 + dy[i]

#             if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
#                 # 벽이라면
#                 if board[nx1][ny1] == "#":
#                     nx1, ny1 = x1, y1
#                 if board[nx2][ny2] == "#":
#                     nx2, ny2 = x2, y2
#                 coin.append((nx1, ny1, nx2, ny2, cnt + 1))
#             elif 0 <= nx1 < n and 0 <= ny1 < m:  # coin2가 떨어진 경우
#                 return cnt + 1
#             elif 0 <= nx2 < n and 0 <= ny2 < m:  # coin1가 떨어진 경우
#                 return cnt + 1
#             else:  # 둘 다 빠진 경우 무시
#                 continue

#     return -1


# if __name__ == "__main__":
#     n, m = map(int, input().split())

#     coin = deque()
#     board = []
#     temp = []
#     for i in range(n):
#         board.append(list(input().strip()))
#         for j in range(m):
#             if board[i][j] == "o":
#                 temp.append((i, j))

#     coin.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))

#     print(bfs())
# 14500 테트로미노 백트랙킹


# def dfs(n, sm, tlst):
#     global ans
#     if ans > sm + max_ans * (4-n): # 4개중 나머지를 최대값으로채워도 
#         return                     # 작을 때는 가지치기 (시간절약)
#     if n == 4:                     # 6400ms --> 200 ms !!!
#         ans = max(ans, sm)
#         return
    
#     for ci, cj in tlst:
#         for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
#             ni, nj = ci +di, cj +dj
#             if 0<= ni <N and 0<= nj <M:
#                 if v[ni][nj] == 0:
#                     v[ni][nj] = 1
#                     dfs(n+1,sm +arr[ni][nj], tlst +[(ni,nj)])
#                     v[ni][nj] = 0

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# v = [[0]*M for _ in range(N)]
# ans = 0
# max_ans = max(map(max, arr))

# for i in range(N):
#     for j in range(M):
#         v[i][j] = 1
#         dfs(1, arr[i][j],[(i,j)])

# print(ans)

# # 14500 테트로미노 부르트포스

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# tetriminos =[[(0,1),(0,2),(0,3)],[(1,0),(2,0),(3,0)],      # 1 - 
#     [(0,1),(1,0),(1,1)],                            # ㅁ 자
#     [(1,0),(2,0),(2,1)],[(0,-1),(0,-2),(1,-2)],     # L 시계방향회전
#     [(-1,0),(-2,0),(-2,-1)],[(0,1),(0,2),(-1,2)],
#     [(1,0),(2,0),(2,-1)],[(0,-1),(0,-2),(-1,-2)],   # L 대칭 시계방향
#     [(-1,0),(-2,0),(-2,1)],[(0,1),(0,2),(1,2)],
#     [(1,0),(1,1),(2,1)],[(0,-1),(1,-1),(1,-2)],     # ㄹ 시계방향
#     [(-1,0),(-1,-1),(-2,-1)],[(0,1),(-1,1),(-1,2)],
#     [(1,0),(1,-1),(2,-1)],[(0,-1),(-1,-1),(-1,-2)], # ㄹ 대칭 시계방향
#     [(-1,0),(-1,1),(-2,1)],[(0,1),(1,1),(1,2)],
#     [(0,1),(0,2),(1,1)],[(1,0),(2,0),(1,-1)],       # ㅜ 시계방향
#     [(0,-1),(0,-2),(-1,-1)],[(-1,0),(-2,0),(-1,1)]]

# ans = 0

# for i in range(N):
#     for j in range(M):
#         for t in tetriminos:
#             sm=arr[i][j]
#             for di,dj in t:
#                 if 0<= i+di <N and 0<= j+dj <M:
#                     sm += arr[i+di][j+dj]
#                 else:
#                     sm = 0
#                     break
#             ans = max(ans, sm)        
# print(ans)

# def dfs(n,s, roto):
#     if n == 6:
#         ans.append(roto)
#         return
#     for i in range(s,k):
#         dfs(n+1, i+1, roto + [S[i]])

# while True:        
#     lst = list(map(int,input().split()) )  
#     k = lst[0]
#     if k == 0:break
#     S = lst[1::]
#     ans = []

#     dfs(0, 0,[])
#     for i in ans:
#         print(*i)
#     print()

# def calc(A, B):
#     a_sum = b_sum = 0
#     for i in range(M):
#         for j in range(M):
#             a_sum += S[A[i]][A[j]]
#             b_sum += S[B[i]][B[j]]   
#     return abs(a_sum - b_sum)                             
    
# def dfs(n, a_list, b_list):
#     global ans
#     if n == N: 
#         if len(a_list) == len(b_list):
#             ans = min(ans, calc(a_list, b_list))
#         return
#     dfs(n+1, a_list + [n],b_list)
#     dfs(n+1, a_list, b_list + [n])

# N = int(input())
# S = [list(map(int, input().split())) for _ in range(N)]

# M = N//2
# ans = N*100*100
# dfs(0, [], [])
# print(ans)

# # 14888 연산자끼워넣기  (백 트랙킹-- 조건 달린 회귀)

# N = int(input())
# lst = list(map(int, input().split())) # 숫자
# add , sub, mul, div = map(int, input().split()) # add , sub, mul, div
# min_sm = int(1e9)
# max_sm = -int(1e9)
# def dfs(n, sm, add, sub, mul, div):
#     global min_sm, max_sm
    
#     if sm > int(1e9) or sm < - int(1e9):    # n
#         return                              # n+1     +  -  x  %
#                                             # 각경우마다 부호가 남았음 계속가지치기
#                                            # n==N 일때 값 저장 비교.... 
#     if n == N: 
#         max_sm = max(max_sm, sm)
#         min_sm = min(min_sm, sm)
#         return
    
#     if add > 0 : 
#         dfs(n+1, sm + lst[n], add - 1, sub, mul, div)
#     if sub > 0 : 
#         dfs(n+1, sm - lst[n], add, sub - 1, mul, div)
#     if mul > 0 : 
#         dfs(n+1, sm * lst[n], add, sub, mul - 1, div)
#     if div > 0 : 
#         dfs(n+1, int(sm/lst[n]), add, sub, mul, div - 1)

# dfs(1, lst[0], add, sub, mul, div)
# print(max_sm, min_sm, sep="\n")





# k = int(input())
# a = list(input().split())

# v = [0] * 10
# s =''
# min_ans = ''
# max_ans = ''
# def check(x, y, symbol):
#     if symbol == '<' and x < y :
#         return True
#     elif symbol == '>' and x > y :
#         return True
#     else:
#         return False
    
# def solve(cur, s):
#     global min_ans, max_ans
#     if  cur == k+1:
#         if len(min_ans) == 0:
#             min_ans = s
#         else:
#             max_ans = s
#         return
            
#     for i in range(10):
#         if v[i] == 0:
#             if cur == 0 or check(s[-1], str(i), a[cur-1]):
#                 v[i] = 1
#                 solve(cur + 1, s + str(i))
#                 v[i] = 0

# solve(0,'')
# print(max_ans)
# print(min_ans)