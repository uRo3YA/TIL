from collections import defaultdict

generated_data = [
    ("P1", "product", 10, None),
    ("P2", "apple", 5, "P1"),
    ("P3", "coco", 8, "P1"),
    ("P4", "apple", 3, "P2"),
    ("P5", "coco", 6, "P2"),
    ("P6", "banana", 2, "P3"),
    ("P7", "milk", 4, "P3"),
    ("P8", "banana", 7, "P4"),
    ("P9", "milk", 9, "P4"),
    ("P10", "banana", 1, "P5"),
    ("P11", "coco", 3, "P5"),
    ("P12", "milk", 5, "P6")
]

# 최상위 노드에서 하위노드의 qty만큼 곱한 결과 저장
results = defaultdict(int)

for node_id, name, qty, parent_id in generated_data:
    if parent_id is not None:
        parent_result = results[parent_id]
        results[node_id] = parent_result * qty
    else:
        results[node_id] = qty

# 같은 name을 가진 노드들의 합 계산
name_sums = defaultdict(int)

for node_id, name, _, _ in generated_data:
    name_sums[name] += results[node_id]

# 결과 출력
print("Results:")
for node_id, result in results.items():
    print(f"{node_id}: {result}")

print("\nName Sums:")
for name, total_sum in name_sums.items():
    print(f"{name}: {total_sum}")
