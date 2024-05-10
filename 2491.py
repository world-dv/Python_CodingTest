import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer_max = 1
answer_min = 1

cnt_max = 1
cnt_min = 1
for i in range(len(arr) - 1):
    if arr[i] < arr[i+1]:
        cnt_max += 1
        cnt_min = 1
    elif arr[i] > arr[i+1]:
        cnt_min += 1
        cnt_max = 1
    else:
        cnt_max += 1
        cnt_min += 1
    answer_min = max(answer_min, cnt_min)
    answer_max = max(answer_max, cnt_max)
print(max(answer_max, answer_min))
