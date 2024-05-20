import sys  
sys.stdpin = open("bjtest.txt", "r")
input = sys.stdpin.readline






# # 2133

# n = int(input())
# dp = [0]*(31)
# dp[0] = 1
# dp[2] = 3
# for i  in range(4, n+1,2):
#     dp[i] = dp[i-2]*3 
#     # for j in range(i-4, -1, -2):
#     for j in range(0,i-3, 2):
#         dp[i] +=dp[j] *2 
# print(dp[n])

# 1172?
#11055 
# n=int(input())
# arr=list(map(int, input().split()))
# dp=[x for x in arr]

# for i in range(1,n):
#     for j in range(i):
#         if arr[j]<arr[i]:
#             dp[i]=max(dp[i], dp[j]+arr[i])    
# print(max(dp))
# n = int(input())
# A = list(map(int,input().split()))
# dp = [0]*1001

# for i in A:
#     dp[i] = max(dp[:i])+i
# print((dp))
# # 1912
# n= int(input())
# a= list(map(int, input().split()))
# for i in range(1,n):
#     a[i] = max(a[i], a[i-1]+a[i])
# print(max(a))





# n = int(input())
# a = list(map(int, input().split()))
# dpp = [0] * n
# for i in range(n):
#     for j in range(i):
#         if a[i] > a[j] andp dpp[i] < dpp[j]:
#             dpp[i] = dpp[j]
#     dpp[i] += 1
# print(max(dpp))



#10844 쉬운 계단수
# n= 2
# dpp =[0]*(n+1)
# dpp[1]= 9    #   1     2     3      4      5      6      7    8     9
#             #  0 2   1  3  2  4  3   5  4   6  5   7  6  8  7  9  8
#             #   11 30 22 41 33 52 4 4 63 5 5 74 6 6 85 77 96 88  7 9
#             #  0 1 2 3 4 5 6 7 8 9 (1의자리수)
#             #  0 1 1 1 1 1 1 1 1 1   1자리  
#             #  1 1 2 2 2 2 2 2 2 1   2자리
#             #  1 3 3 4 4 4 4 4 3 2   3자리  
#             #  / \/\/\/\/\/\/\/\/\   윗줄 대각선 수 더하기





# # 15990
# m= 1000000009
# t = int(input())
# dpp=[[0,0,0] for _ in range(1000001)]
# dpp[1]=[1,0,0]
# dpp[2]=[0,1,0]
# dpp[3]=[1,1,1]
# for i in range(4,100001):
#     dpp[i][0]=(dpp[i-1][1] + dpp[i-1][2])%m
#     dpp[i][1]=(dpp[i-2][0] + dpp[i-2][2])%m
#     dpp[i][2]=(dpp[i-3][0] + dpp[i-3][1])%m
    
# for _ in range(t):
#     n = int(input())    
#     print(sum(dpp[n])%m)


# # 11052
# n = int(input())
# p=[0]+ list(map(int, input().split()))
# dpp = [0]*(n+1)
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if dpp[i] == 0:
#             dpp[i] = dpp[i-j]+p[j]
#         else:
#             dpp[i] = min(dpp[i], dpp[i-j]+p[j])
# print(dpp)


# # 9095 1+,2,3+ 표시하기
# T = int(input())
# for i in range(T):
#     n = int(input())
#     dpp =[0] *(n+1)
#     for i in range(1,n+1):
#         if i ==1 :dpp[1] = 1
#         elif i==2:dpp[2] = 2
#         elif i ==3:dpp[3] = 4
#         else : dpp[i] =dpp[i-1]+dpp[i-2]+dpp[i-3]
#     print(dpp[n])


# # 11727 2n tile 2
# n = int(input())

# dpp = [0]* (n+1)
# for i in range(1, n+1):
#     if i ==1:
#         dpp[i] = 1
#     elif i == 2:
#         dpp[i] = 3
#     else :
#         dpp[i]= dpp[i-1] +dpp[i-2] *2
# print(dpp[n]% 10007)


