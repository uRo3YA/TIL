n, m = map(int, input().split())
for i in range(n):
    string = input()
    reverse_string = "".join(reversed(string))
    print(reverse_string)