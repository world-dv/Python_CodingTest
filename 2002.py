n = int(input())
cars = []
tunnel = []
for _ in range(n):
    cars.append(input())
for _ in range(n):
    tunnel.append(input())
cnt = 0
idx = 0
while idx < len(tunnel):
    if cars.index(tunnel[idx]) != idx:
        cars.pop(cars.index(tunnel[idx]))
        tunnel.pop(idx)
        cnt += 1
    else:
        idx += 1
print(cnt)
