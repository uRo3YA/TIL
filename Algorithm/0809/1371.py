dic = {}

while True:
    try:
        for c in input():
            if c != ' ':
                dic[c] = dic.get(c, 0) + 1 
    except EOFError:
        arr = []
        for c, num in dic.items():
            arr.append([c, num])
        arr.sort(key=lambda x: (-x[1], x[0]))
        max_val = arr[0][1]
        result = ''
        for c, num in arr:
            if num == max_val:
                result += c
            else:
                break
        print(result)
        break