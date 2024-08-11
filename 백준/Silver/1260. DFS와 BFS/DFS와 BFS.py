import sys
input = sys.stdin.readline

node, edge, start = map(int, input().split())

# 1. 그래프 만들기
graph = [[0]*(node+1) for _ in range(node+1)]
for i in range(edge):
    n1, n2 = map(int, input().split())
    # 양방향 그래프
    graph[n1][n2] = graph[n2][n1] = 1


# 2. 방문한 노드 리스트 만들기
visited_dfs = [0] * (node+1)
visited_bfs = visited_dfs.copy()


# 3. dfs (재귀 이용)
def dfs(n):
    visited_dfs[n] = 1  # 방문한 노드는 1로 표시
    print(n, end=' ')
    for i in range(1, node+1):
        if graph[n][i] == 1 and visited_dfs[i] == 0:  # 연결되어 있고, 방문하지 않은 노드 찾기
            dfs(i)

# 4. bfs (queue 이용)
def bfs(n):
    queue = [n]  # 큐에 노드를 추가
    visited_bfs[n] = 1  # 방문한 노드는 1로 표시
    while queue:  # 큐가 빌 때까지 반복
        n = queue.pop(0)  # 큐에 담긴 첫번째 노드를 꺼내기
        print(n, end=' ')
        for i in range(1, node+1):
            if graph[n][i] == 1 and visited_bfs[i] == 0:  # 연결되어 있고, 방문하지 않은 노드 찾기
                queue.append(i)
                visited_bfs[i] = 1

dfs(start)
print()
bfs(start)