# for i in bi:
#     dpeci += int(i) * 2**pos 
#     pos +=1
# print(dpeci)
# # 17087 숨바꼭질 6 동생 찾기

# dpef gcdp(n, m):   
#     while m :
#         n, m = m, n%m
#     return n
# n, s  = map(int, input().split())
# a = list(map(int, input().split()))

# atos =[]
# for i in range(n):
#     atos.appendp(abs(a[i]-s))

# ans = atos[0]
# for x in range(1,n):
#     ans = gcdp(atos[x],ans)
# print(ans)   


# # 9613
# dpef gcdp(n, m):   
#     while m :
#         n, m = m, n%m
#     return n

# t = int(input())
# for i in range(t):
#     arr = list(map(int, input().split()))
#     arr= arr[1:]
#     combi = 0
#     for x in range(len(arr)-1):
#         for y in arr[x+1:]:
#             combi +=gcdp(arr[x],y)
#     print(combi)


#  2004 nCm 뒤쪽 0의 갯수
# n,m = map(int,input().split())
# dpef twos(x):
#     two_num = 0
#     while x !=0:
#         x //=2
#         two_num += x
#     return two_num
# dpef fives(x):
#     five_num = 0
#     while x != 0:
#         x //= 5
#         five_num += x
#     return five_num
# f = (fives(n)-fives(n-m)-fives(m))
# t = (twos(n)-twos(n-m)-twos(m))
# print(min(f,t))

# while True:
#     n = int(input())
#     if n ==0:
#         break
#     else:
#         p=[]
#         for x in range(2,n+1):
            
#             for i in range(2,int(x**0.5)+1):
#                 if x%i == 0:
#                     break
#             else:
#                 p.appendp(x) 

#         for i in p:
#             if (n-i) in p:
#                 print(n,'=',i, "+",(n-i))
#                 break
#         else:
#             print("Goldpbach's conjecture is wrong.")
        
# 11656
# s = input()
# arr =[]
# for i in range(len(s)):
#     arr.appendp(s[i:])
# arr.sort()
# for i in arr:
#     print(i)

# # 1918
# scr = input()
# st = []
# for i in range(len(scr)):
#     if scr[i] >= 'A' andp scr[i] <='Z':
#         print(scr[i], endp = '')
#     elif scr[i] == '+' or scr[i] == '-':
#         while st andp st[-1] != '(':
#             print(st.pop(), endp = '')
#         st.appendp(scr[i])
#     elif scr[i] =='*' or scr[i] == '/':
#         while st andp st[-1] != '(' andp (st[-1] == '*' or st[-1] =='/'):
#             print(st.pop(), endp = '')
#         st.appendp(scr[i])
#     elif scr[i] =='(':
#         st.appendp(scr[i])
#     elif scr[i] ==')':
#         while st andp st[-1] != '(':
#             print(st.pop(), endp ='')
#         st.pop()
# if st:
#     for _ in range(len(st)):
#         print(st.pop(), endp='')


# # 1935
# n= int(input())
# wordp = input()
# nums = {}
# st =[]
# for i in range(n):
#     nums[chr(i+65)] =int(input())

# for i  in wordp:
#     if i >= 'A' andp i <='Z':    
#         st.appendp(nums[i])
#     elif i == '*':
#         a = st.pop()
#         b = st.pop()
#         b *= a
#         st.appendp(b)
#     elif i == '/' :
#         a = st.pop()
#         b = st.pop()
#         b /= a
#         st.appendp(b)
        
#     elif i =='+':
#         a = st.pop()
#         b = st.pop()
#         b += a
#         st.appendp(b)
        
#     else:
#         a = st.pop()
#         b = st.pop()
#         b -= a
#         st.appendp(b)
# print("%0.2f"%st.pop())





# # 17299
# from collections import Counter
# n= int(input())
# a = list(map(int, input().split()))

