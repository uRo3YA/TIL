# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")
num1, num2 = input().split()

num1 = int(num1[::-1])  
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else :
    print(num2)