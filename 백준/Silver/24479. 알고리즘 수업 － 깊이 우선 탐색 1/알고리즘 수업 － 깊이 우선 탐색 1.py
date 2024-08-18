import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

node, edge, start = map(int, input().split())

graph = [[] for _ in range(node+1)]

for i in range(edge):
    n1, n2 = map(int, input().split())
    # 연결된 노드를 저장
    graph[n1].append(n2)
    graph[n2].append(n1)

# 연결된 노드를 오름차순으로 정렬
for i in range(node+1):
    graph[i].sort()

result = [0 for _ in range(node+1)]
visited = [0] * (node+1)  # 방문 여부
t = 1  # 방문 순서

def dfs(graph, n, visited):
    global t

    visited[n] = 1
    result[n] = t
    t += 1

    for node in graph[n]:
        if not visited[node]:
            dfs(graph, node, visited)

dfs(graph, start, visited)

for i in range(1, node+1):
    print(result[i])