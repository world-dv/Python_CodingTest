n, m = map(int, input().split())
A, B = input().split()
dic = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1, 'H': 3, 'I': 1,
       'J': 1, 'K': 3, 'L':1, 'M': 3, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2,
       'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}
arr = []


def calculate(x):
    answer = []
    for i in range(len(x)-1):
        answer.append((x[i] + x[i+1]) % 10)
    return answer


for i, j in zip(A, B):
    arr.append(dic[i])
    arr.append(dic[j])
if len(A) > len(B):
    for i in A[len(B):]:
        arr.append(dic[i])
else:
    for i in B[len(A):]:
        arr.append(dic[i])

while True:
    if len(arr) == 2:
        break
    arr = calculate(arr)

print(f'{int("".join(list(map(str, arr))))}%')
