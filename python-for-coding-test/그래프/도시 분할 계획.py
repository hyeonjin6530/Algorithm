'''
  문제 유형: 크루스칼 알고리즘(최소신장트리)

  문제 풀이 방법: 
    1. 리스트에 (비용, 시작노드, 끝노드)을 저장한다.
    2. 리스트를 비용으로 정렬한다.
    3. 리스트를 돌며 사이클이 발생하지 않을 경우(= 루트노드가 같지 않을 경우) union을 수행하고 비용을 추가한다.
    4. 마지막에 가장 비용이 큰 간선을 제거한다.(두 개의 최소신장트리를 만들어야해서)
'''
import sys

input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, s, e):
  s = find_parent(parent, s)
  e = find_parent(parent, e)

  if s < e:
    parent[e] = s
  else:
    parent[s] = e

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

result = 0

edge = []

for _ in range(m):
  a, b, cost = map(int, input().split())
  edge.append((cost, a, b))

edge.sort()

for c, n1, n2 in edge:
  if find_parent(parent, n1) != find_parent(parent, n2):
    union_parent(parent, n1, n2)
    result += c
    last = c

print(result-last)