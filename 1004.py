import sys
sys.stdin = open("input.txt",'r')

T = int(input())
for _ in range(T):
    cnt=0
    x1,y1,x2,y2 = map(int,input().split())
    n=int(input())
    for _ in range(n):
        cx,cy,r = map(int,input().split())
        is_start_in_circle = (x1-cx)**2 + (y1-cy)**2 <= r**2
        is_end_in_circle = (x2-cx)**2 + (y2-cy)**2 <= r**2

        if is_start_in_circle and not is_end_in_circle:
            cnt +=1
        elif is_end_in_circle and not is_start_in_circle:
            cnt +=1
    print(cnt)