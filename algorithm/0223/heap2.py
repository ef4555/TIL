N = 6
data = [3, 6, 2, 1, 7, 9]
tree = [0 for _ in range(N+1)]
last = 1
for i in range(len(data)):
    if not tree[i]:
        tree[last] = data[i]
    else:
        last += 1
        child = last  # 새로 추가된 정점을 자식으로
        parent = child // 2 # 완전 이진 트리에서 부모 정점 번호
        tree[child] = data[i]
        # print(tree, child, parent)
    # 부모가 있고, 부모가 자식보다 큰 동안(부모가 작아질 때 까지)
        while parent >= 1 and tree[parent] > tree[child]:
        # 부모와 자식의 위치를 변경
            tree[parent], tree[child] = tree[child], tree[parent]
        # 자식 위치를 부모로 변경
            child = parent
        # 부모는 부모 // 2 => 조상노드
            parent = parent // 2

print(tree)


# [0, 1, 2, 3, 6, 7, 9]