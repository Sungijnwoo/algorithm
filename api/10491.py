import re
while True:
    try:
        a=input()
        p=re.match('.*problem', a.lower())
        if p: print('yes')
        else: print('no')
    except EOFError: break