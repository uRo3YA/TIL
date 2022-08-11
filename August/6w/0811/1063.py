# R : 한 칸 오른쪽으로
# L : 한 칸 왼쪽으로
# B : 한 칸 아래로
# T : 한 칸 위로
# RT : 오른쪽 위 대각선으로
# LT : 왼쪽 위 대각선으로
# RB : 오른쪽 아래 대각선으로
# LB : 왼쪽 아래 대각선으로

info = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1)
}

king, stone, n = input().split()
kr, kc = 8-int(king[1]), ord(king[0])-ord("A")
sr, sc = 8-int(stone[1]), ord(stone[0])-ord("A")
for _ in range(int(n)):
    cmd = input()
    dr, dc = info[cmd]
    if not (0 <= kr+dr < 8 and 0 <= kc+dc < 8):
        continue
    kr += dr
    kc += dc
    if (kr, kc) == (sr, sc):
        if not (0 <= sr+dr < 8 and 0 <= sc+dc < 8):
        	# 킹의 움직임 되돌리기
            kr -= dr
            kc -= dc
            continue
        sr += dr
        sc += dc
       
print(chr(ord("A")+kc)+str(8-kr))
print(chr(ord("A")+sc)+str(8-sr))