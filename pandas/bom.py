import pandas as pd
from collections import defaultdict

def calculate_product(node_id, data, results):
    data['부품번호'] = data['부품번호'].astype(str)
    current_node = data[data['부품번호'] == node_id]
    
    if current_node.empty:
        print(f"Error: Node {node_id} not found.")
        return 0

    current_node = current_node.iloc[0]

    value = current_node['수량']
    parent_id = current_node['상위품목']

    if not pd.isna(parent_id):
        value *= calculate_product(parent_id, data, results)

    results[node_id] = value
    return value

def process_data(data):
    results = {}
    name_sums = defaultdict(int)

    for node_id in data['부품번호']:
        calculate_product(node_id, data, results)

    for index, row in data.iterrows():
        name_sums[row['부품번호']] += results[row['부품번호']]
    

    return results, name_sums

def main():
    # CSV 파일에서 데이터 읽기
    file_path = 'pandas/2input.csv'  # 파일 경로를 적절히 변경하세요.

    data = pd.read_csv(file_path, dtype={'부품번호': str,'상위품목':str})
    # 데이터 처리
    results, name_sums = process_data(data)
   
    # 결과 출력
    # print("Results:")
    # for node_id, result in results.items():
    #     print(f"{node_id}: {result}")

    print("\nName Sums:")
    for name, total_sum in name_sums.items():
        print(f"{name}: {total_sum}")

    # # 결과를 CSV 파일로 저장
    # output_data = pd.DataFrame({'부품번호': list(results.keys()), '품명': data['품명'], '결과': list(results.values())})
    # output_data.to_csv('output.csv', index=False)

if __name__ == "__main__":
    main()
