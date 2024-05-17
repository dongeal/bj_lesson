import sys
sys.stdin = open("bjtest.txt","r")

n = int(input())
hab = 0             #그굽단어
for x in range(n):  
    g=1             #판별 체크
    s = input()
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[i] != s[j] : #i번째 글과 그다음이 다르면
                for k in range(j, len(s)): # 그담부터 끝까지       
                    if s[i] != s[k] :      # 계속 같은게 없으면
                        g *= 1    # 그룹단어 유지
                    else:
                        g *= 0   # 그룹단어 아님
    hab += g                    # 그룹단어 합산
print(hab)    