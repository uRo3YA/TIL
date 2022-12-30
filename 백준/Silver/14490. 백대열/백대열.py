from math import gcd

num1, num2 = map(int, input().split(":"))

gcd_num = gcd(num1, num2)

print(f"{num1 // gcd_num}:{num2 // gcd_num}")