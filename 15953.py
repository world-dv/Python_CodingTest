import sys
T = int(sys.stdin.readline())
prize1 = {1: 5000000, 2: 3000000, 3: 2000000, 4: 500000, 5: 300000, 6: 100000}
prize2 = {1: 5120000, 2: 2560000, 3: 1280000, 4: 640000, 5: 320000}

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    answer = 0
    if 0 < a <= 1:
        answer = prize1[1]
    elif 1 < a <= 3:
        answer = prize1[2]
    elif 3 < a <= 6:
        answer = prize1[3]
    elif 6 < a <= 10:
        answer = prize1[4]
    elif 10 < a <= 15:
        answer = prize1[5]
    elif 15 < a <= 21:
        answer = prize1[6]

    if 0 < b <= 1:
        answer += prize2[1]
    elif 1 < b <= 3:
        answer += prize2[2]
    elif 3 < b <= 7:
        answer += prize2[3]
    elif 7 < b <= 15:
        answer += prize2[4]
    elif 15 < b <= 31:
        answer += prize2[5]
    print(answer)
