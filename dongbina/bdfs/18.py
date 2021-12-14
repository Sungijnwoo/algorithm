def solution(p):
    counter = {"(": 0, ")": 0}
    u = ""
    v = ""
    if not p:
        return ''
    for i in p:
        u += i
        counter[i] += 1
        if counter["("] == counter[")"]:
            v = p[len(u):]
            if judge(u):
                return u + solution(v)
            else:
                new_u = ["(" if i == ")" else ")" for i in u[1:-1]]
                return "(" + solution(v) + ")" + ''.join(new_u)

def judge(p):
    q = []
    for i in p:
        if i == "(":
            q.append(i)
        else:
            if not q:
                return False
            if q:
                q = q[:-1]
    return True


if __name__ == "__main__":
    print(solution("(()())()"))