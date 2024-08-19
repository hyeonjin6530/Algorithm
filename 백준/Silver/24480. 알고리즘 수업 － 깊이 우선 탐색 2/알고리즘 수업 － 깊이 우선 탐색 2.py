import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

node, edge, start = map(int, input().split())

# 연결된 노드를 저장
graph = [[] for _ in range(node+1)]

# 간선 정보 저장
for i in range(edge):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 내림차순으로 정렬
for i in range(node+1):
    graph[i].sort(reverse=True)

result = [0] * (node+1)  # 방문 순서 저장
visited = [0] * (node+1)  # 방문 여부
t = 1  # 방문 순서

def dfs(graph, n, visited):
    global t

    visited[n] = 1  # 방문했다고 표시
    result[n] = t  # 방문 순서 저장
    t += 1  # 다음 방문 순서

    # 연결된 노드에 대해 재귀적으로 방문
    for node in graph[n]:
        if not visited[node]:  # 방문하지 않은 노드라면
            dfs(graph, node, visited)  # 재귀적으로 방문

dfs(graph, start, visited)

for i in range(1, node+1):
    print(result[i])