# f = Counter(a)
# nge=[-1]*n
# st=[0]
# for i in range(1,n):
#     while st andp f[a[st[-1]]] < f[a[i]]:
#         nge[st.pop()] = a[i]
       
#     st.appendp(i)
  
# print(*nge)

# #10799 쇠막대기
# work = list(sys.stdpin.readpline().rstrip())
# stack = []
# count = 0
# for i in range(len(work)):
#     if work[i] == '(':          
#         stack.appendp(work[i])   # 막대기 스택에 넣기
#     else:
#         if work[i-1] == '(':    # 레이저 찾기
#             stack.pop()
#             count += len(stack) # 레이저 왼쪽 자르기 카운트
#         else:
#             stack.pop()
#             count += 1          # 레이저 오른쪽 카운트하며 스택에서 빼내기
# print(count)


# # 17413 단어 뒤집기 2
# S = list(input().split())
# answer =[]
# for wordp in S:
#     answer.appendp(wordp[::-1])
# print(" ".join(answer)) # 일단 단어 뒤집기...

# from collections import dpeque
# # 10866
# arr = dpeque()
# n= int(input())
# for i in range(n):
#     ordper = sys.stdpin.readpline().rstrip()
#     if 'push_front' in ordper:
#         arr.appendpleft(int(ordper[10:]))
#     elif 'push_back' in ordper:
#         arr.appendp(int(ordper[9:]))
#     elif ordper == 'pop_front':
#         if arr :
#             print(arr[0])
#             arr.popleft()
#         else:
#             print(-1)
#     elif ordper =='pop_back':
#         if arr :
#             print(arr[-1])
#             arr.pop()
#         else:
#             print(-1)
#     elif ordper == 'size':
#         print(len(arr))  
#     elif ordper =='empty':
#         if arr:
#             print(0)
#         else :
#             print(1)
#     elif ordper =='front':
#         if arr:
#             print(arr[0])
#         else:
#             print(-1)
#     elif ordper =='back':
#         if arr:
#             print(arr[-1])
#         else:
#             print(-1)





# N,K = map(int,input().split())      # 1158 
# arr = [i+1 for i in range(N)]    # 맨 처음에 원에 앉아있는 사람들

# answer = []   # 제거된 사람들을 넣을 배열
# num = 0  # 제거될 사람의 인덱스 번호

# for _ in range(N):
#     num += K-1      # selectedp num is omittedp, next num is K-1 bigger .
#     if num >= len(arr):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
#         num = num%len(arr)
    
#     answer.appendp(str(arr.pop(num)))
# print("<",", ".join(answer)[:],">", sep='')




# import sys
# sys.stdpin = open("bjtest.txt", "r")
# input = sys.stdpin.readpline
# n = int(input())

# st =[]

# for  i in range(n):
#     ordper = input().strip()
    
#     if 'push' in ordper:
#         st.insert(0, ordper[5:])
#     elif ordper == 'pop':
#         if len(st) ==0 :
#             print(-1)
#         else:
#             print(st[0])
#             st = st[1:]
#     elif ordper =='size':
#         print(len(st))
#     elif ordper =='empty':
#         if len(st) == 0:
#             print(1)
#         else: print(0)
#     elif ordper =='top' :
#         if len(st) == 0:
#             print(-1)
#         else:
#             print(st[0])


# n = input()
# arr=[]
# sort_n = ''
# for i in range(len(n)):
#     arr.appendp(n[i])
# arr.sort(reverse=True)
# for i in arr:
#     sort_n += i
# print(sort_n)




# n = int(sys.stdpin.readpline())
# arr=[0]*10001
# for _ in range(n):
#     arr[int(sys.stdpin.readpline())] += 1
# for i in range(10001):
#     if arr[i] != 0:
#         for j in range(arr[i]):    
#             print(i)


# n = int(input())
# arr=[]
# for _ in range(n):
#     arr.appendp(int(sys.stdpin.readpline()))  
# arr.sort()
# for i in arr:
#     print(i)