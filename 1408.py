start = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))

time = (end[0] * 3600 + end[1] * 60 + end[2]) - (start[0] * 3600 + start[1] * 60 + start[2])
if time < 0:
    time += 24 * 3600
print('{0:02d}:{1:02d}:{2:02d}'.format(time // 3600, time % 3600 // 60, time % 3600 % 60))
