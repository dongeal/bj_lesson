import sys
from collections import deque
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

T = int(input())
time = []
ans = [0]*(T)
for t in range(T):
    n,k = map(int,input().split())

    time = [0] + list(map(int, input().split()))
    result = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for i in range(k):
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    x = int(input())
    # print(graph)
    # print(indegree)
    #위상정렬 start
    queue = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)
            result[i] = time[i]
    while queue:
        current = queue.popleft()
        if current == x:
            break
        for c in graph[current]:
            indegree[c] -= 1
            result[c] = max(result[c],result[current] + time[c])
            if indegree[c] == 0:
                queue.append(c)
            
    ans[t] = result[x]
    #위상정렬 end

for t in range(T):
    print(ans[t])
