a_apple, a_orange = map(int, input().split())
b_apple, b_orange = map(int, input().split())

a = a_apple + b_orange
b = a_orange + b_apple
print(min(a, b))
