import sys
input = sys.stdin.readline

# 멀티탭에서 제거할 대상의 인덱스 찾기
def find_device_to_unplug(current_pos, plugin, arr):
    target_idx = 0  # 뽑을 플러그의 인덱스 (기본값: 첫 번째)
    farthest_pos = 0  # 가장 나중에 나타나는 위치 (상대적 거리)
    
    # 현재 멀티탭에 꽂힌 각 전기용품을 검사
    for j in range(len(plugin)):
        try:
            # 현재 위치 이후에서 이 전기용품이 언제 다시 나타나는지 찾기
            next_use = arr[current_pos + 1:].index(plugin[j])
            
            # 더 나중에 사용되는 전기용품을 발견했다면 업데이트
            if next_use > farthest_pos:
                target_idx = j
                farthest_pos = next_use
                
        except ValueError:
            # 이후 사용되지 않는 플러그 발견시 즉시 반환 (최우선 제거 대상)
            return j
    
    return target_idx

n, k = map(int, input().strip().split())
plug_list = list(map(int, input().split()))

cnt = 0
plug = []
future = {}


for i in plug_list:
    if len(plug) == n:
        break
    if not plug:
        plug.append(i)
    elif i in plug:
        continue
    else:
        plug.append(i) 

for idx, p in enumerate(plug_list):
    if p in plug:
        continue
    elif plug:
        unplug_idx = find_device_to_unplug(idx, plug, plug_list)
        plug[unplug_idx] = p  # 직접 교체
        cnt += 1

# print(future)
print(cnt)
#=======================================================

# n,k = map(int,input().split())
# name = list(map(int,input().split()))
# tap = [0] * n
# i=0
# answer = 0
# while i<k:
#     if name[i] in tap:
#         i+=1
#         continue

#     for j in range(n):
#         if tap[j] == 0:
#             tap[j] = name[i]
#             i+=1
#             break
#     else:
#         nextPos = [k] * n
#         for j in range(n):
#             for l in range(i,k):
#                 if name[l] == tap[j]:
#                     nextPos[j] = l
#                     break
        
#         maxPos = 0
#         maxVal = nextPos[0]

#         for j in range(n):
#             if maxVal < nextPos[j]:
#                 maxPos = j
#                 maxVal = nextPos[j]
        
#         tap[maxPos] = 0 
#         answer += 1
# print(answer)
