import math
n = int(input())
radius = list(map(int, input().split()))

Round = [i*2 for i in radius]

for i in Round[1:]:
    gcd = math.gcd(Round[0], i)
    print(f'{Round[0]//gcd}/{i//gcd}')