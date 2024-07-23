n, c = map(int, input().split())
message = list(map(int, input().split()))
x = sorted(set(message), key=lambda a: (message.count(a), -message.index(a)), reverse=True)
for i in x:
    print(f'{(str(i) + " ") * message.count(i)}', end='')
