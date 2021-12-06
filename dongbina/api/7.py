N = input()

left = list(N[:len(N)//2])
right = list(N[len(N)//2:])

if eval('+'.join(left)) == eval('+'.join(right)):
    print("LUCKY")
else:
    print("READY")
