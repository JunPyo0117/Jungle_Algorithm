#크루스칼 알고리즘 (최소 신장 트리)
import sys
import heapq
input = sys.stdin.readline
# sys.setrecursionlimit(10000)
INF = float('inf')

def djikstra(start):
    queue = []

    # 시작 노드를 큐에 삽입 및 거리 0으로 설정
    heapq.heappush(queue, (0, start))
    dist_table[start] = 0

    while queue:
        # 가장 최단 거리가 짧은 노드 i 꺼내기
        i_dist, i = heapq.heappop(queue)

        # 이미 더 짧은 거리로 방문한 경우 무시
        if i_dist > dist_table[i]:
            continue

        # i의 인접 노드 j 확인
        for j, j_dist in graph[i]:
            # j: 인접 노드, j_dist: 간선 가중치
            # 현재 노드를 거쳐, 인접 노드로 이동하는 거리
            new_dist = i_dist + j_dist

            # 거리가 더 짧으면 갱신
            if new_dist < dist_table[j]:
                dist_table[j] = new_dist
                heapq.heappush(queue, (new_dist, j))
                


# 도시, 버스 수 
n = int(input())
m = int(input())
# (시작 도시, 도착 도시, 가중치)
edges = [list(map(int, input().split())) for _ in range(m)]
# 구하고자 하는 출발 도착 도시
start, end = map(int, input().split())

# 초기 거리 테이플 무한으로 초기화
dist_table = [INF] * (n + 1)
# 그래프 초기화
graph = [[] for _ in range(n + 1)] 

# a에서 b로 가는 튜플 추가(도착 도시, 비용) 
for a, b, cost in edges:
    graph[a].append((b, cost))

# print(graph)
# 출발 도시 설정
djikstra(start)
# start에서 end까지 가는 최소 비용 출력
print(dist_table[end])

