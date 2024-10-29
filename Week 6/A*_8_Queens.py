import heapq

def h(s):
    val = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if abs(s[i] - s[j]) == abs(i - j):
                val += 1
            elif s[i] == s[j]:
                val += 1
    return val

def g(s):
    return 8 - len(s)

def a_star():
    s = []
    q = []
    heapq.heappush(q, (8, s))
    while q:
        f, curr = heapq.heappop(q)
        if f == 0:
            return curr
        if len(curr) == 8:
            continue
        for i in range(8):
            ns = curr.copy()
            ns.append(i)
            heapq.heappush(q, (h(ns)+ g(ns), ns))
    return s

def print_board(s):
    print(s)
    board = [['.'] * 8 for _ in range(8)]
    for row in range(len(s)):
        board[row][s[row]] = 'Q'
    for row in board:
        print(' '.join(row))

print_board(a_star())
