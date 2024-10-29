import heapq
import random

def h(s):
    val = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if abs(s[i] - s[j]) == abs(i - j):
                val += 1
            elif s[i] == s[j]:
                val += 1
    return val

def hill_climbing():
    s = [random.randint(0, 7) for i in range(8)]
    while(True):
        q = []
        for i in range(8):
            for j in range(8):
                ns = s.copy()
                ns[i] = j
                heapq.heappush(q, (h(ns), ns))
        f, ps = heapq.heappop(q)
        if ps == s:
            return hill_climbing()
        if(f == 0):
            return ps
        s = ps 
    return s 

def print_board(s):
    print(s)
    board = [['.'] * 8 for _ in range(8)]
    for row in range(len(s)):
        board[row][s[row]] = 'Q'
    for row in board:
        print(' '.join(row))

print_board(hill_climbing())
