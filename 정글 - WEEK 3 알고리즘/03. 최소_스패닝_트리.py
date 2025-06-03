#크루스칼 알고리즘 (최소 신장 트리)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 각 노드의 루트 노드 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 집합 합치기
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b

# 노드 수, 간선 수
v, e = map(int, input().split())
# 각자가 자신의 부모 노드(0번 인덱스는 사용하지 않음)
parent = [i for i in range(v+1)]
# 간선 = (시작 노드, 도착 노드, 가중치)
edge = [list(map(int, input().split())) for _ in range(e)]
edge.sort(key=lambda x:x[2])  # 가중치 기준으로 정렬

# 가중치 초기화
answer = 0

# 가중치가 작은 간선부터 처리
for a, b, cost in edge:
    # 사이클 검사
    if find(parent, a) == find(parent, b):
        continue # 같은 집합이면 사이클 생성 -> 제외
    else:
        answer += cost  # MST에 간선 추가
        union(parent, a, b) # 두 집합 합치기

print(answer)

