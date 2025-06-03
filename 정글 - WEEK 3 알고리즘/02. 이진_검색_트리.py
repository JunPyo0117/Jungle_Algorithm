import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def postorder(start, end):
    if start > end:
        return
    
    root = preorder[start]  # 전위 순회의 첫 번째는 항상 루트
    
    # 루트보다 큰 첫 번째 값의 인덱스 찾기 (오른쪽 서브트리 시작점)
    idx = start + 1
    while idx <= end and preorder[idx] < root:
        idx += 1

    # 재귀적으로 왼쪽, 오른쪽 서브트리 처리
    postorder(start + 1, idx - 1)  # 왼쪽 서브트리
    postorder(idx, end)           # 오른쪽 서브트리
    print(root)                   # 루트 출력 (후위 순회)

preorder = []
while True:
    try:
        x = int(input())
        preorder.append(x)
    except:
        break

# 후위 순회 실행
postorder(0, len(preorder) - 1)